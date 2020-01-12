# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 12:46:06 2016

@author: Jee-Bee for jBae (c) 2016
"""

import numpy as np
from scipy import signal
from scipy.fftpack import fft, fftshift, fftfreq
import matplotlib.pyplot as plt

f0 = 20  # frequency start
f1 = 10000  # frequency end
fs = 44100  # frequency sample
T = 5  # time max
t = np.arange(0, T*fs)/fs  # time array

# Define Window length and window:
factor_f = fs/f1  # factor fs/f1
T = T - (np.ceil(factor_f) + 1) / fs

# x = signal.chirp(t, f0, T, f1, 'log', 90)
x = np.sin(2 * np.pi * 100 * t) + 0.7 * np.sin(2 * np.pi * 880 * t) + 0.2 * np.sin(2 * np.pi * 2400 * t)

bitDept = 16
phi = (f0 * (f1 / f0) ** (t[-4:] / T)) % np.pi
#if all phi >= -1/(2 ** (bitDepth - 1 - 4)) and all phi <= 1/(2 ** (bitDepth - 1 - 4)):

if factor_f < 2:
    # print error
    pass
elif round(factor_f, 0) < 3:
    wl = 2  # window lenght
    overlap = 0.5
    W = signal.get_window('hanning', wl)  # window
elif round(factor_f, 0) < 6:
    wl = 4  # window lenght
    overlap = 0.5
    W = signal.get_window('hanning', wl)  # window
elif round(factor_f, 0) < 13:
    wl = 8  # window lenght
    overlap = 0.5
    W = signal.get_window('hanning', wl)  # window
else:
    wl = 16  # window lenght
    overlap = 0.5
    W = signal.get_window('hanning', wl)  # window

# worked make this concept working in main scripts of signal generators
# except use internal windwo against scipy window for now.
Wx = np.zeros(len(x))
#ul = wl
## loop added for window
#dsample = len(x) % wl  # delta in samples between mod (x/windw length)
#if dsample == 0:
#    nEntries = len(Wx)
#    step = int(wl * overlap)
#    while ul <= nEntries:
#        Wx[ul-wl:ul] += x[ul-wl:ul] * W
#        ul += step
#    Wx = np.append(Wx, 0)
#else:
#    x = np.append(x, np.zeros(wl - dsample))
#    nEntries = len(Wx)
#    step = int(wl * overlap)
#    while ul <= nEntries:
#        Wx[ul-wl:ul] += x[ul-wl:ul] * W
#        ul += step
#    Wx = np.append(Wx, 0)

# using numpy.nditer

dsample = len(x) % wl  # delta in samples between mod (x/windw length)
if dsample == 0:
    ul = np.arange((len(x) - (wl - 1)) / 2) * 2
    it = np.nditer(np.int_(ul), flags=['buffered'], casting='same_kind')  # , 'external_loop'])
    for idx in it:
        Wx[idx:idx + wl] += x[idx:idx + wl] * W
    Wx = np.append(Wx, 0)
else:
    x = np.append(x, np.zeros(wl - dsample))
    ul = np.arange((len(x) - (wl - 1)) / 2) * 2
    it = np.nditer(np.int_(ul), flags=['buffered'], casting='same_kind')  # , 'external_loop'])
    for idx in it:
        Wx[idx:idx + wl] += x[idx:idx + wl] * W
    Wx = np.append(Wx, 0)

# Conclusion:
# becouse nditer makes arrays of 1 value it takes more time as with plain loop!

# NFFT for Pro's:
# Because of the above relationship it is convenient to have N even, as we do assume throughout
# this report. Some subroutine packages even demand that N be a power of 2. That is, however,
# an unnecessarily stringent limitation in many situations. The FFTW package, for example, will
# compute the DFT for any positive integer N , and with high efficiency for integers of the form
# N = 2 a 3 b 5 c 7 d 11 e 13 f ,          (9)
# where e + f is either 0 or 1 and the other exponents are arbitrary.

# Frequency spectrums with NFFT and diferent names (13.152 seconds)
# NFFT = np.int(2 ** np.ceil(np.log2(len(x))))
# NFFW = np.int(2 ** np.ceil(np.log2(len(Wx))))
# X = fft(x, NFFT)
# WX = fft(Wx, NFFW)

# Frequency spectrums with NFFT and same name (13.121 seconds - 13.504 seconds)
NFFT = np.int(2 ** np.ceil(np.log2(len(x))))
X = fft(x, NFFT)
NFFT = np.int(2 ** np.ceil(np.log2(len(Wx))))
WX = fft(Wx, NFFT)

# Frequency spectrums no NFFT (27.034 seconds)
# X = fft(x)
# WX = fft(Wx)
# Conclusion without NFFT (Next number off FFT) loop much slower renamening
# don't do much around the same speed.


# if len(t) < 10000:
#     # mpl.RcParams()
#     plt.rcParams['agg.path.chunksize'] = 2 ** 16
#
# plt.figure()
# plt.plot(t, x)
# plt.plot(t[-10000:], x[-10000:])
# plt.plot(t[-10000:], Wx[-10000:])

# plt.figure()
# # plt.plot(t, x)
# plt.plot(t[:10000], x[:10000])

# plt.figure()
# # plt.plot(t, x)
# plt.plot(W)

# fft signals
# plt.figure()
# plt.semilogx(np.abs(X))
# plt.semilogx(np.abs(WX))
# plt.plot(np.abs(X))
# plt.plot(np.abs(WX))

# Window length frequency band
# fs = 192000
# n = np.arange(10)
# wl = 2 ** n  # window length
# Tw = wl/fs  # time length Window
# freq = 1/Tw
# print(n, wl, freq)
