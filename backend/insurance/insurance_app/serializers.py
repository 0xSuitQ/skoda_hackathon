from rest_framework import serializers
from .models import DrivingData

class DrivingDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrivingData
        fields = [
            'user',
            'overall_average_travel_time_in_min',
            'overall_average_fuel_consumption',
            'overall_average_electric_consumption',
            'overall_average_speed_in_kmph',
            'total_distance_traveled',
            'number_of_hard_brakes_per_1000km',
            'number_of_rash_drives_per_1000km'
        ]