from django.urls import path
from . import views

urlpatterns =[
    path('gettemp/',views.gettemp, name='gettemp'),
    path('viewdata/',views.viewdata, name='veiwdata'),
    
]