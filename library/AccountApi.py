import requests
from .App_Auth import Auth
from variables.configuration import *


class AccountApi(Auth):
    def get_info_current_user(self):
        me_endpoint = BASE_OAUTH_URL + '/api/v1/me'
        headers = {
            'User-Agent': 'Autotest by ' + USERNAME,
            'Authorization': 'bearer ' + self.access_token
        }
        response = requests.get(me_endpoint, headers=headers)
        return response

    def get_friend_list_current_user(self):
        me_friends_endpoint = BASE_OAUTH_URL + '/api/v1/me/friends'
        headers = {
            'User-Agent': 'Autotest by ' + USERNAME,
            'Authorization': 'bearer ' + self.access_token
        }
        response = requests.get(me_friends_endpoint, headers=headers)
        return response

    def get_karma_current_user(self):
        me_karma_endpoint = BASE_OAUTH_URL + '/api/v1/me/karma'
        headers = {
            'User-Agent': 'Autotest by ' + USERNAME,
            'Authorization': 'bearer ' + self.access_token
        }
        response = requests.get(me_karma_endpoint, headers=headers)
        return response
