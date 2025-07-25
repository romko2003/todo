from django.shortcuts import render, redirect
from config.models import Task
from todo_app.forms import TaskForm


def task_list(request):
    tasks = Task.objects.all().order_by('is_done', '-created_at')
    return render(request, 'todo/task_list.html', {'tasks': tasks})


def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task-list')
    else:
        form = TaskForm()
    return render(request, 'todo/form.html', {'form': form, 'title': 'Create Task'})

