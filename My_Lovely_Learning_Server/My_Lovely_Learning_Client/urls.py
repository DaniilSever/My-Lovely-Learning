from django.urls import path
from django.conf.urls.static import static

from My_Lovely_Learning_Server import settings
from .views import * 

urlpatterns = [
    path('', redirectMe),
    path('home/', index,  name='main'),
]   

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)