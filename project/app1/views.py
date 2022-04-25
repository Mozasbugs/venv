from imghdr import tests
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Test
# Create your views here.

def index(request):
    
    return render(request, 'first.html',{'data':Test.objects.all()})
