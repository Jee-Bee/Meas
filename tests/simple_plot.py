import matplotlib.pylab as plt
#from pylab import *

fs = 512
t = plt.arange(0.0, 2.0, 1/fs)
s = plt.sin(250*plt.pi*t)
plt.plot(t, s)

plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('About as simple as it gets, folks')
plt.grid(True)
plt.savefig("test.png")
plt.show()

#
# ----------- From Here Overlab characteristics function ---------------------
#
import sys
import numpy as np


def genhamwind(N, alpha, beta):
    w = np.zeros(N)
    x = np.zeros(N)
    for idx in range(N):
        w[idx] = alpha - beta * np.cos((2 * np.pi * idx) / (N - 1))
        x[idx] = idx
    return (x, w)


def hanwind(N):
    alpha = beta = 0.5
    [x, w] = genhamwind(N, alpha, beta)
    return (x, w)


def Overlap_Characterestics(Window_type, accurency):
#        Calculate AF = Min/Max
#        Calculate PF
#        Calculate OC
#        See 395068 Window Document:
#            Spectrum and spectral density estimation by the Discrete Fourier
#            transform (DFT), including a comprehensive list of window
#            functions and some new at-top windows.
    N = 1024  # Window Length
    Overlab = 30  # [%]
    Overlab_var = 1 - Overlab / 100
    y = np.zeros(np.round(N + N * Overlab_var))
    (dummy, win) = hanwind(N)
    y[:N] = win
    y[N * Overlab_var:] = y[N * Overlab_var:] + win
    x = np.arange(np.round(N + N * Overlab_var))
    return (x, y)
#    pass


def ROV(self, Window_type):
#        Input are values from Input characteresitcs
    pass


[xaxis, yaxis] = Overlap_Characterestics([], [])
plt.plot(xaxis, yaxis)
