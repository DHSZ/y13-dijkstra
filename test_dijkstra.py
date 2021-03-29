from dijkstra import shortest_path

test_graph = {'A': {'B': 8, 'C': 5},
              'B': {'A': 8, 'C': 3, 'D': 1},
              'C': {'A': 5, 'B': 3, 'D': 6, 'E': 9},
              'D': {'C': 6, 'B': 1, 'E': 2},
              'E': {'C': 9, 'D': 2}
              }


def test_b_to_b():
    assert shortest_path(test_graph, 'B', 'B') == "B - 0"


def test_c_to_b():
    assert shortest_path(test_graph, 'C', 'B') == "CB - 3"

    
def test_a_to_d():
    assert shortest_path(test_graph, 'A', 'D') == "ABD - 9"


def test_a_to_e():
    assert shortest_path(test_graph, 'A', 'E') == "ABDE - 11"


def test_e_to_a():
    assert shortest_path(test_graph, 'E', 'A') == "EDBA - 11"
