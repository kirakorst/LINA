from django.shortcuts import render, redirect, get_object_or_404
from .models import entries

def note_list(request):
    notes = entries.objects.all()
    return render(request, 'entries/note_list.html', {'notes': notes})

def note_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        entries.objects.create(title=title, content=content)
        return redirect('note_list')
    return render(request, 'entries/note_form.html')

def note_edit(request, note_id):
    note = get_object_or_404(entries, id=note_id)  # Получаем заметку по ID
    if request.method == 'POST':
        note.title = request.POST['title']
        note.content = request.POST['content']
        note.save()  # Сохраняем изменения
        return redirect('note_list')  # Перенаправляем на список заметок
    return render(request, 'entries/note_form.html', {'note': note})

def note_delete(request, note_id):
    note = get_object_or_404(entries, id=note_id)
    if request.method == 'POST':
        note.delete()  # Удаляем заметку
        return redirect('note_list')  # Перенаправляем на список заметок
    return render(request, 'entries/note_confirm_delete.html', {'note': note})  # Подтверждение удаления

def note_detail(request, note_id):
    note = get_object_or_404(entries, id=note_id)
    return render(request, 'entries/note_detail.html', {'note': note})