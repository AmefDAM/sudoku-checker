import pytest
from checkSudoku import checkSudoku
import casosTest.casosTestSudoku as casosTest


@pytest.mark.parametrize("matriz", [
    casosTest.correcto
])
def test_sudoku_correcto(matriz):
    assert checkSudoku(matriz) == True


@pytest.mark.parametrize("matriz", [
    casosTest.numero_repetido_fila_columna,
    casosTest.numero_repetido_columna,
    casosTest.numero_no_presente,
    casosTest.numero_fuera_del_rango,
    casosTest.caracteres,
    casosTest.numeros_reales
])
def test_sudoku_incorrecto(matriz):
    assert checkSudoku(matriz) == False