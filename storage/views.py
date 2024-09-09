from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import UploadedFile
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_files')  # Перенаправление после успешной загрузки
    else:
        form = UploadFileForm()
    return render(request, 'storage/upload_file.html', {'form': form})
@login_required
def list_files(request):
    files = UploadedFile.objects.all()
    return render(request, 'storage/list_files.html', {'files': files})
@login_required
def download_file(request, id):
    file = UploadedFile.objects.get(id=id)
    response = HttpResponse(file.file.read())
    response['Content-Disposition'] = f'attachment; filename="{file.title}"'
    return response
@login_required
def delete_file(request, id):
    file = UploadedFile.objects.get(id=id)
    file.delete()
    return redirect('list_files')
