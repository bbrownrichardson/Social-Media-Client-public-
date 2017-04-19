from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
import json
import requests


class PostScreen(Screen):
    # This posts list is here just for test purposes
    r = requests.get('http://nsommer.wooster.edu/social/posts')
    json_info = json.loads(r.content)
    posts = json.loads(r.content)

    def CreatePostWidgets(self):
        parent_widget = self.ids.post_widget #access the parent widget that
                                            # will hold all the post,
                                            # which are child widgets of it

        parent_widget.clear_widgets()
        for post in PostScreen.posts:

            post_owner = str(post['postid'])
            post_content = "Post ID: " + str(post['postid']) + "\n" + \
                            "User ID: " + str(post['uid']) + "\n" + \
                            "Username: " + post['username'] + "\n" + \
                            "Time: " + post['time'] + "\n" +  \
                            "Content: " + post['content']
            parent_widget.add_widget(Button(id=post_owner,
                text=post_content,
                size_hint_y = 10)) # it is this size because the scrollview
                                    # is being weird right now

