from django.urls import path

from TasksAPP.views import index, create_task, delete_task

urlpatterns = [
    path('', index, name='HomePage'),
    path('create/', create_task, name='CreateTask'),
    path('tasks/delete/<int:task_id>/', delete_task, name='DeleteTask')
]
