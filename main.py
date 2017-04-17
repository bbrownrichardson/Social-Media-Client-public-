from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.uix.screenmanager import FallOutTransition
from PrivateMessenger import PrivateMessenger
from PostScreen import PostScreen

kv = Builder.load_file('my.kv')


class ScreenApp(App):
    def build(self):
        self.manager = ScreenManager(transition=FallOutTransition())
        self.manager.add_widget(PrivateMessenger(name='PrivateMessenger'))
        self.manager.add_widget(PostScreen(name='PostScreen'))

        return self.manager


if __name__ == '__main__':
    ScreenApp().run()