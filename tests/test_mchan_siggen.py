# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 11:40:51 2016

@author: Jee-Bee for jBae (c) 2016
"""

import numpy as np
from scipy.fftpack import fft, ifft
from scipy.signal import chirp
import matplotlib.pyplot as plt

# test script for making multi channel calculations

# make a loop of single valued arrays containing the array number and
# a length  of 1024 samples.

transformed = True
cascade = True  # serie matig iedere output om de beurt
method = 2

T = 5
T_s = 1  # silence after signal
fs = 1024
nChan = 3
nrepeates = 3
f0 = fs/128
f1 = fs/8

# simple multi channel sine generator
t = np.arange(T * fs) / fs
si_chirp = chirp(t, f0, T, f1, method='log', phi=90)
si_chirp = np.append(si_chirp, np.zeros(T_s * fs))
if cascade is True:
    # method 1: repeats chirps per channel than channels in serie
    if method == 1:
        chan_chirp = []
        rep_chirp = []
        # step 1: repeat chrip signal:
        for repeats in range(nrepeates):
            chan_chirp = np.concatenate((chan_chirp, si_chirp))
        rep_chirp = np.zeros((nChan, nChan * len(chan_chirp)))
        print("len rep_chirp", len(rep_chirp.T))
        # step 2 place chirps in total lenght signal positions
        for Channel in range(nChan):
            rep_chirp[Channel, Channel * len(temp_chirp): (Channel + 1) * len(temp_chirp)] = temp_chirp
        t = np.arange(len(rep_chirp.T))/fs
    # method 2: chirps in channels; repeat all channels
    elif method == 2:
        chan_chirp = []
        rep_chirp = np.zeros((nChan, nChan * len(si_chirp)))
        # step 1 place chirps in single chirp positions
        for Channel in range(nChan):
            rep_chirp[Channel, Channel * len(si_chirp) : (Channel + 1) * len(si_chirp)] = si_chirp
        # step 2: repeat total signal set:
        for repeats in range(nrepeates):
            rep_chirp = np.concatenate((rep_chirp, rep_chirp[0:len(si_chirp)]), axis=1)
        t = np.arange(len(rep_chirp.T))/fs
    else:
        raise ValueError("method should be a 1 or a 2")
elif cascade is False:
    # in practice: if cascade is false a single signal should be send to all
    # channels.
    # it looks this happens automaticly...
    rep_chirp = []
    for repeats in range(nrepeates):
        rep_chirp = np.concatenate((rep_chirp, si_chirp))
    for channels in range(nChan-1):
        if channels == 0:
            rep_chirp = np.vstack((rep_chirp, rep_chirp))
        else:
            rep_chirp = np.vstack((rep_chirp, rep_chirp[0]))
        print(np.shape(rep_chirp))
    t = np.arange(len(rep_chirp.T))/fs
else:
    raise ValueError("for cascade only values True or False are alloud")

chan_chirp = []
for Channel in range(nChan):
    if Channel == 0:
        chan_chirp = np.concatenate((chan_chirp, (0.5 + 0.5 * Channel) * np.sin(2 * np.pi * (1 + Channel * 5) * t)), axis=0)
    else:
        #chan_stack = np.concatenate((chan_stack, np.ones(1024)*chan),axis=0)
        chan_chirp = np.vstack((chan_chirp, (0.5 + 0.5 * Channel) * np.sin(2 * np.pi * (1 + Channel * 5) * t)))


# dimension checker
chirpshape = np.shape(rep_chirp)
# Shape give de dimesnions of the number of arrays as a tuple.
# shape tuple exist of (len(x), len(x.T))
# if len(shape) = 1 one dimensional (mono recording).
# if len(shape) = 2 two dimensional (stereo(2) or more channels)


# plot single values and plot array of the signals
plt.figure()
plt.plot(si_chirp)
plt.show()
if len(chirpshape) > 1:
    if chirpshape[0] < chirpshape[1]:
        plt.figure()
        for plotn in range(len(rep_chirp)):
            plt.plot(t, rep_chirp[plotn])
        plt.show()
    else:
        plt.figure()
        for plotn in range(len(rep_chirp.T)):
            plt.plot(t, rep_chirp.T[plotn])
        plt.show()


# FFT analysis at signals:
# multi fft in form of (channels, length), otherwise transpose
# limit number of channels to 32
chirpshape = np.shape((rep_chirp))
if len(chirpshape) == 1:
    # std fft is correct
    print('std FFT is fine no multi channel FFT Needed')
elif len(chirpshape) == 2:
    if chirpshape[0] < chirpshape[1]:
        print('right direction')
        CHIRP_REP = []
        for channel in range(chirpshape[0]):
            print(channel)
            # add fft here
            SI_CHIRP = fft(rep_chirp[Channel])  # single channel
            if channel == 0:
                print("channel 0")
                CHIRP_REP = np.append(CHIRP_REP,SI_CHIRP)
            else:
                print("channel >0")
                CHIRP_REP = np.vstack((CHIRP_REP,SI_CHIRP))
    else:
        # wrong direction... Transform needed
        print('Transform Needed')
        chirp_rep = chirp_rep.T  # signal transformed
        # now fft
        CHIRP_REP = []
        for channel in range(chirpshape[1]):
            print(channel)
            # add fft here
            SI_CHIRP = fft(rep_chirp[channel])  # single channel
            if channel == 0:
                print("channel 0")
                CHIRP_REP = np.append(CHIRP_REP,SI_CHIRP)
            else:
                print("channel >0")
                CHIRP_REP = np.vstack((CHIRP_REP,SI_CHIRP))
    print(chirpshape[0])
else:
    raise ValueError('not a valid number of dimensions')

F = np.arange(len(CHIRP_REP.T)/2)
F = np.append(np.arange(-len(CHIRP_REP.T)/2,0),F)

plt.figure()
for plotn in range(len(CHIRP_REP)):
    plt.plot(F, abs(CHIRP_REP[plotn]))
plt.show()
