from django.urls import path
from .views import note_list, note_create, note_edit, note_delete, note_detail

urlpatterns = [
    path('', note_list, name='note_list'),
    path('create/', note_create, name='note_create'),
    path('edit/<int:note_id>/', note_edit, name='note_edit'),  # URL для редактирования
    path('delete/<int:note_id>/', note_delete, name='note_delete'),  # URL для удаления
    path('detail/<int:note_id>/', note_detail, name='note_detail'),
]