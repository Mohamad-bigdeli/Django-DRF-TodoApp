from django.urls import path
from .views import (TaskListApiView, TaskDetailApiView)

app_name = "api-v1"

urlpatterns = [
    path("tasks/", TaskListApiView.as_view(), name="task-list"),
    path("tasks/<int:pk>/", TaskDetailApiView.as_view(), name="task-detail"),
]