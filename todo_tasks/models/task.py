from django.db import models
from django.utils import timezone

class Task(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'tasks'
        verbose_name = 'Tasks'
        verbose_name_plural = 'Tasks'
        ordering = ('-created_at', )