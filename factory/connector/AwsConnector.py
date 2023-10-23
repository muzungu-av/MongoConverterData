from factory.connector.Connector import Connector


class AwsConnector(Connector):
    mongoClient = None
    mongoDb = None
    Uri: str = None
    Db: str = None
    Collection: str = None
    User: str = None
    Pass: str = None

    def open_source(self, **kwargs) -> bool:
        for key, value in kwargs.items():
            print("AwsConnector. Received key: '{}' - value: '{}'".format(key, value))
            setattr(self, key, value)

        # print("LocalConnector. Try connect to '{}'".format(self.Uri))
        print("AwsConnector... Not Working")
        return False