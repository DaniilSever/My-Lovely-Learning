from django.urls import path, include
from django.conf.urls.static import static

from Server import settings
from .views import * 

urlpatterns = [
    path('', redirectMe),
    path('home/', LoginUser.as_view(),  name='main'),
    path('cource/', my_cource, name='user_cource'),
    path('cource/favorit', favorit_cource, name='user_favorit'),
    path('cource/archiv', archiv_cource, name='user_archiv'),
    path('cource/class', class_cource, name='user_class'),
    path('reg/', RegisterUser.as_view(), name='registr'),
    path('profile/', profile, name='profile'),
    path('logout/', logout_user, name='logout'),
]   

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)