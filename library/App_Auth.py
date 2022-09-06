import requests
from variables.configuration import *


class Auth:
    def __init__(self):
        client_auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
        post_data = {'grant_type': 'password', 'username': USERNAME, 'password': PASSWORD}
        headers = {
            'User-Agent': 'Autotest by ' + USERNAME
        }
        token_access_endpoint = BASE_URL + '/api/v1/access_token'
        response = requests.post(token_access_endpoint, data=post_data, headers=headers, auth=client_auth)
        self.access_token = response.json()['access_token']
