# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 19:06:07 2016

@author: Jee-Bee for Jbae (c) 2016
"""
# https://wiki.python.org/moin/HandlingExceptions

import sys
#import Exception


class MeasError(Exception):
    """Base class for Meas Error handling"""
    pass


class Error(MeasError):
    """Exeption raised for wrong input values"""
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class DataError(MeasError):
    """Exeption raised data Array"""
    def __init__(self, expression, message):
        # Maybe same type of Error as input Error
        self.expression = expression
        self.message = message


class EmptyError(MeasError):
    """Exeption raised non existing Functions"""
    def __init__(self, function):
        # Maybe same type of Error as input Error
        self.function = function


class FunctionError(MeasError):
    """Exeption raised non existing Functions"""
    def __init__(self, function):
        # Maybe same type of Error as input Error
        self.function = function


class InputValError(MeasError):
    """Exeption raised for wrong input values"""
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class InputTypeError(MeasError):
    """Exeption raised for wrong input types"""
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class InterfaceError(MeasError):
    """Exeption raised for non working combinations of inputs"""
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class SizeError(MeasError):
    """Exeption raised for non working combinations of inputs"""
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


# small Test From here

#a = []
#b = 5
#
#try:
#    c = a + b
#    print(c)
#except EmptyError:
#    raise ValueError("No Value chosen")
#except b > a:
#    raise ValueError("Value 'b' have to be bigger")

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

#divide(2, 1)
#
#
#divide(2, 0)
#
#
#divide("2", "1")


#def varlist(var, length):
#    from numpy import array
#    try:
#        return True
#    except len(array(var)) > length:
#        return False
#        raise ValueError('#Your Error message 1')
#    except len(array(var)) < length:
#        return False
#        raise ValueError('#Your Error message 2')
#
#import numpy as np
#a = np.arange(3)
#b = 2
#c = varlist(a,b)
