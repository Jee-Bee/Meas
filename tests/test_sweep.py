# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#import
import numpy as np
import scipy.signal as sig
import matplotlib.pylab as plt

f0 = 50
f1 = 20000 
t1 = 10
t = np.arange(0,t1,1/44100)#[numpy.newaxis]; 
print(t.shape)

sine = np.sin(2*np.pi*f0*t)

plt.plot(t, sine)
plt.xlabel('Angle [rad]')
plt.ylabel('sin(t)')
plt.axis('tight')
plt.show()

sweep = sig.chirp(t,f0,t1,f1,'linear',90) 
# http://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.signal.chirp.html

plt.plot(t, sweep)
plt.xlabel('Angle [rad]')
plt.ylabel('sin(t)')
plt.axis('tight')
plt.show()

#poly= scipy.signal.sweep_poly(t, poly, phi=0)[source] 
# http://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.signal.sweep_poly.html#scipy.signal.sweep_poly




