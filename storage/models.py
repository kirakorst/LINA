from django.db import models
from django.conf import settings



class UploadedFile(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    file = models.FileField(upload_to='files/', verbose_name="Файл")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата загрузки")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Пользователь")

    def __str__(self):
        return self.title