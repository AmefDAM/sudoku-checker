
from src.checkSquare import checkSquare
from src.checkValNum import checkValNum
from src.checkRows import checkRows
from src.checkCols import checkCols


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
