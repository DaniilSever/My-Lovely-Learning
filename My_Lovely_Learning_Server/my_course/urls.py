from django.urls import path, include
from django.conf.urls.static import static

from Server import settings
from .views import * 

urlpatterns = [
    path('', my_cource, name='user_cource'),
    path('favorit/', favorit_cource, name='user_favorit'),
    path('archiv/', archiv_cource, name='user_archiv'),
    path('class/', class_cource, name='user_class'),
]   

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)