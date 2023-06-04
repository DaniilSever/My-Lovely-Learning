from django.db import models
from django.contrib.auth.models import User
from courses.models import Course, Lesson

class CourseProgress(models.Model):
    course = models.ForeignKey(Course, related_name="progress", on_delete=models.CASCADE, verbose_name="Прогресс прохождения курса")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Урок')
    tries_count = models.PositiveIntegerField(default=0, verbose_name="Количество попыток")
    lesson_passed = models.BooleanField(default=False, verbose_name="Урок пройден")