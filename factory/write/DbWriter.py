from typing import Any
from pymongo import MongoClient
from factory.db.Connector import Connector
from factory.write.Writer import Writer


class DbWriter(Writer):

    def __init__(self):
        self.connector = None
        self.db_collection = None

    def set_connector(self, connector: Connector) -> None:
        print("[DbWriter] Used this connector {}".format(connector))
        self.connector = connector

    def set_collection(self, **kwargs) -> MongoClient:
        for key, value in kwargs.items():
            setattr(self, key.lower(), value)
            print("[DbWriter] Received key: '{}' - value: '{}'".format(key.lower(), value))

            # return self.collection(self, self.collection)  # self.collection приходит из kwargs
        # self.connector.mongoDb[self.collection]
        # x = self.connector.mongoDb[self.collection].insert_one(data)
        # print("[DbWriter] Successfully wrote data '{}' to collection '{}'".format( self.collection))
        print("[DbWriter] set a new collection: {}".format(self.collection))
        self.db_collection = self.connector.mongoDb[self.collection]
        return self.db_collection


    # def write_collection(self, data: Any) -> str:
    #     x = self.connector.mongoDb[self.collection].insert_one(data)
    #     print("[DbWriter] Successfully wrote data '{}' to collection '{}'".format(x, self.collection))
    #     return "DbWriter write_collection"

