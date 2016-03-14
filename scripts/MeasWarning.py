# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 10:42:34 2016
@author: Jee-Bee for Jbae (c) 2016
"""
import sys
import Warning


class MeasWarning(Warning):
    """Base class for Meas Warnings handling"""
    pass


class DimWarning(MeasWarning):
    """Base class for Meas Warnings handling"""
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

    def __str__(self):
        return repr([self.expression, self.message])
# For object Dimensions longer expected but not deadly for programm running


class InterfaceWarning(MeasWarning):
    """Base class for Meas Warnings handling"""
    # def __init__(self, expression, message):  # till expression is selcted interface
    def __init__(self, message):
        # self.expression = expression
        self.message = message

    def __str__(self):
        # return repr([self.expression, self.message])
        return repr(self.message)
# For choosen input \neq equal with output but not deadly for programm running


class SigGenaratorWarning(MeasWarning):
    """Base class for Meas Warnings handling"""
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

    def __str__(self):
        return repr([self.expression, self.message])
# For choosen input \neq equal with output but not deadly for programm running
