
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
