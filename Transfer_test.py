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

#
#
#
#import numpy as np
#from scipy.fftpack import fft
#from scipy.signal import chirp
#from scripts import Transform
#import matplotlib.pylab as plt
#
#N = 64
#t = np.arange(0, 1, 1 / N)
#x = chirp(t, 1, 1, 8, phi=90)
#y = 2 * np.sin(2 * np.pi * 4 * t) + 0.707 * np.sin(2 * np.pi * 6 * t)
#
#X = fft(x)
#Y = fft(y)
#F = np.arange(-N/2+1, N/2+1)
#
#Xr = np.real(X)
#Xi = np.imag(X)
#Yr = np.real(Y)
#Yi = np.imag(Y)
#
## From here test\
## for now just real and imag or complex.
## next step also Magnitude and phase
#
## Most Needed Function is not finished...
#
## X_in = x, X_out = complex
#H0_1_val = Transform.Transfer(x, Y, N)
#
## X_in = tuple, X_out = complex
#H0_2_val = Transform.Transfer((Xr, Xi), Y, N)
#
## X_in = complex, X_out = tuple
#H0_3_val = Transform.Transfer(X, (Yr, Yi), N)
## Fix Odd symmetry check
#
#plt.plot(F,abs(X))
#
#plt.figure()
#plt.plot(t,x,t,y)
#plt.figure()
#plt.plot(F,abs(X))
#plt.plot(F,np.real(X),F,np.imag(X))
#plt.figure()
#plt.plot(F, H0_1_val, F, H0_2_val, F, H0_3_val)
#
#


#
# ----- Part 2 of test
#

from scripts import Transform, Window, DefaultFigures
import numpy as np
from scipy.signal import chirp
import sounddevice as sd
import matplotlib.pylab as plt

# signal generation
# allready exist
N = 2 ** 16
fs = 2 ** 12
overlap = 50  # [%]
t = np.arange(0, N / fs, 1 / fs)
x = chirp(t, 20, N / fs - 1 / fs, 2000, phi=90)
x = np.append(x, np.zeros(fs))  # silece for tail of real live sound

y = sd.playrec(x, samplerate=fs, channels=1)
sd.wait()
y = np.reshape(y, len(y))
# averaging multiple signals
# pass  # for later on


# window + multi fft
Nw = fs
hannw = Window.Window(Nw)
(dummy, hann) = hannw.hanwind()

S_1 = np.sum(hann)
S_2 = np.sum(hann ** 2)
NENBW = Nw * S_2 / (S_1 ** 2)
ENBW = fs * S_2 / (S_1 ** 2)  # = NENBW * fs/N

print(NENBW, ENBW)

overlap = overlap/100 *Nw
idxl = 0
idxu = Nw
Y = []
while idxu <= len(y):
    (F, Yd) = Transform.FFT(y[idxl:idxu] * hann, fs)
    Y = np.concatenate((Y, Yd), axis=0)
    #(F, Y) = np.append(Y, Transform.FFT(y[idxl:idxu] * hann,fs), axis=1)
    idxl += (Nw - overlap)
    idxu += (Nw - overlap)
Y /= S_1
Y = np.reshape(Y,(Nw,len(Y)/Nw))
(m, n) = np.shape(Y)
twind = np.arange(0,16.5,0.5)

## Later on fix
## now not volt_rms so PS, PSD, LS and LSD are just V and not V_rms 
## PS_rms = 2 * np.abs(y_m)/S1 equation 23
#PS_rms = 2 * np.abs(WIND_nf)/S_1
#
## PSD_rms = PS_rms/ENBW equation 24
#PSD_rms = 2 * np.abs(WIND_nf)**2/(fs*S_2)


# spectogram
#DefaultFigures.Default3D(Y, F, twind)
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D
plt.figure()
#spectfig = DefaultFigures.default3D(twind, F, Y)
#spectfig.Spect()
Axes3D.plot_surface(twind, F, abs(Y))

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
