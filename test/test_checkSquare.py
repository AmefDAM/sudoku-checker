import pytest
from src.checkSquare import checkSquare
import casosTest.casosTestSudoku as casosTest


@pytest.mark.parametrize("matriz", [
    casosTest.correcto
])
def test_cuadrados_validos(matriz):
    assert checkSquare(matriz) == True


@pytest.mark.parametrize("matriz", [
    casosTest.numero_repetido_fila_columna,
    casosTest.numero_repetido_columna
])
def test_cuadrados_repetidos(matriz):
    assert checkSquare(matriz) == False