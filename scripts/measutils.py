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
    if N % 2 == 0:
        # N / 2 ia aloud to be odd it can be half spectrum...
        N_half = np.int(N / 2)
        if (x[1: N_half] == np.flipud(x[-N_half + 1:])).all():
            evenvals = True
        else:
            evenvals = False
    else:
        N_half = np.int((N - 1) / 2)
        if (x[1: N_half] == np.flipud(x[-N_half + 1:])).all():
            evenvals = True
        else:
            evenvals = False
    return(evenvals)


def convertFloat(data):
    """
    Input:
        data = array of data recorded by input of audio/ vibration interface.
    output:
        data but nof floating point +/-1.

    Check d-type or data type (class) of the input array. After this it
    rescaled the data to floating point data array of +/- 1."""
    if data.dtype == np.float64():
        return(data)
    elif data.dtype == np.int64():
        data = data.astype(float) / (2 ** (64 - 1))
        return(data)
    elif data.dtype == np.int32:
        data = data.astype(float) / (2 ** (32 - 1))
        return(data)
    elif data.dtype == np.int16:
        data = data.astype(float) / (2 ** (16 - 1))
        return(data)
    elif data.dtype == np.int8:
        data = data.astype(float) / (2 ** (8 - 1))
        return(data)
    elif isinstance(data, int):
        data = data.astype(float) / (2 ** (32 - 1))
        return(data)
    elif isinstance(data, float):
        return(data)
    else:
        raise TypeError('wrong input type')


def ShapeDirection(sig):
    """ input direction
    inputs:
        sig = Array of signals
    outputs:
        sig = signal or transposed signal
    ndimensions not larger as 2 dimensional
    max number of axis is two (0 and 1) else gives an input error

    TODO:
    - Implement Axis?
    """
    sig_shape = np.shape(sig)
    if sig.ndim == 1:
        pass
    elif sig.ndim == 2:
        if sig_shape[0] < sig_shape[1]:
            print('right direction')
        else:
            # wrong direction... Transform needed
            sig = sig.T  # signal transformed
            print('Data is Transformed')            
    else:
        raise ValueError('not a valid number of dimensions')


def isfloat(data):
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
    return(isinstance(data.any(), np.float))


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
    if N % 2 == 0:
        N_half = np.int(N / 2)
        if (x[1:N_half] == - np.flipud(x[-N_half + 1:])).all():
            oddvals = True
        else:
            oddvals = False
    else:
        N_half = np.int((N - 1) / 2)
        if (x[1:N_half] == - np.flipud(x[-N_half +1:])).all():
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

def addzeros(signal, l0, fs=None):
    """
    Input:
        signal
        l0 = length in samples or if it an array T(length time) together
        with fs (sample frequency)
        fs(optional) = sample Frequency
    Output:
        signal = repeated signal"""
    if fs is not None:
        zerroarray = np.zeros(l0 * fs)
        signal = np.append(signal, zerroarray)
    else:
        zerroarray = np.zeros(l0)
        signal = np.append(signal, zerroarray)
    return(signal)


def zeroCheck(vals):
    """
    Inputs:
        vals = (ndim) array of values
    Output:
        vals_no0 = same array of values when it contain no zeros otherwise
                    new array without the zeros.

    check for zeros in array. After this remove the vallues from array.
    Or replace the value for another value.

    TODO:
     - replace the zero by given value"""
    arrdims = np.shape(vals)
    if len(arrdims) >= 3:
        raise ValueError("dimensions of ndim array are bigger than 2")
    elif len(arrdims) == 2:
        valsno0 = ()
        for idx in np.arange(arrdims[1]):
            exec('vals' + str(idx) + ' = vals.T[' + str(idx) + ']')
            delrows= np.where(eval('vals' + str(idx)) == 0)
            exec('vals' + str(idx) + '= np.delete(vals' + str(idx) + ', delrows, 0)')
            valsno0 = valsno0 + (eval('vals' + str(idx)),)
        return(valsno0)
    elif len(arrdims) == 1:
        #valsno0 = np.array([])
        delrows= np.where(vals == 0)
        exec('vals0 = np.delete(vals, delrows, 0)')
        valsno0 = eval('vals0')
        return(valsno0)


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
