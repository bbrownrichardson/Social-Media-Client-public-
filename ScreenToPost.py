from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from mock_interface import MockServerInterface
from PostScreen import PostScreen
from kivy.uix.label import Label
from ServerInterfaceException import ServerInterfaceException

class ScreenToPost(Screen):


    def update_post(self):
        current_uid = MockServerInterface.temp_uid
        current_token = MockServerInterface.temp_token
        temp_content = self.ids.Post_text.text

        try:
            (MockServerInterface.add_post(self, temp_content, current_uid,
                                         current_token,parentid=1) )
            self.manager.current = 'PostScreen'
            self.ids.Post_button.on_press = PostScreen.CreatePostWidgets(self)
            self.ids.Post_text.text = ''

        except ServerInterfaceException as e:
            # This will need to replaced with some error pop or something
            # of that nature
            content = BoxLayout(orientation='vertical')
            message_label = Label(
                text=str(e))
            dismiss_button = Button(text='OK')
            content.add_widget(message_label)
            content.add_widget(dismiss_button)
            popup = Popup(title='Error', content=content,
                          size_hint=(0.3, 0.25))
            dismiss_button.bind(on_press=popup.dismiss)
            popup.open()

    def clear_post_text(self):
        self.ids.Post_text.text = ''  # clears the text if user cancels
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

