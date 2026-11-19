# Sudoku Checker

A lightweight Python project that validates square matrices using basic specified rules.

The project checks whether a matrix satisfies the following conditions:
- It must be square (N × N).
- All values must be integers.
- All values must be within the range [1, N].
- No values can be repeated within the same row.
- No values can be repeated within the same column.

## Project Structure

```text
sudoku-checker/
│
├── checkSquare.py    # Checks whether the matrix is square.
├── checkValNum.py    # Checks whether all values are integers and within the valid range.
├── checkRows.py      # Checks for duplicate values in rows.
├── checkCols.py      # Checks for duplicate values in columns.
├── checkSudoku.py    # Combines all validation functions.
│
└── README.md
```

## Usage

The main function is `checkSudoku(matrix)`, which returns:

- `True` if the matrix satisfies all validation rules.
- `False` if at least one validation rule is not satisfied.

## Individual Validation Functions

Each validation function can also be used independently:

| Function | Description |
|---|---|
| `checkSquare(matrix)` | Checks whether the matrix has the same number of rows and columns. |
| `checkValNum(matrix)` | Checks whether all values are integers between 1 and N. |
| `checkRows(matrix)` | Checks that each row contains unique values. |
| `checkCols(matrix)` | Checks that each column contains unique values. |
| `checkSudoku(matrix)` | Combines all four validation functions. |
