
def checkValNum(matrix):
    return all(1 <= element <= len(matrix) for row in matrix for element in row)

assert checkValNum([[1, 2, 3],
            [2, 3, 1],
            [3, 1, 2]]) is True

assert checkValNum([[1, 1, 3],
            [2, 3, 1],
            [3, 1, 2]]) is True

assert checkValNum([[1, 2, 3],
            [2, 4, 1],
            [3, 1, 2]]) is False

assert checkValNum([[1, 2, -1],
            [2, 3, 1],
            [3, 1, 2]]) is False

assert checkValNum([[1, 0, 3],
            [2, 3, 1],
            [3, 1, 2]]) is False