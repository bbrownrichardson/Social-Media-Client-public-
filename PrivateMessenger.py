from kivy.uix.screenmanager import Screen
from mock_interface import MockServerInterface
from LoginScreen import LoginScreen
from ChoosePMRecipient import ChoosePMRecipient
from kivy.uix.gridlayout import GridLayout
from kivy.uix.bubble import BubbleButton
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

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
            content = BoxLayout(orientation='vertical')
            message_label = Label(
                text="Message failed, please double check information and try again")
            dismiss_button = Button(text='OK')
            content.add_widget(message_label)
            content.add_widget(dismiss_button)
            popup = Popup(title='Error', content=content,
                          size_hint=(0.3, 0.25))
            dismiss_button.bind(on_press=popup.dismiss)
            popup.open()

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
            content = BoxLayout(orientation='vertical')
            message_label = Label(
                text="There is a problem connecting to the server please try again")
            dismiss_button = Button(text='OK')
            content.add_widget(message_label)
            content.add_widget(dismiss_button)
            popup = Popup(title='Error', content=content,
                          size_hint=(0.3, 0.25))
            dismiss_button.bind(on_press=popup.dismiss)
            popup.open()


