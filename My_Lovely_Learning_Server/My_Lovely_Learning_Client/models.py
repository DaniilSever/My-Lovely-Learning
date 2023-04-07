from django.db import models

class User(models.Model):
    user_id = models.IntegerField(auto_created=True, primary_key=True)
    user_nickname = models.CharField(max_length=30, unique=True)
    user_email = models.EmailField(max_length=254)
    user_password = models.CharField(max_length=32)
    user_sign = models.BooleanField(default=False)
    

