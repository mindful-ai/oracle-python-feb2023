def getdata():
    #return list(range(1, 6))
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


# --------------------------

r = getdata()
print(type(r))
for i in r:
    print(i, end=' ')

print("\n----------------------------------------\n")

# del r

r = getdata()
for i in r:
    print(i, end=' ')

print("\n----------------------------------------\n")

r = getdata()
print(next(r))
print(next(r))
for i in r:
    print(i, end=' ')