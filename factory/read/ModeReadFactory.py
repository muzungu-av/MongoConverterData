from typing import TypeVar, Generic

from factory.connector.Connector import Connector
from factory.read.DbReader import DbReader
from factory.read.FileReader import FileReader
from factory.read.Reader import Reader

SwitcherModeReadFactory = {
    'file': FileReader,
    'db': DbReader
}

R = TypeVar("R", FileReader, DbReader)


class ModeReadFactory:
    def switch(mode: str, connector: Connector) -> Generic[R]:
        reader = SwitcherModeReadFactory.get(mode)
        reader.set_connector(reader, connector) ## Unexpected type ??
        return reader
