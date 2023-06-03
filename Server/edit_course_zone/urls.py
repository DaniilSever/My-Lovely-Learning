from django.urls import path
from .views import *

app_name = 'courses'

urlpatterns = [
    # path("", index, name=''),
    
    # для учеников
    path("<int:course_pk>/promo/", index, name="promo"), # главная страница курса
    # TODO: как на stackoverflow: после pk указывается ещё и slug (/1/vvedenie-v-python/promo)
    
    path("<int:course_pk>/syllabus/", index, name="syllabus"), # учебный план курса
    path("<int:course_pk>/lesson/<int:lesson_pk>/", index, name="lesson"), # прохождение урока
    
    # для преподавателей
    # path("my_courses/", index, name="my_courses"),
    path("create/", CreateCourseView.as_view(), name="create"),
    path("<int:course_pk>/edit/", EditCourseView.as_view(), name="edit"), # редактирование основных моментов курса: заголовка, описания, публикации и т.п.
    path("<int:course_pk>/edit_content/", index, name="edit_content"),
    path("<int:course_pk>/delete/", index, name="delete"),
    path("add_chapter/", index, name="add_chapter"),
    path("add_subchapter/", index, name="add_subchapter"),
    path("<int:course_pk>/add_lesson/", index, name="add_lesson"),
    path("<int:course_pk>/lesson/<int:lesson_pk>/edit/", index, name="edit_lesson"), # редактирование урока

    # добавление, редактирование и удаление контента из урока
    # TODO: поиск по тегам (стр. 132)
]
