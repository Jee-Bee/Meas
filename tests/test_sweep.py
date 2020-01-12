# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 16:45:59 2016

@author: Jee-Bee for jBae (c) 2016
"""

#import
import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt

f0 = 50
f1 = 20000 
t1 = 10
t = np.arange(0, t1, 1 / 44100)  # [numpy.newaxis]; 
print(t.shape)

if len(t)> 100000:
#    mpl.RcParams()
    plt.rcParams['agg.path.chunksize'] = 10000

sine = np.sin(2 * np.pi * f0 * t)

plt.plot(t, sine)
plt.xlabel('Angle [rad]')
plt.ylabel('sin [t]')
plt.axis('tight')
plt.show()


sweep = sig.chirp(t, f0, t1, f1, 'linear', 90) 
# http://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.signal.chirp.html

if len(t)> 100000:
#    mpl.RcParams()
    plt.rcParams['agg.path.chunksize'] = 10000

plt.plot(t, sweep)
plt.xlabel('Angle [rad]')
plt.ylabel('sin(t)')
plt.axis('tight')
plt.show()

#poly= scipy.signal.sweep_poly(t, poly, phi=0)[source] 
# http://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.signal.sweep_poly.html#scipy.signal.sweep_poly

#test_sweep.py
#Made by Jee-Bee for jBae (c) 2016