# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 14:32:59 2016

@author: Jee-Bee for jBae (c) 2016
"""

# transfer function test
# Signal out is signal for speaker. 
# Signal in1 is recorded by mic.
# Signal in2 is recorded + filter
# transfer function is:
#     in signal     in1    in2
# H = ---------- --> --- or ---
#     out signal     out    out


# http://www.mathworks.com/matlabcentral/answers/33500-2nd-order-digital-butterworth-filter
# Filtering acc:
# [B, A] = sig.butter(2, ff[0] / fs, 'bandstop')
# in3 = np.transpose(sig.filtfilt(B, A, np.transpose(in3)))
# [B, A] = sig.butter(4, (ff[1] * 2)/fs, 'bandstop')
# in3 = np.transpose(sig.filtfilt(B, A, np.transpose(in3)))
# [B, A] = sig.butter(2, 19000 * 2 / fs, 'lowpass')
# in3 = np.transpose(sig.filtfilt(B, A, np.transpose(in3)))

# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 19:34:55 2016

@author: winkelk
"""
import numpy as np
from scipy.fftpack import fft
from scipy.signal import chirp
from scripts import Transform
import matplotlib.pylab as plt

N = 64
t = np.arange(0, 1, 1 / N)
x = chirp(t, 1, 1, 8, phi=90)
y = 2 * np.sin(2 * np.pi * 4 * t) + 0.707 * np.sin(2 * np.pi * 6 * t)

X = fft(x)
Y = fft(y)
F = np.arange(-N/2+1, N/2+1)

Xr = np.real(X)
Xi = np.imag(X)
Yr = np.real(Y)
Yi = np.imag(Y)

# From here test\
# for now just real and imag or complex.
# next step also Magnitude and phase

# Most Needed Function is not finished...

# X_in = x, X_out = complex
H0_1_val = Transform.Transfer(x, Y, N)

# X_in = tuple, X_out = complex
H0_2_val = Transform.Transfer((Xr, Xi), Y, N)

# X_in = complex, X_out = tuple
H0_3_val = Transform.Transfer(X, (Yr, Yi), N)
# Fix Odd symmetry check

plt.plot(F,abs(X))

plt.figure()
plt.plot(t,x,t,y)
plt.figure()
plt.plot(F,abs(X))
plt.plot(F,np.real(X),F,np.imag(X))
plt.figure()
plt.plot(F, H0_1, F, H0_2, F, H0_3)


#
# ---TEST-----------TEST------------TEST----------TEST----
#

#H4 = OUT / fftshift(IN1)
#plt.figure()
#plt.plot(t, ifft(H4))  # hold all;
#
#SIH3 = fftshift(ifft(H3))
#ISH3 = ifft(fftshift(H3))
#
#plt.figure()
## plt.plot(t, SIH3)# hold all;
#plt.plot(t, ISH3)
