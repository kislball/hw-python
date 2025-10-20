import pytest
from src.heap_sort import heap_sort
from src.sorting.sorting import sort as bubble_sort


def heap_sort_wrapper(data):
    data_copy = data[:]
    return heap_sort(data_copy)


def bubble_sort_wrapper(data):
    data_copy = data[:]
    bubble_sort(data_copy)
    return data_copy


SORTING_ALGORITHMS = [
    (heap_sort_wrapper, "heap_sort"),
    (bubble_sort_wrapper, "bubble_sort")
]

TEST_CASES = [
    ([], "empty_list"),
    ([42], "single_element"),
    ([1, 2, 3, 4, 5], "already_sorted"),
    ([5, 4, 3, 2, 1], "reverse_sorted"),
    ([4, 1, 3, 4, 1, 2], "duplicates"),
    ([3, -2, 5, 0, -1, 4], "mixed_numbers"),
    ([7, 7, 7, 7], "all_same_values")
]


@pytest.mark.parametrize("algorithm,algorithm_name", SORTING_ALGORITHMS)
@pytest.mark.parametrize("data,test_name", TEST_CASES)
def test_sorting_cases(algorithm, algorithm_name, data, test_name):
    expected = sorted(data)
    assert algorithm(data) == expected


@pytest.mark.parametrize("algorithm,algorithm_name", SORTING_ALGORITHMS)
def test_small_random_list(algorithm, algorithm_name, small_random_list):
    assert algorithm(small_random_list) == sorted(small_random_list)


@pytest.mark.parametrize("algorithm,algorithm_name", SORTING_ALGORITHMS)
def test_large_random_list(algorithm, algorithm_name, large_random_list):
    assert algorithm(large_random_list) == sorted(large_random_list)


@pytest.mark.parametrize("algorithm,algorithm_name", SORTING_ALGORITHMS)
def test_edge_case_lists(algorithm, algorithm_name, edge_case_lists):
    for i, data in enumerate(edge_case_lists):
        assert algorithm(data) == sorted(data)
