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

##################################################
# Recover lines:
# remove line 15 - ...
# uncomment line:
# 49 - 61
# 89 - 103
# 119 - 127

import numpy as np
from scipy.io import wavfile
from scipy.fftpack import fft, fftshift
import matplotlib.pyplot as plt
from scripts.Window import *

# Vars
N = int(1024)
itt = int(2)
t = np.arange(0,N)

# Method
method = 'file' # options are 'signal' or 'file'
if method == 'signal':
    data_f = np.sin(2 * np.pi/N * 10 * t)  # Fit
    data_nf = np.sin(2 * np.pi/N * 10.3 * t+(45*np.pi/180))  # No fit 
    DATA_f = fftshift(fft(data_f))  # Fit
    DATA_nf = fftshift(fft(data_nf))  # No fit
    F = np.linspace(-N/2,N/2,N)
elif method == 'file':
    [fs,data] = wavfile.read("../09 Sample 15sec.wav")#,dtype=float)
    data_nf = data[2048:2048+N:]
    data_nf = np.reshape(np.delete(data_nf,0, 1),len(data_nf))
    DATA_nf = fftshift(fft(data_nf))  # No fit
    F = np.linspace(-N/2,N/2,N) #(0,N/2,N/2+1)


if method == 'signal':
    plt.figure()
    plt.subplot(3,1,1), plt.plot(t,data_f,t,data_nf)
    plt.title("time: 2 sines")
    plt.subplot(3,1,2), plt.stem(F,np.abs(DATA_f/N)), #plt.stem(np.linspace(-N/2,N/2,N),np.imag(SIN_f/N),'g')
    plt.title("Spectrum Fit - Absolut No Window")
    plt.subplot(3,1,3), plt.stem(F,np.abs(DATA_nf/N)), #plt.stem(np.linspace(-N/2,N/2,N),np.imag(SIN_nf/N), 'g')
    plt.title("Spectrum No Fit - Absolut No Window")
elif method == 'file':
    plt.figure()
    plt.subplot(2,1,1), plt.plot(t,data_nf)
    plt.title("time: wav file")
    plt.subplot(2,1,2), plt.stem(F,np.abs(DATA_nf/N)), #plt.stem(np.linspace(-N/2,N/2,N),np.imag(SIN_nf/N), 'g')
    plt.title("Spectrum No Fit - Absolut No Window")

#[wt,x] = Window.triwind(N)
[x,whan] = Window.hanwind(N) 
#[x,wcos] = Window.coswind(N)


S_1 = np.sum(whan)
S_2 = np.sum(whan**2)

NENBW = N * S_2/(S_1**2)
ENBW = fs * S_2/(S_1**2) # = NENBW * fs/N

print(NENBW, ENBW)

WIND_nf = fftshift(fft(data_nf*whan))
WIND_o =  fftshift(fft(whan))


plt.figure()
#plt.subplot(3,1,1), plt.plot(t,sinp,t,sinp*wt)
#plt.subplot(3,1,1), plt.plot(x,whan)
plt.subplot(3,1,1), plt.plot(x,whan)
plt.title("Window function")
plt.subplot(3,1,2), plt.stem(F,np.abs(DATA_nf/N)), plt.stem(F,np.abs(WIND_o/N), 'g')
plt.title("Spectrum No Fit - Absolut No Window & FFT Window")
plt.subplot(3,1,3), plt.stem(F,np.abs(WIND_nf/N)), #plt.stem(np.linspace(-N/2,N/2,N),np.imag(WIND_nf/N), 'g')
plt.title("Spectrum No Fit - Absolut with Window")


plt.figure()
plt.plot(F,20*np.log10(abs(DATA_nf)))
plt.plot(F,20*np.log10(abs(WIND_nf)))
plt.title("dB Spectrum No Window Vs. Windowed signal")

#now not volt_rms so PS, PSD, LS and LSD are just V and not V_rms
# PS_rms = 2 * np.abs(y_m)/S1 equation 23
PS_rms = 2 * np.abs(WIND_nf)/S_1

# PSD_rms = PS_rms/ENBW equation 24
PSD_rms = 2 * np.abs(WIND_nf)**2/(fs*S_2)

# LSD = sqrt(PSD)
LSD_rms = np.sqrt(PSD_rms) 

# LS = AS = sqrt(PS)
LS_rms = np.sqrt(PS_rms)

#plt.figure()
#plt.subplot(2,2,1), plt.plot(F,PS_rms)
#plt.title("PS")
#plt.subplot(2,2,2), plt.plot(F,PSD_rms)
#plt.title("PSD")
#plt.subplot(2,2,3), plt.plot(F,LS_rms)
#plt.title("LS = AS")
#plt.subplot(2,2,4), plt.plot(F,LSD_rms)
#plt.title("LSD = SD")


# test_window.py
# By Jee-Bee for jBae (c) 2016