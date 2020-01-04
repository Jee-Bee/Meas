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
#from src import MeasWarning
#MeasWarning.


def even(x):
    """
    inputs:
        spec = input array of unknown values.
    Output:
        Symetry check = True or False boolean

    Check for symmetry in given Signals
    - Real signals have \'even\' symmerty
    - Imaginair signals have \'odd\' symmetry
    - Magnitute signals have \'even\' symmetry
    - phase signals have \'odd\' symmetry +/- pi"""
    N = np.int(len(x))
    if (x[1: N/2] == np.flipud(x[-N/2 + 1:])).all():
        evenvals = True
    else:
        evenvals = False
    return(evenvals)


def input_type(data):
    """
    Input:
        data = array of data recorded by input of audio/ vibration interface.
    output:
        data but nof floating point +/-1.

    Check d-type or data type (class) of the input array. After this it
    rescaled the data to floating point data array of +/- 1."""
    if np.ndim(data) == 0:
        # print("input ndim = 0")
        if isinstance(data, np.float()):
            return(data)
        elif isinstance(data, np.int64()):
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

    if np.ndim(data) == 1:
        # print("input ndim = 1")
        # print(data.T[1])
        if isinstance(data.T[0], np.float):
            print('floating point data')
            return(data)
        elif isinstance(data.T[0], np.float_):
            return(data)
        elif isinstance(data.T[0], np.int64):
            data = data.astype(float) / (2 ** (64 - 1))
            return(data)
        elif isinstance(data.T[0], np.int32):
            data = data.astype(float) / (2 ** (32 - 1))
            return(data)
        elif isinstance(data.T[0], np.int16):
            data = data.astype(float) / (2 ** (16 - 1))
            return(data)
        elif isinstance(data.T[0], np.int8):
            data = data.astype(float) / (2 ** (8 - 1))
            return(data)
        else:
            raise TypeError('wrong input type')

    elif np.ndim(data) == 2:
        # print("input ndim = 2")
        # print(data.T[1])
        if isinstance(data.T[0][0], np.float):
            return(data)
        elif isinstance(data.T[0][0], np.float_):
            return(data)
        elif isinstance(data.T[0][0], np.int64):
            data = data.astype(float) / (2 ** (64 - 1))
            return(data)
        elif isinstance(data.T[0][0], np.int32):
            data = data.astype(float) / (2 ** (32 - 1))
            return(data)
        elif isinstance(data.T[0][0], np.int16):
            data = data.astype(float) / (2 ** (16 - 1))
            return(data)
        elif isinstance(data.T[0][0], np.int8):
            data = data.astype(float) / (2 ** (8 - 1))
            return(data)
        else:
            raise TypeError('wrong input type')

    else:
        raise TypeError('wrong input type')


def input_check(data):
    """
    Input:
        data = array of one or more values
    Output:
        True/ False
    Check ndim size of the data object. This can also be the a list or a tuple.
    After this the function checks of the input data are floating point values.
    It returns a True or a False

    TODO:
        - Add Inputtype to function
        - Check all data"""
    if np.ndim(data) > 0:
        if isinstance(data[0], np.float):
            return(True)
        else:
            # raise TypeWarning('wrong input type')
            return(False)
    elif np.ndim(data) == 0:
        if isinstance(data, np.float):
            return(True)
        else:
            return(False)
            # raise MeasWarning.TypeWarning('wrong input type')


def istuple(var):
    """
    Input:
        var = [-] variable
    Output:
        return a True or False value if it is a tuple
    """
    return(isinstance(var, tuple))


def odd(x):
    """
    inputs:
        spec = input array of unknown values.
    Output:
        Symetry check = True or False boolean

    Check for symmetry in given Signals
    - Real signals have \'even\' symmerty
    - Imaginair signals have \'odd\' symmetry
    - Magnitute signals have \'even\' symmetry
    - phase signals have \'odd\' symmetry +/- pi"""
    N = np.int(len(x))
    if (x[1: N/2] == - np.flipud(x[-N/2 +1 :])).all():
        oddvals = True
    else:
        oddvals = False    
    return(oddvals)


def oddphase(x):
    """
    inputs:
        spec = input array of unknown values.
    Output:
        Symetry check = True or False boolean

    Check for symmetry in given Signals
    - Real signals have \'even\' symmerty
    - Imaginair signals have \'odd\' symmetry
    - Magnitute signals have \'even\' symmetry
    - phase signals have \'odd\' symmetry +/- pi"""
    N = np.int(len(x))
    phx_1 = np.round(x[1:N/2], decimals=7)  # first half spectrum
    phplus = np.round(np.flipud(-x[-N/2 + 1:] + np.pi), decimals=7)  # 2nd + pi
    phmin = np.round(np.flipud(-x[-N/2 + 1:] - np.pi), decimals=7)  # 2nd - pi
    if ((phx_1 == phplus) | (phx_1 == phmin)).all():
        oddvals=True
    else:
        oddvals=False
    return(oddvals)


def phasecheck(x):
    """
    Input:
        x = 
    Output:
        True/ False Boolean
    check for:
    - -pi to pi
    - -180 to 180 deg
    TODO:
    - unwraped -pi to pi
    - unwrapped -180 to 180 
    """
    from numpy import pi
    minval = np.amin(x)
    maxval = np.amax(x)
    if (minval < -0.9 * pi and minval >= -pi ) and (maxval > 0.9 * pi and maxval <= pi):
        return(True)
    elif (minval < -160 and minval >= -180 ) and (maxval > 160 and maxval <= 180):
        return(True)
    else:
        return(False)


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
