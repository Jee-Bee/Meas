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
    Return RMS value of time signal
    """
    return(np.sqrt(( 1 / len(sig)) * np.sum(sig ** 2)) * sig)

def RMSf(fsig):
    """
    Return RMS value of frequency signal
    """
    return (np.sqrt(np.sum(abs(fsig / len(fsig))) ** 2) * fsig)

def RMSe(sigx, sigy):
    """
    Return RMS error value(s)
    """
    if len(sigx) != len(sigy):
        pass # return Error
    else:
        N = len(sigx)
    return (np.sqrt(1 / N * np.sum((sigx - sigy ) ** 2)) * sigx)

def Crestarr(sig):  # Crest Factor array
    """
    Return Crest array is this needed?
    """
    rms = RMS(sig)
    C = abs(sig) / rms
    return(C)

def Crest(sig):  # Crest Factor singe value from array
    """
    Return Crest Single value
    """
    rms = RMS(abs(sig))
    peak = abs(sig)
    C_zero = zero_check(abs(peak/rms))
    C = sum(C_zero) / len(sig)  # peak/rms is bij 0/0 NAN... Fix this - done
    return(C)

def PAPR(sig):  # Peak to Average Power Ratio
    rms =np.sqrt((1 / len(sig)) * np.sum(sig ** 2))
    papr_zero = zero_check((abs(sig) ** 2) / (rms ** 2))
    papr = sum((papr_zero) / len(sig))
    return (papr)

def PAPR_dB(sig):  # Peak to Average Power Ratio
    rms =np.sqrt((1 / len(sig)) * np.sum(sig ** 2))
    papr_zero = zero_check((abs(sig) ** 2) / (rms ** 2))
    papr_dB = 10 * np.log10(sum(papr_zero) / len(sig))
    return(papr_dB)

# par

# RMS.py