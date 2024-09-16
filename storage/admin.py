from django.contrib import admin
from .models import UploadedFile


@admin.register( UploadedFile )
class UploadedFileAdmin( admin.ModelAdmin ):
    list_display = ['title', 'file', 'uploaded_at', 'user']
