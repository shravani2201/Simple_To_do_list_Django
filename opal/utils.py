import requests
import json

OPA_URL = "http://localhost:8181/v1/data/example/authz/allow"

def check_permission(user, action):
    input_data = {
        "input": {
            "user": user,
            "action": action
        }
    }
    try:
        response = requests.post(OPA_URL, data=json.dumps(input_data))
        response.raise_for_status()
        result = response.json()
        return result.get("result", False)
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to OPA: {e}")
        return False
