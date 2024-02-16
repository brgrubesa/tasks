# Flask Optimal Job Interview Scheduling API

## Description
This Flask application provides a REST API endpoint for scheduling job interviews and calculating the maximum number of non-overlapping interviews a person can attend.

## Installation
1. Clone the repository:
    ```bash
    git clone <repository_url>
    ```

2. Navigate to the project directory:
    ```bash
    cd <project_directory>
    ```

3. (Optional) Set up a virtual environment (recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Start the Flask server by running the `app.py` file:
    ```bash
    python app.py
    ```

2. Send a POST request to the `/calculate-max-interviews` endpoint with JSON data containing start times and end times of job interviews.

    Example using cURL:
    ```bash
    curl -i -X POST -H "Content-Type: application/json" -d "{\"start_times\": [10, 20, 30, 40, 50, 60], \"end_times\": [15, 25, 35, 45, 55, 65]}" http://127.0.0.1:5000/calculate-max-interviews
    ```

## API Endpoint
- `/calculate-max-interviews`
  - Method: POST
  - Accepts JSON data with start times and end times of job interviews.
  - Returns JSON response containing the maximum number of interviews a person can attend.

## Dependencies
- Flask: 2.0.1
