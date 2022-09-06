import requests
from .App_Auth import Auth
from variables.configuration import *


class SubredditsApi(Auth):
    def search_thread(self, subreddit_name, query):
        search_thread_endpoint = BASE_OAUTH_URL + '/r/' + subreddit_name + '/search'
        headers = {
            'User-Agent': 'Autotest by ' + USERNAME,
            'Authorization': 'bearer ' + self.access_token
        }
        params = {
            'q': query
        }
        response = requests.get(search_thread_endpoint, headers=headers, params=params)
        return response

    def subscribe_subreddit(self, subreddit_name, sub):
        subscribe_subreddit_endpoint = BASE_OAUTH_URL + '/api/subscribe'
        headers = {
            'User-Agent': 'Autotest by ' + USERNAME,
            'Authorization': 'bearer ' + self.access_token
        }
        params = {
            'sr_name': subreddit_name,
            'action': sub
        }
        response = requests.post(subscribe_subreddit_endpoint, headers=headers, params=params)
        return response

    def make_post(self, subreddit_name, title, text):
        subscribe_subreddit_endpoint = BASE_OAUTH_URL + '/api/submit'
        headers = {
            'User-Agent': 'Autotest by ' + USERNAME,
            'Authorization': 'bearer ' + self.access_token
        }
        params = {
            'sr': subreddit_name,
            'kind': 'self',
            'title': title,
            'text': text
        }
        response = requests.post(subscribe_subreddit_endpoint, headers=headers, params=params)
        return response
