#!/bin/env python
# Filename: func_key.py

def func(a, b=5, c=10):
    print 'a is', a, 'b is', b, 'c is', c

func(3, 7)
func(25, c=24)
func(c=50, a=100)
# func(ba=10)
# TypeError: func() got an unexpected keyword argument 'ba'
