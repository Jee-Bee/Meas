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

import sys
import numpy as np
<<<<<<< HEAD:src/spectraldistr.py
from src.transform import FFT  # , NFFT
if sys.version_info.major <3:
    from __future__ import division
=======
import scipy.fftpack as fft
from scripts.transform import FFT, NFFT
from scripts.checks import istuple
>>>>>>> Change beahvour Power Spectrum. Input only complex or amplitude phase + add multi channel:scripts/spectraldistr.py

# Creating class from this??

# ESD = 
#
#
def PSD(sig, fs=None, window='hann', window_length=8192, weighting=False, inputspec=True):
    """
    Calculate Spectral Density Spectrum [W]
    Inputs:
        sig = time or spectrum - Default is spectrum
        fs = [Hz] sample frequency - only valid when time signal
            (inputspec=False)
    Outputs:
        F = [Hz] frequency bins
        PSD = [W?] Power spectral density - power per hertz
    Options:
        window = [string] name of windowtype - Only valid when inputspec is
                time (False)
        window_length = [-] length of window in number of samples - Only valid
                        when inputspec is time (False)
        weighting = True/False Boolean for setting if a weighting is applied on
                    spectrum - only valid when inputspec is time(False)
        inputspec = True/False Boolean for setting input as spectrum(True) or
                    as time Signal(False)

    AS creates a single sided spectrum of Frequency and phase.
    There two possible input signals. a time signal and a spectral signal
    (complex or Real and Imaginair).

    When time signal is applied some extra parameters can be set.
    window and weighting.
    For window it is possible to set the window type and length of samples.
    default for this is hanning window and length of 8192 samples.
    after this the single sided power spectrum is created and returned.

    When input is a spectrum. it is checked for complex vallued signal and for
    symmetry.
    after this the single sided power spectrum is created and returned.
    """
    if inputspec is True:
        from src.checks import istuple, even, odd, oddphase, phasecheck
        if istuple(sig):
            sig1phase = phasecheck(sig[1])
            if sig1phase is True:
                sig0even = even(sig[0])
                sig1odd = oddphase(sig[1])
                if (sig0even is True) and (sig1odd is True):
                    N = len(sig)
                    F = np.arange(1, N / 2)
                    PSD = (sig[0][1:len(sig[0]) / 2] ** 2) / F
                    # power per Hertz
                    PH = sig[1][1:len(sig[1])/2]
                else:
                    N = len(sig)
                    F = np.arange(1, N / 2)
                    PSD = (sig[0] ** 2) / F  # power per hertz
                    PH = sig[1]
            else:
                sig0even = even(sig[0])
                sig1odd = odd(sig[1])
                if (sig0even is True) and (sig1odd is True):
                    N = len(sig)
                    F = np.arange(1, N/2)
                    PSD = (np.sqrt(sig[0][1:len(sig[0]) / 2] ** 2 + sig[1][1:len(sig[1]) / 2] ** 2) ** 2) / F
                    PH = np.arctan2(sig[0][1:len(sig[0]) / 2], sig[1][1:len(sig[1]) / 2])
                else:
                    N = len(sig)
                    F = np.arange(1, N / 2)
                    PSD = (np.sqrt(sig[0] ** 2 + sig[1] ** 2) ** 2) / F
                    # power per hertz
                    PH = np.arctan2(sig[0], sig[1])
        elif np.iscomplex(sig):
            print('from complex spectum is becomming a magnitude pahse spectrum... \nshow olny N/2 frequency bins')
            N = len(sig)
            F = np.arange(1, N / 2)
            PSD = (abs(sig[1:N / 2]) ** 2) / F  # power per hertz
            PH = np.arctan2(sig.real, sig.imag)
    elif inputspec is False:
        F, PSD, PH = AS(sig, fs, window, window_length, weighting, inputspec)
        PSD = (PSD ** 2) / F  # Power per hertz - AS to PSD 
    else:
        raise ValueError('inputspec should be True or False')
    return(F, PSD, PH)


