from floyd_warshall import floyd_warshall, decrement_edges

def test():
    # Arrange
    n_nodes = 4
    graph = decrement_edges([[1, 3, -2], [2, 1, 4], [2, 3, 3], [3, 4, 2], [4, 2, -1]])
    # Act
    table = floyd_warshall(n_nodes, graph)
    # Assert
    # pair     dist    path
    # 1 → 2    -1       1 → 3 → 4 → 2
    assert len(table) == 12
    assert table[0]['dist'] == -1
    assert table[0]['path'] == [0, 2, 3, 1]

def test_two_points():
    # Arrange
    n_nodes = 2
    graph = [[0, 1, 1], [1,0,1]]
    # Act
    table = floyd_warshall(n_nodes, graph)
    # Assert
    assert len(table) == 2
    assert table[0]['dist'] == 1
    assert table[0]['path'] == [0, 1]
    assert table[1]['dist'] == 1
    assert table[1]['path'] == [1, 0]
