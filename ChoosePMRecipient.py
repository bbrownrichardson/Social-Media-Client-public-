from kivy.uix.screenmanager import Screen
from mock_interface import MockServerInterface


class ChoosePMRecipient(Screen):
    chosen_uid = None

    def select_user(self):
        chosen_user = self.ids.choose_recipient.text
        if MockServerInterface.get_recipient_users(self, chosen_user):
            ChoosePMRecipient.chosen_uid = MockServerInterface.temp_recipientid
            self.ids.confirm_recipient.on_press = self.manager.current = \
                'PrivateMessenger'
            self.ids.choose_recipient.text = ''

        else:
            # This will need to be replaced by an error up or something of
            # of that nature
            self.ids.confirm_recipient.text = 'UH OH'
