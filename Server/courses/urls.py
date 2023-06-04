from django.urls import path
from .views import *

app_name = 'courses'

urlpatterns = [
    # для учеников
    path("<int:course_pk>/promo/", CoursePromoView.as_view(), name="promo"), # главная страница курса
    path("<int:course_pk>/syllabus/", index, name="syllabus"), # учебный план курса
    path("lesson/<int:lesson_pk>/", LessonView.as_view(), name="lesson"), # прохождение урока
    path("lesson/<int:lesson_pk>/<slug:lesson_slug>/", LessonViewWithSlug.as_view(), name="lesson_with_slug"),
    
    # для преподавателей
    # path("my_courses/", index, name="my_courses"),
    path("create/", CreateCourseView.as_view(), name="create"),
    path("<int:course_pk>/edit/", EditCourseView.as_view(), name="edit"), # редактирование основных моментов курса: заголовка, описания, публикации и т.п.
    path("<int:course_pk>/edit_content/", EditContentOfCourseView.as_view(), name="edit_content"),
    path("subchapter/<int:subchapter_pk>/edit_lessons/", EditContentOfSubchapterView.as_view(), name="edit_content_of_subchapter")

    # добавление, редактирование и удаление контента из урока
    # TODO: поиск по тегам (стр. 132)
]
