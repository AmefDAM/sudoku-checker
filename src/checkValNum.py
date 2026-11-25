
def checkValNum(matrix):
    # Precs
    assert isinstance(matrix, list)
    assert len(matrix) > 0
    assert all(len(row) == len(matrix) for row in matrix)

    # Cod
    result = all(
        isinstance(element, int) and not isinstance(element, bool)
        and 1 <= element <= len(matrix)
        for row in matrix
        for element in row
    )

    # Posc
    assert isinstance(result, bool)

    return result