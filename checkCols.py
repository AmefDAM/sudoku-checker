
def checkCols(matrix):
    # Precs
    assert isinstance(matrix, list)
    assert len(matrix) > 0
    assert all(len(row) == len(matrix) for row in matrix)

    # Cod
    result = all(
        len(set(row[i] for row in matrix)) == len(matrix)
        for i in range(len(matrix))
    )

    # Posc
    assert isinstance(result, bool)

    return result

if __name__ == "__main__":

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