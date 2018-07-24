from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    owner = models.ForeignKey(User, related_name='todos', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    task_name = models.CharField(max_length=100, unique=True)
    deadline = models.DateField()
    completion = models.BooleanField(default=False)

    class Meta:
        ordering = ('created_date',)