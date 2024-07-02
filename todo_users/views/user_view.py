from rest_framework import viewsets
from todo_users.models import User
from todo_users.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer