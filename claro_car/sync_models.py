# import requests
# import json
# import time
# from requests.auth import HTTPBasicAuth
# import logging

# # Setting up logging
# logging.basicConfig(level=logging.INFO)

# # Function to fetch car models
# def get_models():
#     url = "https://api.dev.tryclaro.com/v1/cars/models/"
#     headers = {
#         "X-Api-Key": "RDq6PLIW.Rb0COjF7RjgPsyKmNzNX1oKXM7thQYIZ",  # Replace with your actual API key
#     }
    
#     models = []
#     while url:
#         try:
#             response = requests.get(url, headers=headers, timeout=10)  # Added timeout
#             response.raise_for_status()

#             try:
#                 models_json = response.json()  # Ensure the response is in JSON format
#                 print("Parsed JSON:", models_json)

#                 if 'results' in models_json:
#                     models.extend([{"model_name": model["name"], "uuid": model["uuid"]} for model in models_json['results'] if model.get("name")])
#                 else:
#                     print("No 'results' key found in the response.")
#                     break

#                 url = models_json.get('next', None)

#             except ValueError:
#                 print("Response is not in JSON format")
#                 break
        
#         except requests.exceptions.HTTPError as http_err:
#             print(f"HTTP error occurred: {http_err}")
#             break
#         except requests.exceptions.RequestException as err:
#             print(f"Error fetching models: {err}")
#             break
#         except requests.exceptions.Timeout:
#             print("Request timed out, retrying...")
#             time.sleep(2)  # Retry mechanism
#             continue

#     return models

# # Function to get the brand ID from ERPNext
# def get_brand_id(brand_name, api_key, api_secret):
#     erp_url = f"https://erp.claro.sa/api/resource/Brand/{brand_name}"
#     auth = HTTPBasicAuth(api_key, api_secret)
    
#     try:
#         response = requests.get(erp_url, auth=auth)
        
#         if response.status_code == 200:
#             return response.json()['data']['name']  # Return the actual brand name from ERPNext
#         elif response.status_code == 404:  # Brand does not exist
#             logging.error(f"Brand {brand_name} not found in ERPNext.")
#             return None
#         else:
#             logging.error(f"Could not find brand: {brand_name}. Error: {response.status_code} - {response.text}")
#             return None
#     except requests.exceptions.RequestException as err:
#         logging.error(f"Error fetching brand {brand_name}: {err}")
#         return None

# # Function to post models to ERPNext
# def post_models_to_erp(models, api_key, api_secret, retry_count=3):
#     erp_url = "https://erp.claro.sa/api/resource/Model"
#     auth = HTTPBasicAuth(api_key, api_secret)

#     for model in models:
#         if not model.get("model_name") or not model.get("uuid"):
#             logging.error(f"Missing model_name or uuid for {model}")
#             continue

#         # Extract the brand dynamically if available
#         brand_name = model.get("brand")  # Ensure API provides this field
#         if not brand_name:
#             logging.warning(f"No brand found for {model['model_name']}, using fallback brand.")
#             brand_name = "Toyota"  # Change this to a valid brand in ERPNext

#         # Ensure the brand exists in ERPNext
#         brand_id = get_brand_id(brand_name, api_key, api_secret)
#         if not brand_id:
#             logging.warning(f"Brand '{brand_name}' not found. Creating brand...")
#             create_brand_in_erp(brand_name, api_key, api_secret)
#             brand_id = get_brand_id(brand_name, api_key, api_secret)  # Re-fetch after creation

#         if not brand_id:
#             logging.error(f"Cannot proceed without a valid brand for {model['model_name']}")
#             continue

#         data = {
#             "name1": model["model_name"],
#             "uuid": model["uuid"],
#             "brand": brand_id
#         }

#         logging.info(f"Posting data: {data}")

#         attempt = 0
#         while attempt < retry_count:
#             try:
#                 response = requests.post(erp_url, auth=auth, headers={"Content-Type": "application/json"}, json=data, timeout=10)
                
#                 if response.status_code == 201:
#                     logging.info(f"Successfully posted {model['model_name']}")
#                     break
#                 else:
#                     logging.error(f"Error posting {model['model_name']}: {response.status_code} - {response.text}")
#                     break
                
#             except requests.exceptions.Timeout:
#                 logging.warning(f"Timeout error posting {model['model_name']}. Retrying... ({attempt + 1}/{retry_count})")
#             except requests.exceptions.RequestException as err:
#                 logging.error(f"Error posting {model['model_name']}: {err}")
#                 break

#             time.sleep(2)
#             attempt += 1
#         else:
#             logging.error(f"Failed to post {model['model_name']} after {retry_count} attempts.")


# # Example usage:
# api_key = "fd3417f5e310390"
# api_secret = "3dd18f32550b6ab"

# # Fetch models from the external API
# models = get_models()

# # If models exist, post them to ERP, otherwise print no models message
# if models:
#     post_models_to_erp(models, api_key, api_secret)
# else:
#     print("No models to post.")



# # Example usage:
# api_key = "fd3417f5e310390"
# api_secret = "3dd18f32550b6ab"

# # Fetch models from the external API
# models = get_models()

# # If models exist, post them to ERP, otherwise print no models message
# if models:
#     post_models_to_erp(models, api_key, api_secret)
# else:
#     print("No models to post.")


import requests
import json
import time
from requests.auth import HTTPBasicAuth
import logging

