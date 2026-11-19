
def checkCols(matrix):
    return all(len(set(row[i] for row in matrix)) == len(matrix) for i in range(len(matrix)))




assert checkCols([[1, 2, 3],
            [2, 3, 1],
            [3, 1, 2]]) is True

assert checkCols([[1, 1, 3],
            [2, 3, 1],
            [3, 1, 2]]) is False

assert checkCols([[1, 2, 2],
            [2, 4, 1],
            [3, 1, 2]]) is False

assert checkCols([[1, 2, -1],
            [2, 1, 1],
            [3, 1, 2]]) is False

assert checkCols([[1, 0, 3],
            [2, 3, 1],
            [3, 1, 1]]) is False