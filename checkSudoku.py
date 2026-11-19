
from checkSquare import checkSquare
from checkValNum import checkValNum
from checkRows import checkRows
from checkCols import checkCols


def checkSudoku(matrix):
    return all([checkSquare(matrix), checkValNum(matrix), checkRows(matrix), checkCols(matrix)])

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