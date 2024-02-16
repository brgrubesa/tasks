# Flask Unauthorized Sales Detection API

## Description
This Flask application provides a REST API endpoint for detecting unauthorized sales transactions from provided datasets of product listings and actual sales records.

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

2. Send a POST request to the `/detect-unauthorized-sales` endpoint with JSON data containing product listings and sales transactions.

    Example using cURL:
    ```bash
    curl -i -X POST -H "Content-Type: application/json" -d "{\"productListings\": [{\"productID\": \"123\", \"authorizedSellerID\": \"A1\"}], \"salesTransactions\": [{\"productID\": \"123\", \"sellerID\": \"B2\"}]}" http://127.0.0.1:5000/detect-unauthorized-sales
    ```

## API Endpoint
- `/detect-unauthorized-sales`
  - Method: POST
  - Accepts JSON data with product listings and sales transactions.
  - Returns JSON response containing unauthorized sales transactions.

## Dependencies
- Flask: 2.0.1
