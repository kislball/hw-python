import pytest
import random


@pytest.fixture(scope="module")
def small_random_list() :
    random.seed(42)
    return [random.randint(-100, 100) for _ in range(100)]


@pytest.fixture(scope="module")
def large_random_list() :
    random.seed(42)
    return [random.randint(-10000, 10000) for _ in range(10000)]


@pytest.fixture(scope="module")
def edge_case_lists():
    return [
        [], 
        [42], 
        [1, 2, 3, 4, 5], 
        [5, 4, 3, 2, 1], 
        [4, 1, 3, 4, 1, 2], 
        [3, -2, 5, 0, -1, 4], 
        [7, 7, 7, 7], 
        [9, 1], 
        [1, 1, 1, 1, 1], 
        [-5, -3, -1, -2, -4], 
        [0, 0, 0], 
    ]


@pytest.fixture
def random_test_data():
    random.seed(42)
    test_cases = []
    
    for _ in range(50):
        size = random.randint(0, 100)
        data_type = random.choice(['random', 'sorted', 'reverse', 'duplicates', 'negative'])
        
        if data_type == 'random':
            data = [random.randint(-1000, 1000) for _ in range(size)]
        elif data_type == 'sorted':
            data = list(range(size))
        elif data_type == 'reverse':
            data = list(range(size, 0, -1))
        elif data_type == 'duplicates':
            data = [random.randint(1, 10) for _ in range(size)]
        elif data_type == 'negative':
            data = [random.randint(-1000, -1) for _ in range(size)]
        
        test_cases.append(data)
    
    return test_cases


@pytest.fixture
def boundary_test_data():
    return [
        [], 
        [42], 
        [1, 1], 
        [1, 2], 
        [2, 1], 
        [1, 1, 1], 
        [1, 2, 3], 
        [3, 2, 1], 
        [0, 0, 0], 
        [-1, 0, 1], 
        [1000, -1000, 0], 
    ]


@pytest.fixture
def stress_test_data():
    random.seed(42)
    return {
        'small': [random.randint(-100, 100) for _ in range(100)],
        'medium': [random.randint(-1000, 1000) for _ in range(1000)],
        'large': [random.randint(-10000, 10000) for _ in range(10000)],
        'very_large': [random.randint(-100000, 100000) for _ in range(100000)],
    }


@pytest.fixture
def duplicate_heavy_data():
    random.seed(42)
    data = []
    
    for value in range(1, 11):
        count = random.randint(3, 10)
        data.extend([value] * count)
    
    random.shuffle(data)
    return data


