from time import time as tick

def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

def time(fn, *args, **kwds):
    start = tick()
    result = fn(*args, **kwds)
    stop = tick()
    return stop - start, result

def memo(fn):
    cache = {}
    def proxy(*args):
        if args not in cache:
            cache[args] = fn(*args)
        return cache[args]
    return proxy
