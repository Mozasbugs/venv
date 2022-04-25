from imghdr import tests
from pydoc import Doc
from tkinter.filedialog import test
from unicodedata import name
from django.shortcuts import render

# Create your views here.

def gettemp(request):
    return render(request, 'home.html')

def viewdata(request):
    return render(request, 'dataview.html')




