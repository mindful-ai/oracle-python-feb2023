''' 
x + jy 
c1 = 3 + j4
c2 = 5 - j7
c1 + c2

'''

class complex(object):

    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __repr__(self):
        return str(self.real) + " + j" + str(self.imag)

    def __str__(self):
        return str(self.real) + " + j" + str(self.imag)   

    # + -> __add__() 
    # - -> __sub__()

    def __add__(self, other):
        newreal = self.real + other.real
        newimag = self.imag + other.imag
        return complex(newreal, newimag)

    def __sub__(self, other):
        newreal = self.real - other.real
        newimag = self.imag - other.imag
        return complex(newreal, newimag)

# ------------------------------------------------------


c1 = complex(5, 6)
c2 = complex(6, -4)
print(c1 + c2)
print(c1 - c2)