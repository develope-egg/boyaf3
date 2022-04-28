import email
import random
from tkinter import PhotoImage
from unittest.mock import DEFAULT
from django.db import models
from ckeditor.fields import RichTextField
from django_grapesjs.models import GrapesJsHtmlField
from django.contrib.auth.models import User
import uuid

class FileUpload(models.Model):
    file = models.FileField()

class FileWord(models.Model):
    file = models.FileField()




class blogs(models.Model):
     title= models.CharField(max_length=25)
     background=models.ImageField(default='null')
     owner_blog = models.CharField(max_length=8)
     user = models.OneToOneField(User, on_delete=models.CASCADE)
     html = GrapesJsHtmlField()
     date = models.DateTimeField()

     def __str__(self):
         return f"{self.owner_blog}"


