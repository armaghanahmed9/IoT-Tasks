import threading          # For running the IoT simulation in a separate thread
import json               # For working with JSON data (messages)
from azure.iot.device import IoTHubDeviceClient, Message  # Azure IoT SDK imports
from django.conf import settings   # For accessing settings (e.g., connection string)
import random            # For generating simulated temperature and humidity
import time              # For controlling the telemetry sending interval

# Azure IoT Hub Connection String
# -------------------------------
CONNECTION_STRING = settings.AZURE_IOT_CONNECTION_STRING  # Retrieve from Django settings


# Message Listener (Command Handler)
# -----------------------------------
def message_listener(message):
    """
    Callback function to handle incoming cloud-to-device (C2D) messages.
    This function parses the message, looks for specific commands, and takes appropriate actions.
    """

    print("Message received:")
    print(message.data)
    
    try:
        command_data = json.loads(message.data)  # Parse JSON data from message
        command_name = command_data.get("command")  # Get the command name

        # Command Handling
        # -----------------
        if command_name == "setReportingFrequency":
            new_frequency = command_data.get("frequency", 10)  # Default to 10 seconds if not provided
            print(f"Setting reporting frequency to {new_frequency} seconds")
            global TELEMETRY_INTERVAL   # Modify the global telemetry interval
            TELEMETRY_INTERVAL = new_frequency
        elif command_name == "toggleLed":  
            led_state = command_data.get("state", False)
            print(f"Toggling LED state to {'ON' if led_state else 'OFF'}") 
        else:
            print("Unknown command received")
    
    except json.JSONDecodeError:  # Handle JSON parsing errors
        print("Error decoding JSON command")


# Global Telemetry Sending Interval (Seconds)
# --------------------------------------------
TELEMETRY_INTERVAL = 10  # Initial telemetry sending interval (10 seconds)


# IoT Hub Client Initialization
# ------------------------------
def iothub_client_init():
    """
    Creates and returns an IoT Hub Device Client instance.
    Sets up the message listener for C2D commands.
    """
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    client.on_message_received = message_listener  # Register message listener
    return client


# Telemetry Simulation Loop
# --------------------------
def iothub_client_telemetry_sample_run():
    """
    Main function for the telemetry simulation.
    Continuously sends simulated temperature and humidity data to the IoT Hub.
    Handles KeyboardInterrupt for graceful shutdown.
    """

    try:
        client = iothub_client_init()  # Initialize IoT Hub client
        print("IoT Hub device sending periodic messages")

        while True:
            temperature = random.randint(20, 30)   # Simulate temperature
            humidity = random.randint(40, 60)     # Simulate humidity
            data = {'temperature': temperature, 'humidity': humidity}  # Prepare telemetry data
            msg = Message(json.dumps(data))      # Create a JSON message
            print(f"Sending message: {msg}")
            client.send_message(msg)              # Send the message to IoT Hub
            time.sleep(TELEMETRY_INTERVAL)        # Sleep for the specified interval
    except KeyboardInterrupt:                     # Allow graceful exit with Ctrl+C
        print("IoT Hub Device stopped")



# Simulation Thread Starter
# -------------------------
def start_iot_simulation(): 
    """
    Starts the IoT simulation in a background thread.
    Allows Django to continue handling web requests.
    """
    iot_thread = threading.Thread(target=iothub_client_telemetry_sample_run)
    iot_thread.daemon = True   # Set as daemon thread so it doesn't block server shutdown
    iot_thread.start()          # Start the simulation thread