
def checkSquare(matrix):
    counter = 0
    column = len(matrix)

    if not matrix:
        return False 

    while counter < len(matrix):
        row = len(matrix[counter])

        if column != row:
            return False

        counter += 1

    return True
    