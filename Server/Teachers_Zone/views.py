from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView
from courses.models import Course
from .mixins import ListOwnerMixin

# TODO: в этой вкладке должно содержаться всё, связанное с преподаванием: список курсов, разработанных преподавателем, высланные выполненные задания от учеников и т.п.
class TeachingMainView(LoginRequiredMixin, ListOwnerMixin, ListView):
    model = Course
    template_name = 'teaching/teachers_main.html'
    context_object_name = 'my_courses'
