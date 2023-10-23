from factory.write.Writer import Writer


class FileWriter(Writer):
    def write(self) -> str:
        return "FileWriter"
