# Generated by Django 4.1.7 on 2023-04-28 23:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_all_patch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course_table',
            name='by',
        ),
        migrations.RemoveField(
            model_name='tasks_table',
            name='by',
        ),
        migrations.DeleteModel(
            name='Author_table',
        ),
        migrations.DeleteModel(
            name='Course_table',
        ),
        migrations.DeleteModel(
            name='Tasks_table',
        ),
    ]
