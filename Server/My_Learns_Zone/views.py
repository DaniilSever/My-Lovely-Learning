from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.list import ListView
from courses.models import CourseParticipant
from courses.utils import last_passed_lesson

class LearnCourseListView(ListView):
    model = CourseParticipant
    template_name = 'learning/user_learn_cource.html'
    context_object_name = "courses"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['last_lesson'] = last_passed_lesson(self.request, )
        return context
    
    def get_queryset(self):
        return self.model.objects.filter(participant=self.request.user)