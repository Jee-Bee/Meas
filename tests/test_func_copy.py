# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 21:30:39 2016

@author: Jee-Bee for jBae (c) 2016
"""

import types
import functools

def copy_f(f):
    """Based on http://stackoverflow.com/a/6528148/190597 (Glenn Maynard)"""
    g = types.FunctionType(f.__code__, f.__globals__, name=f.__name__,
                           argdefs=f.__defaults__,
                           closure=f.__closure__)
    print(f, g)
    g = functools.update_wrapper(g, f)
    g.__kwdefaults__ = f.__kwdefaults__
    return g

def f(arg1, arg2, arg3, kwarg1="FOO", *args, kwarg2="BAR", kwarg3="BAZ"):
    sum_123 = sum([arg1, arg2, arg3])
    return (sum_123, args, kwarg1, kwarg2, kwarg3)
f.cache = [1,2,3]
g = copy_f(f)

print(f(1,2,3,4,5))
print(g(1,2,3,4,5))
print(g.cache)
assert f is not g

v1 = 2
v2 = 3
v3 = 4
v4 = 5


def sum3_red(sum3):
    g = types.FunctionType(sum3.__code__, sum3.__globals__, name=sum3.__name__,
                           argdefs=sum3.__defaults__, closure=sum3.__closure__)
    print(g)
    return(g)


def sum3(a, b, c):
    sum3val = a+b+c
    return (sum3val)

answ = sum3(v1,v2,v3)
print(answ)

answ2 = sum3_red(v1,v2,v3)
print(answ2)
