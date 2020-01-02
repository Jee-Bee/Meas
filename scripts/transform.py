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

import sys
import numpy as np
# from ..script import MeasError #as ME # , MeasWarning
if sys.version_info.major <3:
    from __future__ import division


def NFFT(x):
    """
    Input:
        x = length of array
        or
        x = array - TODO
    Output:
        nfft = Next higher value of 2 ^ n for FFT

    Calculate Next higher 2^N order for FFT"""
    log2val = np.ceil(np.log2(len(x)))
    nfft = 2 ** log2val
    return(nfft)


def MagPh2ReIm(Mag, Phi, output='ReIm'):
    """
    Inputs:
        MAG = Magnitude spectrum *
        PHI = phase spectrum *
    Outputs:
        RE = real vallued output
        IM = Imaginear vallued output
    Options:
        output='complex'(default); other options are 'ReIm'

    * at this moment only to Real and Imaginaire vallues later on also Complex

    Calculate back the Real and imaginary Values
    To Do:
        - Make Real + Imag to Complex values - If required """
    Re = Mag * np.cos(Phi)
    Im = Mag * np.sin(Phi)
    return(Re, Im)

# def FFT(x, fs, *args, **kwargs):
def FFT(x, fs, Window_type=None, Window_length=8192, shift=False, spectrum='complex'):
    # FFT(x, fs, Window_type, Window_length, shift=False, spectrum=complex)
    from scipy.fftpack import fft, fftshift, fftfreq
    from scripts import window, repeat
    """
    Inputs:
        sig = [sec] time domain signal
        fs = [Hz] sample frequency
        Window_Type = [string] name window
        window_length = [-] length of window in number of samples
        smoothing - canceled - moved to own function
    Options:
        shift = True/ False
        spectrum = complex(=real+imag)/AmPh0(amp+phase + 0)/AmPh(amp+phase)
        side - canceled= singele/ double sided
    Output:
        F = Frequencie bands
        X = spectrum
    fft of the form:
         n-1                      m*k
    A_k =sum a_m * exp ( -2pi * i ----)    for k = 0, ..., n-1
         m=0                       n
    Therefore fft * 1/N to correct amplitude

    TODO:
    - remove smoothing and make solo function from it
    - fix right place of F(frequency bins)
    - Update Window for """
    nfft = NFFT(x)
    N = len(x)  # Temporary solution
    if Window_type is None:
        X = fft(x, nfft) / N
        N = np.int(nfft)
    elif Window_type == 'rectangle':
        N = np.int(Window_length)
    elif Window_type == 'triangle':
        N = np.int(Window_length)
    elif Window_type == 'partzen':
        N = np.int(Window_length)
    elif Window_type == 'genhamming':
        N = np.int(Window_length)
    elif Window_type == 'hann':
        N = np.int(Window_length)
        itterations = np.int32(np.ceil(len(x) / Window_length))
        X = []
        whan = window.Window(Window_length)
        (W, _) = whan.hanwind()
        for itt in range(itterations):
            upper = (itt + 1) * Window_length
            if upper < len(x):
                X_itt = fft(x[itt*Window_length:upper]*W) / Window_length
                X = np.append(X, X_itt)
            else:
                x_itt = np.zeros(Window_length)
                nsamp = len(x) - itt * Window_length
                x_itt[:nsamp] = x[itt * Window_length:]
                X_itt = fft(x_itt * W) / Window_length
                X = np.append(X, X_itt)
        X = repeat.repAvg(X, itterations)
    elif Window_type == 'hamming':
        N = np.int(Window_length)
    elif Window_type == 'cosine':
        N = np.int(Window_length)
    elif Window_type == 'gengaussian':
        N = np.int(Window_length)
    elif Window_type == 'gaussian':
        N = np.int(Window_length)
    elif Window_type == 'tukey':
        N = np.int(Window_length)
    else:
        pass
    if shift is True:
        if spectrum is 'complex':
            X = fftshift(X)
            F = np.linspace(0, (N-1)/2, N/2)
            F = np.append(F, np.linspace(-N/2, -1, N/2))
            F = F/(N/fs)
            return(F, X, [])
        elif spectrum is 'ReIm':
            X = fftshift(X)
            F = np.linspace(0, (N-1)/2, N/2)
            F = np.append(F, np.linspace(-N/2, -1, N/2))
            F = F/(N/fs)
            RE = np.real(X)
            IM = np.imag(X)
            return(F, RE, IM)
        elif spectrum is 'AmPh0':
            F = np.linspace(0, (N-1)/2, N/2)
            F = F/(N/fs)
            AMP = abs(X[0:N/2])
            PHI = np.arctan(np.real(X[0:N / 2]) / np.imag(X[0:N / 2]))
            return(F, AMP, PHI)
        elif spectrum is 'AmPh':
            F = np.linspace(1, (N-1)/2, N/2 - 1)
            F = F/(N/fs)
            AMP = abs(X[1:N/2])
            PHI = np.arctan(np.real(X[1:N / 2])/np.imag(X[1:N / 2]))
            return(F, AMP, PHI)
    else:
        if spectrum is 'complex':
            F = np.linspace(0, (N-1)/2, N/2)
            F = np.append(F, np.linspace(-N/2, -1, N/2))
            F = F/(N/fs)
            return(F, X, [])
        elif spectrum is 'ReIm':
            F = np.linspace(0, (N-1)/2, N/2)
            F = np.append(F, np.linspace(-N/2, -1, N/2))
            F = F/(N/fs)
            RE = np.real(X)
            IM = np.imag(X)
            return(F, RE, IM)
        elif spectrum is 'AmPh0':
            F = np.linspace(0, (N-1)/2, N/2)
            F = F/(N/fs)
            AMP = abs(X[0:N/2])
            PHI = np.arctan(np.real(X[0:N / 2]) / np.imag(X[0:N / 2]))
            return(F, AMP, PHI)
        elif spectrum is 'AmPh':
            F = np.linspace(1, (N-1)/2, N/2 - 1)
            F = F/(N/fs)
            AMP = abs(X[1:N/2])
            PHI = np.arctan(np.real(X[1:N / 2])/np.imag(X[1:N / 2]))
            return(F, AMP, PHI)
    # X = ft.fft(x, nfft) / N
    # F = np.arange(0, fs, 1 / (N / fs))
    # F = np.arange(-fs / 2, fs / 2, 1 / (N / fs))
    # fft shift = True: -fs / 2, fs / 2
    # fft shift = False: 0, fs
    # return(F, X)


