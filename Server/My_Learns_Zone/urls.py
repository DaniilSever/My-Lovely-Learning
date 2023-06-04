from django.urls import path
from .views import *

app_name = "learning"

urlpatterns = [
    path("", LearnCourseListView.as_view(), name="my_learn"),
]
