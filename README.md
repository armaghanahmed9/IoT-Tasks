# IoT Monitoring and Analysis Dashboard

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project demonstrates a real-time IoT monitoring and analysis solution. It collects telemetry data (e.g., temperature, humidity) from simulated devices, visualizes the data, and applies machine learning to classify device status.

## Features

- **Real-time Monitoring:**  View live updates of sensor data from simulated IoT devices.
- **Cloud-to-Device Commands:** Control device behavior (e.g., adjust reporting frequency) using C2D commands.
- **Data Visualization:** Interactive scatter plots visualize the relationship between temperature and humidity.
- **Machine Learning:**  A Random Forest classifier predicts device status (normal/alert) based on telemetry.

## Technologies Used

- **Frontend:** React.js with Material-UI
- **Backend:** Django REST framework

- 
## Project Structure
project_root/
├── frontend/        # React frontend
│   ├── public/
│   ├── src/
│   └── package.json
├── backend/        # Django backend
│   ├── api/
│   │   ├── iot.py     # Azure IoT Hub integration
│   │   ├── views.py
│   │   └── urls.py
│   ├── my_iot_backend/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── manage.py
├── README.md


## Getting Started

### Prerequisites

- Python (3.x)
- Node.js and npm
- Azure account (for IoT Hub simulation)

### Installation

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/](https://github.com/)<your_username>/<your_repo_name>.git

    Backend Setup:
        Navigate to the backend directory.
        Create a virtual environment: python -m venv venv
        Activate the virtual environment:
            Windows: venv\Scripts\activate
            macOS/Linux: source venv/bin/activate
        Install dependencies: pip install -r requirements.txt
        Add your Azure IoT Hub connection string to backend/my_iot_backend/settings.py:
        Python

        AZURE_IOT_CONNECTION_STRING = "your_iot_hub_connection_string"

        Use code with caution.

    Frontend Setup:
        Navigate to the frontend directory.
        Install dependencies: npm install

Running the Application

    Start the Backend:
        From the backend directory, run: python manage.py runserver

    Start the Frontend:
        From the frontend directory, run: npm start
        Open your browser to http://localhost:3000/
