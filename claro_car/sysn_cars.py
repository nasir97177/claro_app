# import requests
# import json
# import time
# from requests.auth import HTTPBasicAuth

# def get_cars():
#     url = "https://api.dev.tryclaro.com/v1/customers/cars/"
#     headers = {
#         "X-Api-Key": "RDq6PLIW.Rb0COjF7RjgPsyKmNzNX1oKXM7thQYIZ",  # Replace with your actual API key
#     }
    
#     cars = []
#     while url:  # Continue fetching while there is a 'next' page URL
#         try:
#             response = requests.get(url, headers=headers, timeout=10)  # Added timeout
#             response.raise_for_status()  # Raises an exception for 4xx/5xx errors

#             try:
#                 cars_json = response.json()  # Ensure the response is in JSON format
#                 print("Parsed JSON:", cars_json)  # Print the JSON to see the structure

#                 # Check if 'results' is in the JSON and add car details to the list
#                 if 'results' in cars_json:
#                     cars.extend([{"car_name": car["name"], "car_model": car.get("model"), "car_year": car.get("year")} for car in cars_json['results'] if car.get("name")])
#                 else:
#                     print("No 'results' key found in the response.")
#                     break

#                 # Move to the next page if available
#                 url = cars_json.get('next', None)

#             except ValueError:
#                 print("Response is not in JSON format")
#                 break
        
#         except requests.exceptions.HTTPError as http_err:
#             print(f"HTTP error occurred: {http_err}")
#             break
#         except requests.exceptions.RequestException as err:
#             print(f"Error fetching cars: {err}")
#             break
#         except requests.exceptions.Timeout:
#             print("Request timed out, retrying...")
#             time.sleep(2)  # Adding a retry mechanism in case of timeout
#             continue  # Retry the request

#     return cars

# def post_cars_to_erp(cars, api_key, api_secret, retry_count=3):
#     erp_url = "https://erp.claro.sa/api/resource/car"
    
#     # Use HTTPBasicAuth for Basic Authentication
#     auth = HTTPBasicAuth(api_key, api_secret)

#     for car in cars:
#         # Check if the 'car_name' key is present and not empty
#         if not car.get("car_name"):
#             print(f"Error: Missing or empty car for {car}")
#             continue
        
#         # Format the data to match ERPNext API's expected structure
#         data = {
#             "car_name": car["car_name"],
#             "car_model": car.get("car_model"),
#             "car_year": car.get("car_year")
#         }
        
#         # Debugging: Print data before posting
#         print("Posting data:", data)

#         attempt = 0
#         while attempt < retry_count:
#             try:
#                 response = requests.post(erp_url, auth=auth, headers={"Content-Type": "application/json"}, json=data, timeout=10)
                
#                 if response.status_code == 200:
#                     print(f"Successfully posted {car['car_name']}")
#                     break
#                 else:
#                     print(f"Error posting {car['car_name']}: {response.status_code} - {response.text}")
#                     break  # Stop retrying if it's not a temporary error (e.g., 4xx, 5xx errors)
                
#             except requests.exceptions.Timeout:
#                 print(f"Timeout error posting {car['car_name']}. Retrying... ({attempt + 1}/{retry_count})")
#             except requests.exceptions.RequestException as err:
#                 print(f"Error posting {car['car_name']}: {err}")
#                 break  # Stop retrying if the error is not timeout related

#             time.sleep(2)  # Delay before retrying
#             attempt += 1
#         else:
#             print(f"Failed to post {car['car_name']} after {retry_count} attempts.")


# # Example usage:
# api_key = "fd3417f5e310390" 
# api_secret = "7d128c85346232d"  

# cars = get_cars()

# if cars:
#     post_cars_to_erp(cars, api_key, api_secret)
# else:
#     print("No cars to post.")

import requests
import json
import time
import os
from requests.auth import HTTPBasicAuth

def get_cars():
    url = "https://api.dev.tryclaro.com/v1/customers/cars/"
    headers = {
        "X-Api-Key": os.getenv("RDq6PLIW.Rb0COjF7RjgPsyKmNzNX1oKXM7thQYIZ"),  # Use environment variable for API key
    }
    
    cars = []
    while url:  # Continue fetching while there is a 'next' page URL
        try:
            response = requests.get(url, headers=headers, timeout=10)  # Added timeout
            response.raise_for_status()  # Raises an exception for 4xx/5xx errors

            try:
                cars_json = response.json()  # Ensure the response is in JSON format
                print("Parsed JSON:", cars_json)  # Print the JSON to see the structure

                # Check if 'results' is in the JSON and add car details to the list
                if 'results' in cars_json:
                    cars.extend([{"car_name": car["name"], "car_model": car.get("model"), "car_year": car.get("year")} for car in cars_json['results'] if car.get("name")])
                else:
                    print("No 'results' key found in the response.")
                    break

                # Move to the next page if available
                url = cars_json.get('next', None)

            except ValueError:
                print("Response is not in JSON format")
                break
        
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            break
        except requests.exceptions.RequestException as err:
            print(f"Error fetching cars: {err}")
            break
        except requests.exceptions.Timeout:
            print("Request timed out, retrying...")
            time.sleep(2)  # Adding a retry mechanism in case of timeout
            continue  # Retry the request

    return cars

def post_cars_to_erp(cars, api_key, api_secret, retry_count=3):
    erp_url = "https://erp.claro.sa/api/resource/car"
    
    # Use HTTPBasicAuth for Basic Authentication
    auth = HTTPBasicAuth(api_key, api_secret)

    for car in cars:
        # Check if the 'car_name' key is present and not empty
        if not car.get("car_name"):
            print(f"Error: Missing or empty car for {car}")
            continue
        
        # Format the data to match ERPNext API's expected structure
        data = {
            "car_name": car["car_name"],
            "car_model": car.get("car_model"),
            "car_year": car.get("car_year")
        }
        
        # Debugging: Print data before posting
        print("Posting data:", data)

        attempt = 0
        while attempt < retry_count:
            try:
                response = requests.post(erp_url, auth=auth, headers={"Content-Type": "application/json"}, json=data, timeout=10)
                
                if 200 <= response.status_code < 300:
                    print(f"Successfully posted {car['car_name']}")
                    break
                elif 400 <= response.status_code < 500:
                    print(f"Client error {response.status_code} for {car['car_name']}: {response.text}")
                    break  # No retry needed for 4xx errors
                elif 500 <= response.status_code < 600:
                    print(f"Server error {response.status_code} for {car['car_name']}: {response.text}")
                    # Retry for server-side issues
                
            except requests.exceptions.Timeout:
                print(f"Timeout error posting {car['car_name']}. Retrying... ({attempt + 1}/{retry_count})")
            except requests.exceptions.RequestException as err:
                print(f"Error posting {car['car_name']}: {err}")
                break  # Stop retrying if the error is not timeout related

            time.sleep(2)  # Delay before retrying
            attempt += 1
        else:
            print(f"Failed to post {car['car_name']} after {retry_count} attempts.")


# Example usage:
api_key = os.getenv("7d128c85346232d") 
api_secret = os.getenv("7d128c85346232d")  

cars = get_cars()

if cars:
    post_cars_to_erp(cars, api_key, api_secret)
else:
    print("No cars to post.")
