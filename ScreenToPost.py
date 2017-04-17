from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup


class ScreenToPost(Screen):
    def clear_post_text(self):
        self.ids['Post_text'].text = ''

    def popup_open(self):
        """
        This function is just for a popup widget that pops up on the screen
        when the user is cancelling a post. Currently it is not linked,
        as I cannot figure out how to bind one of the buttons on this popup
        widget to the post screen, so currently cancel button will simply
        go back to PostScreen

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
