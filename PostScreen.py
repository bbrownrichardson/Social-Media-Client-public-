from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label

class PostScreen(Screen):
    # This posts list is here just for test purposes
    posts = [
        {
            'uid': 10,
            'postid': 20,
            'content': 'Hello, world!',
            'timestamp': '2017-04-14-11:00:00',
            'parentid': -1,
            'upvotes': 3,
            'tags': ['greeting']
        },
        {
            'uid': 40,
            'postid': 60,
            'content': 'Test Post',
            'timestamp': '2017-04-14-11:00:00',
            'parentid': -1,
            'upvotes': 2,
            'tags': ['greeting']
        },
        {
            'uid': 14,
            'postid': 20,
            'content': 'hey heres a post!',
            'timestamp': '2017-04-14-11:00:00',
            'parentid': -1,
            'upvotes': 3,
            'tags': ['greeting']
        },
        {
            'uid': 22,
            'postid': 20,
            'content': 'one more test!',
            'timestamp': '2017-04-14-11:00:00',
            'parentid': -1,
            'upvotes': 3,
            'tags': ['greeting']
        }
    ]

    def CreatePostWidgets(self):
        parent_widget = self.ids.post_widget #access the parent widget that
                                            # will hold all the post,
                                            # which are child widgets of it

        parent_widget.clear_widgets()
        for post in PostScreen.posts:

            post_owner = str(post['uid'])
            post_content = post['content'] + '\n' + post['timestamp'] + \
                           '\n'
            parent_widget.add_widget(Button(id=post_owner,
                text=post_content,
                size_hint_y = 10)) # it is this size because the scrollview
                                    # is being weird right now

