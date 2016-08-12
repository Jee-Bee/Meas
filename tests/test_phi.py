# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 10:34:16 2016

@author: Jee-Bee for jBae (c) 2016
"""

# tests from question at dsp.stackexcange (dsp.se):

# input values:
import numpy as np

f0 = 20
f1 = 20000
fs = 44100
t1 = 3+144/fs

# phase answer 1
# phi_a1 = 2 * np.pi * t1 / np.log10(f1 / f0) * f0 * ((f1 / f0) ** (t1 / t1) - 1)
# phi_a1 = phi_a1 % (2 * np.pi)

beta = t1 / np.log10(f1 / f0)
phi_a1 = 2 * np.pi * beta * f0 * (np.power(f1 / f0, (t1-1/fs)/t1) - 1)
phi_a1 = phi_a1 % (2 * np.pi)

# phase answer 2
phi_a2 = (f1 * t1) / (np.log(20000) - np.log(20))
phi_cycl = phi_a2
phi_a2 = phi_a2 % (2 * np.pi)
phi_cycl = phi_cycl / (2 * np.pi)

# f_1_ref = 

# phase wikipedia:
# https://en.wikipedia.org/wiki/Chirp
phi_aw = 2 * np.pi * f0 * ((f1 / f0) ** (t1) - 1) / np.log(f1 / f0)
phi_aw = phi_a2 % (2 * np.pi)

# simultanieous Measurement of impulse...
# Farina AES 108 convention 2000 preprint

omega_1 = f0 * np.pi
omega_2 = f1 * np.pi
# T = t1
t = np.copy(t1) - 1/fs  # at moment t = t1 and t1 = T; so t/T = 1

phi_fa = omega_1 * t1 / np.log(omega_2 / omega_1) * (np.e ** ((t / t1) * np.log(omega_2/ omega_1)) - 1)
phi_fa = phi_fa % (2 * np.pi)

phi_fa_mod = omega_1 * t1 / np.log(omega_2 / omega_1) * (np.e ** ((t / t1) * np.log(omega_2/ omega_1)) - 1)
phi_fa_mod = phi_fa % (2 * np.pi)
