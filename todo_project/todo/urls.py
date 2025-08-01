from django.urls import path

from . import views

urlpatterns = [
    path("add/",views.taskList,name="task_list"),
    path('',views.addTask,name='add_task'),
    path('complete/<int:pk>',views.completeTask,name="complete_task"),
    path('edit/<int:pk>',views.editTask,name="edit_task"),
    path('delete/<int:pk>',views.deleteTask,name="delete_task")

]