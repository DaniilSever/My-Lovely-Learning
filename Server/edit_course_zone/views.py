from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.urls import reverse, reverse_lazy, resolve
from django.views.generic import TemplateView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .forms import *
from .models import *
from teachers_zone.mixins import *
from .mixins import *

def index(request):
    if request.is_ajax():
        pass

class CreateCourseView(LoginRequiredMixin, CreateView):
    model = Course
    template_name = 'courses/create_course.html'
    form_class = CreateCourseForm
    
    def form_valid(self, form):
        self.object = form.save()
        self.object.owners.add(self.request.user)
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse("courses:edit", kwargs={"course_pk": self.object.pk})

class EditCourseView(OwnerEditMixin, LoginRequiredMixin, UpdateView):
    model = Course
    pk_url_kwarg = "course_pk"
    template_name = 'courses/edit_course.html'
    fields = ['title', 'description', 'tags', 'header_photo', 'visibility']
    success_url = reverse_lazy('teaching:home')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["course_pk"] = resolve(self.request.path).kwargs.get("course_pk")
        return context

class EditContentOfCourseView(TemplateView):
    template_name = "courses/edit_content.html"
    pk_url_kwarg = "course_pk"
