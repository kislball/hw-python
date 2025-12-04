"""
Этот файл содержит функции для сжатия какой-либо последовательности бит
алгоритмом Хафмана, при этом сохраняя словарь и сами сжатые данные
в одну последовательность байт.

В формате кодируется последовательность бит следующим образом:
    1. Используется Big Endian
    2. Считывается 4 байта, которые обозначают длину в битах
    3. Затем считывается наименьшее целое число байт, необходимое для
       кодирования данного числа бит. Лишние биты на конце игнорируются.

Формат файла:
    1. Используется Big Endian
    2. Первые 4 байта обозначают количество записей(N) в словаре
    3. Затем идёт N пар байт + битовая последовательность, где байт - символ,
       кодируемый следующей за ним битовой последовательностью
    4. Наконец, файл оканчивается битовой последовательностью в виде сжатых данных
"""
import math
import struct


def read_bits(file: bytes) -> str:
    bits_len = struct.unpack(">I", file[0:4])[0]
    bytes_len = math.ceil(bits_len / 8)
    if bytes_len == 0:
        return ""
    bts = struct.unpack(f">{bytes_len}B", file[4:4+bytes_len])
    out = ''.join(f"{x:08b}" for x in bts)
    return out[:bits_len]

def write_bits(s: str) -> bytes:
    assert all(x in '01' for x in s)

    bit_len = len(s)
    pad = (-bit_len) % 8
    if pad:
        s_padded = s + ("0" * pad)
    else:
        s_padded = s

    bts = []
    for i in range(0, len(s_padded), 8):
        as_int = int(s_padded[i:i+8], 2)
        bts.append(as_int)

    if bts:
        return struct.pack(f">I{len(bts)}B", bit_len, *bts)
    return struct.pack(">I", bit_len)


def read_bytes(file: bytes) -> tuple[str, dict[str, str]]:
    dict_length = struct.unpack(">I", file[0:4])[0]
    dictionary = {}
    offset = 4

    for i in range(dict_length):
        char_byte, code_len = struct.unpack(">BI", file[offset:offset+5])
        character = chr(char_byte)

        code = read_bits(file[offset + 1:])

        offset += math.ceil(code_len / 8) + 5

        dictionary[character] = code

    encoded_msg = read_bits(file[offset:])

    return (encoded_msg, dictionary)

def write_bytes(msg: str, dictionary: dict[str, str]) -> bytes:
    dict_len = struct.pack(">I", len(dictionary))
    out = dict_len
    for k, v in dictionary.items():
        out += struct.pack(">B", ord(k)) + write_bits(v)
    out += write_bits(msg)
    return out

