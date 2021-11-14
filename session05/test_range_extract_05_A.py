from range_extract_05_A import *

def test0():
    # Arrange
    pages = []
    # Act
    ranges_as_string = pages_to_ranges_string(pages)
    # Assert
    assert '' ==  ranges_as_string   

def test1():
    # Arrange
    pages = [100]
    # Act
    ranges_as_string = pages_to_ranges_string(pages)
    # Assert
    assert '100' ==  ranges_as_string  

def test_with_negative_numbers():
    # Arrange
    pages = [-8, -7, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]
    # Act
    ranges_as_string = pages_to_ranges_string(pages)
    # Assert
    assert '-8--6,-3-1,3-5,7-11,14,15,17-20' ==  ranges_as_string

def test_from_0():
    # Arrange
    pages = [0, 1, 2, 4, 6, 7, 8, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 35, 36, 37, 38, 39]
    # Act
    ranges_as_string = pages_to_ranges_string(pages)
    # Assert
    assert '0-2,4,6-8,11,12,14-25,27-33,35-39' == ranges_as_string

