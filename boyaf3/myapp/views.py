
from turtle import width
from django import http
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.contrib import messages
from reportlab.lib.utils import ImageReader
from django.http import FileResponse
from reportlab.pdfgen import canvas
from PIL import Image
from . import forms
from googleapiclient.http import MediaFileUpload
from .Google import Create_Service
from googleapiclient.http import MediaIoBaseDownload
import io
import os
from . import models
import datetime
from django.http import HttpResponse
import PyPDF2
from random import choice
from docx2pdf import convert
# Create your views here.
from django.contrib.auth import authenticate
from django.contrib.auth import login as authlogin

def index(request):
    if request.method == 'POST':
        return render(request, 'home.html')
    else:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for is not None:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        print(ip)
        uf = forms.UploadFileForm()
    return render(request, 'home.html', {'uf': uf})

def decument(request):
    allfiles = models.FileUpload.objects.all()
    now = datetime.datetime.now()
    time = now.strftime("%H""%M")
    if time == 8 :
        for allfiles in allfiles:
            allfiles.delete()
    return render(request, 'about.html', {'allfiles': allfiles})

def login(request):
    if request.method == "POST":
      username= request.POST.get('username')
      password = request.POST.get('pass')
      user = authenticate(username=username, password=password)
      if user is not None:
        authlogin(request, user)
        return redirect('index')
      else:
          m=messages.MessageFailure('نأسف لايمكنك تسجيل الدخول')
          return HttpResponse(m)
    else:
     return render(request, "log in.html")

def png(request):
 if request.method == 'POST':
        imagelist = request.FILES.getlist('files')
        width
        response = HttpResponse(content_type='application/pdf')
        a= request.FILES['files']
        fs = FileSystemStorage()

        p= canvas.Canvas(response)
        page_width, page_height =p._pagesize
        for image in imagelist:
          img=Image.open(image)
          image_width, image_height = img.size
          print(image_width)
          print(image_height)
          #fs.save(image.name, image)10, 500mask='auto'
          my_image=ImageReader(image)
          p.drawImage(my_image, 0, 0, width=image_width, height=image_height, preserveAspectRatio=True )
          p.setPageSize((image_width, image_height))
          p.showPage()
         


        p.save()
        response['Content-Disposition'] = "attachment; filename="+ a.name + ".pdf"
        return response
 else:
  return render(request, 'jpg to pdf.html')

def merge(request):
    if request.method == 'POST':
        fs = FileSystemStorage().open("ip", "w+")
        print(request.POST.get('name'))
        fs.write(request.POST.get('name')+"----------------------------------------------------")
        fs.close()
        return render(request, 'merge pdf.html')

    else:
        return render(request, 'merge pdf.html')

def word(request, ):
 if request.method == "POST":
        r_file = request.FILES['files']
        name_file= request.POST.get('name')
        fs = FileSystemStorage()
        SCOPES = ['https://www.googleapis.com/auth/drive']
        filename = fs.save(r_file.name, r_file)
        path=str(fs.path(r_file.name))
        
        service = Create_Service('client-secret.json', 'drive', "v3", SCOPES)
        file_metadata = {'name': r_file.name,'parents': ['1I70x6KvlYOk3bOetAPdqIh0J2gqoj83G'],'mimeType': 'application/vnd.google-apps.document'}
        media_content = MediaFileUpload(path, mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        file = service.files().create(
         body=file_metadata,
         media_body=media_content).execute()
        fileid= file['id']
        print(fileid)
        request = service.files().export_media(fileId=fileid,mimeType='application/pdf')
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        path1= path.replace(str(r_file.name), fileid+'.pdf')
        while done is False:
         status, done = downloader.next_chunk()
         print("Download %d%%." % int(status.progress() * 100))

        fh.seek (0)
        filename= fileid+'.pdf'
        with open(path1, 'wb') as f:
         f.write(fh.getvalue())
         f.close()

        with open(path1,"rb") as f:
         fileend= f.read()
        response = HttpResponse(fileend, content_type='application/pdf')
        response['Content-Disposition'] = "attachment; filename="+str(name_file)+".pdf"
        fs.delete(str(name_file)+".pdf")
        return response
        

 else:
   x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
   if x_forwarded_for is not None:
    ip = x_forwarded_for.split(',')[0]
   else:
    ip = request.META.get('REMOTE_ADDR')
    fs = FileSystemStorage().open("ip", "w+")
    fs.write(ip+'-------------------------------------')
   return render(request, "word to pdf.html")



def tools(request):
    if request.method == "POST":
        return render(request, "2.html")
    else:
        return render(request, "2.html")

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('index')

def logging(request):
    render(request, 'loggin.html')

def blog(request,id):
    try:
        blog = models.blogs.objects.get(owner_blog=id)
        print(blog)
        b=blog.title
        a = blog.html
        print(a)
        return render(request, 'blank.html', {'a': a ,'b': b})

    except:
        return HttpResponse('')
def blogs(request):
  a=models.blogs.objects.all()
  return render(request,'blogs.html',{'a':a})

    
