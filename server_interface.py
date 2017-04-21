import abc


class ServerInterface:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_posts(self):
        pass

    @abc.abstractmethod
    def add_post(self, content):
        pass

    @abc.abstractmethod
    def get_users(self, username):
        pass

    @abc.abstractmethod
    def add_users(self, username):
        pass