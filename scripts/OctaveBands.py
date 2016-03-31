# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 11:48:31 2016

@author: Jee-Bee for jBae (c) 2016
"""

# Made with help of:
# http://apmr.matelys.com/Standards/OctaveBands.html
#and
# https://nl.wikipedia.org/wiki/Resolutie_(geluidsmeting)
#http://blog.prosig.com/2006/02/17/standard-octave-bands/


#2DO:
#1/n octave
#self calculating octave range(1/n)
#self calculating freq bands/ check prefered if needed
#self asking for making plot or return to plot depends on direction...
#Update to 1/n method

import numpy as np
import MeasError


def Octave(Measurement, F):
#    Based on 1/3 Octave version. See Link
    Freq_pref = np.array([16, 31.5, 63, 125, 250, 500, 1000, 2000, 4000,
                          8000, 16000])
    # Determine lower and upper limits of each 1/3 octave band
    freq1 = np.zeros(len(Freq_pref))
    bands1 = np.zeros((2, len(Freq_pref)))
    for a in range(len(Freq_pref)):
        freq1[a] = (1000 * ((2 ** (1 / 1))) ** (a - 7))
        bands1[0][a] = freq1[a] / 2 ** (1 / 2)
        bands1[1][a] = freq1[a] * 2 ** (1 / 2)

    # Compute the acoustic absorption coefficient per 1/3 octave band
    bands = []
    for a in range(np.size(bands1, 1)):
        bands = np.append(bands, [0])
        idx = np.where((F >= bands1[0][a]) & (F < bands1[1][a]))
        idx = idx[0]
#        If we have no 'measurement' point in this band:
        if (len(idx) == 0):
            print('Warning: no point found in band centered at %4.0f\n' % freq1[a])
#        If we have only 1 'measurement' point in this band:
        elif (len(idx) == 1):
            print('Warning: only one point found in band centered at %4.0f\n' % freq1[a])
            bands[a] = Measurement[idx[0]]
#        If we have more than 1 'measurement' point in this band:
        elif (len(idx) > 1):
            for b in range(len(idx)):
                bands[a] = bands[a] + (F[idx[0] + b] - F[idx[0] + b - 1]) * abs(Measurement[idx[0] + b] + Measurement[idx[0] + b - 1]) / 2
            bands[a] = bands[a] / (F[idx[len(idx) - 1]] - F[idx[0]])
    return (Freq_pref, bands)


def Octave3(Measurement, F):
#    The input parameters are:
#    o frequencies: frequency values
#        (with a fixed of variable frequency step),
#    o measurements: acoustic absorption coefficent values
#        (corresponding to the frequency vector defined above).
#
#    The output parameters are:
#    o one_third_freq: center frequencies of 1/3 octave bands,
#    o bands: values of the acoustic absorption coefficent in 1/3 bands
#
#    First edition based on
#    Copyleft 2007-2011 luc.jaouen@matelys.com
#    cf. APMR on the web,
#    Standards/OctaveBands.html
#    for more information
    Freq_pref = np.array([16, 20, 25,  31.5, 40, 50, 63, 80, 100, 125, 160,
                          200, 250, 315, 400, 500, 630, 800, 1000, 1250, 1600,
                          2000, 2500, 3150, 4000, 5000, 6300, 8000, 10000,
                          12500, 16000, 20000])

    # Determine lower and upper limits of each 1/3 octave band
    freq3 = np.zeros(len(Freq_pref))
    bands3 = np.zeros((2, len(Freq_pref)))
    for a in range(len(Freq_pref)):
        freq3[a] = (1000 * ((2 ** (1 / 3))) ** (a - 19))
        bands3[0][a] = freq3[a] / 2 ** (1 / 6)
        bands3[1][a] = freq3[a] * 2 ** (1 / 6)
    # Compute the acoustic absorption coefficient per 1/3 octave band
    bands = []
    for a in range(np.size(bands3, 1)):
        bands = np.append(bands, [0])
        idx = np.where((F >= bands3[0][a]) & (F < bands3[1][a]))
        idx = idx[0]
#        If we have no 'measurement' point in this band:
        if (len(idx) == 0):
            print('Warning: no point found in band centered at %4.0f\n' % freq3[a])
#        If we have only 1 'measurement' point in this band:
        elif (len(idx) == 1):
            print('Warning: only one point found in band centered at %4.0f\n' % freq3[a])
            bands[a] = Measurement[idx[0]]
#        If we have more than 1 'measurement' point in this band:
        elif (len(idx) > 1):
            for b in range(len(idx)):
                bands[a] = bands[a] + (F[idx[0] + b] - F[idx[0] + b - 1]) * abs(Measurement[idx[0] + b] + Measurement[idx[0] + b - 1]) / 2
            bands[a] = bands[a] / (F[idx[len(idx) - 1]] - F[idx[0]])
    return (Freq_pref, bands)


def OctaveN(Measurement, F, *args, **kwargs):
#    prefered args = n = 1, 3, 6, 12, 24, 48 and 96
    if len(args) == 0:
        n = 3
    elif len(args) == 1:
        if isinstance(args[0], int):
            print("n = int")
            n = np.int(args[0])
        elif isinstance(args[0], float):
            if args[0] % 1 == 0:
                print("n = float")
                n = np.int(args[0])
            else:
                raise ValueError("Input Value have to be int or float with hole numbers")
        else:
            print("ended wrong instance")
            raise ValueError("Input Value have to be int or float with hole numbers")
    else:
        raise MeasError.SizeError("Length of input var n have worng size")
    # kwargs centerfrequency=int
    if kwargs == {}:
        c = 1000
    else:
        c = kwargs[1]

    rangeF = np.log2(F[-1] / F[0])
    rangeFc = np.log2(c / F[0])
    freqn = np.zeros(rangeF * n)
    bandsn = np.zeros((2, rangeF * n))
    print(np.shape(bandsn))
    for a in range(len(freqn)):
        freqn[a] = (c * ((2 ** (1 / n))) ** (a - rangeFc * n))
        print(a, freqn[a], n, c, rangeFc)
        bandsn[0][a] = freqn[a] / 2 ** (1 / (2 * n))
        bandsn[1][a] = freqn[a] * 2 ** (1 / (2 * n))
    # Compute the acoustic absorption coefficient per 1/n octave band
    bands = []
    for a in range(np.size(bandsn, 1)):
        bands = np.append(bands, [0])
        idx = np.where((F >= bandsn[0][a]) & (F < bandsn[1][a]))
        idx = idx[0]
#        If we have no 'measurement' point in this band:
        if (len(idx) == 0):
            print('Warning: no point found in band centered at %4.0f\n' % freqn[a])
#        If we have only 1 'measurement' point in this band:
        elif (len(idx) == 1):
            print('Warning: only one point found in band centered at %4.0f\n' % freqn[a])
            bands[a] = Measurement[idx[0]]
#        If we have more than 1 'measurement' point in this band:
        elif (len(idx) > 1):
            for b in range(len(idx)):
                bands[a] = bands[a] + (F[idx[0] + b] - F[idx[0] + b - 1]) * abs(Measurement[idx[0] + b] + Measurement[idx[0] + b - 1]) / 2
            bands[a] = bands[a] / (F[idx[len(idx) - 1]] - F[idx[0]])
    return (Freq_pref, bands)



#np.abs(np.array(np.random.rand(T * fs / 2)))
T = 5
fs = 44100
F = np.arange(1/T, fs/2, 1 / T )
oct_array = OctaveN(np.abs(np.array(np.random.rand(T * fs / 2))), F)

#Small tests - delete later on:
#    a = np.array([[1 ,2], [3, 4], [5,6]])
#    a[1] = array([3,4])
#    a[1][1] = 4
#
#    for idx in range(len(a)):
#        print(a[idx][0])
#
#    b = np.where((a>=3) & (a<=5)) = (array([1, 1, 2], dtype=int64), array([0, 1, 0], dtype=int64))


#Example:
#T =3
#f = 1000 Hz #= basic frequency
#np.log10(1000/1) = 3
#np.log10(1000/(1/T)) = 3.477...
#
#np.log2(1000/(1/T)) = 11.55...
#but since formulation octave is:
#1000*2**(n/2) or 1000/2**(n/2)
#i need to compensate my factor 2 so...
#1000 / 2**((2*12)/2) = 0.244... is around 0.33 Hz what was the signal

# 1/n test = 1/24
