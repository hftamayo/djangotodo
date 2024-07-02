from rest_framework import serializers
from todo_users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password', 'age', 'created_at', 'updated_at']