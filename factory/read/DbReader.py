from factory.db.Connector import Connector
from factory.read.Reader import Reader


class DbReader(Reader):

    def __init__(self):
        self.connector = None
        self.db_collection = None
        self.collection: str = None

    def set_connector(self, connector: Connector) -> None:
        print("[DbReader] Used this connector {}".format(connector))
        self.connector = connector

    def read_collection(self, **kwargs) -> bool:
        for key, value in kwargs.items():
            setattr(self, key.lower(), value)
            print("[DbReader] Received key: '{}' - value: '{}'".format(key.lower(), value))
            return self.found_collection(self, self.collection)  # self.collection приходит из kwargs

    def found_collection(self, collection: str) -> bool:
        collist = self.connector.mongoDb.list_collection_names()
        print("[DbReader] Try find collection: '{}' ".format(collection))
        if collection not in collist:
            print("[DbReader] Sorry. The collection '{}' does not exists!".format(collection))
            exit(4)
        else:
            print("[DbReader] Successfully found a collection")
            self.db_collection = self.connector.mongoDb[collection]
        return True

    def get_collection(self):
        return self.db_collection

