from atexit import register
from distutils.command import upload
from email.mime import image
from unicodedata import name
from django.db import models
from datetime import datetime
# Create your models here.

class Test(models.Model):
    x= [
        ('Heart','Heart'),
        ('blood','blood'),
       ]
    
    name = models.CharField(max_length=100, default='Type Name')
    image = models.ImageField(upload_to='photos')
    register = models.DateTimeField(default= datetime.now, null=True)
    specialization = models.CharField(max_length=250,choices=x)

    
    def __str__(self):
        return self.name
        
