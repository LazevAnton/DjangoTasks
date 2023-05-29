from django.urls import path

from TasksAPP.views import index, create_task

urlpatterns = [
    path('', index, name='HomePage'),
    path('create/', create_task, name='CreateTask')
]
