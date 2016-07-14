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
#from ..script import MeasError #as ME # , MeasWarning


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


def Symmetry(spec, Stype):
    """
    inputs:
        spec = input array of unknown values.
        Stype = symetry type \'even\' or \'odd\'
    Output:
        Symetry check = True or False boolean

    Check for symmetry in given Signals"""
    N = len(spec)
    if Stype == 'even':
        for idx in range(int(N / 2 - 1)):
            if round(spec[idx + 1], 6) == round(spec[(N - 1) - idx], 6):
                pass
                # print(idx, x[idx + 1], round(x[idx + 1], 6), round(x[(N - 1) - idx]))  # pass
            else:
                return (False)
                break
    elif Stype == 'odd':
        for idx in range(int(N / 2 - 1)):
            if round(spec[idx + 1], 6) == - round(spec[(N - 1) - idx], 6):
                pass
                # print(idx, x[idx + 1], round(x[idx + 1], 6), round(x[(N - 1) - idx]))  # pass
            else:
                return (False)
                break
    else:
        raise TypeError('No valid input type or value')
        return(False)
    return(True)


def MagPh2ReIm(Mag, Phi, output='ReIm'):
    """
    Inputs:
        MAG = Magnitude spectrum *
        PHI = phase spectrum *
    Outputs:
        RE = real vallued output
        IM = Imaginear vallued output

    * at this moment only to Real and Imaginaire vallues later on also Complex

    Calculate back the Real and imaginary Values
    To Do:
        - Make Real + Imag to Complex values - If required """
    Re = Mag * np.cos(Phi)
    Im = Mag * np.sin(Phi)
    return(Re, Im)


def FFT(x, fs, *args, **kwargs):
    from scipy.fftpack import fft, fftshift, fftfreq
    """
    Inputs:
        sig = [sec] time domain signal
        fs = [Hz] sample frequency
        Window_Type = [string] name window
        Window_size = [N] number of samples window
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
    - fix right place of F(frequency bins)"""
    nfft = NFFT(x)
    N = len(x)  # Temporary solution
    # print(N, nfft)
    if len(args) == 0:
        X = fft(x, nfft) / N
        N = np.int(nfft)
    elif len(args) <= 3:
        if len(args) == 3:
            if isinstance(args[1], str):
                # Window_Type = argv[1]
                pass
            else:
                errorstr = "Window Type not right type: Has to be 'str'" 
                raise TypeError(errorstr)
            # argv[2]print
            if isinstance(args[2], int) == True:
                # Window_size = (args[2])
                pass
            elif isinstance(args[2], float) == True:
                if args[2] % 1 == 0:
                    # Window_size = int(args[2])
                    pass
            else:
                errorstr = "Window Length not right type: Has to be 'int' or 'float'" 
                raise TypeError(errorstr)
            # argv[3]
            if isinstance(args[3], int):
                # smoothing = (args[3])
                pass
            elif isinstance(args[2], float):
                if args[2] % 1 == 0:
                    # smoothing = int(args[3])
                    pass
            else:
                errorstr = "Smooting not the right input type: Has to be 'int' or Float" 
                raise TypeError(errorstr)
        else:
            if isinstance(args[1], str):
                # Window_Type = argv[1]
                pass
            elif isinstance(args[1], int):
                # smoothing = int(args[1])
                pass
            elif isinstance(args[1], float):
                if args[1] % 1 == 0:
                    # smoothing = int(args[1])
                    pass
            else:
                raise TypeError("not the right input type")
    else:
