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
    # spectrum = complex(=real+imag)/amp+phase, Shift = True # removed: side = singele/ double sided
    nfft = NFFT(data)
    if args == []:
        DATA = ft.fft(data, nfft)
    elif len(args) <= 2:
        if len(args) == 2:
            if isinstance(args[1],str)== True:
#                Window_Type = argv[1]
                pass
            else:
                print ("Window type not the right input type")
            # argv[2]
            if isinstance(args[2],int)== True:
#                smoothing = int(args[2])
                pass
            elif isinstance(args[2], float) == True:
                if args[2]%1 == 0:
#                    smoothing = int(args[2])
                    pass
            else:
                print ("Smooting not the right input type")
        else:
            if isinstance(args[1],str)== True:
#                Window_Type = argv[1]
                pass
            elif isinstance(args[1],int)== True:
#                smoothing = int(args[1])
                pass
            elif isinstance(args[1], float) == True:
                if args[1]%1 == 0:
#                    smoothing = int(args[1])
                    pass
            else:
                print ("not the right input type")
    else:
        print ("not the right number of parameters")
        print(args)
    if kwargs == []:
        pass
    else:
        print (kwargs)
    
    DATA = ft.fft(data, nfft)
    print(fs)
    return (DATA)
