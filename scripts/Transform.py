# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 15:25:42 2016

@author: Jee-Bee for jBae (c) 2016
"""

# Transforms (make class)
# |_ Fourier FFT/ DFT   5
#    |_ Wrap phase      3
#    |_ STFT
# |_ Laplace/ Z-trans   0
# |_ Transferfunction   0
# |_ Impulse response   0
# |_ Cepstrum           0


import scipy.fftpack as ft
import numpy as np
def NFFT (data):
    log2val = np.ceil(np.log2(len(data)))
    nfft = 2**log2val
    return (nfft)


def FFT (data,fs,*args, **kwargs):
    # sig, fs,window,smoothing, 
    # spectrum = complex(=real+imag)/amp+phase, Shift = yes # removed: side = singele/ double sided
    if args == []:
        pass
    else:
        print(args)
    if kwargs == []:
        pass
    else:
        print (kwargs)
    nfft = NFFT(data)
    DATA = ft.fft(data, nfft)
    print(fs)
    return (DATA)
