from django.urls import path

from .views import * 

urlpatterns = [
    path('', redirectMe),
    path('home/', index, name='main'),
    path('home/catalog/', catalog, name='catalog')
]   
