
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
