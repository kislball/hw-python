import base64
import random

import src.huffman.binary as hbinary
from src.huffman.encoding import decode, encode


def test_fuzzy():
    for i in range(100):
        string = base64.b64encode(random.randbytes(128)).decode('utf-8')
        encoded, dictionary = encode(string)
        decoded = decode(encoded, dictionary)
        assert decoded == string

        encoded_binary = hbinary.write_bytes(encoded, dictionary)
        encoded2, dict2 = hbinary.read_bytes(encoded_binary)
        assert encoded2 == encoded
        assert dictionary == dict2
