# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 20:39:45 2016

@author: Jee-Bee for jBae (c) 2016
"""
import numpy as np
import matplotlib.pylab as plt
from scipy.io import wavfile

def findPeak(data, m=None, itt=4, nf=60):
    """Inputs:
        data:
        m:
        itt:
        nf: Noise floor in dB
    Outputs:
        Peak:
    
    description:
    """
    if m is None:
        for idx in range(itt):
            if idx == 0:
                peak = (data > np.roll(data, 1)) & (data > np.roll(data, -1)) & (data > 10**(-nf/20))
            else:
                peak[peak] = (data[peak] > np.roll(data[peak], 1)) & (data[peak] > np.roll(data[peak], -1))
    else:
        for idx in range(itt):
            if idx == 0:
                peak = ((data - np.roll(data, 1)) > m) & ((data - np.roll(data, -1)) > m) & (data > 10**(-nf/20))
            else:
                peak[peak] = ((data[peak] - np.roll(data[peak], 1)) > m) & ((data[peak] - np.roll(data[peak], -1)) > m)
        peak = ((data - np.roll(data, 1)) > m) & ((data - np.roll(data, -1)) > m)
        return(peak)

fs, IR_wav = wavfile.read("ir1_-_ir_masseria_gloria.wav")
IR_wav = IR_wav.astype(float)/(2**15)
t_wav = np.arange(len(IR_wav))/fs

# delay estamation
# make impulse like signal
# Create 2 time points and level difference
T = 0.5
T_i = np.array([0.1, 0.35])  # time between max and min value
lev_adj = 60  # in dB level lowering mostly -60 -30 or -20
fs = 44100 # [Hz] Sample Frequency



# noise floor = -96 dB
# 20 * log10(x/y) = -96(n) so 10^(-96/20) = x/y and x/y = z
# y = 1 dus z = x
IR_curve = np.ones(np.round(T*fs))*10**(-96/20)
T_i = np.ndarray.astype(np.round(T_i*fs), int)
IR_curve[T_i[0]:T_i[1]] = np.linspace(1, 10**(-96/20), T_i[1] - T_i[0], endpoint=False)

# IR Parameters see..
# http://www.openairlib.net/category/generation-type/real-world
# Source Sound: Paper banger
# Microphone: Zoom H1 build in X/Y unidirection microphones
# Source Receiver Distance (m): 15 m
# Source Height: 1.1 m
# Receiver Height: 1.1 m
# Temperature: 5 °C
IR = (np.random.rand(np.round(T*fs))* 2 - 1) * IR_curve
t = np.arange(T*fs)/fs

# plot IR
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.plot(t_wav, IR_wav)


fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.plot(t,20*np.log10(abs(IR)))


# find peaks
# http://stackoverflow.com/questions/22583391/peak-signal-detection-in-realtime-timeseries-data
# Peakutils python package

# simple form extend to more complicated...
#import numpy as np
#import matplotlib.pyplot as plt
input = np.array([ 1. ,  1. ,  1. ,  1. ,  1. ,  1. ,  1. ,  1.1,  1. ,  0.8,  0.9,
    1. ,  1.2,  0.9,  1. ,  1. ,  1.1,  1.2,  1. ,  1.5,  1. ,  3. ,
    2. ,  5. ,  3. ,  2. ,  1. ,  1. ,  1. ,  0.9,  1. ,  1. ,  3. ,
    2.6,  4. ,  3. ,  3.2,  2. ,  1. ,  1. ,  1. ,  1. ,  1. ])
signal = (input > np.roll(input,1)) & (input > np.roll(input,-1))
signal2 = ((input - np.roll(input,1)) > 0.5) & ((input - np.roll(input,-1)) > 0.5)
fig3 = plt.figure()
ax3 = fig3.add_subplot(111)
ax3.plot(input)
ax3.plot(signal.nonzero()[0], input[signal], 'ro')
ax3.plot(signal2.nonzero()[0], input[signal2], 'bo')
ax3.legend(["signal", "Peak all", "Peak >0.5"])
fig3.show()


# calculate lowest point of peaks
IR_signal = (IR > np.roll(IR,1)) & (IR > np.roll(IR,-1)) & (IR > 10**(-90/20))
IR_signal2 = ((IR - np.roll(IR,1)) > 0.5) & ((IR - np.roll(IR,-1)) > 0.5)
# positive values only
IR_signal3 = ((IR - np.roll(IR,1)) > 0.55) & ((IR - np.roll(IR,-1)) > 0.55) & (IR > 0)

# wav peak detection
wav_peak = (IR_wav > np.roll(IR_wav,1)) & (IR_wav > np.roll(IR_wav,-1)) & (IR_wav > 10**(-60/20))
wav_peak2 = ((IR_wav - np.roll(IR_wav,1)) > 0.5) & ((IR_wav - np.roll(IR_wav,-1)) > 0.5)
# positive values only
wav_peak3 = ((IR_wav - np.roll(IR_wav,1)) > 0.55) & ((IR_wav - np.roll(IR_wav,-1)) > 0.55) & (IR_wav > 0)


wav_peak_double = np.copy(wav_peak)
wav_peak_double[wav_peak] = (IR_wav[wav_peak] > np.roll(IR_wav[wav_peak],1)) & (IR_wav[wav_peak] > np.roll(IR_wav[wav_peak],-1))
wav_peak_triple = np.copy(wav_peak_double)
wav_peak_triple[wav_peak_double] = (IR_wav[wav_peak_double] > np.roll(IR_wav[wav_peak_double],1)) & (IR_wav[wav_peak_double] > np.roll(IR_wav[wav_peak_double],-1))
wav_peak_quatro = np.copy(wav_peak_triple)
wav_peak_quatro[wav_peak_triple] = (IR_wav[wav_peak_triple] > np.roll(IR_wav[wav_peak_triple],1)) & (IR_wav[wav_peak_triple] > np.roll(IR_wav[wav_peak_triple],-1))

# function usage!!
wav_peak_func = findPeak(IR_wav, 0.25)
# With and without m works both

print(np.count_nonzero(wav_peak), np.count_nonzero(wav_peak_double), np.count_nonzero(wav_peak_triple), np.count_nonzero(wav_peak_quatro))

# http://stackoverflow.com/questions/4098131/how-to-update-a-plot-in-matplotlib
# http://stackoverflow.com/questions/38765173/matplotlib-add-plot-to-existing-figure - post reaction if answered mine
# ax1.plot(IR_signal2.nonzero()[0],IR[IR_signal2],'ro')
#ax1.plot(wav_peak.nonzero()[0]/fs,IR_wav[wav_peak],'ro')
#fig1.canvas.draw()

# http://stackoverflow.com/questions/8213522/matplotlib-clearing-a-plot-when-to-use-cla-clf-or-close
ax2.cla() # clear axis
ax2.plot(t_wav, IR_wav)
ax2.plot(wav_peak.nonzero()[0]/fs,IR_wav[wav_peak],'r+')
ax2.plot(wav_peak_double.nonzero()[0]/fs,IR_wav[wav_peak_double], 'ro')
ax2.plot(wav_peak_triple.nonzero()[0]/fs,IR_wav[wav_peak_triple], 'go')
ax2.plot(wav_peak_quatro.nonzero()[0]/fs,IR_wav[wav_peak_quatro], 'ko')
ax2.legend(["signal", "Peak all", "2nd itteration", "3th itt", "4th itt"])
fig2.canvas.draw()


# Curve plotting

# polynomal calculations
curve = np.polyfit(wav_peak_quatro.nonzero()[0]/fs,IR_wav[wav_peak_quatro],1)

polyvals = np.polyval(curve, IR_wav[wav_peak_quatro])


plt.figure()
plt.plot(polyvals)

# calculate delay

# Resample

import numpy as np
from scipy.signal import *
import matplotlib.pyplot as plt

#fs=44100
#t=np.arange(3*fs)/fs
#
#a = chirp(t,12000,2.99,20000)
#b= resample(a, 4*len(a))
#
#t1 = np.arange(len(b))/(4*fs)
#
#
#plt.figure()
#if len(t) > 100000:
#        # mpl.RcParams()
#        plt.rcParams['agg.path.chunksize'] = 10000
#plt.plot(t,a)
#plt.plot(t1,b)

IR_wav_over= resample(IR_wav, 8*len(IR_wav))
t1_wav = np.arange(len(IR_wav_over))/(8*fs)

if len(t) > 100000:
        # mpl.RcParams()
        plt.rcParams['agg.path.chunksize'] = 10000

ax1.plot(t1_wav,IR_wav_over,'r')
fig1.canvas.draw()
