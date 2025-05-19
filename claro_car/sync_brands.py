import requests
import json
import time
from requests.auth import HTTPBasicAuth

def get_brands():
    url = "https://api.dev.tryclaro.com/v1/cars/brands/"
    headers = {
        "X-Api-Key": "RDq6PLIW.Rb0COjF7RjgPsyKmNzNX1oKXM7thQYIZ",  # Replace with your actual API key
    }
    
    brands = []
    while url:  # Continue fetching while there is a 'next' page URL
        try:
            response = requests.get(url, headers=headers, timeout=10)  # Added timeout
            response.raise_for_status()  # Raises an exception for 4xx/5xx errors

            try:
                brands_json = response.json()  # Ensure the response is in JSON format
                print("Parsed JSON:", brands_json)  # Print the JSON to see the structure

                # Check if 'results' is in the JSON and add brand names to the list
                if 'results' in brands_json:
                    brands.extend([{"brand_name": brand["name"]} for brand in brands_json['results'] if brand.get("name")])
                else:
                    print("No 'results' key found in the response.")
                    break

                # Move to the next page if available
                url = brands_json.get('next', None)

            except ValueError:
                print("Response is not in JSON format")
                break
        
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            break
        except requests.exceptions.RequestException as err:
            print(f"Error fetching brands: {err}")
            break
        except requests.exceptions.Timeout:
            print("Request timed out, retrying...")
            time.sleep(2)  # Adding a retry mechanism in case of timeout
            continue  # Retry the request

    return brands

def post_brands_to_erp(brands, api_key, api_secret, retry_count=3):
    erp_url = "https://erp.claro.sa/api/resource/Brand"
    
    # Use HTTPBasicAuth for Basic Authentication
    auth = HTTPBasicAuth(api_key, api_secret)

    for brand in brands:
        # Check if the 'brand_name' key is present and not empty
        if not brand.get("brand_name"):
            print(f"Error: Missing or empty brand for {brand}")
            continue
        
        # Format the data to match ERPNext API's expected structure
        data = {
            "brand": brand["brand_name"]
            # "uuid":brand["uuid"]
        }
        
        # Debugging: Print data before posting
        print("Posting data:", data)

        attempt = 0
        while attempt < retry_count:
            try:
                response = requests.post(erp_url, auth=auth, headers={"Content-Type": "application/json"}, json=data, timeout=10)
                
                if response.status_code == 200:
                    print(f"Successfully posted {brand['brand_name']}")
                    break
                else:
                    print(f"Error posting {brand['brand_name']}: {response.status_code} - {response.text}")
                    break  # Stop retrying if it's not a temporary error (e.g., 4xx, 5xx errors)
                
            except requests.exceptions.Timeout:
                print(f"Timeout error posting {brand['brand_name']}. Retrying... ({attempt + 1}/{retry_count})")
            except requests.exceptions.RequestException as err:
                print(f"Error posting {brand['brand_name']}: {err}")
                break  # Stop retrying if the error is not timeout related

            time.sleep(2)  # Delay before retrying
            attempt += 1
        else:
            print(f"Failed to post {brand['brand_name']} after {retry_count} attempts.")


# Example usage:
api_key = "fd3417f5e310390"  # Replace with your actual API key
api_secret = "7d128c85346232d"  # Replace with your actual API secret

brands = get_brands()  # Fetch the brands from the API

if brands:
    post_brands_to_erp(brands, api_key, api_secret)
else:
    print("No brands to post.")