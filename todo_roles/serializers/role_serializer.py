# roles/role_serializer.py
from rest_framework import serializers
from todo_roles.models import Role

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name', 'description']