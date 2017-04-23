from kivy.uix.screenmanager import Screen
from mock_interface import MockServerInterface


class LoginScreen(Screen):
    current_uid = None
    current_username = None
    current_token = None

    def kivy_login(self):
        current_username = self.ids.username_login.text
        current_token = self.ids.token_login.text

        if MockServerInterface.get_users(self,current_username):
            self.ids.login_button.on_press = self.manager.current = \
                'PostScreen'
            LoginScreen.current_uid = MockServerInterface.temp_uid
            LoginScreen.current_username = MockServerInterface.temp_username
            MockServerInterface.temp_token = current_token
            self.ids.username_login.text = ''

        else:
            # This will need to be replaced by an error up or something of
            # of that nature
            content = BoxLayout(orientation='vertical')
            message_label = Label(
                text="User not found, please try again.")
            dismiss_button = Button(text='OK')
            content.add_widget(message_label)
            content.add_widget(dismiss_button)
            popup = Popup(title='Error', content=content,
                          size_hint=(0.3, 0.25))
            dismiss_button.bind(on_press=popup.dismiss)
            popup.open()
