# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 13:53:54 2016

@author: Jee-Bee for jBae 2016(c)
"""
import numpy as np

# 2Do
# check input type
# find peak? 
# scale to 1

# http://samcarcagno.altervista.org/blog/basic-sound-processing-python/

def zero_check(vals):
    (rows,cols) = np.shape(vals)
    delrows = []
    for idx in range(rows):
        for idy in range(cols):
            if vals[idx][idy] == 0:
                if len(delrows) == 0:
                    delrows.append(idx)
                    print(idx, idy)
                elif delrows[-1] == idx:
                    pass
                else:
                    delrows.append(idx)
                    print(idx, idy)
            else:
                pass
    vals_no0 = np.delete(vals, delrows, 0)
    return(vals_no0)

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
    rms = RMS(abs(sig))
    peak = abs(sig)
    C_zero = zero_check(abs(peak/rms))
    C = sum(C_zero) / len(sig)  # peak/rms is bij 0/0 NAN... Fix this - done
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
    rms =np.sqrt((1 / len(sig)) * np.sum(sig ** 2))
    papr_zero = zero_check((abs(sig) ** 2) / (rms ** 2))
    papr = sum((papr_zero) / len(sig))
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
    rms =np.sqrt((1 / len(sig)) * np.sum(sig ** 2))
    papr_zero = zero_check((abs(sig) ** 2) / (rms ** 2))
    papr_dB = 10 * np.log10(sum(papr_zero) / len(sig))
    return(papr_dB)

# par

# RMS.py