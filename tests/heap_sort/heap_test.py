import pytest
import random
from src.heap_sort import heap_sort

@pytest.fixture(scope="module")
def small_random_list():
    data = [random.randint(-100, 100) for _ in range(100)]
    return data

@pytest.fixture(scope="module")
def large_random_list():
    data = [random.randint(-10000, 10000) for _ in range(10000)]
    return data

def test_empty_list():
    assert heap_sort([]) == []


def test_single_element():
    assert heap_sort([42]) == [42]


def test_already_sorted():
    assert heap_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_reverse_sorted():
    assert heap_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_duplicates():
    assert heap_sort([4, 1, 3, 4, 1, 2]) == [1, 1, 2, 3, 4, 4]

def test_mixed_numbers():
    arr = [3, -2, 5, 0, -1, 4]
    assert heap_sort(arr) == sorted(arr)

def test_small_random_list(small_random_list):
    arr = small_random_list[:]
    assert heap_sort(arr) == sorted(arr)

def test_large_random_list(large_random_list):
    arr = large_random_list[:]
    assert heap_sort(arr) == sorted(arr)

def test_all_same_values():
    assert heap_sort([7, 7, 7, 7]) == [7, 7, 7, 7]

def test_two_elements():
    assert heap_sort([9, 1]) == [1, 9]
