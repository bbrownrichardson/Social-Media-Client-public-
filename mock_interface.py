from __future__ import print_function
from server_interface import ServerInterface
import json
import requests
from ServerInterfaceException import ServerInterfaceException

class MockServerInterface(ServerInterface):
    # These variables are here so it would easier to transfer current user
    # content on a different screen if there is an easier way please change
    temp_username = None
    temp_uid = None
    temp_content = None
    temp_time = None
    temp_token = None
    temp_recipient = None
    temp_recipientid = None
    temp_messagedict = None
    temp_posts = None
    temp_conversationdict = None

    def __init__(self, uid, token):
        self.uid = uid
        self.token = token
        self.base_url = 'http://nsommer.wooster.edu/social'

    @staticmethod
    def get_posts(self):
        response = requests.get('http://nsommer.wooster.edu/social/posts')
        json_info = json.loads(response.content)
        if response.status_code == 200:
            MockServerInterface.temp_posts = json.loads(response.content)
        elif response.status_code == 400:
            error_message = json.loads(response.content)['message']
            raise ServerInterfaceException(error_message)
        else:
            raise ServerInterfaceException(
                'Bad request with code {}'.format(response.status_code))


    @staticmethod
    def add_post(self, content, uid, token, parentid=1):
            url = 'http://nsommer.wooster.edu/social/posts'
            data = {
                'uid': uid,
                'token': token,
                'content': content,
                'parentid': parentid
            }
            response = requests.post(url, data=data)
            if response.status_code == 200:
                 MockServerInterface.temp_token = token
                 MockServerInterface.temp_uid = uid
            elif response.status_code == 400:
                error_message = json.loads(response.content)['message']
                raise ServerInterfaceException(error_message)
            else:
                raise ServerInterfaceException(
                    'Bad request with code {}'.format(response.status_code))

    @staticmethod
    def get_users(self, username):
        url = 'http://nsommer.wooster.edu/social/users'
        user = requests.get(url,
                            data={'username': username})
        temp_dict = json.loads(user.content)
        if user.status_code == 200:
            MockServerInterface.temp_username = temp_dict['username']
            MockServerInterface.temp_uid = temp_dict['uid']
            # MockServerInterface.temp_token = temp_dict['token']
        elif user.status_code == 400:
            error_message = json.loads(user.content)['message']
            raise ServerInterfaceException(error_message)
        else:
            raise ServerInterfaceException(
                'Bad request with code {}'.format(user.status_code))

    @staticmethod
    def add_users(self, username):
        url = 'http://nsommer.wooster.edu/social/users'
        user = requests.post(url, data={'username': username})
        temp_dict = user.json()
        if user.status_code == 200:
            MockServerInterface.temp_username = temp_dict['username']
            MockServerInterface.temp_uid = temp_dict['uid']
            MockServerInterface.temp_token = temp_dict['token']
        elif user.status_code == 400:
            error_message = json.loads(user.content)['message']
            raise ServerInterfaceException(error_message)
        else:
            raise ServerInterfaceException(
                'Bad request with code {}'.format(user.status_code))


    @staticmethod
    def send_message(self, senderid, recipientid, token, content):
        url = 'http://nsommer.wooster.edu/social/messages'

        data = {
            'senderid': senderid,
            'recipientid': recipientid,
            'token': token,
            'content': content,
        }

        response = requests.post(url, data=data)
        temp_dict = response.json()
        if response.status_code == 200:
            MockServerInterface.temp_messageid = temp_dict['messageid']

        elif response.status_code == 400:
            error_message = json.loads(response.content)['message']
            raise ServerInterfaceException(error_message)
        else:
            raise ServerInterfaceException(
                'Bad request with code {}'.format(response.status_code))


    @staticmethod
    def get_recipient_users(self, username):
        url = 'http://nsommer.wooster.edu/social/users'
        user = requests.get(url,
                            data={'username': username})
        temp_dict = json.loads(user.content)
        if user.status_code == 200:
            MockServerInterface.temp_recipient = temp_dict['username']
            MockServerInterface.temp_recipientid = temp_dict['uid']
            # MockServerInterface.temp_token = temp_dict['token']
        elif user.status_code == 400:
            error_message = json.loads(user.content)['message']
            raise ServerInterfaceException(error_message)
        else:
            raise ServerInterfaceException(
                'Bad request with code {}'.format(user.status_code))


    @staticmethod
    def get_messages(self, uid, otherid, token):
        """
        :param uid: id of the the user that is logged in
        :param otherid: id of the user you want to get messages from
        :param token: the token of the current user
        :return: conversations between users
        """
        url = 'http://nsommer.wooster.edu/social/messages'
        data ={
            'uid': uid,
            'otherid': otherid,
            'token' : token
        }
        response = requests.get(url,data=data)
        temp_dict = json.loads(response.content)
        if response.status_code == 200:
            MockServerInterface.temp_messagedict = temp_dict
        elif response.status_code == 400:
            error_message = json.loads(response.content)['message']
            raise ServerInterfaceException(error_message)
        else:
            raise ServerInterfaceException(
                'Bad request with code {}'.format(response.status_code))

    @staticmethod
    def get_conversations(self, uid, token):
        url = 'http://nsommer.wooster.edu/social/conversations'
        data={
            'uid': uid,
            'token': token
        }
        response = requests.get(url, data=data)
        if response.status_code == 200:
            MockServerInterface.temp_conversationdict = response.json()
        elif response.status_code == 400:
            error_message = json.loads(response.content)['message']
            raise ServerInterfaceException(error_message)
        else:
            raise ServerInterfaceException('Bad request with code {}'.format(response.status_code))






# if __name__ == '__main__':
    # interface = MockServerInterface()

    # for post in interface.get_posts():
        # print('uid:',post['uid'])

    # print(interface.get_posts())

    # interface.get_users()
