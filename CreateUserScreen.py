from kivy.uix.screenmanager import Screen, ScreenManager
import requests


class CreateUserScreen(Screen):
    def createuser(self):
        url = 'http://nsommer.wooster.edu/social/users/post'
        new_user = self.ids['create_user'].text

        response = requests.post(url, data={'username': new_user})
        if response.status_code == 200:
            self.manager.current = 'PostScreen'
        else:
            pass # add popup widget to handle error
