# f_n = f_n-1 + f_n-2
def fib(index):
    if index<2:
        return index
    else:
        return fib(index-1) + fib(index-2)
    
def fibi(index):
    tmpMemory = [0,1]
    if index<2:
        return index
    else:
        outVal = 0
        for i in range(1,index):
            outVal = tmpMemory[0] + tmpMemory[1]
            tmpMemory[0] = tmpMemory[1]
            tmpMemory[1] = outVal
    return outVal
    
def fibi2(N):
    c = 0
    n = 1
    while N>0:
        c, n = n, c+n
        N -= 1
    return c
        



from time import time as globalTime

def time(functionHandle,*args):
    startTime = globalTime()
    result = functionHandle(*args)
    endTime = globalTime()
    return endTime-startTime, result
     
def time_alt(thunk):
    startTime = globalTime()
    result = thunk()
    endTime = globalTime()
    return result, endTime-startTime

class memo_class:
    def __init__(self, functionHandle):
        self._functionHandle = functionHandle
        self._callMemory = {}
        
    def __call__(self, *args):
        if args not in self._callMemory:
            self._callMemory[args] = self._functionHandle(*args)
        return self._callMemory[args]

def memo_func(functionHandle):
    callMemory = {}
    
    def memo(*args):
        if args not in callMemory:
            callMemory[args] = functionHandle(*args)
        return callMemory[args]
    
    return memo

memo = memo_class


    

