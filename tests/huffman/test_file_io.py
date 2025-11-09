import pytest

from src.huffman import binary as hf


def test_roundtrip_inmemory_and_file(tmp_path):
    bits = "1011001110"

    data = hf.write_bits(bits)
    assert isinstance(data, (bytes, bytearray))

    read_back = hf.read_bits(data)
    assert read_back == bits

def test_invalid_bits_raises():
    with pytest.raises(AssertionError):
        hf.write_bits("10x01")
