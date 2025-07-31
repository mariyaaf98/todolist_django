from django.shortcuts import render,redirect
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