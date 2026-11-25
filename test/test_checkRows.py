import pytest
from src.checkRows import checkRows
import casosTest.casosTestSudoku as casosTest


@pytest.mark.parametrize("matriz", [
    casosTest.correcto,
    casosTest.numero_repetido_columna
])
def test_filas_validas(matriz):
    assert checkRows(matriz) == True


@pytest.mark.parametrize("matriz", [
    casosTest.numero_repetido_fila_columna
])
def test_filas_repetidas(matriz):
    assert checkRows(matriz) == False