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
def NFFT (x):
    log2val = np.ceil(np.log2(len(x)))
    nfft = 2**log2val
    return (nfft)


def FFT (x,fs,*args, **kwargs):
    # sig, fs,Window_Type, Wwindow_size, smoothing, 
    # spectrum = complex(=real+imag)/amp+phase, Shift = True # removed: side = singele/ double sided
#    fft of the form:
#         N-1                      m*k
#    y_m =sum x_k * exp ( -2pi * i ----)
#         k=0                        N
#    Therefore fft * 1/N to correct amplitude
    nfft = NFFT(x)
    N = len (x)
    if len(args) == 0:
        X = ft.fft(x, nfft)
    elif len(args) <= 3:
        if len(args) == 3:
            if isinstance(args[1],str)== True:
#                Window_Type = argv[1]
                pass
            else:
                print ("Window type not the right input type")
            # argv[2]
            if isinstance(args[2],int)== True:
#                Window_size = (args[2])
                pass
            elif isinstance(args[2], float) == True:
                if args[2]%1 == 0:
#                    Window_size = int(args[2])
                    pass
            else:
                print ("Window size not the right input type")
            # argv[3]
            if isinstance(args[3],int)== True:
#                smoothing = (args[3])
                pass
            elif isinstance(args[2], float) == True:
                if args[2]%1 == 0:
#                    smoothing = int(args[3])
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
    if len(kwargs) == 0:
        pass
    else:
        print (kwargs)
    
    X = ft.fft(x, nfft)/N
    F = np.arange(0,fs,1/(N/fs))
#    F = np.arange(-fs/2,fs/2,1/(N/fs))
    # fft shift = True: -fs/2, fs/2
    # fft shift = False: 0, fs
    return (F, X)


def Transfer(x_in, x_out, fs): # possible some input paremeters addded later
# transfer function is in case of in = microphone and out is ref signal:
#     in signal     in1    in2     blackbox out
# H = ---------- --> --- or --- is ------------
#     out signal     out    out     blackbox in
    X_IN = FFT (x_in,fs)
    X_OUT = FFT (x_out,fs)
    H_0 = X_IN/X_OUT
    return H_0


def Cepstrum (x):
    pass
