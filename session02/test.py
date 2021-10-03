from range_extract_02_D import range_extract

test_data = [
    [],
    [-8, -7, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20],
    [0, 1, 2, 4, 6, 7, 8, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 35, 36, 37, 38, 39]
]

if __name__ == '__main__':
    for lst in test_data:
        print( f"Pages  : {lst}" )
        print( f"Extract: {range_extract(lst)}" )
