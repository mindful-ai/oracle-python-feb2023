def myfunc(choice):

    def checkodd(n):
        return n % 2 != 0

    def checkeven(n):
        return n % 2 == 0

    if(choice):
        return checkodd
    else:
        return checkeven

# ----------------------------------------

''' 
f = myfunc(0)
print(f(100), f(101))

'''

# ----------------------------------------

import random

def jumble(funcobj):
    def wrapper(inputstr):
        L = list(inputstr)
        random.shuffle(L)
        inputword = ''.join(L)
        return funcobj(inputword)
    return wrapper

@jumble
def modifystring(s):
    return ' '.join([c.upper() for c in s])

print(modifystring("computer"))

#modifystring = jumble(modifystring)

print(modifystring("computer"))