from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from .serializers import TaskSerializer
from ...models import Task
from rest_framework.permissions import IsAuthenticated

class TaskListApiView(ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user)
        return queryset
    

class TaskDetailApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user)
        return queryset
