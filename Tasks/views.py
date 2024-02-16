from django.shortcuts import render, redirect
from .models import Category, Tag, Task
from .forms import CheckboxForm
from django.contrib.auth.decorators import login_required

@login_required
def all_tasks_view(request):
    tasks = Task.objects.filter(creator = request.user)
    content = {'tasks': tasks}
    return render(request, 'Tasks/show-all-tasks.html', content)

@login_required
def show_detail_view(request, task_id):
    task = Task.objects.get(id=task_id)
    form = CheckboxForm()
    tags = Tag.objects.filter(task__title = task.title)
    content = {'task': task, 'tags': tags, 'form': form}
    return render(request, 'Tasks/see-more.html', content)

@login_required
def task_complete_view(request, task_id):
    task = Task.objects.get(id=task_id, creator=request.user)
    if task.done == "I" :
        task.done = "C"
    else :
        task.done = "I"
    task.save()
    return redirect('all')

@login_required
def show_categories_view(request):
    categories = Category.objects.filter()
    context = {'categories': categories}
    return render(request, 'Tasks/show-categories.html', context)


def show_categories_tasks_view(request, category_id):
    tasks = Task.objects.filter(creator = request.user, category__id = category_id)
    context = {'tasks': tasks}
    return render(request, 'Tasks/show-all-tasks.html', context)