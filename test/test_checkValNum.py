import pytest
from src.checkValNum import checkValNum
import casosTest.casosTestSudoku as casosTest


@pytest.mark.parametrize("matriz", [
    casosTest.correcto,
    casosTest.numero_repetido_fila_columna,
    casosTest.numero_repetido_columna
])
def test_numeros_validos(matriz):
    assert checkValNum(matriz) == True


@pytest.mark.parametrize("matriz", [
    casosTest.numero_no_presente,
    casosTest.numero_fuera_del_rango
])
def test_numeros_fuera_del_rango(matriz):
    assert checkValNum(matriz) == False


@pytest.mark.parametrize("matriz", [
    casosTest.caracteres,
    casosTest.numeros_reales
])
def test_valores_no_numericos_validos(matriz):
    assert checkValNum(matriz) == False