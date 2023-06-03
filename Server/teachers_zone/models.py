from django.db import models
from django.contrib.auth.models import User
from edit_course_zone.models import Course

class ClassRoom(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Наименование класса")
    class_teacher = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Преподаватель класса")
    
    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'
    
    def __str__(self):
        if self.name:
            return f"{self.class_teacher.get_full_name()}. {self.name}"
        else:
            return self.class_teacher.get_full_name()

class ClassContent(models.Model):
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE, verbose_name="Класс")
    student = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Студент")
    
    class Meta:
        verbose_name = 'Состав класса'
        verbose_name_plural = 'Составы классов'

class Grade(models.Model):
    rated_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="Кем оценено")
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, verbose_name="Курс")
    student = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="rates", verbose_name="Ученик")
    rate = models.PositiveIntegerField(help_text="_/100 %")
    rate_created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время оценки")
    rate_updated_at = models.DateTimeField(auto_now=True, verbose_name="Время изменения оценки")