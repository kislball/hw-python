from src.graph.graph import Graph


def test_empty_graph():
    g = Graph([], [])
    result = list(g)
    assert result == []


def test_single_vertex():
    g = Graph([1], [])
    result = list(g)
    assert result == [1]


def test_linear_graph():
    g = Graph([1, 2, 3], [(1, 2), (2, 3)])
    result = list(g)
    assert result == [1, 2, 3]


def test_branching_graph():
    g = Graph([1, 2, 3, 4], [(1, 2), (1, 3), (2, 4)])
    result = list(g)
    assert result == [1, 2, 4, 3]


def test_disconnected_graph():
    g = Graph([1, 2, 3, 4], [(1, 2), (3, 4)])
    result = list(g)
    assert result == [1, 2]


def test_cycle():
    g = Graph([1, 2, 3], [(1, 2), (2, 3), (3, 1)])
    result = list(g)
    assert result == [1, 2, 3]


def test_complex():
    g = Graph([1, 2, 3, 4, 5], [(1, 2), (1, 3), (1, 4), (1, 5)])
    result = list(g)
    assert result == [1, 2, 3, 4, 5]
