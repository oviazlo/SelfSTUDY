import functools
import operator

from functools import reduce

with open('/home/oviazlo/SelfSTUDY/pythonCERNCourse/dummy.txt','r') as fileIn:
    for line in fileIn:
        if line != '\n':
            intList = map(int, line.split())
            print(reduce(operator.add, intList))

# example that when one go through lazy container once container become empty!!!
with open('/home/oviazlo/SelfSTUDY/pythonCERNCourse/dummy.txt','r') as fileIn:
    for line in fileIn:
        if line != '\n':
            intList = map(int, line.split())
            print(list(intList))
            print(list(intList))
# but know it works:
with open('/home/oviazlo/SelfSTUDY/pythonCERNCourse/dummy.txt','r') as fileIn:
    for line in fileIn:
        if line != '\n':
            intList = list(map(int, line.split()))
            print(intList)
            print(intList)
            

with open('/home/oviazlo/SelfSTUDY/pythonCERNCourse/dummy2.txt','r') as fileIn:
    for line in fileIn:
        #clearList = list(filter(lambda a:a.isnumeric(),line.split()))
        clearList = list(filter(str.isnumeric,line.split()))
        #print(clearList)
        if len(clearList) == 0:
            continue
        intList = map(int, clearList)
        print(reduce(operator.add, intList))


with open('/home/oviazlo/SelfSTUDY/pythonCERNCourse/dummy2.txt','r') as fileIn:
    for line in fileIn:
        #clearList = list(filter(lambda a:a.isnumeric(),line.split()))
        clearList = list(filter(str.isnumeric,line.split()))
        intList = map(int, clearList)
        print(reduce(operator.add, intList,0))


def bottom():
    print('bottom 1')
    middle()
    print('bottom 2')
    
def middle():
    #top()
    try:
        top()
        print('middle')
    except ValueError:
        print('handling ValueErrir')
        
def top():
    raise ValueError
    
bottom()





def convertToInt(returnValue):
    def convertToInt(a):
        try:
            return int(a)
        except ValueError:
            print("catching non-numeric value:",a)
            return returnValue
    return convertToInt

with open('/home/oviazlo/SelfSTUDY/pythonCERNCourse/dummy2.txt','r') as fileIn:
    output = ()
    for line in fileIn:
        #clearList = list(filter(str.isnumeric,line.split()))
        #intList = map(int, clearList)
        clearList = list(line.split())
        intList = map(convertToInt(0), clearList)
        output += ((reduce(operator.add, intList,0)),)
    print(output)
    
def is_int(a):
    try:
        int(a)
    except ValueError:
        return False
    else:
        return True

with open('/home/oviazlo/SelfSTUDY/pythonCERNCourse/dummy2.txt','r') as fileIn:
    output = ()
    for line in fileIn:
        clearList = list(filter(is_int,line.split()))
        intList = map(int, clearList)
        output += ((reduce(operator.add, intList,0)),)
    print(output) 
    

class Counter:
    
    def __init__(self,start):
        #print(dir(self))
        self.count = start
        #print(dir(self))

    def up(self,n=1):
        self.count += n
        
    def down(self, n=1):
        self.count -= n

a = Counter(10)

a.up(2)
print(a.count) 
Counter.up(a,2) # identical to a.up(2)
print(a.count) 

print(a)
print(Counter)

print(Counter.count)
a.foo = 9
del a.count

class Queue:
    
    def __init__(self):
        self.body = []

    def add(self, item):
        #self.body += [item]
        self.body.append(item)
        return self.body
        
    def remove(self):
        if len(self.body)==0:
            pass
        else:
            return self.body.pop(0)
#        try:
#            self.body.pop(0)
#        except IndexError:
#            pass
            
a = Queue()
a.add(1)
a.add(2)
a.add(3)
a.remove()
a.remove()
a.remove()
a.remove()


class Counter:
    
    def __init__(self,start):
        #print(dir(self))
        self.count = start
        #print(dir(self))

    def up(self,n=1):
        self.count += n
        
    def down(self, n=1):
        self.count -= n


class Addcounter(Counter):
    
    def __repr__(self):
        return 'Addcounter({.count})'.format(self)
    
    __str__ = __repr__
    
    def __add__(self,other):
        return Addcounter(self.count + other.count)
    
    __radd__ = __add__
    
c = Counter(2)
a = Addcounter(3)
a+a
a+c
c+a
c+c

foo = Counter(341)

'--->{.count}<----->'.format(foo)
f'-----><----'
f'----->{a+a}<----'
    


class EmergencyQueue(Queue):
    def addToFront(self, item):
        self.body.insert(0,item)
        print(self.body)

eq = EmergencyQueue()
eq.addToFront(5)
eq.add(2)
eq.add(2)
eq.add(4)
eq.addToFront(5)


class Noisy(Queue):
    def add(self, item):
        Queue.add(self,item)
        print(item)

nq = Noisy()
nq.add(4)

class QueueIsEmpty(Exception):
    pass

class EmptyQueue:
    
    def __init__(self):
        self.body = []

    def add(self, item):
        #self.body += [item]
        self.body.append(item)
        return self.body
        
    def remove(self):
#        if len(self.body)==0:
#            pass
#        else:
#            return self.body.pop(0)
        try:
            self.body.pop(0)
        except IndexError:
            raise QueueIsEmpty

eq = EmptyQueue()
eq.remove()





