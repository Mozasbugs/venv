from distutils.command import upload
from email.mime import image
from django.db import models

# Create your models here.

class Doc(models.Model):
    image = models.ImageField(upload_to='photos/%y/%m/%d')
    name = models.CharField(max_length=100)
    ID = models.IntegerField()
    specialization = models.CharField(max_length=250)
    content = models.TextField(default=True)
    
    def __str__(self):
        return self.name 
    
    
class Patient(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(default=True)
    
    
    
    
    
