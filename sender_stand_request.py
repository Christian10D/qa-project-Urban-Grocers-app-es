import requests
from configuration import URL_SERVICE, CREATE_USER_PATH, KITS_PATH

def post_new_client_kit(kit_body, auth_token):
    url = URL_SERVICE + KITS_PATH
    headers = {
        'Authorization': f'Bearer {auth_token}',
        'Content-Type': 'application/json'
    }
    response = requests.post(url, json=kit_body, headers=headers)
    return response
