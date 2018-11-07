# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def my_enumerate(sequence):
    """ docstring"""
    return zip(range(len(sequence)), sequence)

print("standard implementation")
for i, x in enumerate('hello'):
    print(f'{x} was in position {i}')

print("custom implementation")
for i, x in my_enumerate('hello'):
    print(f'{x} was in position {i}')
