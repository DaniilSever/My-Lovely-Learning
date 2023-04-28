from django.urls import path, include
from django.conf.urls.static import static

from Server import settings
from .views import * 

urlpatterns = [
    path('using/', terms_of_use, name='using'),
    path('privacy/', privacy_policy, name='privacy'),
]   

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)