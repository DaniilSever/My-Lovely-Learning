from django.urls import path
from api.views.course_views import *
from edit_course_zone.models import lesson_content_types

app_name = "course_api"

urlpatterns = [
    path('create/', CreateCourse.as_view(), name="create_course"),
    path('delete/<int:pk>/', DeleteCourse.as_view(), name="delete_course"),
    path('<int:pk>/', RetrieveUpdateCourse.as_view(), name="retrieve_course"),
    
    path('<int:course_id>/add_chapter/', AddChapter.as_view(), name="add_chapter"),
    path('delete_chapter/<int:pk>/', DeleteChapter.as_view(), name="delete_chapter"),
    path('chapter/<int:pk>/', RetrieveUpdateChapter.as_view(), name="retrieve_chapter"),
    
    path('add_subchapter/<int:chapter_id>/', AddSubchapter.as_view(), name="add_subchapter"),
    path('delete_subchapter/<int:pk>/', DeleteSubchapter.as_view(), name="delete_subchapter"),
    path('subchapter/<int:pk>/', RetrieveUpdateSubchapter.as_view(), name="retrieve_subchapter"),
    
    path('add_lesson/<int:subchapter_id>/', AddLesson.as_view(), name="add_lesson"),
    path('delete_lesson/<int:pk>/', DeleteLesson.as_view(), name="delete_lesson"),
    path('lesson/<int:pk>/', RetrieveUpdateLesson.as_view(), name="retrieve_lesson"),
    
    #TODO: throught re_path
    path('add_lesson_content/<int:lesson_id>/<str:lesson_content_type>/', AddLessonContent.as_view(), name="add_lesson_content"),
    path('delete_lesson_content/<int:pk>/', DeleteLessonContent.as_view(), name="delete_lesson_content"),
    path('lesson_content/<int:pk>/', RetrieveUpdateLessonContent.as_view(), name="retrieve_lesson_content"),
]
