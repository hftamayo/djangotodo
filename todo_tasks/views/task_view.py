from rest_framework import viewsets
from todo_tasks.models import Task
from todo_tasks.serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer