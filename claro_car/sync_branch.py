import requests
import json
import time
from requests.auth import HTTPBasicAuth
import logging

# Setting up logging
logging.basicConfig(level=logging.INFO)

# Function to fetch models
def get_models():
    url = "https://api.dev.tryclaro.com/en/admin/businesses/branchs/"
    headers = {
        "X-Api-Key": "RDq6PLIW.Rb0COjF7RjgPsyKmNzNX1oKXM7thQYIZ",  # Replace with your actual API key
    }
    
    models = []
    while url:
        try:
            response = requests.get(url, headers=headers, timeout=10)  # Added timeout
            response.raise_for_status()  # This will raise an error for 4xx/5xx responses
            
            # Print the raw response content to debug
            print(f"Raw response content: {response.text}")
            
            try:
                models_json = response.json()  # Ensure the response is in JSON format
                
                if 'results' in models_json:
                    models.extend([
                        {
                            "name": model.get("name"),
                            "business": model.get("business"),
                            "status": model.get("status")  
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


# Function to post models to ERPNext
def post_models_to_erp(models, api_key, api_secret, retry_count=3):
    erp_url = "https://erp.claro.sa/api/resource/Model"
    auth = HTTPBasicAuth(api_key, api_secret)

    for model in models:
        if not model.get("name") or not model.get("business"):
            logging.error(f"Missing name or business for {model}")
            continue

        data = {
            "branch": model["name"],
            "custom_company": model["business"],
            "custom_status": model["status"]  
        }

        logging.info(f"Posting data: {data}")

        attempt = 0
        while attempt < retry_count:
            try:
                response = requests.post(erp_url, auth=auth, headers={"Content-Type": "application/json"}, json=data, timeout=10)
                
                if response.status_code in [200, 201]:
                    logging.info(f"Successfully posted {model['name']}")
                    break
                else:
                    logging.error(f"Error posting {model['name']}: {response.status_code} - {response.text}")
                    break
                
            except requests.exceptions.Timeout:
                logging.warning(f"Timeout error posting {model['name']}. Retrying... ({attempt + 1}/{retry_count})")
            except requests.exceptions.RequestException as err:
                logging.error(f"Error posting {model['name']}: {err}")
                break

            time.sleep(2)
            attempt += 1
        else:
            logging.error(f"Failed to post {model['name']} after {retry_count} attempts.")

# Example usage:
api_key = "fd3417f5e310390"
api_secret = "3dd18f32550b6ab"

# Fetch models from the external API
models = get_models()

# If models exist, post them to ERP, otherwise print a message
if models:
    post_models_to_erp(models, api_key, api_secret)
else:
    print("No models to post.")
