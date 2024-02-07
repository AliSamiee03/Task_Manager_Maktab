from django.shortcuts import render
from .models import Category, Tag, Task

def all_tasks_view(request):
    tasks = Task.objects.filter(creator = request.user)
    content = {'tasks': tasks}
    print(content)
    return render(request, 'Tasks/show-all-tasks.html', content)

def show_detail_view(request, task_id):
    task = Task.objects.get(id=task_id)
    tags = Tag.objects.filter(task__title = task.title)
    content = {'task': task, 'tags': tags}
    return render(request, 'Tasks/see-more.html', content)