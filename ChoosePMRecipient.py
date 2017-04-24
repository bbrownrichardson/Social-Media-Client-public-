from kivy.uix.screenmanager import Screen
from mock_interface import MockServerInterface
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from ServerInterfaceException import ServerInterfaceException

class ChoosePMRecipient(Screen):
    chosen_uid = None

    def select_user(self):
        chosen_user = self.ids.choose_recipient.text
        try:
            MockServerInterface.get_recipient_users(self, chosen_user)
            ChoosePMRecipient.chosen_uid = MockServerInterface.temp_recipientid
            #self.ids.confirm_recipient.on_press = \
            self.manager.current = 'PrivateMessenger'
            self.ids.choose_recipient.text = ''

        except ServerInterfaceException as e:
            # This will need to be replaced by an error up or something of
            # of that nature
            content = BoxLayout(orientation='vertical')
            message_label = Label(text=str(e))
            dismiss_button = Button(text='OK')
            content.add_widget(message_label)
            content.add_widget(dismiss_button)
            popup = Popup(title='Error', content=content,
                          size_hint=(0.3, 0.25))
            dismiss_button.bind(on_press=popup.dismiss)
            popup.open()