from src.checkSquare import checkSquare
from src.checkValNum import checkValNum
from src.checkRows import checkRows
from src.checkCols import checkCols


def checkSudoku(matrix):

    try:
        # Precondiciones / validación de entrada
        if not isinstance(matrix, list):
            return False

        if len(matrix) == 0:
            return False

        if not all(isinstance(row, list) for row in matrix):
            return False

        if not all(len(row) == len(matrix) for row in matrix):
            return False

        # Código
        result = (
            checkSquare(matrix)
            and checkValNum(matrix)
            and checkRows(matrix)
            and checkCols(matrix)
            )

        # Postcondición
        assert isinstance(result, bool)

        return result

    except (TypeError, ValueError, IndexError):
        return False