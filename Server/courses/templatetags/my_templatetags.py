from django import template
from courses.models import *

register = template.Library()

@register.filter
def get_chapters(value):
    return Chapter.objects.filter(course=value.subchapter.chapter.course.pk)

@register.filter
def get_subchapters(value):
    return Subchapter.objects.filter(chapter=value.pk)

@register.filter
def get_course_title(value):
    return value.subchapter.chapter.course.title

@register.filter
def get_first_lesson_url(value):
    return reverse("courses:lesson", kwargs={"lesson_pk": value.lessons.first().pk})
