# import requests
# import logging

# # Setting up logging
# logging.basicConfig(level=logging.INFO)

# # Function to fetch cars
# def get_cars():
#     url = "https://api.dev.tryclaro.com/en/admin/customers/cars/"
#     headers = {
#         "X-Api-Key": "RDq6PLIW.Rb0COjF7RjgPsyKmNzNX1oKXM7thQYIZ",  # Replace with your actual API key
#     }
    
#     cars = []
#     while url:
#         try:
#             response = requests.get(url, headers=headers, timeout=10)  # Added timeout
#             response.raise_for_status()  # Check for any HTTP errors

#             # Log full response for debugging purposes
#             logging.info(f"Response Status Code: {response.status_code}")
#             logging.info(f"Response Body: {response.text}")  # Log the full response body

#             # Check if response is in JSON format
#             if "application/json" in response.headers.get("Content-Type", ""):
#                 try:
#                     cars_json = response.json()  # Ensure the response is in JSON format

#                     if 'results' in cars_json:
#                         # Check if there are any cars in the results
#                         if cars_json['results']:
#                             cars.extend([
#                                 {
#                                     "car_name": car.get("name"),
#                                     "uuid": car.get("uuid"),
#                                     "model": car.get("model"),
#                                     "brand": car.get("brand"),
#                                     "year": car.get("year")
#                                 }
#                                 for car in cars_json['results'] if car.get("name")
#                             ])
#                         else:
#                             logging.info("No cars found in the current page.")
#                             break
                        
#                         url = cars_json.get('next', None)
#                     else:
#                         logging.error("No 'results' key found in the response.")
#                         break

#                 except ValueError:
#                     logging.error("Response is not in JSON format")
#                     logging.error(f"Response Body: {response.text}")  # Log the full HTML body
#                     break
#             else:
#                 logging.error(f"Expected JSON response, but got: {response.text}")
#                 break
        
#         except requests.exceptions.HTTPError as http_err:
#             logging.error(f"HTTP error occurred: {http_err}")
#             break
#         except requests.exceptions.RequestException as err:
#             logging.error(f"Error fetching cars: {err}")
#             break
#         except requests.exceptions.Timeout:
#             logging.warning("Request timed out, retrying...")
#             time.sleep(2)  # Retry mechanism
#             continue

#     return cars

# # Example usage:
# api_key = "fd3417f5e310390"
# api_secret = "3dd18f32550b6ab"

# # Fetch cars from the external API
# cars = get_cars()

# # If cars exist, post them to ERP, otherwise print no cars message
# if cars:
#     logging.info(f"Found {len(cars)} cars to post.")
# else:
#     logging.info("No cars to post.")



import requests
import logging

logging.basicConfig(level=logging.INFO)

GET_CARS_URL = "https://api.dev.tryclaro.com/en/admin/customers/cars/"

HEADERS_GET = {
    "Accept": "application/json",  # Request JSON response
    "Authorization": "Bearer RDq6PLIW.Rb0COjF7RjgPsyKmNzNX1oKXM7thQYIZ",  # Replace with actual token if required
}

def get_cars():
    """Fetch cars from API and print full response details."""
    try:
        response = requests.get(GET_CARS_URL, headers=HEADERS_GET, timeout=10)
        response.raise_for_status()  # Raise error for HTTP errors

        # Log response details
        logging.info(f"Response Code: {response.status_code}")
        logging.info(f"Response Headers: {response.headers}")
        logging.info(f"Raw Response: {response.text[:500]}")  # Show first 500 characters

        # Check Content-Type
        content_type = response.headers.get("Content-Type", "")
        if "application/json" in content_type:
            data = response.json()
            logging.info(f"Parsed JSON: {data}")
            return data
        else:
            logging.error("Response is not JSON format. Possible HTML or XML received.")
            return None
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching cars: {e}")
        return None

# Run Debug
get_cars()
