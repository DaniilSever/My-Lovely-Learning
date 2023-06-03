from typing import Any
from django import forms
from .models import *
from .utils.forms import *
from django.forms.models import BaseInlineFormSet, inlineformset_factory
from edit_course_zone.models import Course

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
    title = forms.CharField(label='Название курса:', widget=forms.TextInput(attrs={'class': 'course-input', 'placeholder': 'Название...'}))
    description = forms.CharField(label='Описание курса:', widget=forms.Textarea(attrs={'class': 'course-inputarea', 'placeholder': 'Описание...'}))
    visibility = forms.CharField(label='Кому виден:', widget=forms.Select(attrs={'class': 'course-select'}, choices=Course.VisibilityChoice.choices))
    
    class Meta:
        model = Course
        fields = ["title", "description", "visibility"]
        # widgets = {
        #     "tags": forms.CharField(attrs={"required": False}),
        #     "header_photo": forms.FileField(required=False),
        # }

class EditCourseForm(forms.ModelForm):
    title = forms.CharField(label='Название курса:', widget=forms.TextInput(attrs={'class': 'course-input', 'placeholder': 'Название...'}))
    description = forms.CharField(label='Описание курса:', widget=forms.Textarea(attrs={'class': 'course-inputarea', 'placeholder': 'Описание...'}))
    tags = forms.CharField(label='Название курса:', widget=forms.TextInput(attrs={'class': 'course-input', 'placeholder': 'Название...'}))
    header_photo = forms.CharField(label='Название курса:', widget=forms.FileInput(attrs={'class': 'course-input',}))
    visibility = forms.CharField(label='Кому виден:', widget=forms.Select(attrs={'class': 'course-select'}, choices=Course.VisibilityChoice.choices))

    class Meta:
        model = Course
        fields = ["title", "description", "tags", "header_photo", "visibility"]
