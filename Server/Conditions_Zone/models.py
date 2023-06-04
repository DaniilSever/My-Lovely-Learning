from django.db import models

# Create your models here.
class Conditions_Using(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=False)

class Conditions_Confidentiality(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=False)