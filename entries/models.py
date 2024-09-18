from django.db import models
from django.conf import settings


class entries(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)


    class Meta:   #Склоняет имя модели в ед и мн числе в (админе)
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'

    def __str__(self):
        return self.title