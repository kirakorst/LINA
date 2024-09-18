from django.contrib import admin
from .models import entries


@admin.register( entries )
class Entries(admin.ModelAdmin):
    list_display = ['title', 'content', 'user']