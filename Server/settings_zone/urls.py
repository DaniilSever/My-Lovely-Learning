from django.urls import path, include
from django.conf.urls.static import static

from Server import settings
from .views import * 

urlpatterns = [
    path('profile/', main_settings, name='settings'),
    path('email/', email_settings, name='set_email'),
    path('pass/', PasswordChangeView.as_view(), name='set_pass')
]   

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)