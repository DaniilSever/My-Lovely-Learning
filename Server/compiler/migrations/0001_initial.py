# Generated by Django 4.1.7 on 2023-06-04 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompiledCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('py', 'python'), ('go', 'golang'), ('rs', 'rust'), ('kt', 'kotlin'), ('java', 'java'), ('c', 'c'), ('cs', 'cs'), ('cpp', 'cpp')], max_length=4, verbose_name='Язык программирования')),
                ('user_code', models.TextField(verbose_name='Код от пользователя')),
                ('errors', models.TextField(blank=True, null=True, verbose_name='Ошибки из терминала')),
                ('result', models.TextField(blank=True, null=True, verbose_name='Результат отработанного кода')),
                ('code_execution_start', models.DateTimeField(verbose_name='Начало выполнения кода')),
                ('code_execution_end', models.DateTimeField(verbose_name='Конец выполнения кода')),
            ],
            options={
                'verbose_name': 'Скомпилированный код',
                'verbose_name_plural': 'Скомпилированные коды',
            },
        ),
    ]