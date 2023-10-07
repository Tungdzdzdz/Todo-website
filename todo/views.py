from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .forms import TaskForm
from .models import Task


def home(request):
    tasks = Task.objects.all().filter(user=request.user)
    return render(request, 'todo/home.html', {'tasks': tasks, 'title_site': 'Home'})


@login_required
def create(request):
    if request.method == 'GET':
        form = TaskForm()
        return render(request, 'todo/update.html', {'form': form, 'title_site': 'Create'})
    elif request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('home')
        return render(request, 'todo/update.html', {'form': form, 'title_site': 'Create'})


@login_required
def update(request, id):
    task = get_object_or_404(Task, id=id)
    if task.user == request.user:
        if request.method == 'GET':
            form = TaskForm(instance=task)
            return render(request, 'todo/update.html', {'form': form, 'title_site': 'Update'})
        elif request.method == 'POST':
            if 'delete' in request.POST:
                task.delete()
                return redirect('home')
            elif 'save' in request.POST:
                form = TaskForm(request.POST, instance=task)
                if form.is_valid():
                    form.save()
                    return redirect('home')
                return render(request, 'todo/update.html', {'form': form, 'title_site': 'Update'})
    return redirect('home')
