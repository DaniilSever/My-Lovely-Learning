from django.urls import path
from django.conf.urls.static import static

from My_Lovely_Learning_Server import settings
from .views import * 

class_list = [
    LoginUser.as_view,
    RegisterUser.as_view,
]

urlpatterns = [
    path('', redirectMe),
    path('home/', LoginUser.as_view(),  name='main'),
    path('reg/', RegisterUser.as_view(), name='registr'),
    path('profile/', profile, name='profile'),
    path('logout/', logout_user, name='logout'),
    path('settings/profile', main_settings, name='settings'),
]   

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)