from django.urls import path
from django.conf.urls.static import static

from My_Lovely_Learning_Server import settings
from .views import * 

urlpatterns = [
    path('', redirect_to_main),
    path('home/', index,  name='main'),
    path('home/catalog/', catalog, name='catalog'),
    path('learning/', catalog, name='learning'),
    path('teaching/', catalog, name='teaching'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
]