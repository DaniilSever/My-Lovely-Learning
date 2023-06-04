from typing import Any
from django import forms
from .models import *
from .forms import *
from django.forms.models import BaseInlineFormSet, inlineformset_factory

SubchapterLessonFormset = inlineformset_factory(Subchapter, Lesson, \
    fields=('theme',), extra=2)

class BaseSubchapterWithLessonsFormset(BaseInlineFormSet):
    def add_fields(self, form: Any, index: Any) -> None:
        super().add_fields(form, index)
        form.nested = SubchapterLessonFormset(
            instance=form.instance,
            data=form.data if form.is_bound else None,
            files=form.files if form.is_bound else None,
            prefix=f"lesson-{form.prefix}-{SubchapterLessonFormset.get_default_prefix()}"
        )


# ChapterSubchapterFormset = inlineformset_factory()



class CreateCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["title", "description", "visibility"]
        # widgets = {
        #     "tags": forms.CharField(attrs={"required": False}),
        #     "header_photo": forms.FileField(required=False),
        # }

class EditCourseForm(forms.ModelForm):   
    class Meta:
        model = Course
        fields = ['title', 'description', 'tags', 'header_photo', 'visibility']


def is_empty_form(form):
    """
    A form is considered empty if it passes its validation,
    but doesn't have any data.

    This is primarily used in formsets, when you want to
    validate if an individual form is empty (extra_form).
    """
    if form.is_valid() and not form.cleaned_data:
        return True
    else:
        # Either the form has errors (isn't valid) or
        # it doesn't have errors and contains data.
        return False


def is_form_persisted(form):
    """
    Does the form have a model instance attached and it's not being added?
    e.g. The form is about an existing Book whose data is being edited.
    """
    if form.instance and not form.instance._state.adding:
        return True
    else:
        # Either the form has no instance attached or
        # it has an instance that is being added.
        return False