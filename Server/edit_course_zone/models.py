from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from taggit.managers import TaggableManager
from .utils.fields import *

lesson_content_types = ('text', 'table', 'code', 'video',
                        'image', 'file', 'test', 'writeaprogram')

class Course(models.Model):
    class VisibilityChoice(models.TextChoices):
        PRIVATE = "PR", "Никому"
        FOR_CLASSES = "FC", "Только моим классам"
        PUBLIC = "PB", "Всем"
    
    owners = models.ManyToManyField(User, related_name='created_courses', verbose_name="Владельцы")
    slug = models.SlugField(unique=False, blank=True, null=True)
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    tags = TaggableManager(blank=True, verbose_name="Теги курса")
    header_photo = models.ImageField(blank=True, null=True, verbose_name="Шапка курса")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated = models.DateTimeField(auto_now=True, verbose_name="Обновлён")
    visibility = models.CharField(max_length=2, choices=VisibilityChoice.choices, default=VisibilityChoice.PRIVATE, 
                                 verbose_name="Кому виден курс")
    
    class Meta:
        ordering = ["-updated"]
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("courses:promo", kwargs={"course_pk": self.pk})
    
    def get_edit_url(self):
        return reverse("courses:edit", kwargs={"course_pk": self.pk})

class Chapter(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="chapters", verbose_name="Курс")
    title = models.CharField(max_length=255, verbose_name="Заголовок главы")
    order = OrderField(blank=True, null=True, for_fields=['course'])
    
    class Meta:
        ordering = ['course_id', 'order']
        verbose_name = 'Главу'
        verbose_name_plural = 'Главы'
    
    def __str__(self):
        return f'Курс {self.course.title}. Глава № {self.order} - {self.title}'

class Subchapter(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name="subchapters", verbose_name="Глава")
    title = models.CharField(max_length=255, verbose_name="Заголовок подраздела")
    order = OrderField(blank=True, null=True, for_fields=['chapter'])
    
    class Meta:
        ordering = ['order']
        verbose_name = 'Подраздел'
        verbose_name_plural = 'Подразделы'
    
    def __str__(self):
        return f'Курс {self.chapter.course.title}. Глава {self.chapter.title}. \
            Подраздел № {self.order} - {self.title}'

class Lesson(models.Model):
    subchapter = models.ForeignKey(Subchapter, related_name="lessons",
                                   on_delete=models.CASCADE, verbose_name="Подраздел")
    theme = models.CharField(max_length=255, verbose_name="Тема урока")
    slug = models.SlugField(unique=False)
    order = OrderField(blank=True, for_fields=['subchapter'])
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создан в")
    updated = models.DateTimeField(auto_now=True, verbose_name="Изменён в")
    
    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ['order']
    
    def __str__(self):
        return f'Курс {self.subchapter.chapter.course.title}. \
            Глава {self.subchapter.chapter.title}. \
            Подраздел {self.subchapter.title}. \
            Урок № {self.order} - {self.theme}'
    
    def get_absolute_url(self):
        return reverse("courses:lesson", kwargs={"lesson_pk": self.pk,
                                                 "course_pk": self.subchapter.chapter.course.pk})

class LessonContent(models.Model):
    lesson = models.ForeignKey(Lesson, related_name='contents', on_delete=models.CASCADE, verbose_name="Урок")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,
                                     limit_choices_to={'model__in': lesson_content_types})
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    order = OrderField(blank=True, for_fields=['lesson'])
    
    class Meta:
        ordering = ['order']
        verbose_name = 'Содержание урока'
        verbose_name_plural = 'Содержания уроков'


class WriteAProgram(models.Model):
    class Meta:
        verbose_name = 'Практическую часть урока - написание программы'
        verbose_name_plural = 'Практические части уроков - написание программ'

class Text(models.Model):
    content = models.TextField()

    class Meta:
        verbose_name = 'Текстовую часть урока'
        verbose_name_plural = 'Текстовые части уроков'
    
    def __str__(self):
        return self.content[:30]

