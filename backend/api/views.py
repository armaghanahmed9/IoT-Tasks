from django.shortcuts import render  # Import the 'render' function for generating HTML templates
from django.http import JsonResponse  # Import the 'JsonResponse' class for creating JSON responses
import json  # Import the 'json' module for working with JSON data
from .iot import start_iot_simulation  # Import the simulation function from your 'iot' module

# Simulation Startup
#---------------------
# Immediately start the IoT simulation when the Django server initializes.
start_iot_simulation() 


# View Function for Device List Retrieval
#----------------------------------------
def get_device_list(request):
    """
    This view function fetches a list of IoT devices and their status data.
    It returns this data in JSON format for easy consumption by the frontend.
    """

    # Dummy Device Data (Replace with Real Data in Production)
    #----------------------------------------------------------
    device_data = [
        { 'device_id': 1, 'status': 'Online', 'temperature': 25.5, 'humidity': 50 },
        { 'device_id': 2, 'status': 'Offline', 'temperature': 22.8, 'humidity': 48 },
        # ... more device data (In a real scenario, fetch this from a database or API)
    ]

    # Return JSON Response
    #-----------------------
    return JsonResponse(device_data, safe=False) 
    # safe=False allows returning lists (not just dictionaries) as the top-level JSON object.