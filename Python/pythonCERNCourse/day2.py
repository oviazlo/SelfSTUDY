# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#import math
#trig = math.sin, math.cos, math.tan
#for fn in trig:
#    print(fn, fn(math.pi/3))
    
# this structure is called a lexical closure    
def make_adder(n):
    
    def adder(x):
        return n+x
    
    return adder

add3 = make_adder(3)
add9 = make_adder(9)
print(add3(4), add9(4))

# works, because there is no binding of "a" inside the function
a = 1
def fn():
    print(a)
fn()
###

# DOESN'T work, because there is binding of "a" inside the function but after lookup of a
# in this case compiler is not very smart
a = 1
def fn():
    print(a)
    a = 9
fn()
###


def one(*args):
    return args

one()
one(1,"trr",dir)

def two(a=1, b=2):
    return a,b

two()
two('a')
two('a','b')
two(b='b')

def three(a=1,*args, **kwds):
    return args, kwds

a,b, *x, z = 'abcdef'

d = {}
d[1] = "eins"; d["zwei"] = 2


fileIn = open('myfile','w')
print(1,2,3,4, "sdf", file = fileIn)
fileIn.write('5 6 7 8')
fileIn = open('myfile', 'r')
for line in fileIn:
    print(line)


d = {}
with open('/etc/passwd', 'r') as fileIn:
    for line in fileIn:
        uname,_,uid,_ = line.split(":",3)
        #print(uname,uid)
        d[int(uid)]=uname
        #print(line.split(':')[0:4:2])
print(d)
for uid in sorted(d):
    print(uid,d[uid])
   
    
def makeLabelSortingFunc(indexToUse):
    def getLabel(seq):
        return seq[indexToUse]
    return getLabel
    
def xxx(indexToUse, seq):
    return seq[indexToUse]

# makeLabelSortingFunc is a currying version of function xxx

readList = []
with open('/etc/passwd', 'r') as fileIn:
    for line in fileIn:
        uname,_,uid,_ = line.split(":",3)
        readList += [(int(uid),uname)]

print(sorted(readList, key=makeLabelSortingFunc(0)))

import functools
print(sorted(readList, key=functools.partial(xxx,0)))

import operator
print(sorted(readList, key=operator.itemgetter(0)))

# using lambda function
# lambda <list of args> : <return expression>
# lambds a,b,c: a*b+c
print(sorted(readList, key=lambda pair:pair[0] ))


def dummy(a,b,c):
    return a+b+c

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

