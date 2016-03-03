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


def NFFT(x):
    log2val = np.ceil(np.log2(len(x)))
    nfft = 2 ** log2val
    return(nfft)


def Symmetry(x, Stype):
    N = len(x)
    temp = []
    if Stype == 'even':
        for idx in range(int(N / 2 - 1)):
            if round(x[idx + 1], 6) == round(x[(N - 1) - idx], 6):
                pass
                # print(idx, x[idx + 1], round(x[idx + 1], 6), round(x[(N - 1) - idx]))  # pass
            else:
                # print(False)
                return (False)
                break
    elif Stype == 'odd':
        for idx in range(int(N / 2 - 1)):
            if round(x[idx + 1], 6) == - round(x[(N - 1) - idx], 6):
                pass
                # print(idx, x[idx + 1], round(x[idx + 1], 6), round(x[(N - 1) - idx]))  # pass
            else:
                # print(False)
                return (False)
                break
    else:
        print('No valid input type or value')
        return(False)
    return(True)


def MagPh2ReIm(MAG, PHI):
    RE = MAG * np.cos(PHI)
    IM = MAG * np.sin(PHI)
    return(RE, IM)


def FFT(x, fs, *args, **kwargs):
    # sig, fs,Window_Type, Window_size, smoothing,
    # spectrum = complex(=real+imag)/amp+phase, Shift = True # removed: side = singele/ double sided
    # fft of the form:
    #      N-1                      m*k
    # y_m =sum x_k * exp ( -2pi * i ----)
    #      k=0                        N
    # Therefore fft * 1/N to correct amplitude
    nfft = NFFT(x)
    N = len(x)
    if len(args) == 0:
        X = ft.fft(x, nfft)
    elif len(args) <= 3:
        if len(args) == 3:
            if isinstance(args[1], str) == True:
#                Window_Type = argv[1]
                pass
            else:
                print("Window type not the right input type")
            # argv[2]
            if isinstance(args[2], int) == True:
#                Window_size = (args[2])
                pass
            elif isinstance(args[2], float) == True:
                if args[2] % 1 == 0:
#                    Window_size = int(args[2])
                    pass
            else:
                print("Window size not the right input type")
            # argv[3]
            if isinstance(args[3], int) == True:
#                smoothing = (args[3])
                pass
            elif isinstance(args[2], float) == True:
                if args[2] % 1 == 0:
#                    smoothing = int(args[3])
                    pass
            else:
                print("Smooting not the right input type")
        else:
            if isinstance(args[1], str):
#                Window_Type = argv[1]
                pass
            elif isinstance(args[1], int):
#                smoothing = int(args[1])
                pass
            elif isinstance(args[1], float):
                if args[1] % 1 == 0:
#                    smoothing = int(args[1])
                    pass
            else:
                print("not the right input type")
    else:
        print("not the right number of parameters")
        print(args)
    if len(kwargs) == 0:
        pass
    else:
        print(kwargs)
    X = ft.fft(x, nfft) / N
    F = np.arange(0, fs, 1 / (N / fs))
#    F = np.arange(-fs / 2, fs / 2, 1 / (N / fs))
    # fft shift = True: -fs / 2, fs / 2
    # fft shift = False: 0, fs
    return(F, X)


def Transfer(x_in, x_out, fs):  # possible some input paremeters addded later
    # transfer function is in case of in = microphone and out is ref signal:
    #     in signal     in1    in2     blackbox out
    # H = ---------- --> --- or --- is ------------
    #     out signal     out    out     blackbox in
    X_IN = FFT(x_in, fs)
    X_OUT = FFT(x_out, fs)
    H_0 = X_IN / X_OUT
    return(H_0)


def ImpulseResponse(H, F):
    print("""This function works only correct when:
            - no smoothing or averaging is applied
            - full spectrum data is returned!""")
    # 2DO Check for full Spectrum
    if isinstance(H, tuple):  # could also use assert
        # Check arrays for type of signal
        # Mag + Phase --> Mag is absolut no neg values
        # Check symetrie no symmerie is false info...
        # Without shift X[0] = F - 0Hz and X[fs/2] =
        # shift check on symmetry?
        H0even = Symmetry(H[0], 'even')
        H1odd = Symmetry(H[1], 'odd')
        if (H0even and H1odd) == True:
            if H[0] == abs(H[0]):
                if max(abs(H[1])) <= np.pi:  # check for phase RAD information
                    pass
                elif max(abs(H[1])) <= 180:  # check for phase DEG information
                    H[1] = H[1] * np.pi / 180
                    pass
#                    http://stackoverflow.com/questions/2598734/numpy-creating-a-complex-array-from-2-real-ones
#            elif ...:  # check for complex paterns don't know how
#                pass
            else:
                pass
        else:
            print('No valid frequency array')
            break
    else:
        if np.iscomplex(H):
            IR = ft.ifft(H)
        else:
            print('Not right input type')
    IR = ft.ifft(H)
    dF = F[1]-F[0]
    T = 1 / dF
    F_Upper = len(F)/2 * dF
    fs = 2 * F_Upper
    return(IR, fs, T)


def Cepstrum(x):
    pass
