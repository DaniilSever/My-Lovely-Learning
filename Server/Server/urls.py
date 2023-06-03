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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_zone.urls')),
    path('', include('teachers_zone.urls')),
    path('condition/', include('conditions_zone.urls')),
    path('my_learn/', include('my_course_zone.urls')),
    path('settings/', include('settings_zone.urls')),
    path('course/', include("edit_course_zone.urls", namespace="courses")),
    path('api/v1/', include('api.urls.urls', namespace='api')),
    path('social-auth/', include('social_django.urls', namespace='social')),
]
