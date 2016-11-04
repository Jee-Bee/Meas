# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 10:08:53 2016

@author: Jee-Bee for jBae (c) 2016
"""

import numpy as np
import matplotlib.pylab as plt
import matplotlib.mlab as mlab
from scipy.io import wavfile

fs, IR_wav = wavfile.read("ir1_-_ir_masseria_gloria.wav")
IR_wav = IR_wav.astype(float)/(2**15)
t_wav = np.arange(len(IR_wav))/fs

# the histogram of the data
n, bins, patches = plt.hist(IR_wav, 250, normed=1, facecolor='green')

IR_wav_cl = IR_wav * 25  # clipped signal
IR_wav_cl = np.where(IR_wav_cl > 1, 1, IR_wav_cl)
IR_wav_cl = np.where(IR_wav_cl < -1, -1, IR_wav_cl)

# add a 'best fit' line
mu = np.sum(IR_wav)/len(IR_wav)
sigma = 1
y = mlab.normpdf(bins, mu, 0.01)
l = plt.plot(bins, y, 'r--', linewidth=1)

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=100,\ \sigma=15$')
#plt.axis([40, 160, 0, 0.03])
plt.grid(True)

plt.show()

plt.figure()
n, bins, patches = plt.hist(IR_wav_cl, 250, facecolor='blue')
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=100,\ \sigma=15$')

plt.show()