from rest_framework import viewsets
from todo_roles.models import Role
from todo_roles.serializers import RoleSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer