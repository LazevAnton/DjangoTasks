from django.shortcuts import render, redirect
from TasksAPP.forms import CreateTaskForm
from TasksAPP.models import Tasks


def index(request):
    tasks = Tasks.objects.order_by('-created_at')
    context = {
        'tasks': tasks,
        'title': 'Tasks'
    }
    return render(request, 'index.html', context)


def create_task(request):
    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('HomePage')
    else:
        form = CreateTaskForm()
    context = {
        'form': form,
        'title': 'CreateTask'
    }
    return render(request, 'create_task.html', context)