def SD(sig, fs=None, window='hann', window_length=8192, weighting=False, inputspec=True):
    """
    Calculate Power Spectrum [W]
    Inputs:
        sig = time or spectrum - Default is spectrum
        fs = [Hz] sample frequency - only valid when time signal
            (inputspec=False)
    Outputs:
        F = [Hz] frequency bins
        SD = spectral density
    Options:
        window = [string] name of windowtype - Only valid when inputspec is
                time (False)
        window_length = [-] length of window in number of samples - Only valid
                        when inputspec is time (False)
        weighting = True/False Boolean for setting if a weighting is applied on
                    spectrum - only valid when inputspec is time(False)
        inputspec = True/False Boolean for setting input as spectrum(True) or
                    as time Signal(False)

    AS creates a single sided spectrum of Frequency and phase.
    There two possible input signals. a time signal and a spectral signal
    (complex or Real and Imaginair).

    When time signal is applied some extra parameters can be set.
    window and weighting.
    For window it is possible to set the window type and length of samples.
    default for this is hanning window and length of 8192 samples.
    after this the single sided power spectrum is created and returned.

    When input is a spectrum. it is checked for complex vallued signal and for
    symmetry.
    after this the single sided power spectrum is created and returned.
    """
    if inputspec is True:
        from src.checks import istuple, even, odd, oddphase, phasecheck
        if istuple(sig):
            sig1phase = phasecheck(sig[1])
            if sig1phase is True:
                sig0even = even(sig[0])
                sig1odd = oddphase(sig[1])
                if (sig0even is True) and (sig1odd is True):
                    N = len(sig)
                    F = np.arange(1, N / 2)
                    SD = sig[0][1:len(sig[0])/2] / np.sqrt(F)  # devide sqrt(Hz)
                    PH = sig[1][1:len(sig[1])/2]
                else:
                    N = len(sig)
                    F = np.arange(1, N / 2)
                    SD = sig[0] / np.sqrt(F)  # devide sqrt(Hz)
                    PH = sig[1]
            else:
                sig0even = even(sig[0])
                sig1odd = odd(sig[1])
                if (sig0even is True) and (sig1odd is True):
                    N = len(sig)
                    F = np.arange(1, N/2)
                    SD = np.sqrt(sig[0][1:len(sig[0]) / 2] ** 2 + sig[1][1:len(sig[1]) / 2] ** 2) / np.sqrt(F)  # devide sqrt(Hz)
                    PH = np.arctan2(sig[0][1:len(sig[0]) / 2], sig[1][1:len(sig[1]) / 2])
                else:
                    N = len(sig)
                    F = np.arange(1, N / 2)
                    SD = np.sqrt(sig[0] ** 2 + sig[1] ** 2) / np.sqrt(F)
                    # devide sqrt(Hz)
                    PH = np.arctan2(sig[0], sig[1])
        elif np.iscomplex(sig):
            print('from complex spectum is becomming a magnitude pahse spectrum... \nshow olny N/2 frequency bins')
            N = len(sig)
            F = np.arange(1, N / 2)
            SD = abs(sig[1:N / 2]) / np.sqrt(F)  # devide sqrt(Hz)
            PH = np.arctan2(sig.real, sig.imag)
    elif inputspec is False:
        F, PS, PH = AS(sig, fs, window, window_length, weighting, inputspec)
        SD = SD / np.sqrt(F)  # devide sqrt(Hz) -AS to SD
    else:
        raise ValueError('inputspec should be True or False')
    return(F, SD, PH)


# ASD =


def PS(spectrums):
    """
    Calculate Power Spectrum [W]
    Inputs:
        spectrums = Frequency spectrums - Default is spectrum
    Outputs:
        PS = [W?] Power spectrum

    PS creates from a single sided  Amplitude spectrum of Frequency and phase
    a power spectrum.

    The input is a spectrum. This can be a complex signal or an tuple of
    Amplitude and phase. The complex signal is converted to amplitude and Phase
    and after this the power spectrum is created.
    """
