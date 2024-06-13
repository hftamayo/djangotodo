from django.db import models
from django.utils import timezone

class Role(models.Model):
    ROLE_CHOICES = [
        ('ADMIN', 'admin'),
        ('SUPERVISOR', 'supervisor'),
        ('USER', 'user'),
    ]

    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    role_type = models.CharField(max_length=20, choices=ROLE_CHOICES, default='USER')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'roles'
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'
        ordering = ('-created_at', )