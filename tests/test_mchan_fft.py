# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 11:40:51 2016

@author: Jee-Bee for jBae (c) 2016
"""

import numpy as np
from scipy.fftpack import fft, ifft
import matplotlib.pylab as plt

# test script for making multi channel calculations

# make a loop of single valued arrays containing the array number and
# a length  of 1024 samples.

transformed = True

nChan = 3
chan = []
for channel in range(nChan):
    print(channel)
    if channel == 0:
        chan = np.concatenate((chan, np.ones(1024)*channel),axis=0)
    else:
        #chan_stack = np.concatenate((chan_stack, np.ones(1024)*chan),axis=0)
        chan = np.vstack((chan, np.ones(1024)*channel))


# simple multi channel sine generator
t = np.arange(1024)/1024
chansine = []
for channel in range(nChan):
    print(channel)
    if channel == 0:
        chansine = np.concatenate((chansine, (0.5 + 0.5 * channel) * np.sin(2*np.pi * (1 + channel * 5) *t)),axis=0)
    else:
        #chan_stack = np.concatenate((chan_stack, np.ones(1024)*chan),axis=0)
        chansine = np.vstack((chansine, (0.5 + 0.5 * channel) * np.sin(2*np.pi * (1 + channel * 5) *t)))

if transformed == True:
    chan = chan.T
    chansine = chansine.T


# test transformations:
chansinet = chansine.T
chansinett = chansinet.T
# chansinett == chansine so theye are equal and not inversed.
# so if size[m,n] = len(signal), n-channels a single transform is allready
# correcting the result!!

# dimension checker
sineshape = np.shape(chansine)
sineshapet = np.shape(chansine.T)
ssineshape = np.shape(chansine[0])
print(sineshape, sineshapet, ssineshape, len(chansine.T))
# Shape give de dimesnions of the number of arrays as a tuple.
# shape tuple exist of (len(x), len(x.T))
# if len(shape) = 1 one dimensional (mono recording).
# if len(shape) = 2 two dimensional (stereo(2) or more channels)


# plot single values and plot array of the signals
plt.figure()
plt.plot(chan)
plt.show()
if len(sineshape) > 1:
    if sineshape[0] < sineshape[1]:
        plt.figure()
        for plotn in range(len(chansine)):
            plt.plot(t, chansine[plotn])
        plt.show()
    else:
        plt.figure()
        for plotn in range(len(chansine.T)):
            plt.plot(t, chansine.T[plotn])
        plt.show()


# FFT analysis at signals:
# multi fft in form of (channels, length), otherwise transpose
# limit number of channels to 32
chanshape = np.shape((chansine))
if len(chanshape) == 1:
    # std fft is correct
    print('std FFT is fine no multi channel FFT Needed')
elif len(chanshape) == 2:
    if chanshape[0] < chanshape[1]:
        print('right direction')
        CHANSINE = []
        for channel in range(chanshape[0]):
            print(channel)
            # add fft here
            SI_CHAN = fft(chansine[channel])  # single channel
            if channel == 0:
                print("channel 0")
                CHANSINE = np.append(CHANSINE,SI_CHAN)
            else:
                print("channel >0")
                CHANSINE = np.vstack((CHANSINE, SI_CHAN))
    else:
        # wrong direction... Transform needed
        print('Transform Needed')
        chansine = chansine.T  # signal transformed
        # now fft
        CHANSINE = []
        for channel in range(chanshape[1]):
            print(channel)
            # add fft here
            SI_CHAN = fft(chansine[channel])  # single channel
            if channel == 0:
                print("channel 0")
                CHANSINE = np.append(CHANSINE,SI_CHAN)
            else:
                print("channel >0")
                CHANSINE = np.vstack((CHANSINE, SI_CHAN))
    print(chanshape[0])
else:
    raise ValueError('not a valid number of dimensions')

F = np.arange(512)
F = np.append(np.arange(-512,0),F)

plt.figure()
for plotn in range(len(CHANSINE)):
    plt.plot(F, abs(CHANSINE[plotn]))
plt.show()
