from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.bubble import BubbleButton
from mock_interface import MockServerInterface
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from ServerInterfaceException import ServerInterfaceException


class ConversationScreen(Screen):
    temp_convo_holder = None
    def clear_conversation_widgets(self):
        self.manager.current = 'PostScreen'
        if ConversationScreen.temp_convo_holder != None:
            ConversationScreen.temp_convo_holder.clear_widgets()

    def get_conversation_list(self):
        uid = MockServerInterface.temp_uid
        token = MockServerInterface.temp_token

        try:
            MockServerInterface.get_conversations(self, uid, token)
            conversations = MockServerInterface.temp_conversationdict
            holder = self.ids.conversation_holder

            holder.clear_widgets()
            for item in conversations:
                layer1 = GridLayout(cols=1)
                layer1.add_widget(BubbleButton(text=item['username'],
                                               size_hint=(1,2),
                                background_color=(0.0, 1.0, 1.0, 1.0)))
                holder.add_widget(layer1)
                ConversationScreen.temp_convo_holder = holder

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
