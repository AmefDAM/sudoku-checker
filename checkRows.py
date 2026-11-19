def checkRows(matrix):
    return all(len(set(element)) == len(element) for element in matrix)

assert checkRows([[1, 2, 3],
            [2, 3, 1],
            [3, 1, 2]]) is True

assert checkRows([[1, 1, 3],
            [2, 3, 1],
            [3, 1, 2]]) is False

assert checkRows([[1, 2, 2],
            [2, 4, 1],
            [3, 1, 2]]) is False

assert checkRows([[1, 2, -1],
            [2, 1, 1],
            [3, 1, 2]]) is False

assert checkRows([[1, 0, 3],
            [2, 3, 1],
            [3, 1, 1]]) is False
