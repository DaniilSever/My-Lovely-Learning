"""Server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from Main.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Main.urls')),
    path('settings/', include('settings.urls')),
    path('cource/', include('my_course.urls')),
    path('condition/', include('conditions.urls')),
    path('teachers/', include('teachers.urls')),
    path('edit-learn/', include('edit_learn.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),
]
