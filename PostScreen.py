from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.bubble import BubbleButton
from mock_interface import MockServerInterface


class PostScreen(Screen):


    def CreatePostWidgets(self):
        parent_widget = self.ids.post_widget # access the parent widget that
                                            # will hold all the post,
                                            # which are child widgets of it
        if MockServerInterface.get_posts(self):
            parent_widget.clear_widgets()
            for post in MockServerInterface.temp_posts:

                post_owner = str(post['postid'])
                post_content = "Post ID: " + str(post['postid']) + "\n" + \
                            "User ID: " + str(post['uid']) + "\n" + \
                            "Time: " + post['time'] + "\n" +  \
                            "Content: " + post['content'] + "\n" +  \
                            "Upvotes: " + str(post['upvotes'])

                second_layer = GridLayout(cols=1)
                second_layer.add_widget(BubbleButton(text=post['username'],
                    background_color=(0.0, 1.0, 1.0, 1.0)))

                second_layer.add_widget(Label(text=post_content))

                third_layer = BoxLayout()

                third_layer.add_widget(BubbleButton(id=post_owner, text='LIKE',
                                                  background_color=(
                                                      0.0, 1.0, 1.0, 1.0)))
                third_layer.add_widget(BubbleButton(id='edit '+post_owner,
                                            text= 'EDIT', background_color=(
                                                      0.0, 1.0, 1.0, 1.0)))
                third_layer.add_widget(BubbleButton(id='reply_to_'+post_owner,
                                            text= 'REPLY', background_color=(
                                                      0.0, 1.0, 1.0, 1.0)))
                third_layer.add_widget(BubbleButton(id='delete_' + post_owner,
                                                text='DELETE',
                                                background_color=(
                                                    0.0, 1.0, 1.0, 1.0)))

                second_layer.add_widget(third_layer)
                parent_widget.add_widget(second_layer)
                # parent_widget.add_widget(Button(id=post_owner, text=post_content,
                                            # size_hint_y=10))
        else:
            pass
