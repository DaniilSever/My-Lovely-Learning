from django.db import models
from courses.models import Lesson
from courses.models import Code
from django.contrib.auth.models import User
from django.utils.timesince import timesince

class CompiledCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name="Урок", blank=True, null=True)
    language = models.CharField(choices=Code.LanguageChoice.choices, max_length=4, verbose_name='Язык программирования')
    user_code = models.TextField(verbose_name="Код от пользователя")
    errors = models.TextField(blank=True, null=True, verbose_name="Ошибки из терминала")
    result = models.TextField(blank=True, null=True, verbose_name="Результат отработанного кода")
    code_execution_start = models.DateTimeField(verbose_name="Начало выполнения кода")
    code_execution_end = models.DateTimeField(verbose_name="Конец выполнения кода")
    
    class Meta:
        verbose_name = 'Скомпилированный код'
        verbose_name_plural = 'Скомпилированные коды'
    
    def get_execution_time_delta(self):
        return (self.code_execution_end - self.code_execution_start).total_seconds()


# TODO: linux среда для различных задач. docker_image_id