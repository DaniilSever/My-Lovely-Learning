from django.urls import path, include
from django.conf.urls.static import static

from Server import settings
from .views import * 

urlpatterns = [
    path('', redirectMe),
    path('home/', LoginUser.as_view(),  name='main'),
    path('reg/', RegisterUser.as_view(), name='registr'),
    path('profile/', profile, name='profile'),
    path('logout/', logout_user, name='logout'),
    path('accounts/profile/', redirectMe),
]   

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)