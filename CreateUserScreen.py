from kivy.uix.screenmanager import Screen
from mock_interface import MockServerInterface


class CreateUserScreen(Screen):
    current_uid = None
    current_token = None
    current_username = None

    def create_a_user(self):
        current_username = self.ids['create_user'].text
        if MockServerInterface.add_users(self, current_username):
            CreateUserScreen.current_uid = MockServerInterface.temp_uid
            CreateUserScreen.current_username = MockServerInterface.temp_username
            CreateUserScreen.current_token = MockServerInterface.temp_token
            self.ids.create_username.on_press = self.manager.current = \
                'PostScreen'
            self.ids['create_user'].text = ''
        else:
            # This will need to replaced with an error popup or something of
            # of that nature
            self.ids['create_username'].text = 'OH NO'

