# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 14:00:45 2016

@author: Jee-Bee for jBae (c) 2016
"""

import numpy as np


class Window():
    """Class of different Window types"""
    def __init__(self, N):
        self.N = N
#        self.alpha = alpha
#        self.beta = beta
#        self.gamma = gamma
#        self.p = p

#1. Compute the average of the whole time series (before splitting it into segments) and
#subtract that average from all data points.
#2. Compute a straight line between the first and last data point of the whole time series
#(before splitting it into segments) and subtract that line from all data points.
#3. Compute an average trend via linear regression of the whole time series (before splitting
#it into segments) and subtract that line from all data points.
#4. Compute the average of each segment (before applying the window function) and subtract
#that average from the data points.
#5. Compute a straight line between the first and last data point of each segment (before
#applying the window function) and subtract that line from the data points.
#6. Compute an average trend via linear regression of each segment (before applying the
#window function) and subtract that line from the data points.
#7. Pass the input time series through a digital high-pass filter.

    def segment_avg(self, Signal):
        pass

# B slpine Windows:
# Rectangular: k = 1 (st order)
# Triangular: k = 2 (nd Order)
# Parzen: k = 4 (th order)

    def rectwind(self):
        w = np.ones(self.N)
        x = np.arange(0, self.N - 1, 1)
        return(w, x)

    def triwind(self):
        w = np.zeros(self.N)
        x = np.zeros(self.N)
        for idx in range(int(self.N)):
            w[idx] = 1 - abs((idx - ((self.N - 1) / 2))/(self.N / 2))
            x[idx] = idx
        return (w, x)

    def partzwind(self):
        w = np.zeros(int(self.N / 2))
        x = np.zeros(int(self.N / 2))
        for idx in range(int(self.N/2)):
            x[idx] = idx
            if (idx >= 0) and (idx <= (self.N/4)):
                w[idx] = 1 - (6 * (idx / (self.N / 2)) ** 2) * (1 - abs(idx) / (self.N / 2))
            elif(idx >= self.N/4) and (idx <= (self.N/2)):
                w[idx] = 2 * (1 - abs(idx) / (self.N / 2)) ** 3
        x = np.append(x, x + int(self.N/2))
        w = np.append(w[::-1], w)
        return (x, w)
# #    if (idx < 3) == True:

#
# -----------------------------------------------------------------------------
#

    def genhamwind(self, alpha, beta):
        w = np.zeros(self.N)
        x = np.zeros(self.N)
        for idx in range(int(self.N)):
            w[idx] = alpha - beta * np.cos((2 * np.pi * idx) / (self.N - 1))
            x[idx] = idx
        return (x, w)

    def hanwind(self):
        alpha = beta = 0.5
        N = self.N
        gh = Window(N)
        (x, w) = gh.genhamwind(alpha, beta)
        return (x, w)

    def hamwind(self):
        alpha = 0.53836
        beta = 1 - alpha
        N = self.N
        gh = Window(N)
        (x, w) = gh.genhamwind(alpha, beta)
        return (x, w)

#
# -----------------------------------------------------------------------------
#

    def coswind(self):
        w = np.zeros(self.N)
        x = np.zeros(self.N)
        alpha = 1  # rectangular window alpha = 0; cos window alpha = 1; Hann window alpha =2.
        for idx in range(int(self.N)):
            w[idx] = np.cos((np.pi * idx / (self.N - 1)) - np.pi / 2) ** alpha
            x[idx] = idx
        return (x, w)

#
# -----------------------------------------------------------------------------
#

    def gengausswind(self, sigma, p):
        w = np.zeros(self.N)
        x = np.zeros(self.N)
        for idx in range(int(self.N)):
            num = idx-(self.N-1)/2
            denum = sigma*(self.N-1)/2
            w[idx] = np.e ** ((-1 / 2) * (num / denum) ** p)
            x[idx] = idx
        return (x, w)

    def gausswind(self):
        sigma = 0.5
        p = 2
        N = self.N
        gg = Window(N)
        [x, w] = gg.gengausswind(sigma, p)
        return (x, w)

#
# -----------------------------------------------------------------------------
#

    def Tukeywind(self):
        w = np.zeros(self.N)
        x = np.zeros(self.N)
        alpha = 0.5
        for idx in range(int(self.N)):
            if idx <= int(alpha*(self.N-1)/2):
                w[idx] = 1 / 2 * (1 + np.cos(np.pi * (2 * idx / (alpha * (self.N - 1)) - 1)))
                x[idx] = idx
            elif idx >= int(alpha * (self.N - 1) / 2) and idx <= int((self.N - 1) * (1 - alpha / 2)):
                w[idx] = 1
                x[idx] = idx
            elif idx >= int((self.N - 1) * (1 - alpha / 2)) and idx <= (self.N - 1):
                w[idx] = 1 / 2 * (1 + np.cos(np.pi * (2 * idx / (alpha * (self.N - 1)) - 2 / alpha + 1)))
                x[idx] = idx
        return (x, w)

#
# -----------------------------------------------------------------------------
#

# Frome here calculate Overlab carcteristics:
    def Overlap_Characterestics(self, Window_type, accurency):
#        Calculate AF = Min/Max
#        Calculate PF
#        Calculate OC
#        See 395068 Window Document:
#            Spectrum and spectral density estimation by the Discrete Fourier
#            transform (DFT), including a comprehensive list of window
#            functions and some new at-top windows.
        pass

    def ROV(self, Window_type):
#        Input are values from Input characteresitcs
        pass
