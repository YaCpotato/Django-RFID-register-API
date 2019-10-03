from django.db import models
from django.utils import timezone

class User(models.Model):
    name = models.CharField(max_length=200)
    password = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
