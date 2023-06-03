from django.urls import path
from api.views.course_views import *

app_name = "course_api"

urlpatterns = [
    path('create/', CreateCourse.as_view(), name="create"),
    path('delete/<int:pk>/', DeleteCourse.as_view(), name="delete"),
    path('<int:pk>/', RetrieveCorse.as_view(), name="retrieve"), # и для получения данных и для редактирования всего курса
]
