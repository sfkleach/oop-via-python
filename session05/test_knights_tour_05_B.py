from knights_tour_05_B import *

def test_knights_tour():
    # Arrange
    size = 20
    # Act
    board = knights_tour('a1', boardsize=size)
    # Assert
    assert sorted(board.values()) == list(range(1, size**2 + 1))
    assert sorted(board.keys()) == list((x, y) for x in range(0, size) for y in range(0, size))
