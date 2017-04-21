from __future__ import print_function
from server_interface import ServerInterface
import json
import requests


class MockServerInterface(ServerInterface):
    # These variables are here so it would easier to transfer current user
    # content on different screen if there is an easier way please change
    temp_username = None
    temp_uid = None
    temp_content = None
    temp_token = None
    posts = None

    def __init__(self, uid, token):
        self.uid = uid
        self.token = token
        self.base_url = 'http://nsommer.wooster.edu/social'

    @staticmethod
    def get_posts(self):
        response = requests.get('http://nsommer.wooster.edu/social/posts')
        json_info = json.loads(response.content)
        posts = json.loads(response.content)

    @staticmethod
    def add_post(self, content):
            url = 'http://nsommer.wooster.edu/social/posts'

            data = {
            'uid': self.uid,
            'token': self.token,
            'content': content
            }

            response = requests.post(url, data=data)

    @staticmethod
    def get_users(self, username):
        url = 'http://nsommer.wooster.edu/social/users'
        user = requests.get(url,
                            data={'username': username})
        temp_dict = json.loads(user.content)
        if user.status_code == 200:
            MockServerInterface.temp_user = temp_dict['username']
            MockServerInterface.temp_uid = temp_dict['uid']
            # temp_token = temp_dict['token']
            return True
        else:
            return False

    @staticmethod
    def add_users(self, username):
        url = 'http://nsommer.wooster.edu/social/users'
        user = requests.post(url, data={'username' : username})
        temp_dict = user.json()
        if user.status_code == 200:
            MockServerInterface.temp_user = temp_dict['username']
            MockServerInterface.temp_uid = temp_dict['uid']
            MockServerInterface.temp_token = temp_dict['token']
            return True
        else:
            return False

# if __name__ == '__main__':
    # interface = MockServerInterface()

    # for post in interface.get_posts():
        # print('uid:',post['uid'])

    # print(interface.get_posts())

    # interface.get_users()
