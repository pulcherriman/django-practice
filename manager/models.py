from django.db import models
from datetime import datetime

class Person(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()

class Task(models.Model):
    client = models.CharField(max_length=128)
    claimant = models.CharField(max_length=128)
    registration_at = models.DateTimeField(default=datetime.now)
    deadline_at = models.DateTimeField(null=True, blank=True)
    summary = models.CharField(max_length=128)
    detail = models.CharField(max_length=1024)
