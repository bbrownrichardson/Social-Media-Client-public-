from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.uix.screenmanager import FallOutTransition
from PrivateMessenger import PrivateMessenger
from PostScreen import PostScreen
from ScreenToPost import ScreenToPost
from ChoosePMRecipient import ChoosePMRecipient
from CreateUserScreen import CreateUserScreen
from LoginScreen import LoginScreen
from mock_interface import MockServerInterface

kv = Builder.load_file('my.kv')

# ClientApp = App.get_running_app().server_interface


class ScreenApp(App):
    def build(self):
        # self.server_interface = MockServerInterface()
        self.manager = ScreenManager(transition=FallOutTransition())
        self.manager.add_widget(CreateUserScreen(name='CreateUserScreen'))
        self.manager.add_widget(LoginScreen(name='LoginScreen'))
        self.manager.add_widget(PostScreen(name='PostScreen'))
        self.manager.add_widget(PrivateMessenger(name='PrivateMessenger'))
        self.manager.add_widget(ChoosePMRecipient(name='ChoosePMRecipient'))
        self.manager.add_widget(ScreenToPost(name='ScreenToPost'))

        return self.manager


if __name__ == '__main__':
    ScreenApp().run()
