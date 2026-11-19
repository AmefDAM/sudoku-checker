
def checkInteger(matrix):
    for i in matrix:
        if (set(i)).isalpha():




assert checkInteger([[1, 2, 3],
            [2, 3, 1],
            [3, 1, 2]]) is True

assert checkInteger([[1, 2, 3, 4],
               [2, 3, 1, 3],
               [3, 1, 2, 3],
               [4, 4, 4, 4]]) is True


assert checkInteger([[1, 2, 3, 4],
               [2, 3, 1, 4],
               [4, 1, 2, 3],
               [3, 4, 1, 2]]) is True

'''       
incorrecto3 = [[1, 2, 3, 4, 5],
               [2, 3, 1, 5, 6],
               [4, 5, 2, 1, 3],
               [3, 4, 5, 2, 1],
               [5, 6, 4, 3, 2]]
'''
assert checkInteger([['a', 'b', 'c'],
               ['b', 'c', 'a'],
               ['c', 'a', 'b']]) is True
'''
incorrecto5 = [[1, 1.5],
               [1.5, 1]]
'''
assert checkInteger([[1, 0, 0, 0],
               [0, 1, 0],
               [0, 0, 0, 1]]) is False

print("All tests passed!")