# http://stackoverflow.com/questions/2598734/numpy-creating-a-complex-array-from-2-real-ones
def Transfer(x_in, x_out, fs):  # possible some input paremeters addded later
    """
    Inputs:
        x_in = input signal or recorded signal
        x_out = output signal or calculated signal
        fs = [Hz] sample frequency
    Output:
        H_0 = derived signal X_in / x_out

    Before makeing the transfer the input data is checked if it exist out the
    right information. This means the data have to be frequency specific data.
    This data exist out of amplitude and phase info from the form \' Real\'
    and \'Imaginair\' or complex data.

    transfer function is in case of in = microphone and out is ref signal:
        in signal     in1    in2     blackbox out
    H = ---------- --> --- or --- is ------------
        out signal     out    out     blackbox in
    2 Do:
        - Check complex values
        - check equal sized
        - if complex than no FFT
    """
    # Tuple = FFT or wrong input
    # Compex valued signals = FFT
    # Nummeric is real valued and neeed FFT!!
    # else is wrong valued type and give error
    from scripts.checks import even, odd, oddphase, phasecheck

    if isinstance(x_in, tuple):
        if phasecheck(x_in[1]) == True:
            x_in0even = even(x_in[0])  # even symmetry
            x_in1phodd = oddphase(x_in[1])  # odd symmetry
        else:
            x_in0even = even(x_in[0])  # even symmetry
            x_in1odd = odd(x_in[1])  # odd symmetry
            print(x_in0even, x_in1odd)
        # make complex array
        if (x_in0even & x_in1odd):
            x_in = x_in[0] + 1j*x_in[1]
        elif (x_in0even & x_in1phodd):
            x_in = x_in[0]*np.sin(x_in[1]) + 1j * x_in[0]*np.cos(x_in[1])
        if isinstance(x_out, tuple):
            x_out0even = even(x_out[0])
            x_out1odd = odd(x_out[1])
            # make complex array
            if (x_out0even & x_out1odd):
                x_out = x_out[0] + 1j*x_out[0]
                H_0 = x_in / x_out
        elif np.iscomplexobj(x_out):
            H_0 = x_in / x_out
        elif np.isrealobj(x_out):
            (X_OUT, F, _) = FFT(x_out, fs)
            H_0 = x_in / X_OUT
        else:
            raise TypeError("Wrong input type")
    elif np.iscomplexobj(x_in):
        if isinstance(x_out, tuple):
            x_in0even = even(x_in[0])  # even symmetry
            x_in1odd = odd(x_in[1])  # odd symmetry
            # make complex array
            if (x_out0even & x_out1odd):
                x_out = x_out[0] + 1j*x_out[0]
                H_0 = x_in / x_out
        elif np.iscomplexobj(x_out):
            H_0 = x_in / x_out
        elif np.isrealobj(x_out):
            (F, X_OUT, _) = FFT(x_out, fs)
            H_0 = x_in / X_OUT
        else:
            raise TypeError("Wrong input type")
    elif np.isrealobj(x_in):
        (F, X_IN, _) = FFT(x_in, fs)
        if isinstance(x_out, tuple):
            x_in0even = even(x_in[0])  # even symmetry
            x_in1odd = odd(x_in[1])  # odd symmetry
            # make complex array
            if (x_out0even & x_out1odd):
                x_out = x_out[0] + 1j*x_out[0]
                H_0 = X_IN / x_out
        elif np.iscomplexobj(x_out):
            H_0 = X_IN / x_out
        elif np.isrealobj(x_out):
            (F, X_OUT, _) = FFT(x_out, fs)
            H_0 = X_IN / X_OUT
        else:
            raise TypeError("Wrong input type")
    else:
        raise TypeError("Wrong input type")
    return(H_0)


