from typing import Any, Dict
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404, redirect
from django.urls import reverse, reverse_lazy, resolve
from django.views.generic import TemplateView, View
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .forms import *
from .models import *
from Teachers_Zone.mixins import *
from .mixins import *
from .utils import recently_viewed


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
        context[self.pk_url_kwarg] = resolve(self.request.path).kwargs.get(self.pk_url_kwarg)
        return context

class EditContentOfCourseView(TemplateView):
    template_name = "courses/edit_content.html"
    pk_url_kwarg = "course_pk"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course_instance'] = get_object_or_404(Course, pk=resolve(self.request.path).kwargs.get(self.pk_url_kwarg))
        return context

class EditContentOfSubchapterView(TemplateView):
    template_name = "courses/edit_subchapter_content.html"
    pk_url_kwarg = "subchapter_pk"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance = get_object_or_404(Subchapter, pk=resolve(self.request.path).kwargs.get(self.pk_url_kwarg))
        context['course_instance'] = instance.chapter.course
        context['course_pk'] = instance.chapter.course.pk
        return context

class CoursePromoView(DetailView):
    model = Course
    template_name = "courses/promo.html"
    pk_url_kwarg = 'course_pk'
    context_object_name = 'course'
    
    def get(self, request, *args, **kwargs):
        recently_viewed(request, kwargs.get(self.pk_url_kwarg))
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.pk_url_kwarg] = self.kwargs.get(self.pk_url_kwarg)
        first_lesson = Lesson.objects.filter(subchapter__chapter__course__pk=self.kwargs.get(self.pk_url_kwarg))\
            .order_by('subchapter__chapter_order').first()
        if first_lesson:
            context['first_lesson_pk'] = first_lesson.pk
        
        return context

class LessonView(DetailView):
    model = Lesson
    pk_url_kwarg = "lesson_pk"
    template_name = 'courses/lesson.html'
    
    def get(self, request, *args, **kwargs):
        lesson_pk = self.kwargs.get(self.pk_url_kwarg)
        lesson_slug = self.model.objects.get(pk=lesson_pk).slug
        my_kwargs = {
            "lesson_pk": lesson_pk,
            "lesson_slug": lesson_slug
        }
        return redirect(reverse("courses:lesson_with_slug", kwargs=my_kwargs))

class LessonViewWithSlug(DetailView):
    model = Lesson
    template_name = 'courses/lesson.html'
    pk_url_kwarg = "lesson_pk"
    context_object_name = 'lesson'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lesson_instance'] = self.get_object()
        context['subchapter_pk'] = context['lesson_instance'].subchapter.pk
        return context