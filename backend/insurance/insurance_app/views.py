import json
import os
from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
import subprocess
from .models import DrivingData

GENERATE_BINARY_PATH = "/path/to/first_binary"
VALIDATE_BINARY_PATH = "/path/to/second_binary"

def generate_and_verify_zkproof(request):
    if request.method == "POST":
        try:
            driving_data = DrivingData.objects.first()
            if not driving_data:
                return JsonResponse({"status": "error", "message": "No driving data found"}, status=404)

            # Step 2: Serialize model data to JSON
            driving_data_dict = {
                "overall_average_travel_time_in_min": driving_data.overall_average_travel_time_in_min,
                "overall_average_fuel_consumption": driving_data.overall_average_fuel_consumption,
                "overall_average_electric_consumption": driving_data.overall_average_electric_consumption,
                "overall_average_speed_in_kmph": driving_data.overall_average_speed_in_kmph,
                "total_distance_traveled": driving_data.total_distance_traveled,
                "number_of_hard_brakes": driving_data.number_of_hard_brakes,
                "number_of_night_drives": driving_data.number_of_night_drives,
                "number_of_rash_drives": driving_data.number_of_rash_drives
            }

            # Step 3: Save JSON data to a temporary file
            json_file_path = os.path.join(settings.BASE_DIR, 'temp_data.json')  # Temporary JSON file path
            with open(json_file_path, 'w') as json_file:
                json.dump(driving_data_dict, json_file)

            # Step 4: Run the first binary (ZKProof generation) with the JSON file as input
            generate_result = subprocess.run([GENERATE_BINARY_PATH, json_file_path], capture_output=True, text=True)
            
            if generate_result.returncode != 0:
                return JsonResponse({"status": "error", "message": "Failed to generate ZKProof", "output": generate_result.stderr}, status=500)
            
            # Step 5: Run the second binary (ZKProof validation)
            validate_result = subprocess.run([VALIDATE_BINARY_PATH], capture_output=True, text=True)
            
            if validate_result.returncode == 0:
                # Success: Return both generation and validation outputs
                return JsonResponse({
                    "status": "success", 
                    "generate_output": generate_result.stdout, 
                    "validation_output": validate_result.stdout
                })
            else:
                return JsonResponse({"status": "error", "message": "ZKProof validation failed", "output": validate_result.stderr}, status=500)
        
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)
    
    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=400)