# make complex array
# x_out = x_out[0] + 1j*x_out[0]
def ImpulseResponse(H, F):
    """
    Input:
        H = existing transferfunction spectrum
        F = [Hz] Frequency bins array
    output:
        IR = [sec] time signal of resultin impulse respose
        T = time of the total impusle response inluding silence
        fs = measured sample frequency

    Impulse response makes use of ifft method to calculate a time signal back
    from the transferfunction.
    fft of the form:
               n-1                      m*k
    a_m =1/n * sum A_k * exp ( -2pi * i ----)    for m = 0, ..., n-1
               k=0                       n
    Therefore fft * 1/N to correct amplitude

    TODO:
    - correction for N
    - Silence removal
    """
    print("""This function works only correct when:
            - no smoothing or averaging is applied
            - full spectrum data is returned!""")
    from scipy.fftpack import ifft, fftshift, fftfreq
    # 2DO Check for full Spectrum
    if isinstance(H, tuple):  # could also use assert
        # Check arrays for type of signal
        # Mag + Phase --> Mag is absolut no neg values
        # Check symetrie no symmerie is false info...
        # Without shift X[0] = F - 0Hz and X[fs/2] =
        # shift check on symmetry?
        H0even = Symmetry(H[0], 'even')
        H1odd = Symmetry(H[1], 'odd')
        if (H0even and H1odd):
            if H[0] == abs(H[0]):
                if max(abs(H[1])) <= np.pi:  # check for phase RAD information
                    pass
                elif max(abs(H[1])) <= 180:  # check for phase DEG information
                    H[1] = H[1] * np.pi / 180
#                    http://stackoverflow.com/questions/2598734/numpy-creating-a-complex-array-from-2-real-ones
#            elif ...:  # check for complex paterns don't know how
#                pass
            else:
                pass
        else:
            raise MeasError.DataError(H, 'No valid frequency array')
    elif np.any(np.iscomplex(H)):
        IR = ifft(H)
    else:
        raise TypeError('Not right input type')
    IR = ifft(H)
    dF = F[1]-F[0]
    fs = np.round(len(F) * dF)
    T = len(F) * 1 / fs
    return(IR, fs, T)


def Cepstrum(x):
    pass
