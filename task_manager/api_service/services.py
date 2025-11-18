import requests

base_url = "http://127.0.0.1:8000/"
protected_path = "/api/tasks/"
auth_path = "/auth/token/login/"

login_credentials = {
    "username" : "bolu",
    "password" : "123",
}

try:
    response = requests.post(f"{base_url}{auth_path}", data=login_credentials)
    response.raise_for_status()
    data = response.json()    
    auth_token = data.get("auth_token")
    print(f"Token: {auth_token}")
except requests.exceptions.HTTPError as e:
    print(f"HTTP error: {e.response.status_code}")
except requests.exceptions.JSONDecodeError:
    print("Could not decode JSON data")

# auth_header = {
#     "Authorization" : f"Token {auth_token}"
# }

# try:
#     protected_response = requests.get(f"{base_url}{protected_path}", headers=auth_header)
#     protected_response.raise_for_status
#     protected_data = protected_response.json()
#     print(f"User data: {protected_data}")
# except requests.exceptions.HTTPError as e:
#     print(f"HTTP error: {e.response.status_code}")
# except requests.exceptions.JSONDecodeError:
#     print("Could not decode JSON data")

