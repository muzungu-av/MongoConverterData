from abc import ABCMeta, abstractmethod

from factory.db.Connector import Connector


class Reader():
    __metaclass__ = ABCMeta

    @abstractmethod
    def set_connector(self, connector: Connector) -> None:
        """set connector"""

    @abstractmethod
    def read_collection(self, **kwargs) -> bool:
        """read collection"""

