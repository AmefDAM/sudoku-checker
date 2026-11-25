import pytest
from src.checkCols import checkCols
import casosTest.casosTestSudoku as casosTest


@pytest.mark.parametrize("matriz", [
    casosTest.correcto,
    casosTest.numero_repetido_fila_columna
])
def test_columnas_validas(matriz):
    assert checkCols(matriz) == True


@pytest.mark.parametrize("matriz", [
    casosTest.numero_repetido_columna
])
def test_columnas_repetidas(matriz):
    assert checkCols(matriz) == False