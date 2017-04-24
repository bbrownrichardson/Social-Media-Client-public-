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
from ServerInterfaceException import ServerInterfaceException


class PrivateMessenger(Screen):
    temp_message_holder = None
    def clear_messages(self):
        self.manager.current = 'PostScreen'
        if PrivateMessenger.temp_message_holder != None:
            PrivateMessenger.temp_message_holder.clear_widgets()
            ChoosePMRecipient.chosen_uid = None

    def send_message(self):

        recipientid = ChoosePMRecipient.chosen_uid
        senderid = LoginScreen.current_uid
        token = MockServerInterface.temp_token
        content = self.ids.Messenger_text.text

        try:
            MockServerInterface.send_message(self, senderid, recipientid, token,
                                         content)
            self.ids.Messenger_Label.text = 'MESSAGE SENT SUCCESSFULLY'
            self.ids.Messenger_text.text = ''
        except ServerInterfaceException as e:
            content = BoxLayout(orientation='vertical')
            message_label = Label(
                text=str(e))
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

        try:
            MockServerInterface.get_messages(self, senderid,
                                            otherid,
                                            token)
            messages_holder.clear_widgets()
            for item in MockServerInterface.temp_messagedict:
                layer1 = GridLayout(cols=1, size_hint=(1, 2))
                layer1.add_widget(BubbleButton(text=item['sender'] +
                                                    ' said: ' +
                                              item['content'] + '\n\n'+
                                                        item['time'],
                                             size_hint=(1,10)))

                messages_holder.add_widget(layer1)
                PrivateMessenger.temp_message_holder = messages_holder

        except ServerInterfaceException as e:
            content = BoxLayout(orientation='vertical')
            message_label = Label(
                text=str(e))
            dismiss_button = Button(text='OK')
            content.add_widget(message_label)
            content.add_widget(dismiss_button)
            popup = Popup(title='Error', content=content,
                          size_hint=(0.3, 0.25))
            dismiss_button.bind(on_press=popup.dismiss)
            popup.open()