# Setting up logging
logging.basicConfig(level=logging.INFO)

# Function to fetch car models
def get_models():
    url = "https://api.dev.tryclaro.com/v1/cars/models/"
    headers = {
        "X-Api-Key": "RDq6PLIW.Rb0COjF7RjgPsyKmNzNX1oKXM7thQYIZ",  # Replace with your actual API key
    }
    
    models = []
    while url:
        try:
            response = requests.get(url, headers=headers, timeout=10)  # Added timeout
            response.raise_for_status()

            try:
                models_json = response.json()  # Ensure the response is in JSON format

                if 'results' in models_json:
                    models.extend([
                        {
                            "model_name": model.get("name"),
                            "uuid": model.get("uuid"),
                            "brand": model.get("brand")  # Ensure brand is fetched
                        }
                        for model in models_json['results'] if model.get("name")
                    ])
                else:
                    print("No 'results' key found in the response.")
                    break

                url = models_json.get('next', None)

            except ValueError:
                print("Response is not in JSON format")
                break
        
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            break
        except requests.exceptions.RequestException as err:
            print(f"Error fetching models: {err}")
            break
        except requests.exceptions.Timeout:
            print("Request timed out, retrying...")
            time.sleep(2)  # Retry mechanism
            continue

    return models

# Function to get the brand ID from ERPNext
def get_brand_id(brand, api_key, api_secret):
    erp_url = f"https://erp.claro.sa/api/resource/Brand/{brand}"
    auth = HTTPBasicAuth(api_key, api_secret)
    
    try:
        response = requests.get(erp_url, auth=auth)
        
        if response.status_code == 200:
            return response.json()['data']['name']  # Return the actual brand name from ERPNext
        elif response.status_code == 404:  # Brand does not exist
            logging.error(f"Brand {brand} not found in ERPNext.")
            return None
        else:
            logging.error(f"Could not find brand: {brand}. Error: {response.status_code} - {response.text}")
            return None
    except requests.exceptions.RequestException as err:
        logging.error(f"Error fetching brand {brand}: {err}")
        return None

# **New Function: Create Brand in ERPNext**
def create_brand_in_erp(brand, api_key, api_secret):
    """Creates a new brand in ERPNext if it does not exist."""
    erp_url = "https://erp.claro.sa/api/resource/Brand"
    auth = HTTPBasicAuth(api_key, api_secret)
    
    data = {"brand": brand}  # Data format for creating a new Brand

    try:
        response = requests.post(erp_url, auth=auth, headers={"Content-Type": "application/json"}, json=data, timeout=10)
        
        if response.status_code == 200 or response.status_code == 201:
            logging.info(f"Brand '{brand}' created successfully in ERPNext.")
        else:
            logging.error(f"Error creating brand '{brand}': {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as err:
        logging.error(f"Error creating brand '{brand}': {err}")

# Function to post models to ERPNext
def post_models_to_erp(models, api_key, api_secret, retry_count=3):
    erp_url = "https://erp.claro.sa/api/resource/Model"
    auth = HTTPBasicAuth(api_key, api_secret)

    for model in models:
        if not model.get("model_name") or not model.get("uuid"):
            logging.error(f"Missing model_name or uuid for {model}")
            continue

        # Extract the brand name properly
        brand_data = model.get("brand")
        if isinstance(brand_data, dict):
            brand = brand_data.get("name")  # Get the actual brand name
        else:
            brand = brand_data  # Fallback if it's already a string

        if not brand:
            logging.warning(f"No brand found for {model['model_name']}, using fallback brand.")
            brand = "Toyota"  # Change this to a valid brand in ERPNext

        # Ensure the brand exists in ERPNext
        brand_id = get_brand_id(brand, api_key, api_secret)
        if not brand_id:
            logging.warning(f"Brand '{brand}' not found. Creating brand...")            
            create_brand_in_erp(brand, api_key, api_secret)
            brand_id = get_brand_id(brand, api_key, api_secret)  # Re-fetch after creation

        if not brand_id:
            logging.error(f"Cannot proceed without a valid brand for {model['model_name']}")
            continue

        data = {
            "name1": model["model_name"],
            "uuid": model["uuid"],
            "brand": brand_id  # Ensure the brand is correctly posted
        }

        logging.info(f"Posting data: {data}")

        attempt = 0
        while attempt < retry_count:
            try:
                response = requests.post(erp_url, auth=auth, headers={"Content-Type": "application/json"}, json=data, timeout=10)
                
                if response.status_code == 201:
                    logging.info(f"Successfully posted {model['model_name']}")
                    break
                else:
                    logging.error(f"Error posting {model['model_name']}: {response.status_code} - {response.text}")
                    break
                
            except requests.exceptions.Timeout:
                logging.warning(f"Timeout error posting {model['model_name']}. Retrying... ({attempt + 1}/{retry_count})")
            except requests.exceptions.RequestException as err:
                logging.error(f"Error posting {model['model_name']}: {err}")
                break

            time.sleep(2)
            attempt += 1
        else:
            logging.error(f"Failed to post {model['model_name']} after {retry_count} attempts.")



# Example usage:
api_key = "fd3417f5e310390"
api_secret = "3dd18f32550b6ab"

# Fetch models from the external API
models = get_models()

# If models exist, post them to ERP, otherwise print no models message
if models:
    post_models_to_erp(models, api_key, api_secret)
else:
    print("No models to post.")
