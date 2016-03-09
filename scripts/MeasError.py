# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 19:06:07 2016

@author: Jee-Bee for Jbae (c) 2016
"""
import sys
import Exeption


class MeasError(Exeption):
    """Base class for Meas Error handling"""
    pass


class InputError(MeasError):
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


class NotKnownError(MeasError):
    pass
