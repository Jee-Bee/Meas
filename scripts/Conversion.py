# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 13:45:23 2016

@author: enjbwink
"""

# scale type(float int etc)
# 
# scale based on size <1 en >1.
# scale to 1 and then times signal

# 2 Do
# Fix error messages 
# check for floating values or int values in floating array

import numpy as np


def input_type(data):
    if np.ndim(data) > 0:
        if isinstance(data[0], np.float):
            return(data)
        elif isinstance(data[0], np.int64):
            data = data.astype(float) / (2 ** (64 - 1))
            return(data)
        elif isinstance(data[0], np.int32):
            data = data.astype(float) / (2 ** (32 - 1))
            return(data)
        elif isinstance(data[0], np.int16):
            data = data.astype(float) / (2 ** (16 - 1))
            return(data)
        elif isinstance(data[0], np.int8):
            data = data.astype(float) / (2 ** (8 - 1))
            return(data)
        else:
            print('wrong input type')
    elif np.ndim(data) == 0:
        if isinstance(data, np.float):
            return(data)
        elif isinstance(data, np.int64):
            data = data.astype(float) / (2 ** (64 - 1))
            return(data)
        elif isinstance(data, np.int32):
            data = data.astype(float) / (2 ** (32 - 1))
            return(data)
        elif isinstance(data, np.int16):
            data = data.astype(float) / (2 ** (16 - 1))
            return(data)
        elif isinstance(data, np.int8):
            data = data.astype(float) / (2 ** (8 - 1))
            return(data)
        else:
            print('wrong input type')

def input_check(data):
#    For what do i need the input check??
#    Check for float data signals
    if np.ndim(data) > 0:
        if isinstance(data[0], np.float):
            return(True)
        else:
            print('wrong input type')
            return(False)
    elif np.ndim(data) == 0:
        if isinstance(data, np.float):
            return(True)
        else:
            return(False)
            print('wrong input type')

def U_LSB(data, n):
    MaxVal = np.amax(data)
    MinVal = np.amin(data)
    LSB = (MaxVal - MinVal) / (2 ** n)
    return(LSB)


def LSB_Sig(data, n, *argv):
    LSB = U_LSB(data, n)
    LSB_sig = LSB * data
    return(LSB_sig)


def Bits2Volt(data, n, *argv):
    # inputs on argv are: Amplification or Gain/ Offset 
    # 2DO
    Volt = LSB_Sig (data, n, argv)
    return(Volt)


def V2P(data, *argv):
    if len(argv) == 0:
        R = 50.0
    elif len(argv) == 1:
        if (type(argv[1]) == float) or (type(argv[1]) == int):
            R = argv[1]
        else:
            print ("Wrong Inpute Type")
    else:
        print ("Too many parameters")
    power = (data ** 2) / R
    return(power)
