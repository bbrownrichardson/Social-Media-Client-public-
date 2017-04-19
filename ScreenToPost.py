from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from PostScreen import PostScreen
from random import random


class ScreenToPost(Screen):
    def update_post(self):
        """
        Purpose is to add a "post", its just a dictionary, to the test list
        I have in the PostScreen class. Method will change once we have an
        actual server to read from.
        :return: new "post"
        """
        new_post_content = self.ids['Post_text'].text # text user puts in
                                                      # textbox for a post
        random_uid = random()  # to generate a random int for the uid
        random_postid = random()  # to generate a random int for the postid
        temp_dict = {
            'uid': random_uid,
            'postid': random_postid,
            'content': new_post_content,
            'timestamp': '2017-04-14-11:00:00',
            'parentid': -1,
            'upvotes': 3,
            'tags': ['greeting']
        }
        self.ids['Post_text'].text = ''  # clears the text
        PostScreen.posts.append(temp_dict)  # the test post list from
                                            # PostScreen class

    def clear_post_text(self):
        self.ids['Post_text'].text = ''  # clears the text if user cancels
                                        # making a post

    def popup_open(self):
        """
        This function is just for a popup widget that pops up on the screen
        when the user is cancelling a post. Currently it is not linked,
        as I cannot figure out how to bind one of the buttons on this popup
        widget to the post screen, so currently cancel button will simply
        go back to PostScreen. OVERALL YOU CAN IGNORE THIS!!!!

        :return: popup widget
        """
        content = BoxLayout(orientation='vertical')
        keep_posting = Button(text='Just Kidding', size_hint=(1, 1))
        return_to_timeline = Button(text='Return to Timeline',
                                    size_hint=(1, 1))
        content.add_widget(keep_posting)
        content.add_widget(return_to_timeline)
        popup = Popup(title='Are you sure you wanna cancel??',
                      content=content, size_hint=(0.3, 0.25))
        keep_posting.bind(on_press=popup.dismiss)
        # return_to_timeline.bind(on_press=)
        popup.open()
