import random

import pytest

from src.huffman import binary as hf


@pytest.mark.parametrize("seed,iterations,max_bytes", [
    (0, 200, 32),
    (1, 500, 64),
])
def test_fuzz_roundtrip_simple(seed: int, iterations: int, max_bytes: int, tmp_path):
    rng = random.Random(seed)

    for _ in range(iterations):
        n = rng.randint(0, max_bytes)
        raw = rng.randbytes(n)
        bits = ''.join(f"{b:08b}" for b in raw)

        data = hf.write_bits(bits)
        assert hf.read_bits(data) == bits
