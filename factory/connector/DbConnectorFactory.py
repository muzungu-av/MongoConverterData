from typing import Generic, TypeVar

from factory.connector.AwsConnector import AwsConnector
from factory.connector.LocalConnector import LocalConnector

SwitcherConnectorFactory = {
    'local': LocalConnector,
    'aws': AwsConnector
}

C = TypeVar("C", LocalConnector, AwsConnector)


class DbConnectorFactory:
    def getConnector(type: str) -> Generic[C]:
        return SwitcherConnectorFactory.get(type)