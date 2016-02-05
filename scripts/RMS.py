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

def RMS (sig):
    return np.sqrt((1/len(sig))*np.sum(sig**2))*sig

def RMSf (fsig):
    return np.sqrt(np.sum(abs(fsig/len(fsig)))**2)*fsig

def RMSe (sigx, sigy):
    if len(sigx) != len(sigy):
        pass # return Error
    else:
        N = len(sigx)
    return (np.sqrt(1/N * np.sum((sigx - sigy )**2))*sigx)

def Crestarr (sig):  # Crest Factor array
    rms = RMS(sig)
    C = abs(sig)/rms
    return (C)

def Crest (sig):  # Crest Factor singe value from array
    rms = RMS(sig)
    peak = abs(sig)
    C = sum(peak/rms)/len(sig)  # peak/rms is bij 0/0 NAN... Fix this
    print(peak, rms)
#    C = sum(abs(sig))/sum(rms)
#    C = sum(Crestarr (sig))
    return (C)

def PAPR (sig):  # Peak to Average Power Ratio
    rms =np.sqrt((1/len(sig))*np.sum(sig**2))
    papr = sum((abs(sig)**2)/(rms**2))/len(sig)
    return (papr)

def PAPR_dB (sig):  # Peak to Average Power Ratio
    rms =np.sqrt((1/len(sig))*np.sum(sig**2))
    papr_dB = 10* np.log10( sum((abs(sig)**2)/(rms**2))/len(sig) )
    return (papr_dB)

# par

# RMS.py