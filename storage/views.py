from django.shortcuts import render, redirect, get_object_or_404
from .forms import UploadFileForm
from .models import UploadedFile
from django.contrib.auth.decorators import login_required
import os
from django.http import HttpResponse, Http404

@login_required
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('list_files')  # Перенаправление после успешной загрузки
    else:
        form = UploadFileForm()
    return render(request, 'storage/upload_file.html', {'form': form})

@login_required
def list_files(request):
    files = UploadedFile.objects.filter(user=request.user)
    return render(request, 'storage/list_files.html', {'files': files})

@login_required
def download_file(request, id):
    # Получаем объект UploadedFile по id
    uploaded_file = get_object_or_404(UploadedFile, id=id)
    file_path = uploaded_file.file.path  # Получаем полный путь к файлу

    if uploaded_file.user != request.user:
        raise Http404("Access denied")

    file_path = uploaded_file.file.path

    if not os.path.exists(file_path):
        raise Http404("File does not exist")

    try:
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/octet-stream")
            response['Content-Disposition'] = f'attachment; filename={os.path.basename(file_path)}'
            return response
    except IOError:
        raise Http404("File does not exist")

@login_required
def delete_file(request, id):
    file = get_object_or_404(UploadedFile, id=id)
    if file.user == request.user:
        file.delete()
        return redirect('list_files')
    else:
        raise Http404("Access denied")