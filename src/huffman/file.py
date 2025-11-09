from .binary import read_bytes, write_bytes
from .encoding import decode, encode


class HuffmanFile:
    def __init__(self, file_name: str):
        self.file_object = open(file_name, 'rb+')

    def _read_entire(self):
        return self.file_object.read()

    def read(self):
        data = self._read_entire()
        msg, dictionary = read_bytes(data)
        return decode(msg, dictionary)

    def write(self, data: str, overwrite = False):
        new_data = data
        if not overwrite:
            new_data = self.read() + data
        encoded, dictionary = encode(new_data)
        binary_data = write_bytes(encoded, dictionary)
        self.file_object.write(binary_data)


    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.file_object.close()
