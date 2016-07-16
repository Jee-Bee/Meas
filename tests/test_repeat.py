# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 17:17:27 2016

@author: winkelk
"""

# test repeat

import scipy.signal as sg
import numpy as np
import scripts.Repeat as rp

T = 5
fs = 44100
f0 = 20
f1 = 2000
repeats = 3

t = np.arange(0, T*fs)/fs
sig = sg.chirp(t, f0, T, f1, method='log', phi=-90)

repeated_signal,l_ur = rp.repSig(sig, repeats)

repeated_signal_zeros,l_urz = rp.repSig(sig, repeats, 2, fs, addzeros=True)

# averaging from here:

sig_avg = rp.repAvg(repeated_signal, repeats)
print(l_ur, len(sig_avg))
print(sig[0:15], sig_avg[0:15])

sig_avg_zeros = rp.repAvg(repeated_signal, repeats)
print(l_urz, len(sig_avg_zeros))
print(sig[0:15], sig_avg_zeros[0:15])


