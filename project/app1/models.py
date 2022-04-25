from distutils.command import upload
from email.mime import image
from unicodedata import name
from django.db import models

# Create your models here.

class Test(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos')
        
