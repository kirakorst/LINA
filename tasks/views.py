from django.shortcuts import render,redirect
from tasks.models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})
@login_required
def task_detail(request, pk):
    task = Task.objects.get(pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task})
@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})
@login_required
def task_update(request, pk):
    task = Task.objects.get(pk=pk)
    if task.user != request.user:
        return redirect('task_list')
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})
@login_required
def task_delete(request, pk):
    task = Task.objects.get(pk=pk)
    if task.user != request.user:
        return redirect('task_list')
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/confirm_delete.html', {'task': task})

@login_required
def task_accept(request, pk):
    task = Task.objects.get(pk=pk)
    if task.user != request.user:
        return redirect('task_list')
    task.status = 'В процессе'
    task.save()
    return redirect('task_detail', pk=task.pk)

@login_required
def task_complete(request, pk):
    task = Task.objects.get(pk=pk)
    if task.user != request.user:
        return redirect('task_list')
    task.status = 'Выполнена'
    task.save()
    return redirect('task_detail', pk=task.pk)