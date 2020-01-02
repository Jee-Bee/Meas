# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 14:00:45 2016

@author: Jee-Bee for jBae (c) 2016
"""

import sys
import numpy as np
if sys.version_info.major <3:
    from __future__ import division

class Window():
    """Class of different Window types"""
    def __init__(self, N):
        self.N = N
#        self.alpha = alpha
#        self.beta = beta
#        self.gamma = gamma
#        self.p = p

# 1. Compute the average of the whole time series (before splitting it into
# segments) and subtract that average from all data points.
# 2. Compute a straight line between the first and last data point of the whole
# time series (before splitting it into segments) and subtract that line from
# all data points.
# 3. Compute an average trend via linear regression of the whole time series
# (before splitting it into segments) and subtract that line from all data points.
# 4. Compute the average of each segment (before applying the window function)
# and subtract that average from the data points.
# 5. Compute a straight line between the first and last data point of each
# segment (before applying the window function) and subtract that line from the
# data points.
# 6. Compute an average trend via linear regression of each segment (before
# applying the #window function) and subtract that line from the data points.
# 7. Pass the input time series through a digital high-pass filter.

    def segment_avg(self, Signal):
        """ TODO:
        - create function. making average over window segement"""
        pass

# B slpine Windows:
# Rectangular: k = 1 (st order)
# Triangular: k = 2 (nd Order)
# Parzen: k = 4 (th order)

    def rectwind(self):
        """ Recatangular window also 1st order B-spline window
        Input:
            N = [-] lenght of window
        Output:
            w = Window
            x = coresponing values at x axis
        create window of rectangular form( straight line)
        TODO:
        - remove x from output not needed"""
        w = np.ones(self.N)
        x = np.arange(0, self.N - 1, 1)
        return(w, x)

    def triwind(self):
        """ Triangular window also 2nd order B-spline window
        Input:
            N = [-] lenght of window
        Output:
            w = Window
            x = coresponing values at x axis
        create window of triangular form( straight line to midle and than to 0)
        TODO:
        - remove x from output not needed"""
        w = np.zeros(self.N)
        x = np.zeros(self.N)
        for idx in range(int(self.N)):
            w[idx] = 1 - abs((idx - (self.N / 2))/(self.N / 2))
            x[idx] = idx
        return (w, x)

    def partzwind(self):
        """ Partzian window also 4th order B-spline window
        Input:
            N = [-] lenght of window
        Output:
            w = Window
            x = coresponing values at x axis

        TODO:
        - remove x from output not needed"""
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
        """ gennerazied hamming window
        Input:
            N = [-] lenght of window
            alpha = coeffiient for shaping bell
            beta = coefficient for shaping bell
        Output:
            w = Window
            x = coresponing values at x axis

        TODO:
        - remove x from output not needed"""
        # w = np.zeros(self.N)
        x = np.arange(self.N)
        w = alpha - beta * np.cos((2 * np.pi * x) / self.N)
        return (x, w)

    def hanwind(self):
        """ hanning window named after Julius von Hann
        Input:
            N = [-] lenght of window
            alpha = coeffiient for shaping bell = 0.5
            beta = coefficient for shaping bell = 0.5
        Output:
            w = Window
            x = coresponing values at x axis

        TODO:
        - remove x from output not needed"""
        alpha = beta = 0.5
        N = self.N
        gh = Window(N)
        (x, w) = gh.genhamwind(alpha, beta)
        return (x, w)

    def hamwind(self):
        """ hamming window named after Richard W Hamming
        Input:
            N = [-] lenght of window
            alpha = coeffiient for shaping bell = 25/46
            beta = coefficient for shaping bell = 21/46
        Output:
            w = Window
            x = coresponing values at x axis

        TODO:
        - remove x from output not needed"""
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
        """ cosine window or power of cosine window.
        With alpha = 0 rectangular window; alpha = 1 cosine window and with 
        alpha = 2 hann window is also part of family
        Input:
            N = [-] lenght of window
            alpha = coeffiient for power = 1
        Output:
            w = Window
            x = coresponing values at x axis

        TODO:
        - remove x from output not needed"""
        w = np.zeros(self.N)
        x = np.zeros(self.N)
        alpha = 1  # rectangular window alpha = 0; cos window alpha = 1; Hann window alpha =2.
        for idx in range(int(self.N)):
            w[idx] = np.cos((np.pi * idx / self.N) - np.pi / 2) ** alpha
            x[idx] = idx
        return (x, w)

#
# -----------------------------------------------------------------------------
#

    def gengausswind(self, sigma, p):
        """ generalized Gausian normal window
        Gausian window have as fft also an gausian window.
        Input:
            N = [-] lenght of window
            sigma = coeffiient for shaping bell
            p = coefficient for shaping bell
        Output:
            w = Window
            x = coresponing values at x axis

        TODO:
        - remove x from output not needed"""
        w = np.zeros(self.N)
        x = np.zeros(self.N)
        for idx in range(int(self.N)):
            num = idx-self.N/2
            denum = sigma*(self.N-1)/2
            w[idx] = np.e ** ((-1 / 2) * (num / denum) ** p)
            x[idx] = idx
        return (x, w)

    def gausswind(self):
        """ generalized Gausian normal window
        Gausian window have as fft also an gausian window.
        Input:
            N = [-] lenght of window
            sigma = coeffiient for shaping bell = 0.5
            p = coefficient for shaping bell = 2
        Output:
            w = Window
            x = coresponing values at x axis
        When P goes to infty the gausian window become rectangular

        TODO:
        - remove x from output not needed"""
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
        """ Tukey window also known as tapered cosine window
        The tukey window can be regarded as sidelobs of cosine window
        convoluted with a rectangular window.
        Input:
            N = [-] lenght of window
            alpha = coeffiient for shaping bell
        Output:
            w = Window
            x = coresponing values at x axis
        with alpha = 0 it becomes a rectangular window and with alpha = 1 it
        becomes a hann window.

        TODO:
        - remove x from output not needed"""
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
            elif idx >= int(self.N * (1 - alpha / 2)) and idx <= (self.N - 1):
                w[idx] = 1 / 2 * (1 + np.cos(np.pi * (2 * idx / (alpha * (self.N - 1)) - 2 / alpha + 1)))
                x[idx] = idx
        return (x, w)

#
# -----------------------------------------------------------------------------
#

# Frome here calculate Overlab carcteristics:
    def Overlap_Characterestics(self, Window_type, accurency):
        # Calculate AF = Min/Max
        # Calculate PF
        # Calculate OC
        # See 395068 Window Document:
        #     Spectrum and spectral density estimation by the Discrete Fourier
        #     transform (DFT), including a comprehensive list of window
        #     functions and some new at-top windows.
        pass

    def ROV(self, Window_type):
#        Input are values from Input characteresitcs
        pass
