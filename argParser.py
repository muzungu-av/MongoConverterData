import argparse

from factory.read.ModeReadFactory import SwitcherModeReadFactory
from factory.write.ModeWriteFactory import SwitcherModeWriteFactory


def createParser():
    parser = argparse.ArgumentParser()
    choices_read = list(SwitcherModeReadFactory.keys())
    choices_write = list(SwitcherModeWriteFactory.keys())
    parser.add_argument('-r', '--read-from', choices=choices_read, required=True)
    parser.add_argument('-w', '--write-to', choices=choices_write, required=True)
    return parser
