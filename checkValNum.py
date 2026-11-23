
def checkValNum(matrix):
    # Precs
    assert isinstance(matrix, list)
    assert len(matrix) > 0
    assert all(len(row) == len(matrix) for row in matrix)

    # Cod
    result = all(
        1 <= element <= len(matrix)
        for row in matrix
        for element in row
    )

    # Posc
    assert isinstance(result, bool)

    return result

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