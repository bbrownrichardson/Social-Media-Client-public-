from kivy.uix.screenmanager import Screen
from mock_interface import MockServerInterface
from LoginScreen import LoginScreen
from ChoosePMRecipient import ChoosePMRecipient
from kivy.uix.gridlayout import GridLayout
from kivy.uix.bubble import BubbleButton


class PrivateMessenger(Screen):

    def send_message(self):

        recipientid = ChoosePMRecipient.chosen_uid
        senderid = LoginScreen.current_uid
        token = MockServerInterface.temp_token
        content = self.ids.Messenger_text.text

        if MockServerInterface.send_message(self, senderid, recipientid, token,
                                         content):
            self.ids.Messenger_Label.text = 'MESSAGE SENT SUCCESSFUL'
            self.ids.Messenger_text.text = ''
        else:
            self.ids.Messenger_Label.text = 'MESSAGE SENT FAILURE'

    def get_all_messages(self):
        senderid = LoginScreen.current_uid
        otherid = ChoosePMRecipient.chosen_uid
        token = MockServerInterface.temp_token
        messages_holder = self.ids.holder_label

        if MockServerInterface.get_messages(self, senderid,
                                            otherid,
                                            token):
            messages_holder.clear_widgets()
            for item in MockServerInterface.temp_messagedict:
                layer1 = GridLayout(cols=1, size_hint=(1, 2))
                layer1.add_widget(BubbleButton(text=item['sender'] +
                                                    ' said: ' +
                                              item['content'] + '\n\n'+
                                                        item['time'],
                                             size_hint=(1,10)))

                messages_holder.add_widget(layer1)

        else:
            self.ids.message_label.text = 'SOMETHING WENT WRONG'

