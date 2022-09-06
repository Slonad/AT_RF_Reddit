import requests
from .App_Auth import Auth
from variables.configuration import *


class LinksCommentsApi(Auth):
    def post_comment(self, thread_id, message):
        pots_comment_endpoint = BASE_OAUTH_URL + '/api/comment'
        headers = {
            'User-Agent': 'Autotest by ' + USERNAME,
            'Authorization': 'bearer ' + self.access_token
        }
        params = {
            'parent': thread_id,
            'text': message
        }
        response = requests.post(pots_comment_endpoint, headers=headers, params=params)
        return response

    def delete_t_entity(self, reddit_fullname):
        delete_comment_endpoint = BASE_OAUTH_URL + '/api/del'
        headers = {
            'User-Agent': 'Autotest by ' + USERNAME,
            'Authorization': 'bearer ' + self.access_token
        }
        params = {
            'id': reddit_fullname
        }
        response = requests.post(delete_comment_endpoint, headers=headers, params=params)
        return response

    """
    def follow_post(access_token, reddit_fullname, follow):
        follow_post_endpoint = BASE_OAUTH_URL + '/api/follow_post'
        headers = {
            'User-Agent': 'Autotest by ' + USERNAME,
            'Authorization': 'bearer ' + access_token
        }
        params = {
            'fullname': reddit_fullname,
            'follow': follow
        }
        response = requests.post(follow_post_endpoint, headers=headers, params=params)
        return response
    """
