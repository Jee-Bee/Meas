# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 08:50:06 2015

@author: Jee-Bee for jBae (c) 2016
"""

import numpy as np
import scipy.signal as sig
from scipy.fftpack import fft
import matplotlib.pyplot as plt

T = 2  # [s] T= Time in seconds
f = (20, 20000)  # [Hz] Frequency signal generation
fs = 44100  # [Hz] fs = Samplerate

t = np.linspace(0, T - (1 / fs), T * fs)
sig = sig.chirp(t, 20, T, 20000, 'linear', 90)

# http://stackoverflow.com/questions/6916978/how-do-i-tell-matplotlib-to-create-a-second-new-plot-then-later-plot-on-the-o
# fig1=plt.figure()
# ax1 =fig1.add_subplot(111)
# ax1.plot(t, sig)

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.plot(t, sig)

SIG = fft(sig)
F = np.linspace(1/T, 22050, int(round(T * fs / 2)))
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.plot(F, abs(SIG[0:len(SIG)/2]))
