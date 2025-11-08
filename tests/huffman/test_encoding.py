import base64
import random

from src.huffman.encoding import decode, encode


def test_fuzzy():
    for i in range(100):
        string = base64.b64encode(random.randbytes(128)).decode('utf-8')
        encoded, dictionary = encode(string)
        decoded = decode(encoded, dictionary)
        assert decoded == string
