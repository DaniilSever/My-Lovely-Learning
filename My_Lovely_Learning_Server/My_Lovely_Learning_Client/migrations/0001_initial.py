# Generated by Django 4.1.7 on 2023-04-07 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('user_nickname', models.CharField(max_length=30, unique=True)),
                ('user_email', models.EmailField(max_length=254)),
                ('user_password', models.CharField(max_length=32)),
                ('user_sign', models.BooleanField(default=False)),
            ],
        ),
    ]