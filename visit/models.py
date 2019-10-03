from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Visit(models.Model):
    visitor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    login_date = models.DateTimeField(
            default=timezone.now)
    logout_date = models.DateTimeField(
            default=timezone.now)
