from django.test import TestCase

# Create your tests here.
from .views import index, login , png ,merge, word , tools, logout_view , blog ,blogs 
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
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer
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

index(request)
login(request) 
png(request)
merge(request) 
word(request)  
tools(request)
logout_view(request) 
blog(request)  
blogs(request)  
