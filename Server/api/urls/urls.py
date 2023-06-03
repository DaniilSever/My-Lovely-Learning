from django.urls import path, include

app_name = 'api'

urlpatterns = [
    path('user/', include('api.urls.user_urls', namespace="user_api")),
    path('course/', include('api.urls.course_urls', namespace="course_api")),
    path('compiler/', include('api.urls.compiler_urls', namespace="compiler_api"))
]
