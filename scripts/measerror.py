# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 19:06:07 2016
@author: Jee-Bee for Jbae (c) 2016
"""
# https://wiki.python.org/moin/HandlingExceptions

import sys
# import Exception


class MeasError(Exception):
    """Base class for Meas Error handling"""
    """MORE INFO:
        Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """
#    def __init__(self, value):
#        self.value = value
#    def __str__(self):
#        return repr(self.value)


class Error(MeasError):
    """Exeption raised for wrong input values"""
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

    def __str__(self):
        return repr([self.expression, self.message])


class DataError(MeasError):
    """Exeption raised data Array"""
    def __init__(self, expression, message):
        # Maybe same type of Error as input Error
        self.expression = expression
        self.message = message

    def __str__(self):
        return repr([self.expression, self.message])


class EmptyError(MeasError):
    """Exeption raised non existing Functions"""
    def __init__(self, expression):
        # Maybe same type of Error as input Error
        self.expression = expression
        self. message = 'is an array with size 0'

    def __str__(self):
        return repr([self.expression, self.message])


class FunctionError(MeasError):
    """Exeption raised non existing Functions"""
    def __init__(self, function):
        # Maybe same type of Error as input Error
        self.function = function
        self.message = 'This function doesn\'t exist'

    def __str__(self):
        return repr([self.function, self.message])


class InputValError(MeasError):
    """Exeption raised for wrong input values"""
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

    def __str__(self):
        return repr([self.expression, self.message])


class InterfaceError(MeasError):
    """Exeption raised for non working combinations of inputs"""
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

    def __str__(self):
        return repr([self.expression, self.message])


class SizeError(MeasError):
    """Exeption raised for non working combinations of inputs"""
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

    def __str__(self):
        return repr([self.expression, self.message])


# small Test From here
# Tests from :
# #1
# #2 
# Don't work method according to @@ Put name here

# import numpy as np
# a = np.arange(2)
# b = 6
# c = varlist(a, b)

# a = np.arange(6)
# b = np.arange(1,6)
# c= a*b
# ValueError: operands could not be broadcast together with shapes (6,) (5,)
# ErrorStr = 'Some text here shapes ' + str(np.shape(a)) + ' ' + str(np.shape(b)) + '.'
# raise ValueError(ErrorStr)

# raise InterfaceError('inputs',ErrorStr)
# raise FunctionError('inputs')
