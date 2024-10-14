from django.db import models
from django.utils import timezone
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.conf import settings

from typing import Optional


class DrivingData(models.Model):
    pass
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # overall_average_travel_time_in_min = models.IntegerField(default=0)
    overall_average_fuel_consumption = models.IntegerField(null=True, blank=True)
    overall_average_electric_consumption = models.IntegerField(null=True, blank=True)
    # overall_average_speed_in_kmph = models.IntegerField(default=0)
    # total_distance_traveled = models.IntegerField(default=0)
    # number_of_hard_brakes_per_1000km = models.IntegerField(default=0)
    # number_of_rash_drives_per_1000km = models.IntegerField(default=0)

    def __str__(self):
        return f"DrivingData for {self.user.username}"