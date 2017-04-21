from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.bubble import BubbleButton
import json
import requests


class PostScreen(Screen):
    r = requests.get('http://nsommer.wooster.edu/social/posts')
    json_info = json.loads(r.content)
    posts = json.loads(r.content)

    def CreatePostWidgets(self):
        parent_widget = self.ids.post_widget # access the parent widget that
                                            # will hold all the post,
                                            # which are child widgets of it

        parent_widget.clear_widgets()
        for post in PostScreen.posts:

            post_owner = str(post['postid'])
            post_content = "Post ID: " + str(post['postid']) + "\n" + \
                            "User ID: " + str(post['uid']) + "\n" + \
                            "Time: " + post['time'] + "\n" +  \
                            "Content: " + post['content'] + "\n" +  \
                            "Upvotes: " + str(post['upvotes'])

            child_widget1 = GridLayout(cols=1)
            child_widget1.add_widget(BubbleButton(text=post['username'],
                    background_color=(0.0, 1.0, 1.0, 1.0)))

            child_widget1.add_widget(Label(text=post_content))

            child_widget2 = BoxLayout()

            child_widget2.add_widget(BubbleButton(id=post_owner, text='LIKE',
                                                  background_color=(
                                                      0.0, 1.0, 1.0, 1.0)))
            child_widget2.add_widget(BubbleButton(id='edit '+post_owner,
                                            text='EDIT', background_color=(
                                                      0.0, 1.0, 1.0, 1.0)))
            child_widget2.add_widget(BubbleButton(id='reply_to_'+post_owner,
                                            text='REPLY', background_color=(
                                                      0.0, 1.0, 1.0, 1.0)))

            child_widget1.add_widget(child_widget2)
            parent_widget.add_widget(child_widget1)
            # parent_widget.add_widget(Button(id=post_owner, text=post_content,
            # size_hint_y=10))
