from abc import ABCMeta, abstractmethod
from typing import Any
from pymongo import MongoClient

class Writer():
    __metaclass__ = ABCMeta

    @abstractmethod
    def set_collection(self, **kwargs) -> MongoClient:
        """set collection name"""


    @abstractmethod
    def write_collection(self, data: Any) -> str:
        """write data"""
