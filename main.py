import sys
from argParser import createParser
from factory.connector.Connector import Connector
from factory.connector.DbConnectorFactory import DbConnectorFactory
from factory.read.ModeReadFactory import ModeReadFactory
from factory.read.Reader import Reader
from factory.write.ModeWriteFactory import ModeWriteFactory
from factory.write.Writer import Writer
from process.Processor import Processor

if __name__ == '__main__':
    parser = createParser()
    namespace_dict = parser.parse_args(sys.argv[1:]).__dict__

    connector: Connector = DbConnectorFactory.getConnector('local')
    connector.open_source(connector, Uri="mongodb://localhost:27017/", Db="hydrus")

    reader: Reader = ModeReadFactory.switch(namespace_dict.get('read_from'), connector)

    writer: Writer = ModeWriteFactory.switch(namespace_dict.get('write_to'), connector)

    proc: Processor = Processor(reader, writer)
    proc.process()

    # local.disconnect(local)
