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
from src.transform import FFT  # , NFFT
from src.checks import istuple
if sys.version_info.major <3:
    from __future__ import division

# Creating class from this??

# ESD = 
#
#
def PSD(spectrums, F):
    """
    Calculate Power Spectral Density [u^2/sqrt(Hz)^2] = [u^2/Hz]
    Inputs:
        spectrums = Frequency spectrums - Default is spectrum
    Outputs:
        SD = Spectral Density

    SD is created from a single sided Amplitude spectrum of Amplitude and phase
    with a frequency array an Spectral density.

    The input is a spectrum and corsponding frequecy array. The spectrum can be
    a complex signal or an tuple of Amplitude and phase. The complex signal is
    converted to amplitude and Phase and after this the spectrum density is 
    created.
    """
    if istuple(spectrums) is True:
        AMP = spectrums[0]
        PHI = spectrums[1]
        AMP_shape = np.shape(AMP)
        PHI_shape = np.shape(PHI)
        F_shape = np.shape(F)
        if AMP_shape == PHI_shape == F_shape:
            pass
        else:
            raise ValueError ("input parameters don't have same shape")
        if len(AMP_shape) == 1:
            AMP = AMP ** 2 / F  # devide sqrt(Hz)
        elif len(AMP_shape) == 2:
            if AMP_shape[0] < AMP_shape[1]:
                pass
            elif AMP_shape[0] > AMP_shape[1]:
                AMP = AMP.T
                PHI = PHI.T
                F = F.T
                AMP_shape = np.shape(AMP)
            for channel in range(AMP_shape[0]):
                AMP[channel] = AMP[channel] ** 2 / F[channel]  # devide sqrt(Hz)
        else:
            raise ValueError("Shape of input can't be greather than 2")
        pass
    elif np.iscomplex(spectrums) is True:
        spec_shape = np.shape(spectrums)
        if len(spec_shape) == 1:
            N = np.int(len(spectrums))
            F = F[1:N / 2]
            AMP = abs(spectrums[1:N / 2]) ** 2 / F
            PHI = np.arctan2(spectrums[1:N / 2].real, spectrums[1:N / 2].imag)
        elif len(spec_shape) == 2:
            if spec_shape[0] < spec_shape[1]:
                N=shape[1]
            elif spec_shape[0] > spec_shape[1]:
                spectrums = spectrums.T
                spec_shape = np.shape(spectrums)
                N = spec_shape[1]
            for channel in range(AMP_shape[0]):
                F = F[1:N / 2]
                AMP[channel] = spectrums[channel][1:N / 2] ** 2 / F
                PHI[channel] = np.arctan2(spectrums[channel][1:N / 2].real, spectrums[channel][1:N / 2].imag)
        else:
            raise ValueError("Shape of input can't be greather than 2")
    else:
        raise TypeError("Variable spectrums should be type complex or tuple")
    return(AMP, PHI, F)


def SD(spectrums, F):
    """
    Calculate Spectral Density [u/sqrt(Hz)]
    Inputs:
        spectrums = Frequency spectrums - Default is spectrum
    Outputs:
        SD = Spectral Density

    SD is created from a single sided Amplitude spectrum of Amplitude and phase
    with a frequency array an Spectral density.

    The input is a spectrum and corsponding frequecy array. The spectrum can be
    a complex signal or an tuple of Amplitude and phase. The complex signal is
    converted to amplitude and Phase and after this the spectrum density is 
    created.
    """
    if istuple(spectrums) is True:
        AMP = spectrums[0]
        PHI = spectrums[1]
        AMP_shape = np.shape(AMP)
        PHI_shape = np.shape(PHI)
        F_shape = np.shape(F)
        if AMP_shape == PHI_shape == F_shape:
            pass
        else:
            raise ValueError ("input parameters don't have same shape")
        if len(AMP_shape) == 1:
            AMP = AMP / np.sqrt(F)  # devide sqrt(Hz)
        elif len(AMP_shape) == 2:
            if AMP_shape[0] < AMP_shape[1]:
                pass
            elif AMP_shape[0] > AMP_shape[1]:
                AMP = AMP.T
                PHI = PHI.T
                F = F.T
                AMP_shape = np.shape(AMP)
            for channel in range(AMP_shape[0]):
                AMP[channel] = AMP[channel] / np.sqrt(F[channel])  # devide sqrt(Hz)
        else:
            raise ValueError("Shape of input can't be greather than 2")
        pass
    elif np.iscomplex(spectrums) is True:
        spec_shape = np.shape(spectrums)
        if len(spec_shape) == 1:
            N = np.int(len(spectrums))
            AMP = abs(spectrums[1:N / 2]) / np.sqrt(F)
            PHI = np.arctan2(spectrums[1:N / 2].real, spectrums[1:N / 2].imag)
            F = F[1:N / 2]
        elif len(spec_shape) == 2:
            if spec_shape[0] < spec_shape[1]:
                N=shape[1]
            elif spec_shape[0] > spec_shape[1]:
                spectrums = spectrums.T
                spec_shape = np.shape(spectrums)
                N = spec_shape[1]
            for channel in range(AMP_shape[0]):
                AMP[channel] = spectrums[channel][1:N / 2] / np.sqrt(F[1:N / 2])
                PHI = np.arctan2(spectrums[channel][1:N / 2].real, spectrums[channel][1:N / 2].imag)
                F = F[1:N / 2]
        else:
            raise ValueError("Shape of input can't be greather than 2")
    else:
        raise TypeError("Variable spectrums should be type complex or tuple")
    return(AMP, PHI, F)

# ASD =


def PS(spectrums):
    """
    Calculate Power Spectrum [W]
    Inputs:
        spectrums = Frequency spectrums - Default is spectrum
    Outputs:
        PS = [W?] Power spectrum

    PS creates from a single sided Amplitude spectrum of Amplitude and phase
    a power spectrum.

    The input is a spectrum. This can be a complex signal or an tuple of
    Amplitude and phase. The complex signal is converted to amplitude and Phase
    and after this the power spectrum is created.
    """
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
