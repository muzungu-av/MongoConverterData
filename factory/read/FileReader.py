from factory.connector.Connector import Connector
from factory.read.Reader import Reader


class FileReader(Reader):

    connector = None

    def set_connector(self, connector: Connector) -> None:
        self.connector = connector

    def read_collections(self, **kwargs) -> str:
        return "FileReader read_collections"

