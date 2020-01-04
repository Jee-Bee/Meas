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
from scripts.transform import FFT  # , NFFT
if sys.version_info.major <3:
    from __future__ import division

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
        from scripts.checks import istuple, even, odd, oddphase, phasecheck
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
        from scripts.checks import istuple, even, odd, oddphase, phasecheck
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


def PS(sig, fs=None, window='hann', window_length=8192, weighting=False, inputspec=True):
    """
    Calculate Spectral Density Spectrum [W]
    Inputs:
        sig = time or spectrum - Default is spectrum
        fs = [Hz] sample frequency - only valid when time signal
            (inputspec=False)
    Outputs:
        F = [Hz] frequency bins
        PS = [W?] Power spectrum
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
        from scripts.checks import istuple, even, odd, oddphase, phasecheck
        if istuple(sig):
            sig1phase = phasecheck(sig[1])
            if sig1phase is True:
                sig0even = even(sig[0])
                sig1odd = oddphase(sig[1])
                if (sig0even is True) and (sig1odd is True):
                    N = len(sig)
                    F = np.arange(1, N / 2)
                    PS = sig[0][1:len(sig[0]) / 2] ** 2
                    PH = sig[1][1:len(sig[1])/2]
                else:
                    N = len(sig)
                    F = np.arange(1, N / 2)
                    PS = sig[0] ** 2
                    PH = sig[1]
            else:
                sig0even = even(sig[0])
                sig1odd = odd(sig[1])
                if (sig0even is True) and (sig1odd is True):
                    N = len(sig)
                    F = np.arange(1, N/2)
                    PS = np.sqrt(sig[0][1:len(sig[0]) / 2] ** 2 + sig[1][1:len(sig[1]) / 2] ** 2) ** 2
                    PH = np.arctan2(sig[0][1:len(sig[0]) / 2], sig[1][1:len(sig[1]) / 2])
                else:
                    N = len(sig)
                    F = np.arange(1, N / 2)
                    PS = np.sqrt(sig[0] ** 2 + sig[1] ** 2) ** 2
                    PH = np.arctan2(sig[0], sig[1])
        elif np.iscomplex(sig):
            print('from complex spectum is becomming a magnitude pahse spectrum... \nshow olny N/2 frequency bins')
            N = len(sig)
            F = np.arange(1, N / 2)
            PS = abs(sig[1:N / 2]) ** 2
            PH = np.arctan2(sig.real, sig.imag)
    elif inputspec is False:
        F, PS, PH = AS(sig, fs, window, window_length, weighting, inputspec)
        PS = PS ** 2  # AS to PS
    else:
        raise ValueError('inputspec should be True or False')
    return(F, PS, PH)


def AS(sig, fs=None, window='hann', window_length=8192, weighting=False, inputspec=True):
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
    When window_length is set to None; no window will be applied
    after this the single sided amplitude spectrum is created and returned.

    When input is a spectrum. it is checked for complex vallued signal and for
    symmetry.
    after this the single sided amplitude spectrum is created and returned.
    """
    if inputspec is True:
        from scripts.checks import istuple, even, odd, oddphase, phasecheck
        if istuple(sig):
            sig1phase = phasecheck(sig[1])
            if sig1phase is True:
                sig0even = even(sig[0])
                sig1odd = oddphase(sig[1])
                if (sig0even is True) and (sig1odd is True):
                    N = len(sig)
                    F = np.arange(1, N / 2)
                    AS = sig[0][1:len(sig[0])/2]
                    PH = sig[1][1:len(sig[1])/2]
                else:
                    N = len(sig)
                    F = np.arange(1, N / 2)
                    AS = sig[0]
                    PH = sig[1]
            else:
                sig0even = even(sig[0])
                sig1odd = odd(sig[1])
                if (sig0even is True) and (sig1odd is True):
                    N = len(sig)
                    F = np.arange(1, N / 2)
                    AS = np.sqrt(sig[0][1:len(sig[0]) / 2] ** 2 + sig[1][1:len(sig[1]) / 2] ** 2)
                    PH = np.arctan2(sig[0][1:len(sig[0]) / 2], sig[1][1:len(sig[1]) / 2])
                else:
                    N = len(sig)
                    F = np.arange(1, N / 2)
                    AS = np.sqrt(sig[0] ** 2 + sig[1] ** 2)
                    PH = np.arctan2(sig[0], sig[1])
        elif np.iscomplex(sig):
            print('from complex spectum is becomming a magnitude pahse spectrum... \nshow olny N/2 frequency bins')
            N = len(sig)
            AS = abs(sig[1:N / 2])
            PH = np.arctan2(sig.real, sig.imag)
            F = np.arange(1, N / 2)
    elif inputspec is False:
        if fs is not None:
            pass
        else:
            raise ValueError('value fs is \'None\' this should be changed')
# https://stackoverflow.com/questions/18472904/how-to-use-a-python-function-with-keyword-self-in-arguments
        if (window_length is None) and (weighting is False):
            F, AS, PH = FFT(sig, fs, spectrum='AmPh0')
        elif (window_length is None) and (weighting is not False):
            F, AS, PH = FFT(sig, fs, spectrum='AmPh')
        elif isinstance(window_length, int) and (weighting is False):
            F, AS, PH = FFT(sig, fs, window, window_length, spectrum='AmPh0')
        elif isinstance(window_length, int) and (weighting is not False):
            F, AS, PH = FFT(sig, fs, window, window_length, spectrum='AmPh')

        if weighting is False:
            pass
        elif weighting is True:
            from scripts.weighting import AWeighting
            aw = AWeighting()
            AS = aw.A_Weighting(F, AS)
        elif weighting == 'A':
            from scripts.weighting import AWeighting
            aw = AWeighting()
            AS = aw.A_Weighting(F, AS)
        elif weighting == 'B':
            from scripts.weighting import BWeighting
            bw = BWeighting()
            AS = bw.B_Weighting(F, AS)
        elif weighting == 'C':
            from scripts.weighting import CWeighting
            cw = CWeighting()
            AS = cw.C_Weighting(F, AS)
        elif weighting == 'D':
            from scripts.weighting import DWeighting
            dw = DWeighting()
            AS = dw.D_Weighting(F, AS)
        else:
            raise ValueError('weighing should be True, False, or the letters A to D')
    else:
        raise ValueError('inputspec should be True or False')
    return(F, AS, PH)


# def complexAS(sig, fs=None, window='hann', window_length=8192, weighting=False, inputspec=True):
#     pass

# spectraldistr.py
# Created by Jee-Bee for jBae 2016(c)
