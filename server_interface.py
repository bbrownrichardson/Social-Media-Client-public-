import abc


class ServerInterface:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_posts(self):
        pass

    @abc.abstractmethod
    def add_post(self, content, uid, token, parentid=1):
        pass

    @abc.abstractmethod
    def get_users(self, username):
        pass

    @abc.abstractmethod
    def add_users(self, username):
        pass

    @abc.abstractmethod
    def send_message(self, senderid, recipientid, token, content):
        pass

    @abc.abstractmethod
    def get_recipient_users(self, username):
        pass

    @abc.abstractmethod
    def get_messages(self, uid, otherid, token):
        pass
    