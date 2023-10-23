from typing import TypeVar, Generic

from factory.connector.Connector import Connector
from factory.write.DbWriter import DbWriter
from factory.write.EmulateWriter import EmulateWriter
from factory.write.FileWriter import FileWriter

SwitcherModeWriteFactory = {
    'emulate': EmulateWriter,
    'file': FileWriter,
    'db': DbWriter
}

W = TypeVar("W", EmulateWriter, FileWriter, DbWriter)


class ModeWriteFactory:
    def switch(mode: str, connector: Connector) -> Generic[W]:
        writer = SwitcherModeWriteFactory.get(mode)
        writer.set_connector(writer, connector)  ## Unexpected type ??
        return writer
