from django.db import models

class all_patch(models.Model):
    title = models.DateField()
    content = models.TextField(blank=False)