from kivy.uix.screenmanager import Screen
from mock_interface import MockServerInterface


class LoginScreen(Screen):
    current_uid = None
    current_username = None

    def kivy_login(self):
        current_username = self.ids.username_login.text

        if MockServerInterface.get_users(self,current_username):
            self.ids.login_button.on_press = self.manager.current = \
                'PostScreen'
            LoginScreen.current_uid = MockServerInterface.temp_uid
            LoginScreen.current_username = MockServerInterface.temp_username
            self.ids.username_login.text = ''

        else:
            # This will need to be replaced by an error up or something of
            # of that nature
            self.ids.login_button.text = 'UH OH'

