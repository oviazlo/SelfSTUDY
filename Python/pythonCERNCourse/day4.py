# list comprehension:
[x*x for x in range(10)]
# is


list(map(lambda x: x*x, range(10)))

# list comprehention
[(x, y) for x in range(6) if x % 2 for y in range(6) if x > y]


#r = [A for x in X if B for y in Y if C]
# ***EQUIVALENT***
#r = []
#for x in X:
#    if B:
#        for y in Y:
#            if C:
#                r.append(A)

# dict comprehention:
{x:x*x for x in range(10)}

# set comprehention (only unique items):
{x*x for x in range(10)}

#lazy list comprehention
a = (n*n for n in range(10))
next(a)

# squash brackets ???
sum(n*n for n in range(10))

# f_n = f_n-1 + f_n-2
def fib(index):
    if index<2:
        return 2
    else:
        return fib(index-1) + fib(index-2)



# implementation of simplified version of lazy range
def gen_ints(start, stop):
    while start < stop:
        yield start
        start += 1
    return

a = gen_ints(3,6)
for i in a: print(i)


def boring():
    yield 1
    yield 2
    yield 3

def fibgen():
    c = 0
    n = 1
    while True:
        yield c
        c, n = n, c+n
        
from itertools import count

# lazy enumerate with itertools
def ienumerate(iterable, start = 0):
    return zip(count(start),iterable)
    

class cenumerate:
    def __init__(self,iterable, start=0):
        self._it = iter(iterable) # get iteration
        self._count = start - 1
        
    def __next__(self):
        self._count += 1
        return self._count, next(self._it)

    def __iter__(self):
        return self
    
    
    
# example of decorator
class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h
    
    @property # equal to "a = property(a)"
    def a(self):
        return self.w * self.h
        
    @a.setter
    def a(self, new):
        self.w = new / self.h


