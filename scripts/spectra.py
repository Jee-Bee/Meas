# -*- coding: utf-8 -*-
"""
Spectral Class ??

@author: Jee-Bee for jBae (c) 2016 
"""
# https://en.wikipedia.org/wiki/Spectral_density
# Spectral eneergie in time series
# \int_{-\inf}^{\inf} \abs(x(t))^2 dt
# 

# https://wiki.python.org/moin/NumericAndScientificRecipes

import numpy as np
import scipy.fftpack as fft
# Creating class from this??

#ESD = 
#
#
def PSD (sig, fs, *arg, **kwargs):
    """
    Calculate Power Spectral Density [W/Hz]
    """"
    # sig, fs,window,smoothing, 
    # spectrum = complex(=real+imag)/amp+phase, Shift = yes # removed: side = singele/ double sided
    log2val = np.ceil(np.log2(len(sig)))
    nfft = 2**log2val
    if kwargs == []:
        spectrum = 'MagPh'
#        side = 'single'
    elif spectrum == ('MagPh' or 'Complex'):
        pass
#    elif side == ('single' or 'double' or 'single0'):
#        pass
    else:
        pass #place error here wrong input value
#    'single0':
#    F = np.arange(len(sig)/fs, fs, (len(sig)/2)+1)
    
    if spectrum == 'MagPh':
        F = np.arange(len(sig)/fs, fs, len(sig)/2)
        SIG = fft(sig,nfft)/len(sig)
        MAG = np.abs(SIG[0,len(SIG)/2])**2
        MAG =MAG/F
        PH = np.angle(SIG[0,len(SIG)/2])
        SIG = (MAG, PH)
        
    elif spectrum == 'Complex':
        F = np.arange(-fs,fs,len(sig))
        SIG = fft(sig,nfft)/len(sig)
        REAL = np.real(SIG)**2
        IMAG = np.imag(SIG)**2
        SIG = (REAL/F, IMAG/F)
        
    return (F,SIG)


#SD = 
#
#
#ASD =


def PS (sig, fs, *arg, **kwargs):
    # sig, fs,window,smoothing, 
    # spectrum = complex(=real+imag)/amp+phase, Shift = yes # removed: side = singele/ double sided
    log2val = np.ceil(np.log2(len(sig)))
    nfft = 2**log2val
    if kwargs == []:
        spectrum = 'MagPh'
#        side = 'single'
    elif spectrum == ('MagPh' or 'Complex'):
        pass
#    elif side == ('single' or 'double' or 'single0'):
#        pass
    else:
        pass #place error here wrong input value
#    'single0':
#    F = np.arange(len(sig)/fs, fs, (len(sig)/2)+1)
    
    if spectrum == 'MagPh':
        F = np.arange(len(sig)/fs, fs, len(sig)/2)
        SIG = fft(sig,nfft)/len(sig)
        MAG = np.abs(SIG[0,len(SIG)/2])**2
        PH = np.angle(SIG[0,len(SIG)/2])
        SIG = (MAG, PH)
        
    elif spectrum == 'Complex':
        F = np.arange(-fs,fs,len(sig))
        SIG = fft(sig,nfft)/len(sig)
        REAL = np.real(SIG)**2
        IMAG = np.imag(SIG)**2
        SIG = (REAL, IMAG)
        
    return (F,SIG)


def AS (sig, fs, *arg, **kwargs):
    # sig, fs,window,smoothing, 
    # spectrum = complex(=real+imag)/amp+phase, Shift = yes # removed: side = singele/ double sided
    log2val = np.ceil(np.log2(len(sig)))
    nfft = 2**log2val
    if kwargs == []:
        spectrum = 'MagPh'
#        side = 'single'
    elif spectrum == ('MagPh' or 'Complex'):
        pass
#    elif side == ('single' or 'double' or 'single0'):
#        pass
    else:
        pass #place error here wrong input value
#    'single0':
#    F = np.arange(len(sig)/fs, fs, (len(sig)/2)+1)
    
    if spectrum == 'MagPh':
        F = np.arange(len(sig)/fs, fs, len(sig)/2)
        SIG = fft(sig,nfft)/len(sig)
        MAG = np.abs(SIG[0,len(SIG)/2])
        PH = np.angle(SIG[0,len(SIG)/2])
        SIG = (MAG, PH)
        
    elif spectrum == 'Complex':
        F = np.arange(-fs,fs,len(sig))
        SIG = fft(sig,nfft)/len(sig)
        REAL = np.real(SIG)
        IMAG = np.imag(SIG)
        SIG = (REAL, IMAG)
        
    return (F,SIG)


# Spectra.py
# Created by Jee-Bee for jBae 2016(c)