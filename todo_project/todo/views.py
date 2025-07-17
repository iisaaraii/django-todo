from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm  

# View for showing the task list
# def index(request):
#     tasks = Task.objects.all()
#     return render(request, 'todo/list.html', {'tasks': tasks})
from django.views.generic import ListView

class TaskListView(ListView):
    model = Task
    template_name = 'todo/list.html'
    context_object_name = 'tasks'


# View for adding new tasks
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm()
    
    return render(request, 'todo/add_task.html', {'form': form})