#    if inputspec is True:
#        from scripts.checks import istuple, even, odd, oddphase, phasecheck
#        if istuple(sig):
#            sig1phase = phasecheck(sig[1])
#            if sig1phase is True:
#                sig0even = even(sig[0])
#                sig1odd = oddphase(sig[1])
#                if (sig0even is True) and (sig1odd is True):
#                    N = len(sig)
#                    F = np.arange(1, N / 2)
#                    PS = sig[0][1:len(sig[0]) / 2] ** 2
#                    PH = sig[1][1:len(sig[1])/2]
#                else:
#                    N = len(sig)
#                    F = np.arange(1, N / 2)
#                    PS = sig[0] ** 2
#                    PH = sig[1]
#            else:
#                sig0even = even(sig[0])
#                sig1odd = odd(sig[1])
#                if (sig0even is True) and (sig1odd is True):
#                    N = len(sig)
#                    F = np.arange(1, N/2)
#                    PS = np.sqrt(sig[0][1:len(sig[0]) / 2] ** 2 + sig[1][1:len(sig[1]) / 2] ** 2) ** 2
#                    PH = np.arctan2(sig[0][1:len(sig[0]) / 2], sig[1][1:len(sig[1]) / 2])
#                else:
#                    N = len(sig)
#                    F = np.arange(1, N / 2)
#                    PS = np.sqrt(sig[0] ** 2 + sig[1] ** 2) ** 2
#                    PH = np.arctan2(sig[0], sig[1])
#        elif np.iscomplex(sig):
#            print('from complex spectum is becomming a magnitude pahse spectrum... \nshow olny N/2 frequency bins')
#            N = len(sig)
#            F = np.arange(1, N / 2)
#            PS = abs(sig[1:N / 2]) ** 2
#            PH = np.arctan2(sig.real, sig.imag)
#    elif inputspec is False:
#        F, PS, PH = AS(sig, fs, window, window_length, weighting, inputspec)
#        PS = PS ** 2  # AS to PS
#    else:
#        raise ValueError('inputspec should be True or False')
#    return(F, PS, PH)
    if istuple(spectrums) is True:
        AMP = spectrums[0]
        PHI = spectrums[1]
        AMP_shape = np.shape(AMP)
        if len(AMP_shape) == 1:
            AMP = AMP ** 2
        elif len(AMP_shape) == 2:
            if AMP_shape[0] < AMP_shape[1]:
                pass
            elif AMP_shape[0] > AMP_shape[1]:
                AMP = AMP.T
                PHI = PHI.T
                AMP_shape = np.shape(AMP)
            for channel in range(AMP_shape[0]):
                AMP[channel] = AMP[channel] ** 2
        else:
            raise ValueError("Shape of input can't be greather than 2")
        pass
    elif np.iscomplex(spectrums) is True:
        spec_shape = np.shape(spectrums)
        if len(spec_shape) == 1:
            N = np.int(len(spectrums))
            AMP = abs(spectrums[1:N / 2]) ** 2
            PHI = np.arctan2(spectrums[1:N / 2].real, spectrums[1:N / 2].imag)
        elif len(spec_shape) == 2:
            if spec_shape[0] < spec_shape[1]:
                N=shape[1]
                pass
            elif spec_shape[0] > spec_shape[1]:
                spectrums = spectrums.T
                spec_shape = np.shape(spectrums)
                N = spec_shape[1]
            for channel in range(AMP_shape[0]):
                AMP[channel] = spectrums[channel][1:N / 2] ** 2
                PHI = np.arctan2(spectrums[channel][1:N / 2].real, spectrums[channel][1:N / 2].imag)
        else:
            raise ValueError("Shape of input can't be greather than 2")
    else:
        raise TypeError("Variable spectrums should be type complex or tuple")
    return(AMP, PHI)


def AS(sig, fs, window=None, window_length=8192):
    """
    Calculate Amplitude Spectrum [v // g // ...]
    Inputs:
        sig = time or spectrum - Default is spectrum (Magnitude, Phase)
        fs = [Hz] sample frequency - only valid when time signal
            (inputspec=False)
    Outputs:
        F = [Hz] Frequency Array of given frequencies - only availeble in time
            input
        AS = [V, g,...] amplitude spectrum depends on input
        PH = [deg] phase output -180 - 180 degrees phase
    Options:
        window = [string] name of windowtype - Only valid when inputspec is
                time (False)
        window_length = [-] length of window in number of samples - Only valid
                        when inputspec is time (False)

    AS creates a single sided spectrum of Frequency and phase.
    The input array is an time signal. So this function is a copy of the mFFT
    function. However the default values are different. The type of output is
    in AS set to Amplitude and Phase and CAN'T be changed!

    For window it is possible to set the window type and length of samples.
    default for this is hanning window and length of 8192 samples.
    When window_length is set to None; no window will be applied
    after this the single sided amplitude spectrum is created and returned.
    """
    import types
    from .transform import mFFT

    def AS_int(mFFT):
        AS_mFFT = types.FunctionType(mFFT.__code__, mFFT.__globals__, name=mFFT.__name__,
                                     argdefs=mFFT.__defaults__, closure=mFFT.__closure__)
        return(AS_mFFT)
    AS_func = AS_int(mFFT)
    AS_val = AS_func(sig, fs, window, window_length, spectrum='AmPh')
    return(AS_val)


# def complexAS(sig, fs=None, window='hann', window_length=8192, weighting=False, inputspec=True):
#     pass

# spectraldistr.py
# Created by Jee-Bee for jBae 2016(c)
