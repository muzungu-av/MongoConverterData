from abc import ABCMeta, abstractmethod


class Connector():
    __metaclass__ = ABCMeta

    @abstractmethod
    def open_source(self, **kwargs) -> bool:
        """connect to resource"""