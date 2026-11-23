
from checkSquare import checkSquare
from checkValNum import checkValNum
from checkRows import checkRows
from checkCols import checkCols


def checkSudoku(matrix):
    # Precs
    assert isinstance(matrix, list)

    # Cod
    if len(matrix) == 0:
        return False

    assert all(len(row) == len(matrix) for row in matrix)

    result = (
        checkSquare(matrix)
        and checkValNum(matrix)
        and checkRows(matrix)
        and checkCols(matrix)
    )

    # Posc
    assert isinstance(result, bool)

    return result

# Matriz válida
assert checkSudoku([
    [1, 2, 3],
    [2, 3, 1],
    [3, 1, 2]
]) is True

# Repetidos en una fila
assert checkSudoku([
    [1, 1, 3],
    [2, 3, 1],
    [3, 1, 2]
]) is False

# Repetidos en una columna
assert checkSudoku([
    [1, 2, 3],
    [1, 3, 2],
    [3, 1, 2]
]) is False

# Número fuera del rango (0)
assert checkSudoku([
    [0, 2, 3],
    [2, 3, 1],
    [3, 1, 2]
]) is False

# Número fuera del rango (4)
assert checkSudoku([
    [1, 2, 4],
    [2, 3, 1],
    [3, 1, 2]
]) is False

# Números negativos
assert checkSudoku([
    [1, 2, -1],
    [2, 3, 1],
    [3, 1, 2]
]) is False

# Matriz vacía
assert checkSudoku([]) is False