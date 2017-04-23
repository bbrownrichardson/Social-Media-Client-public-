from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.bubble import BubbleButton
from mock_interface import MockServerInterface


class ConversationScreen(Screen):
    def get_conversation_list(self):
        uid = MockServerInterface.temp_uid
        token = MockServerInterface.temp_token

        if MockServerInterface.get_conversations(self, uid, token):
            conversations = MockServerInterface.temp_conversationdict
            holder = self.ids.conversation_holder

            holder.clear_widgets()
            for item in conversations:
                layer1 = GridLayout(cols=1)
                layer1.add_widget(BubbleButton(text=item['username'],
                                               size_hint=(1,2),
                                background_color=(0.0, 1.0, 1.0, 1.0)))
                holder.add_widget(layer1)

        else:
            self.ids.conversaton_label.text = 'FAILURE'
