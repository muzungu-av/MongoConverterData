from factory.connector.Connector import Connector
import pymongo


class LocalConnector(Connector):
    mongoClient = None
    mongoDb = None
    uri: str = None
    db: str = None
    # Collection: str = None
    user: str = None
    password: str = None

    # connector = None

    # def __init__(self) -> None:

    #  def open_source(self, uri: str, database: str, user: str, password: str) -> bool:
    #  def use_db(self, database: str) -> bool:
    #  def get_collection(self, collection: str) -> bool:

    def open_source(self, **kwargs) -> bool:
        for key, value in kwargs.items():
            print("[LocalConnector] Received key: '{}' - value: '{}'".format(key.lower(), value))
            setattr(self, key.lower(), value)

        print("[LocalConnector] Try connect to '{}'".format(self.uri))
        try:
            self.mongoClient = pymongo.MongoClient(self.uri)  # username=user, password=password
        except:
            print(Exception)  ##??
            return False

        return self.use_db(self, self.db)

    def use_db(self, db: str) -> bool:
        dblist = self.mongoClient.list_database_names()
        print("[LocalConnector] Try use database: '{}'".format(db))
        if db not in dblist:
            print("[LocalConnector] Sorry. The database '{}' does not exists!".format(db))
            exit(3)
        else:
            print("[LocalConnector] Successfully connected to the database!")
            self.mongoDb = self.mongoClient[db]

        return True
