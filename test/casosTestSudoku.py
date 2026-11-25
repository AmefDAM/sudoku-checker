from sudoku import checkSudoku, checkValNum, checkSquare, checkRows, checkCols


# =========================
# MATRICES DE PRUEBA
# =========================

correcto = [
    [1, 2, 3],
    [2, 3, 1],
    [3, 1, 2]
]

numero_repetido_fila_columna = [
    [1, 2, 3, 4],
    [2, 3, 1, 3],
    [3, 1, 2, 3],
    [4, 4, 4, 2]
]

numero_repetido_columna = [
    [1, 2, 3],
    [2, 3, 1],
    [2, 3, 1]
]

numero_no_presente = [
    [1, 2, 3, 4],
    [2, 3, 1, 2],
    [4, 1, 2, 3],
    [2, 3, 1, 4]
]

numero_fuera_del_rango = [
    [1, 2, 3, 4, 5],
    [2, 3, 1, 5, 6],
    [4, 5, 2, 1, 3],
    [3, 4, 5, 2, 1],
    [5, 6, 4, 3, 2]
]

caracteres = [
    ['a', 'b', 'c'],
    ['b', 'c', 'a'],
    ['c', 'a', 'b']
]

numeros_reales = [
    [1, 1.5],
    [1.5, 1]
]

irregular_fila = [
    [1, 2, 3],
    [2, 3, 1]
]

irregular_columna = [
    [1, 2, 3],
    [2, 3, 1],
    [3, 1]
]

lista_vacia = []

__oculto = [[1]]


# =========================
# TESTS checkSudoku
# =========================

def test_checkSudoku():
    assert checkSudoku(correcto) is True
    assert checkSudoku(numero_repetido_fila_columna) is False
    assert checkSudoku(numero_repetido_columna) is False
    assert checkSudoku(numero_fuera_del_rango) is False
    assert checkSudoku(lista_vacia) is False


# =========================
# TESTS checkValNum
# =========================

def test_checkValNum():
    assert checkValNum(correcto) is True
    assert checkValNum(numero_repetido_fila_columna) is True
    assert checkValNum(numero_repetido_columna) is True
    assert checkValNum(numero_no_presente) is True
    assert checkValNum(numero_fuera_del_rango) is False
    assert checkValNum(caracteres) is False
    assert checkValNum(lista_vacia) is False


# =========================
# TESTS checkSquare
# =========================

def test_checkSquare():
    assert checkSquare(correcto) is True
    assert checkSquare(numero_repetido_fila_columna) is True
    assert checkSquare(numero_repetido_columna) is True
    assert checkSquare(numero_no_presente) is True
    assert checkSquare(numero_fuera_del_rango) is True
    assert checkSquare(caracteres) is True
    assert checkSquare(numeros_reales) is True
    assert checkSquare(irregular_fila) is False
    assert checkSquare(irregular_columna) is False
    assert checkSquare(lista_vacia) is False


# =========================
# TESTS checkRows
# =========================

def test_checkRows():
    assert checkRows(correcto) is True
    assert checkRows(numero_repetido_fila_columna) is False
    assert checkRows(numero_repetido_columna) is True
    assert checkRows(numero_no_presente) is False
    assert checkRows(numero_fuera_del_rango) is False
    assert checkRows(caracteres) is True
    assert checkRows(numeros_reales) is True
    assert checkRows(irregular_fila) is True
    assert checkRows(irregular_columna) is False
    assert checkRows(lista_vacia) is False


# =========================
# TESTS checkCols
# =========================

def test_checkCols():
    assert checkCols(correcto) is True
    assert checkCols(numero_repetido_fila_columna) is False
    assert checkCols(numero_repetido_columna) is False
    assert checkCols(numero_no_presente) is False
    assert checkCols(numero_fuera_del_rango) is False
    assert checkCols(caracteres) is True
    assert checkCols(numeros_reales) is True
    assert checkCols(irregular_fila) is False
    assert checkCols(irregular_columna) is True
    assert checkCols(lista_vacia) is False