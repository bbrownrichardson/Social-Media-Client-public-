import abc


class ServerInterface:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_posts(self):
        pass

    @abc.abstractmethod
    def add_post(self, content, parent_id=-1):
        pass
