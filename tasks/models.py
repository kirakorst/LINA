import datetime
from django.conf import settings
from django.contrib.auth.models import User

from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    status = models.CharField(max_length=20, verbose_name="Статус", choices=[
        ('Новая', 'Новая'),
        ('В процессе', 'В процессе'),
        ('Выполнена', 'Выполнено'),
    ], default='Новая')
    due_date = models.DateField(default=datetime.datetime.now(),verbose_name="Дата", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null = True, blank = True)


    class Meta:   #Склоняет имя модели в ед и мн числе в (админе)
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.title