from django.db import models

class Author_table(models.Model):
    name = models.CharField(max_length=30)

class Course_table(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    description = models.TextField(blank=False)
    tags = models.CharField(max_length=255)
    by = models.ForeignKey(Author_table, on_delete = models.CASCADE)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)


class Tasks_table(models.Model):
    by = models.ForeignKey(Author_table, on_delete = models.CASCADE)
    question = models.TextField(blank=False)
    answer = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

class all_patch(models.Model):
    title = models.DateField()
    content = models.TextField(blank=False)