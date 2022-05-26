from django.shortcuts import render, redirect
from .models import TodoModel
from .forms import TaskForm
# Create your views here.


def index(request):
    tasks = TodoModel.objects.all()
    form = TaskForm()
    context = {'tasks': tasks, 'form': form}
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'index.html', context)

def editview(request, pk):
    task = TodoModel.objects.get(id=pk)
    form = TaskForm(instance=task)
    context = {'task': task, 'form':form}

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'update.html', context)


def deleteview(request,pk):
    task = TodoModel.objects.get(id=pk)
    task.delete()
    return redirect('/')
