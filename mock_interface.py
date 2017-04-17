from __future__ import print_function
from server_interface import ServerInterface


class MockServerInterface(ServerInterface):
    def get_posts(self):
        posts = [
            {
                'uid': 10,
                'postid': 20,
                'content': 'Hello, world!',
                'timestamp': '2017-04-14-11:00:00',
                'parentid': -1,
                'upvotes': 3,
                'tags': ['greeting']
            }
        ]

        return posts

    def add_post(self,content, parent_id=-1):
        pass




if __name__ == '__main__':
    interface = MockServerInterface()

    for post in interface.get_posts():
        print('uid:',post['uid'])

    print(interface.get_posts())
