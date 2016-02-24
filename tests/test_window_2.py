# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 10:34:31 2016

@author: Jee-Bee for jBae (c) 2016
"""

# used documents...
# Spectrum and spectral density estimation by the Discrete Fourier
# transform (DFT), including a comprehensive list of window
# functions and some new at-top windows.
# (is 395068.pdf)
# wikipedia for functions

import numpy as np
#from scipy.io import wavfile
from scipy.fftpack import fft, fftshift
import scipy.stats as stat
import matplotlib.pylab as plt
import Window_1 as wind  # 2 possible error depend on lokation file
# For testing make copy of window function. Otherwise one of the following
#   Errors occure
# ImportError: No module named 'scripts'
# AttributeError: 'module' object has no attribute 'hanwind'
# SystemError: Parent module '' not loaded, cannot perform relative import


# Vars
fs = 10000.  # Sampling FRequency [Hz]
f1 = 1234.  # First Signal Frequency [Hz]
Amp1 = 2 * np.sqrt(2)  # 2Vrms
f2 = 2500.2157  # SEcond signal Frequency [Hz]
Amp2 = 1.  # 0.707 Vrms
ulsb = 1e-3  # Value of 1 LSB in V
t = u = ur = []

for idx in range(100000):
    t = np.append(t, idx / fs)
    u = np.append(u, Amp1 * np.sin(2 * np.pi * f1 * t[idx]) + Amp2 * np.sin(2 * np.pi * f2 * t[idx]))
    ur = np.append(ur, np.floor(u[idx] / ulsb + 0.5) * ulsb)  # Rounding

udig = ulsb / np.sqrt(6 * fs)

# Method from spectrum and spectral desnity ... see top
# 1. Compute the average ...
ur_avg = np.sum(ur) / len(ur)
ur = ur - ur_avg
# 2. Compute a straight line between the first and last data point..
ur_line = np.linspace(-ur[0], -ur[-1], len(ur))
ur = ur - ur_line
# 3. Compute an average trend via linear regression
slope, intercept, r_value, p_value, std_err = stat.linregress(t, ur)
# http://central.scipy.org/item/16/2/basic-linear-regression
predict_ur = intercept + slope * t
ur = ur - predict_ur

# @ 2DO
# @@ Edit to formula equation 9 (page 8)
# @@@ Change afterwards to function within FFT
fres = 100
N = fs / fres
# N = see: Spectrum and spectral density estimation by the DDFT ... Ch 12
if N % 1 != 0:
    np.round(N)
    fres = fs/N
# Don't plot time... not importand for now.!!

wt = wind.Window(N)
(x, wt) = wt.triwind()
wn = wind.Window(N)
(x, whan) = wn.hanwind()
# (x, whan) = Window.Window.hanwind(N)
# [x, wcos] = Window.coswind(N)

S_1 = np.sum(whan)
S_2 = np.sum(whan ** 2)
#
NENBW = N * S_2 / (S_1**2)
ENBW = fs * S_2 / (S_1**2)  # = NENBW * fs/N

print(NENBW, ENBW)

# widx = 0
# while (widx * N) <= len(u):

# 4. Compute the average of each segment (before applying the window function) and subtract
# that average from the data points.


# 5. Compute a straight line between the first and last data point of each segment (before
# applying the window function) and subtract that line from the data points.


# 6. Compute an average trend via linear regression of each segment (before applying the
# window function) and subtract that line from the data points.


# 7. Pass the input time series through a digital high-pass filter.

# MWIND_nf = np.zeros((N, itt))
# MWIND_nf = np.rot90(MWIND_nf)
#
# for idx in range(1, itt+1):
#    idxlow = (idx-1)*N
#    idxup = (idx*N)-1
#    MWIND_nf[idx-1] = fftshift(fft(data_nf[(idx-1)*N:(idx*N):]*whan))
# MWIND_nf = np.rot90(MWIND_nf, 3)

# ## Implement Later!! First read Paper
# whan_ls = np.zeros((len(data_nf), itt))  # Long signal
# for idx in range(itt):
# #    whan_ls[idx * N:(idx+1) * N:][idx] = whan
#    whan_ls[(idx*N):((idx+1) * N), idx] = whan
# whan_ls =np.sum(whan_ls, axis=1)
# #MWIND_ls = fftshift(fft(data_nf[(idx-1) * N:(idx * N):] * whan))

# itt1 = data_nf[0:N:]
# square3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# WIND_nf = fftshift(fft(data_nf * whan))
# WIND_o =  fftshift(fft(whan))

#
# plt.figure()
# plt.subplot(3, 1, 1), plt.plot(x, whan)
# plt.title("Window function")
# plt.subplot(3, 1, 2), plt.stem(np.linspace(-len(DATA_nf) / 2, len(DATA_nf) / 2, len(DATA_nf)), np.abs(DATA_nf / N)), 
# plt.stem(F,np.abs(WIND_o/N), 'g')
# plt.title("Spectrum No Fit - Absolut No Window & FFT Window")
# plt.subplot(3, 1, 3), plt.stem(F, np.abs(MWIND_nf.T[0] / N)), plt.stem(F, np.abs(MWIND_nf.T[1] / N), 'g')
# plt.title("Spectrum No Fit - Absolut with Window")

# #now not volt_rms so PS, PSD, LS and LSD are just V and not V_rms
# # PS_rms = 2 * np.abs(y_m) / S1 equation 23
# PS_rms = 2 * np.abs(WIND_nf) / S_1

# # PSD_rms = PS_rms/ENBW equation 24
# PSD_rms = 2 * np.abs(WIND_nf)**2/(fs*S_2)

# # LSD = sqrt(PSD)
# LSD_rms = np.sqrt(PSD_rms)

# # LS = AS = sqrt(PS)
# LS_rms = np.sqrt(PS_rms)

# plt.figure()
# plt.subplot(2, 2, 1), plt.plot(F, PS_rms)
# plt.title("PS")
# plt.subplot(2, 2, 2), plt.plot(F, PSD_rms)
# plt.title("PSD")
# plt.subplot(2, 2, 3), plt.plot(F, LS_rms)
# plt.title("LS = AS")
# plt.subplot(2, 2, 4), plt.plot(F, LSD_rms)
# plt.title("LSD = SD")


# test_window.py
# By Jee-Bee for jBae (c) 2016
