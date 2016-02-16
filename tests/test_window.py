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
from scipy.io import wavfile
from scipy.fftpack import fft, fftshift
import matplotlib.pylab as plt

# B slpine Windows:
# Rectangular: k = 1 (st order)
# Triangular: k = 2 (nd Order)
# Parzen: k = 4 (th order)

def rectwind(N):
    w = np.ones(N)
    x = np.arange(0,N-1,1)
    return(w,x)

def triwind(N):
    w=np.zeros(N)
    x=np.zeros(N)
    for idx in range(N):
        w[idx] = 1-abs((idx-((N-1)/2))/(N/2))
        x[idx] = idx
    return (w,x)

def partzwind(N):
    w=np.zeros(int(N/2))
    x=np.zeros(int(N/2))
    for idx in range(int(N/2)):
        x[idx] = idx
        if (idx >= 0) and (idx <= (N/4)):
            w[idx] = 1-(6*(idx/(N/2))**2) * (1- abs(idx)/(N/2))
        elif(idx >= N/4) and (idx <= (N/2)):
            w[idx] = 2*(1- abs(idx)/(N/2))**3
    x = np.append(x,x +int(N/2));
    w = np.append(w[::-1],w)
    return (x,w)
##    if (idx < 3) == True:

#
# -----------------------------------------------------------------------------
#

def genhamwind(N,alpha,beta):
    w=np.zeros(N)
    x=np.zeros(N)
    for idx in range(N):
        w[idx] = alpha - beta * np.cos((2*np.pi*idx)/(N-1))
        x[idx] = idx
    return (x,w)

def hanwind(N):
    alpha = beta = 0.5
    [x,w] = genhamwind(N,alpha,beta)
    return (x,w)

def hamwind(N):
    alpha =  0.53836
    beta = 1 - alpha
    [x,w] = genhamwind(N,alpha,beta)
    return (x,w)

#
# -----------------------------------------------------------------------------
#

def coswind (N):
    w = np.zeros(N)
    x = np.zeros(N)
    alpha = 1  # rectangular window alpha = 0; cos window alpha = 1; Hann window alpha =2.
    for idx in range(N):
        w[idx] = np.cos((np.pi * idx/(N-1)) - np.pi/2)**alpha
        x[idx] = idx
    return (x,w)

#
# -----------------------------------------------------------------------------
#

def gengausswind(N,sigma,p): 
    w = np.zeros(N)
    x= np.zeros(N)
    for idx in range(N):
        num = idx-(N-1)/2
        denum = sigma*(N-1)/2
        w[idx] = np.e**((-1/2)*( num/denum )**p )
        x[idx] = idx
    return (x,w)

def gausswind(N): 
    sigma = 0.5
    p = 2
    [x,w] = gengausswind(N,sigma,p)
    return (x,w)

#
# -----------------------------------------------------------------------------
#

def Tukeywind (N):
    w = np.zeros(N)
    x = np.zeros(N)
    alpha = 0.5
    for idx in range(N):
        if idx <= int(alpha*(N-1)/2):
            w[idx] = 1/2*(1 + np.cos(np.pi*(2*idx/(alpha * (N-1)) -1) ) )
            x[idx] = idx
        elif idx >= int(alpha*(N-1)/2) and idx <= int((N-1)*(1-alpha/2)):
            w[idx] = 1
            x[idx] = idx
        elif idx >= int((N-1)*(1-alpha/2)) and idx <= (N-1):
            w[idx] = 1/2*(1 + np.cos(np.pi*(2*idx/(alpha * (N-1)) - 2/alpha + 1) ) )
            x[idx] = idx
    return (x,w)


#
# -----------------------------------------------------------------------------
#

# Vars
N = int(1024/8)
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

#sig = np.sin (2 * np.pi/N * 2 * t)
#rand = np.random.uniform(1,-1,N)
#sig = 0.75*sig + 0.25* rand

#plt.figure()
#plt.plot(t,sig)

#N = 256

[wt,x] = triwind(N)
[x,whan] = hanwind(N)
[x,wcos] = coswind(N)

S_1 = np.sum(hanwind)
S_2 = np.sum(hanwind**2)

NENBW = N * S_2/(S_1**2)
ENBW = fs * S_2/(S_1**2)

print(NENBW, ENBW)

WIND_nf = fftshift(fft(data_nf*whan))
WIND_o =  fftshift(fft(whan))

plt.figure()
#plt.subplot(3,1,1), plt.plot(t,sinp,t,sinp*wt)
#plt.subplot(3,1,1), plt.plot(x,whan)
plt.subplot(3,1,1), plt.plot(x,whan)
plt.title("Window function")
plt.subplot(3,1,2), plt.stem(np.linspace(-N/2,N/2,N),np.abs(DATA_nf/N)), plt.stem(np.linspace(-N/2,N/2,N),np.abs(WIND_o/N), 'g')
plt.title("Spectrum No Fit - Absolut No Window & FFT Window")
plt.subplot(3,1,3), plt.stem(np.linspace(-N/2,N/2,N),np.abs(WIND_nf/N)), #plt.stem(np.linspace(-N/2,N/2,N),np.imag(WIND_nf/N), 'g')
plt.title("Spectrum No Fit - Absolut with Window")


plt.figure()
plt.plot(np.linspace(-N/2,N/2,N),20*np.log10(abs(DATA_nf)))
plt.plot(np.linspace(-N/2,N/2,N),20*np.log10(abs(WIND_nf)))
plt.title("dB Spectrum No Window Vs. Windowed signal")