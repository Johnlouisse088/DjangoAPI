from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=255, null=True)
    completed = models.BooleanField(max_length=255, null=True)


