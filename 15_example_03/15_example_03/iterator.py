class MyNumbers(object):

    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= self.limit:
            x = self.a
            self.a += 1
            return x**2
        else:
            raise StopIteration

myobj = MyNumbers(10)
myiter = iter(myobj)


print(myobj)

for x in myiter:
  print(x)
