from django.db import models
from django.utils import timezone
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.conf import settings

from typing import Optional


class DrivingData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_number_1 = models.IntegerField(default=0)
    user_number_2 = models.IntegerField(default=0)
    user_number_3 = models.IntegerField(default=0)
    user_number_4 = models.IntegerField(default=0)

    def __str__(self):
        return f"DrivingData for {self.user.username}"