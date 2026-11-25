
def checkRows(matrix):
    # Precondiciones
    assert isinstance(matrix, list)
    assert len(matrix) > 0
    assert all(len(row) == len(matrix) for row in matrix)

    # Comprobación
    result = all(
        len(set(element)) == len(element)
        for element in matrix
    )

    # Poscondición
    assert isinstance(result, bool)

    return result

if __name__ == "__main__":

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