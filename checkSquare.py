
def checkSquare(matrix):
    counter = 0
    column = len(matrix)

    while counter < len(matrix):
        row = len(matrix[counter])

        if column != row:
            return False

        counter += 1

    return True
    

assert checkSquare([[1, 2, 3],
            [2, 3, 1],
            [3, 1, 2]]) is True

assert checkSquare([[1, 2, 3, 4],
               [2, 3, 1, 3],
               [3, 1, 2, 3],
               [4, 4, 4, 4]]) is True


assert checkSquare([[1, 2, 3, 4],
               [2, 3, 1, 4],
               [4, 1, 2, 3],
               [3, 4, 1, 2]]) is True

'''       
incorrecto3 = [[1, 2, 3, 4, 5],
               [2, 3, 1, 5, 6],
               [4, 5, 2, 1, 3],
               [3, 4, 5, 2, 1],
               [5, 6, 4, 3, 2]]

incorrecto4 = [['a', 'b', 'c'],
               ['b', 'c', 'a'],
               ['c', 'a', 'b']]

incorrecto5 = [[1, 1.5],
               [1.5, 1]]
'''
assert checkSquare([[1, 0, 0, 0],
               [0, 1, 0],
               [0, 0, 0, 1]]) is False

'''print("All tests passed!")'''