#        raise ME.SizeError(args, "not the right number of parameters")
        print(args)
    
    if ('shift' in kwargs) and ('spectrum' in kwargs):
        pass
    elif 'shift' in kwargs:
        if kwargs['shift'] == 'True' or 'true' or True:
            X = fftshift(X)
            F = np.linspace(0, (N-1)/2, N/2)
            F = np.append(F,np.linspace(-N/2, -1, N/2))
            F = F/(N/fs)
            return(F, X)
        elif kwargs['shift'] == 'False' or 'false' or False:
            F = np.linspace(0, (N-1)/2, N/2)
            F = np.append(F,np.linspace(-N/2, -1, N/2))
            F = F/(N/fs)
            return(F, X)
        else:
            raise ValueError('Wrong ')
    elif 'spectrum' in kwargs:
        if kwargs['spectrum'] == 'complex':
            # F = np.arange(0, fs, 1 / (N / fs))  # alternate frequency array
            F = np.linspace(0, (N-1)/2, N/2)
            F = np.append(F,np.linspace(-N/2, -1, N/2))
            F = F/(N/fs)
            return(F, X)
        elif kwargs['spectrum'] == 'AmPh0':
            F = np.linspace(0, (N-1)/2, N/2)
            F = F/(N/fs)
            Amp = abs(X[0:N/2])
            phi = np.arctan(np.real(X[0:N / 2]) / np.imag(X[0:N / 2]))
            return(F, Amp,phi)
        elif kwargs['spectrum'] == 'AmPh':
            F = np.linspace(1, (N-1)/2, N/2 - 1)
            F = F/(N/fs)
            Amp = abs(X[1:N/2])
            phi = np.arctan(np.real(X[1:N / 2])/np.imag(X[1:N / 2]))
            return(F, Amp, phi)
        else:
            raise ValueError('The element % don\'t exist for the keyword \'spectrum\'' % kwargs['spectrum'])
    elif len(kwargs) == 0:
        F = np.linspace(0, (N-1)/2, N/2)
        F = np.append(F,np.linspace(-N/2, -1, N/2))
        F = F/(N/fs)
        return(F, X)
    else:
        print(kwargs)
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
        
    if isinstance(x_in, tuple):
        x_in0even = Symmetry(x_in[0], 'even')
        x_in1odd = Symmetry(x_in[1], 'odd')
        print(x_in0even, x_in1odd)
        # make complex array
        if (x_in0even & x_in1odd):
            x_in = x_in[0] + 1j*x_in[1]
        if isinstance(x_out, tuple):
            x_out0even = Symmetry(x_out[0], 'even')
            x_out1odd = Symmetry(x_out[1], 'odd')
            # make complex array
            if (x_out0even & x_out1odd):
                x_out = x_out[0] + 1j*x_out[0]
                H_0 = x_in / x_out
        elif np.iscomplexobj(x_out):
            H_0 = x_in / x_out
        elif np.isrealobj(x_out):
            X_OUT, F = FFT(x_out, fs)
            H_0 = x_in / X_OUT
        else:
            raise TypeError("Wrong input type")
    elif np.iscomplexobj(x_in):
        if isinstance(x_out, tuple):
            x_out0even = Symmetry(x_out[0], 'even')
            x_out1odd = Symmetry(x_out[1], 'odd')
            # make complex array
            if (x_out0even & x_out1odd):
                x_out = x_out[0] + 1j*x_out[0]
                H_0 = x_in / x_out
        elif np.iscomplexobj(x_out):
            H_0 = x_in / x_out
        elif np.isrealobj(x_out):
            (F, X_OUT) = FFT(x_out, fs)
            H_0 = x_in / X_OUT
        else:
            raise TypeError("Wrong input type")
    elif np.isrealobj(x_in):
        (F, X_IN) = FFT(x_in, fs)
        if isinstance(x_out, tuple):
            x_out0even = Symmetry(x_out[0], 'even')
            x_out1odd = Symmetry(x_out[1], 'odd')
            # make complex array
            if (x_out0even & x_out1odd):
                x_out = x_out[0] + 1j*x_out[0]
                H_0 = X_IN / x_out
        elif np.iscomplexobj(x_out):
            H_0 = X_IN / x_out
        elif np.isrealobj(x_out):
            (F, X_OUT) = FFT(x_out, fs)
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
                    pass
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
