from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.

def index(request):
    Task = Tasks.objects.all()

    form = TaskForm()    
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {"Task":Task, "Form":form}
    return render(request, 'ToDo/lists.html', context)

def updateTask(request, pk):
    task = Tasks.objects.get(id=pk)

    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect ('/')
    
    context = {'form': form}
    return render(request, 'ToDo/update_task.html', context)

def deleteTask(request, pk):
    item = Tasks.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect('/')
    context = {'item':item}
    return render(request, 'ToDo/delete.html', context)