class Code(models.Model):
    """
    Записи из данной таблицы будут иметь особые стили, чтобы указать пользователю, что это код
    """
    class LanguageChoice(models.TextChoices):
        PYTHON = "py", "python"
        GOLANG = "go", "golang"
        RUST = "rs", "rust"
        KOTLIN = "kt", "kotlin"
        JAVA = "java", "java"
        C = "c", "c"
        CS = "cs", "cs"
        CPP = "cpp", "cpp"
    
    language = models.CharField(max_length=4, choices=LanguageChoice.choices)
    content = models.TextField()

    class Meta:
        verbose_name = 'Пример кода в уроке'
        verbose_name_plural = 'Примеры кода в уроках'
    
    def __str__(self):
        return f"Код на языке {self.language}: {self.content[:30]}"

class Table(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название таблицы", blank=True, null=True)

    class Meta:
        verbose_name = 'Табличную информацию в уроке'
        verbose_name_plural = 'Табличные информации в уроках'
    
    def __str__(self):
        return self.name or super().__str__()

class TableContent(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE, verbose_name='Таблица')
    order = OrderField(blank=True, for_fields=['table'])
    style = models.TextField(verbose_name="Стили, применимые к контенту ячейки")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,
                                     limit_choices_to={'model__in': ('text', 'image')})
    object_id = models.PositiveIntegerField()
    content = GenericForeignKey('content_type', 'object_id')
    
    class Meta:
        ordering = ['order']
        verbose_name = 'Содержимое таблицы'
        verbose_name_plural = 'Содержимое таблиц'
    
    def __str__(self):
        table_name = self.table.name
        # TODO: вывод имени таблицы и содержимого
        # if self.content.__class__ is Text:
        #     content = self.content.
        return table_name

class Test(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название теста', blank=True, null=True)

    class Meta:
        verbose_name = 'Тест на уроке'
        verbose_name_plural = 'Тесты на уроках'
    
    def __str__(self):
        return self.name or super().__str__()

class TestContent(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name="Тест")
    
    class Meta:
        abstract = True

class TestQuestion(TestContent):
    question = models.CharField(max_length=255, verbose_name="Вопрос")
    order = OrderField(for_fields=['question'])
    
    class Meta:
        ordering = ['order']
        verbose_name = 'Вопрос из теста'
        verbose_name_plural = 'Вопросы из тестов'

class TestAnswer(TestContent):
    answer = models.CharField(max_length=255, verbose_name="Ответ", blank=True, null=True)
    order = OrderField(for_fields=['answer'])
    is_correct = models.BooleanField(default=False, verbose_name='Верный ответ')
    
    class Meta:
        ordering = ['order']
        verbose_name = 'Ответ в тесте'
        verbose_name_plural = 'Ответы в тестах'

class TestImageAttachment(models.Model):
    image = models.ImageField(upload_to="images")
    uploaded = models.DateTimeField(auto_now_add=True, verbose_name="Загружено")
    
    class Meta:
        ordering = ['uploaded']
        abstract = True

class QuestionAttachment(TestImageAttachment):
    question = models.ForeignKey(TestQuestion, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Вложение к вопросу'
        verbose_name_plural = 'Вложения к вопросам'

class AnswerAttachment(TestImageAttachment):
    answer = models.ForeignKey(TestAnswer, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Вложение к ответу'
        verbose_name_plural = 'Вложения к ответам'

class File(models.Model):
    file = models.FileField(upload_to='files')

    class Meta:
        verbose_name = 'Файл к уроку'
        verbose_name_plural = 'Файлы к урокам'

class Image(models.Model):
    file = models.ImageField(upload_to='images')

    class Meta:
        verbose_name = 'Картинку к уроку'
        verbose_name_plural = 'Картинки к урокам'

class Video(models.Model):
    url = models.URLField(verbose_name="URL ссылка на видео с онлайн-сервисов")

    class Meta:
        verbose_name = 'Видеоматериал к уроку'
        verbose_name_plural = 'Видеоматериалы к урокам'

class CourseParticipant(models.Model):
    participant = models.ForeignKey(User, on_delete=models.CASCADE, related_name="participates", verbose_name="Участник")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="participants", verbose_name="Курс")

    class Meta:
        verbose_name = 'Участника курса'
        verbose_name_plural = 'Участники курсов'
    
    def __str__(self):
        return f"Участник \
            {self.participant.get_full_name() or self.participant.username} \
                курса {self.course}"