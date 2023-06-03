from django.urls import path
from .views import *

app_name = "teaching"

urlpatterns = [
    path('teaching/', TeachingMainView.as_view(), name='home')
]
