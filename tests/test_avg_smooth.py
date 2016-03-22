# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 10:34:31 2016

@author: Jee-Bee for jBae (c) 2016
"""
import numpy as np
from scipy.fftpack import fft, fftshift
import scipy.signal as sig
import matplotlib.pylab as plt

# Simple Moving Averege
# https://en.wikipedia.org/wiki/Moving_average
#       1   P_m + P_(m-1) + ... P_(m-(n-1))   1   n-1
# SMA = - * ------------------------------- = -   SUM p_(m-i)
#       n                 n                   n   i=0

# http://people.duke.edu/~rnau/411avg.htm
# https://en.wikipedia.org/wiki/Exponential_smoothing


def sma(x,npa):
    sma = np.zeros(len(x))    
    if int(npa) % 2 == 0 :
        npa = int(npa-1)
    for idx1 in range(len(x)):  # calculate mean/ average
        npasum = 0
        for idx2 in range(int(npa)):  # check for zeros
            npaidx = idx2 - np.floor(npa/2)
            if (idx1 + npaidx) <0:             
                npasum = npasum + 0
            elif (idx1 + npaidx) >=len(x):
                npasum = npasum + 0
            else:
                npasum = npasum + x[idx1+npaidx]
        sma[idx1]= npasum/npa
    return (sma)

N = 1024
t = np.arange(0,1,1/N)
f0 = 1
f1 = 100

sig = sig.chirp(t, f0, 1, f1, 'linear',90)
SIG = fftshift(fft(sig))
F = np.linspace(-N/2,N/2,N)

AVGR = sma(np.real(SIG),0.05*len(sig))
AVGI = sma(np.imag(SIG),0.05*len(sig))


plt.figure()
plt.subplot(3,1,1), plt.plot(t,sig)
plt.subplot(3,1,2), plt.stem(F,np.real(SIG/N))
plt.subplot(3,1,2), plt.stem(F,np.imag(SIG/N),'g')
plt.subplot(3,1,3), plt.stem(F,AVGR/N)
plt.subplot(3,1,3), plt.stem(F,AVGI/N,'g')


###################################################################
# Frome here test values

#a = np.array([2.,3.,1.,2.,2.,3.,1.,3.,1.,1.])
#smaval = sma(a,3)
#smahand = np.array([5./3, 6./3, 6./3, 5./3, 7./3, 6./3, 7./3, 5./3, 5./3, 2./3])
#
#for idx in range(len(smaval)):
#    print(smaval[idx], smahand[idx])


