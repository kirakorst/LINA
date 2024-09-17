# Generated by Django 5.1 on 2024-09-17 05:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0004_rename_owner_uploadedfile_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedfile',
            name='file',
            field=models.FileField(upload_to='files/', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='uploadedfile',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='uploadedfile',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки'),
        ),
        migrations.AlterField(
            model_name='uploadedfile',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
