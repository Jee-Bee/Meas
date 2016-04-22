# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 18:22:57 2016

@author: Jee-Bee for jBae (c) 2016
"""

import numpy as np
from scipy.signal import chirp, convolve, deconvolve # , hann # hanning window
from scipy.fftpack import fft, ifft
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D

fs = 44100
T = 10
ws = 0.1
t = np.arange(0, T, 1 / fs)

sig1k = 1 * np.sin(2 * np.pi * 1000 * t)

# 1k = 1
# 2K = 0.2
# 3K = 0.05
# 4K = 0.01
sig1kresp = 1 * np.sin(2 * np.pi * 1000 * t) + 0.2 * np.sin(2 * np.pi * 2000 * t
                    ) + 0.05 * np.sin(2 * np.pi * 3000 * t) + 0.01 * np.sin(2 * np.pi * 4000 * t)

SIG1K = fft(sig1k)
SIG1KRESP = fft(sig1kresp)
# Spectogram forwork
SIG1KRESPS = np.zeros([T / ws, fs * ws])
for idx in range(np.int(T/ws)):
    SIG1KRESPS[:][idx] = fft(sig1kresp[idx * (fs * ws): (idx+1) * (fs * ws)])
TS = np.arange(T / ws) * ws
FS = np.arange(fs * ws) / ws
FS, TS = np.meshgrid(FS, TS)
fig1 = plt.figure()
ax1 = fig.add_subplot(111, projection="3d")
ax1.plot_surface(TS, FS, np.abs(SIG1KRESPS), cmap="autumn_r", lw=0.5, rstride=1, cstride=1)

# F = np.arange(-fs / 2, fs / 2, 1 / T)
F = np.arange(0, fs, 1 / T)

#from scipy import fftpack
#from scipy import signal

deconvolved1kq, deconvolved1kr,= deconvolve(sig1k[1::], sig1kresp[1::])
#convolve()

plt.figure()
plt.plot(t, sig1k, t, sig1kresp)
#plt.axis([T-1, T,])
plt.xlim(0, 0.2)

plt.figure()
plt.plot(F, np.abs(SIG1K), F, np.abs(SIG1KRESP))
plt.xlim(0, fs / 2)


#plt.figure()
#plt.plot(t[:-1:], deconvolved1kr)
#plt.axis([T-1, T,])
#plt.xlim(0, 0.2)`


# ----------------- Sweep -------------------------------------
#sig = chirp(t, 20 ,T,1000)


# ----------------- Temp --------------------------------------
# http://stackoverflow.com/questions/35445424/surface-and-3d-contour-in-matplotlib
#fig = plt.figure()
#ax = fig.add_subplot(111, projection="3d")
#X, Y = np.mgrid[-2:2:60j, -1:1:30j]
#Z = np.sin(np.pi*X)*np.sin(np.pi*Y)
#ax.plot_surface(X, Y, Z, cmap="autumn_r", lw=0.5, rstride=1, cstride=1)