from django import template
from courses.models import *
from courses.models import *
from django.shortcuts import redirect

register = template.Library()

@register.filter
def get_first_lesson(value):
    qs = Lesson.objects.filter(subchapter__chapter__course__pk=value.id)
    f_l = qs.order_by('order').first()
    if f_l is not None:
        return redirect(f_l.get_absolute_url(), lesson_pk=f_l.pk)