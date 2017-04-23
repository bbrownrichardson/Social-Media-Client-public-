from kivy.uix.screenmanager import Screen
from mock_interface import MockServerInterface


class CreateUserScreen(Screen):
    current_uid = None
    current_token = None
    current_username = None

    def create_a_user(self):
        current_username = self.ids.create_user.text
        if MockServerInterface.add_users(self, current_username):
            CreateUserScreen.current_uid = MockServerInterface.temp_uid
            CreateUserScreen.current_username = \
                MockServerInterface.temp_username
            CreateUserScreen.current_token = MockServerInterface.temp_token
            self.ids.create_username.on_press = self.ids.token.text = 'Your User Name is: ' + MockServerInterface.temp_username + '\n' + 'Your Token is: ' + MockServerInterface.temp_token
            #self.manager.current = 'UserInfoScreen'
            self.ids.create_user.text = ''




        else:
            # This will need to replaced with an error popup or something of
            # of that nature
            content = BoxLayout(orientation='vertical')
            message_label = Label(
                text="Not a valid username, please try again")
            dismiss_button = Button(text='OK')
            content.add_widget(message_label)
            content.add_widget(dismiss_button)
            popup = Popup(title='Error', content=content,
                          size_hint=(0.3, 0.25))
            dismiss_button.bind(on_press=popup.dismiss)
            popup.open()


