from django.shortcuts import render,redirect,get_object_or_404
from . models import Task 

def addTask(request):
    if request.method=="POST":
        title=request.POST.get("title")

        if title:
            Task.objects.create(title=title)
        return redirect('task_list')
    return render(request,'todo_list.html')

def taskList(request):
    tasks=Task.objects.all().order_by('created_at')
    return render(request,'todo_list.html',{'tasks':tasks})


def completeTask(request,pk):
    task=get_object_or_404(Task,id=pk)
    task.completed=not task.completed
    task.save()
    return redirect('task_list')


def deleteTask(request,pk):
    task=get_object_or_404(Task,id=pk)
    task.delete()
    return redirect('task_list')

def editTask(request, pk):
    task = get_object_or_404(Task, id=pk)
    tasks = Task.objects.all() 

    if request.method == "POST":
        task.title = request.POST.get('title')
        task.save()
        return redirect('task_list') 

    return render(request, 'todo_list.html', {'tasks': tasks, 'edit_task': task})



