# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 13:45:23 2016

@author: Jee-Bee for jBae (c) 2016
"""

# scale type(float int etc)
#
# scale based on size <1 en >1.
# scale to 1 and then times signal

# 2 Do
# Fix error messages
# check for floating values or int values in floating array

import numpy as np
import scripts.MeasWarning


def input_type(data):
    """ Check number type for required scaling """
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
            raise TypeError('wrong input type')
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
            raise TypeError('wrong input type')


def input_check(data):
    """ Check size and if floating value od input signals 
    2DO:
        - Add Inputtype to function"""
    if np.ndim(data) > 0:
        if isinstance(data[0], np.float):
            return(True)
        else:
            raise MeasWarning.TypeWarning('wrong input type')
            return(False)
    elif np.ndim(data) == 0:
        if isinstance(data, np.float):
            return(True)
        else:
            return(False)
            raise MeasWarning.TypeWarning('wrong input type')


def LSB(data, n):
    """ Calculate single LSB value- Least Significant Bit 
    Inputs:
    data = signal value or signal array
    n  = number of bits depth"""
    MaxVal = np.amax(data)
    MinVal = np.amin(data)
    LSB = (MaxVal - MinVal) / (2 ** n)
    return(LSB)


def iLSB(data, n):
    """ Calculate single inverse LSB value - Least Significant Bit 
    Inputs:
    data = signal value or signal array
    n  = number of bits depth"""
    MaxVal = np.amax(data)
    MinVal = np.amin(data)
    LSB = (MaxVal - MinVal) * (2 ** n)
    return(LSB)


def LSB_Sig(data, n, *argv):
    """ Calculate single inverse LSB signal - Least Significant Bit
    Inputs:
    data = signal value or signal array
    n  = number of bits depth"""
    LSB_val = LSB(data, n)
    LSB_sig = LSB_val * data
    return(LSB_sig)


def iLSB_Sig(data, n, *argv):
    """ Calculate single inverse LSB signal - Least Significant Bit
    Inputs:
    data = signal value or signal array
    n  = number of bits depth"""
    iLSB_val = iLSB(data, n)
    iLSB_sig = iLSB_val * data
    return(iLSB_sig)


def Bits2Volt(data, n, *argv):
    """ Calculate bit valued signal of Voltage signal
    Inputs:
    data = signal value or signal array
    n  = number of bits depth
    inputs on argv are: Amplification or Gain/ Offset
    2DO:
    """
    Volt = LSB_Sig(data, n, argv)
    return(Volt)


def Volt2Bits(data, n, *argv):
    """ Calculate Voltage Signal from Bit vulued signal
    Inputs:
    data = signal value or signal array
    n  = number of bits depth
    inputs on argv are: Amplification or Gain/ Offset
    2DO
    """
    Bits = iLSB_Sig(data, n, argv)
    return(Bits)


def Volt2Power(data, *argv):
    """ Calculate Power Signal from Voltage Signal
    Inputs:
    data = Volt signal value or Volt signal array
    argv = resistence
    r  = resistence in \Ohm
    inputs on argv are: Amplification or Gain/ Offset
    2DO
    """
    if len(argv) == 0:
        R = 50.0
    elif len(argv) == 1:
        if (type(argv[1]) == float) or (type(argv[1]) == int):
            R = argv[1]
        else:
            raise TypeError("Wrong Inpute Type")
    else:
        raise ValueError("Too many parameters")
    power = (data ** 2) / R
    return(power)
