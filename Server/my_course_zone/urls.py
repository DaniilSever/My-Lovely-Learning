from django.urls import path, include
from django.conf.urls.static import static

from Server import settings
from .views import * 

urlpatterns = [
    path('', my_cource, name='user_cource'),
]   

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)