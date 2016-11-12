# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 13:53:54 2016

@author: Jee-Bee for jBae 2016(c)
"""

import sys
if sys.version_info.major <3:
    from __future__ import division
import numpy as np
from src.measutils import zeroCheck


# 2Do
# check input type
# find peak? 
# scale to 1

# http://samcarcagno.altervista.org/blog/basic-sound-processing-python/



def RMS(sig):
    """
    Inputs:
        sig = input signal in x [m = position] or time domain.
    Output:
        RMS = RMS signal in x [m = position] or time domain.

    Return Root Mean Square (RMS) value of (time) signal
    for more info see: https://en.wikipedia.org/wiki/Root_mean_square

              1
    RMS =sqrt(- * (x_1^2 + x_2^2 + ... x_n^2))
              n
    """
    n = len(sig)
    return(np.sqrt(( 1 / n) * np.sum(sig ** 2)) * sig)


def RMSf(fsig):
    """
    Inputs:
        fsig = input signal in F (Frequency) domain.
    Output:
        RMS = RMS signal in F (Frequency) domain.

    Return RMS value of frequency signal
    for more info see: https://en.wikipedia.org/wiki/Root_mean_square

                      1                        1
    RMS{X[N]} = sqrt( - * sum(x[n]^2)) = sqrt(--- * sum(|x[m]^2|))
                      N    n                  N^2    n

              = sqrt(sum(|x[m]|^2))
                      n  |  N |
    """
    return (np.sqrt(np.sum(abs(fsig / len(fsig))) ** 2) * fsig)


def RMSe(x_theo, x_measurement):
    """
    Inputs:
        x_theo = theoreticl input signal in x [m = position] or time domain.
        x_measurement = measured input signal in x [m = position] or time domain.
    Output:
        RMSErrors = RMS signal in x [m = position] or time domain.

    Return RMS error value(s) between theretical model and measurement
    see: http://statweb.stanford.edu/~susan/courses/s60/split/node60.html

                      n
    RMSErrors = sqrt(sum * (x_theo - x_measurement)^2)
                --------------------------------------
                                  n
    """
    if len(x_theo) != len(x_measurment):
        pass  # return Error
    else:
        N = len(x_theo)
    return (np.sqrt(1 / N * np.sum((x_theo - x_measurment) ** 2)) * x_theo)


def Crestarr(sig):  # Crest Factor array
    """
    Inputs:
        sig = input signal in x [m = position] or time domain.
    Output:
        Crest factor = return array of crest factor

    Crest factor is the relation/ ratio between peak values and the corsponing
    RMS value. a Crest value of 1 means that both are the same value.

    Returning an array of Crest factors is unneeded since they are with every
    non zero value the same ratio...

    see for more info: https://en.wikipedia.org/wiki/Crest_factor
        |x_peak|
    C = --------
         x_rms
    """
    rms = RMS(sig)
    C = abs(sig) / rms
    return(C)


def Crest(sig):  # Crest Factor singe value from array
    """
    Inputs:
        sig = input signal in x [m = position] or time domain.
    Output:
        Crest factor = return crest factor

    Crest factor is the relation/ ratio between peak values and the corsponing
    RMS value. a Crest value of 1 means that both are the same value.

    see for more info: https://en.wikipedia.org/wiki/Crest_factor
        |x_peak|
    C = --------
         x_rms
    """
    rms = RMS(sig)
    rms_zero = zeroCheck(rms)
    peak_zero = zeroCheck(sig)
    if isinstance(rms_zero, tuple):
        print('nday array, more than one value')
        C = np.zeros(len(rms_zero))
        for idx in np.arange(len(rms_zero)):
            C_zero = abs(peak_zero[idx]) / rms_zero[idx]
            C[idx] = sum(C_zero) / len(C_zero)
    elif isinstance(rms_zero, np.ndarray):
        C_zero = abs(peak_zero)/rms_zero
        C = sum(abs(C_zero)) / len(C_zero)
    return(C)


def PAPR(sig):  # Peak to Average Power Ratio
    """
    Inputs:
        sig = input signal in x [m = position] or time domain.
    Output:
        PAPR = return PAPR factor

    PAPR stands for peak to average power ratio. This is the relation/ ratio 
    between squared peak values and the corsponing squared RMS values. 

    see for more info: https://en.wikipedia.org/wiki/Crest_factor
           |x_peak|^2
    PAPR = ---------- = C^2
            x_rms^2
    """
    rms = RMS(sig)
    rms2_zero = zeroCheck(rms ** 2)
    peak2_zero = zeroCheck(sig ** 2)
    if isinstance(rms2_zero, tuple):
        print('nday array, more than one value')
        papr = np.zeros(len(papr_zero))
        for idx in np.arange(len(rms2_zero)):
            papr_zero = abs(peak2_zero[idx])/rms2_zero[idx]
            papr[idx] = sum(papr_zero) / len(papr_zero)
    elif isinstance(rms2_zero,np.ndarray):
        papr_zero = abs(peak2_zero)/rms2_zero
        papr = sum(abs(papr_zero)) / len(papr_zero)
    return (papr)


def PAPR_dB(sig):  # Peak to Average Power Ratio
    """
    Inputs:
        sig = input signal in x [m = position] or time domain.
    Output:
        PAPR_dB = return dB version of the PAPR factor

    PAPR stands for peak to average power ratio. This is the relation/ ratio 
    between squared peak values and the corsponing squared RMS values. 

    see for more info: https://en.wikipedia.org/wiki/Crest_factor
                             |x_peak|^2
    PAPR_dB =  10 * log_10 *---------- = C^2
                              x_rms^2
    
    PAPR_dB
    """
    rms = RMS(sig)
    rms2_zero = zeroCheck(rms ** 2)
    peak2_zero = zeroCheck(sig ** 2)
    if isinstance(rms2_zero, tuple):
        print('nday array, more than one value')
        papr_dB = np.zeros(len(papr_zero))
        for idx in np.arange(len(papr_zero)):
            papr_zero = abs(peak2_zero[idx])/rms2_zero[idx]
            papr_dB[idx] = 10 * np.log10(sum(papr_zero) / len(papr_zero))
    elif isinstace(rms2_zero,np.ndarray):
        papr_zero = abs(peak2_zero)/rms2_zero
        papr_dB = 10 * np.log10(sum(papr_zero) / len(papr_zero))
    papr_dB = 10 * np.log10(sum(abs(papr_zero)) / len(sig))
    return(papr_dB)


# par

def mRMS(msig):
    msig_shape = np.shape(msig)
    if len(msig_shape) ==1:
        mRMS = RMS(msig)
    elif len(msig_shape) ==2:
        if msig_shape[0] < msig_shape[1]:
            pass
        elif msig_shape[0] > msig_shape[1]:
            msig = msig.T
            msig_shape = np.shape(msig)
        mRMS = []
        for channel in range(msig_shape[0]):
            si_RMS = RMS(msig[channel])
            if channel == 0:
                mRMS = np.append(mRMS, si_RMS)
            else:
                mRMS = np.vstack((mRMS, si_RMS))
    else:
        raise ValueError('not a valid number of dimensions')
    return(mRMS)


def mRMSf(msig):
    msig_shape = np.shape(msig)
    if len(msig_shape) ==1:
        mRMSf = RMSf(msig)
    elif len(msig_shape) ==2:
        if msig_shape[0] < msig_shape[1]:
            pass
        elif msig_shape[0] > msig_shape[1]:
            msig = msig.T
            msig_shape = np.shape(msig)
        mRMSf = []
        for channel in range(msig_shape[0]):
            si_RMSf = RMSf(msig[channel])
            if channel == 0:
                mRMSf = np.append(mRMSf, si_RMSf)
            else:
                mRMSf = np.vstack((mRMSf, si_RMSf))
    else:
        raise ValueError('not a valid number of dimensions')
    return(mRMSf)


def mRMSe(x_theo, x_measurement):
    theo_shape = np.shape(x_theo)
    measurement_shape = np.shape(x_measurement)
    if (len(theo_shape) == 1) and (len(measurement_shape) == 1):
        mRMSe = RMSe(x_theo, x_measurement)
    elif (len(theo_shape) == 1) and (len(measurement_shape) == 2):
        if measurement_shape[0] < measurement_shape[1]:
            pass
        elif measurement_shape[0] > measurement_shape[1]:
            x_measurement = x_measurement.T
            measurement_shape = np.shape(x_measurement)
        mRMSe = []
        for channel in range(measurement_shape[0]):
            si_RMSe = RMSe(x_theo, x_measurement[channel])
            if channel == 0:
                mRMSe = np.append(mRMSe, si_RMSe)
            else:
                mRMSe = np.vstack((mRMSe, si_RMSe))
    elif (len(theo_shape) == 2) and (len(measurement_shape) == 2):
        if theo_shape[0] < theo_shape[1]:
            pass
        elif theo_shape[0] > theo_shape[1]:
            x_theo = x_theo.T
            theo_shape = np.shape(x_theo)
        if measurement_shape[0] < measurement_shape[1]:
            pass
        elif measurement_shape[0] > measurement_shape[1]:
            x_measurement = x_measurement.T
            measurement_shape = np.shape(x_measurement)
        mRMSe = []
        for channel in range(measurement_shape[0]):
            si_RMSe = RMSe(x_theo[channel], x_measurement[channel])
            if channel == 0:
                mRMSe = np.append(mRMSe, si_RMSe)
            else:
                mRMSe = np.vstack((mRMSe, si_RMSe))
    else:
        raise ValueError('not a valid number of dimensions')
    return(mRMS)

def mCrest(msig):
    msig_shape = np.shape(msig)
    if len(msig_shape) ==1:
        mCrest = Crest(msig)
    elif len(msig_shape) ==2:
        if msig_shape[0] < msig_shape[1]:
            pass
        elif msig_shape[0] > msig_shape[1]:
            msig = msig.T
            msig_shape = np.shape(msig)
        mCrest = []
        for channel in range(msig_shape[0]):
            si_Crest = Crest(msig[channel])
            mCrest = np.append(mCrest,si_Crest )
    else:
        raise ValueError('not a valid number of dimensions')
    return(mCrest)


def mPAPR(msig):
    msig_shape = np.shape(msig)
    if len(msig_shape) == 1:
        mCrest = Crest(msig)
    elif len(msig_shape) == 2:
        if msig_shape[0] < msig_shape[1]:
            pass
        elif msig_shape[0] > msig_shape[1]:
            msig = msig.T
            msig_shape = np.shape(msig)
        mPAPR = []
        for channel in range(msig_shape[0]):
            mPAPR = np.append(mPAPR, PAPR(msig[channel]))
    else:
        raise ValueError('not a valid number of dimensions')
    return(mPAPR)


def mPAPR_dB(msig):
    msig_shape = np.shape(msig)
    if len(msig_shape) == 1:
        mCrest = Crest(msig)
    elif len(msig_shape) == 2:
        if msig_shape[0] < msig_shape[1]:
            pass
        elif msig_shape[0] > msig_shape[1]:
            msig = msig.T
            msig_shape = np.shape(msig)
        mPAPR = []
        for channel in range(msig_shape[0]):
            mPAPR = np.append(mPAPR, PAPR_dB[channel])
    else:
        raise ValueError('not a valid number of dimensions')
    return(mPAPR)

# RMS.py