class Matrix(object):

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        value = ''
        for item in self.matrix:
            value += str(item)[1:-1] + "\n"
        return value

    
# -------------------------------------------

m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(m1)
print(m2)
print(m1 + m2)
print(m1 * m2)