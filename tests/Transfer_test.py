# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 14:32:59 2016

@author: enjbwink
"""

# transfer function test
# Signal out is signal for speaker. 
# Signal in1 is recorded by mic.
# Signal in2 is recorded + filter
# transfer function is:
#     in signal     in1    in2
# H = ---------- --> --- or ---
#     out signal     out    out

import numpy as np
import scipy.signal as sig
from scipy.fftpack import fft, fftshift, ifft
import matplotlib.pyplot as plt

f = np.array([20, 20000])  # [Hz] Frequency
fs = float(44100)  # [Hz] Sample rate/ Sample frequecy
t = np.arange(0.0, 1.0, 1.0/fs)  # [sec] Time
td = float(30)  # [mSec] Delay in milisec 10 - 50
ff = np.array([[250, 500], [8500, 10000]])


# (in) Signal sweep 20 - 20k
out = sig.chirp(t, f[0], t[-1], f[1], 'quadratic', 90.0)
noise = 1 / (2 ** 16) * np.random.rand(len(out))
out = out + noise

# new (out) signal
delsamp = 1 / (2 ^ 16) * np.random.rand(round(td * 10 ** (-3) * fs))
# noise = np.rand.rand(1, len(delsamp) + length(out)) * 1 / (2 ** 16)
in1 = np.append(delsamp, out)  # array 1 copy original
in2 = np.append(delsamp, out)  # array 1 copy original
in3 = np.append(delsamp, out)  # array 1 copy original
out = np.append(out, delsamp)
if len(in1) % 2 == 1:  # make signal even for FFT
    in1 = np.append(in1, 1 / (2 ^ 16)*np.random.rand(1))  # 1 partial adding
    in2 = np.append(in2, 1 / (2 ^ 16)*np.random.rand(1))
    in3 = np.append(in3, 1 / (2 ^ 16)*np.random.rand(1))
    out = np.append(out, 1 / (2 ^ 16)*np.random.rand(1))

t = np.arange(0, len(out) / fs, 1 / fs)

in2 = 2 * in2
# http://www.mathworks.com/matlabcentral/answers/33500-2nd-order-digital-butterworth-filter
# Filtering acc:
[B, A] = sig.butter(2, ff[0] / fs, 'bandstop')
in3 = np.transpose(sig.filtfilt(B, A, np.transpose(in3)))
[B, A] = sig.butter(4, (ff[1] * 2)/fs, 'bandstop')
in3 = np.transpose(sig.filtfilt(B, A, np.transpose(in3)))
[B, A] = sig.butter(2, 19000 * 2 / fs, 'lowpass')
in3 = np.transpose(sig.filtfilt(B, A, np.transpose(in3)))

F = np.arange(fs / (len(out) + 1), fs / 2, fs / (len(out) + 1))  # F = [0 F]  
# add zero for first signal

IN1 = fftshift(fft(in1))  # Nothing
IN2 = fftshift(fft(in2))  # Ampliefied
IN3 = fftshift(fft(in3))  # Filtered
OUT = fftshift(fft(out))

# Transfer function
H1 = IN1 / OUT  # nothing
H2 = IN2 / OUT  # Aamplified times 2
H3 = IN3 / OUT  # Filtered Signal


plt.figure()
plt.plot(t, out)  # hold all;
plt.plot(t, in2)
plt.plot(t, in3)
plt.xlim(0.95, 1.08)

plt.figure()
val = (len(IN1) / 2)
# IN1test = IN1[val::]
plt.subplot(2, 1, 1)
plt.semilogx(F, abs(IN1[val:]))
plt.semilogx(F, abs(IN2[val:]))
plt.semilogx(F, abs(IN3[val:]))
plt.semilogx(F, abs(OUT[val:]))
plt.subplot(2, 1, 2)
plt.semilogx(F, abs(H1[val:]))
plt.semilogx(F, abs(H2[val:]))  # Ampliefied times 2
plt.semilogx(F, abs(H3[val:]))
plt.xlim(1, 22.5*10**3)  # filtered


# Calculate ifft to check what is result of H(0)
IH1 = ifft(fftshift(H1))
IH2 = ifft(fftshift(H2))
IH3 = ifft(fftshift(H3))

plt.figure()
plt.plot(t, IH1)
plt.plot(t, IH2)
plt.plot(t, IH3)


#
# ---TEST-----------TEST------------TEST----------TEST----
#

H4 = OUT / fftshift(IN1)
plt.figure()
plt.plot(t, ifft(H4))  # hold all;

SIH3 = fftshift(ifft(H3))
ISH3 = ifft(fftshift(H3))

plt.figure()
# plt.plot(t, SIH3)# hold all;
plt.plot(t, ISH3)
