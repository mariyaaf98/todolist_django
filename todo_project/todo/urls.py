from django.urls import path

from . import views

urlpatterns = [
    path("add/",views.taskList,name="task_list"),
    path('',views.addTask,name='add_task'),


]