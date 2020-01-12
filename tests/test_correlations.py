# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 16:10:00 2016

@author: Jee-Bee for jBae (c) 2016
"""

import numpy as np
import matplotlib.pyplot as plt

# for info see: https://en.wikipedia.org/wiki/Cross-correlation
# for info see: https://en.wikipedia.org/wiki/Convolution
# for info see: https://en.wikipedia.org/wiki/Autocorrelation

# http://dsp.stackexchange.com/questions/736/how-do-i-implement-cross-correlation-to-prove-two-audio-files-are-similar
# http://dsp.stackexchange.com/questions/18233/solution-to-cross-correlation-problem-of-2-audio-signals

# http://nl.mathworks.com/help/signal/examples/measuring-signal-similarities.html

# Convolution  - Used for making filters (signal + set of impulse Responses)
# Deconvolution ( i understand for finding THD but i have to find out how)
# Cross - Correlation - Compare signals with each other
# Autocorrelation - Compare signals with itself (at different point in time)
# Coherence
# Cross-covariance - Cross correlation - mean value of f and g
# Autocovariance - Autocorrelation - mean value of f or g

def first_diff(sig):
    """
    First difference DFT name for 1st dirivative (Afgeleide)
    """
    dx = np.zeros(len(sig))
    dx[0] = sig[0]
    for idx in range(1, len(sig)):
        dx[idx] = sig[idx] - sig[idx - 1]
    return(dx)


def run_sum(sig):
    """
    Running sum DFT name for integral
    """
    rs = np.zeros(len(sig))
    rs[0] = sig[0]
    for idx in range(1, len(sig)):
        rs[idx] = sig[idx] + sig[idx - 1]
    return(rs)


N = 256
# Test for testing autocorrelation and cross correlation:


# Signal 1 Original (Simple pulse)
f = np.zeros(N)
b = np.ones(32)
posidx = 32
f[posidx - 1:posidx+len(b)-1] = b
#y[posidx + len(b) - 1:posidx + 2 * len(b) - 1] = -1 * b
x = np.arange(N)

# Signal 2 Simple triangle
# convsig = np.sin(np.linspace(0, np.pi, num=7, endpoint=True))
# 7 points sin wave
g = np.arange(len(b), 0, -1)/len(b)

# convolution
convsum = np.zeros((len(f), len(f) + len(g)))
for idx in range(len(f)):
    convsum[idx][idx:idx+len(g)] = f[idx] * g
convsum = np.sum(convsum, axis=0)
xc = np.arange(N+len(g))

convsig = np.convolve(f, g)

plt.figure()
plt.subplot(2, 1, 1)
plt.title('Convolution')
plt.plot(x, f, x[0:len(g)], g)
plt.subplot(2, 1, 2)
plt.plot(xc, convsum, xc[0:len(convsig)], convsig)

# Cross correlation
grev = np.flipud(g)
crosssum = np.zeros((len(f), len(f) + len(grev)))
for idx in range(len(f)-1, 0, -1):
    crosssum[idx][idx:idx+len(grev)] = f[idx] * grev
crosssum = np.sum(crosssum, axis=0)
xc = np.arange(N+len(grev))

crosssig = np.correlate(f, g)

plt.figure()
plt.subplot(2, 1, 1)
plt.title('Cross Correlation')
plt.plot(x, f, x[0:len(g)], grev)
plt.subplot(2, 1, 2)
plt.plot(xc, crosssum, xc[0:len(crosssig)], crosssig)

# Auto correlation
autosum = np.zeros((len(g), 2 * len(g)))
for idx in range(len(g)):
    autosum[idx][idx:idx+len(g)] = g[idx] * grev
autosum = np.sum(autosum, axis=0)
xc = np.arange(2 * len(g))
# works with square and according to wikipedia with triangle. 
# Not equal with convolution of numpy


autosig = np.correlate(g, g, mode='same')

plt.figure()
plt.subplot(2, 1, 1)
plt.title('Auto Correlation')
plt.plot(x, f, x[0:len(g)], g)
plt.subplot(2, 1, 2)
plt.plot(xc, autosum, xc[0:len(autosig)], autosig)

# http://greenteapress.com/thinkdsp/html/thinkdsp006.html
