import requests
import os
import uuid


# The complete API endpoint URL for this flow
url = "https://aws-us-east-2.langflow.datastax.com/lf/b019ea93-e65a-4b61-bf38-c723572b8483/api/v1/run/7e7ecab5-285d-40c6-a584-7a09e78bd48d"

# Request payload configuration
payload = {
    "output_type": "chat",
    "input_type": "chat",
    "input_value": "hello world!"
}
payload["session_id"] = str(uuid.uuid4())

headers = {
    "X-DataStax-Current-Org": "f4959f18-0ab2-4f48-8607-425c0369b95c", 
    "Authorization": "Bearer AstraCS:<Application_Token>",
    "Content-Type": "application/json", 
    "Accept": "application/json",
}

try:
    # Send API request
    response = requests.request("POST", url, json=payload, headers=headers)
    response.raise_for_status()  # Raise exception for bad status codes

    # Print response
    print(response.text)

except requests.exceptions.RequestException as e:
    print(f"Error making API request: {e}")
except ValueError as e:
    print(f"Error parsing response: {e}")