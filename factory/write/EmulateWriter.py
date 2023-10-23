from factory.write.Writer import Writer


class EmulateWriter(Writer):
    def write(self) -> str:
        return "EmulateWriter"

# эмулятор это не вообще а эмулятор записи изменений