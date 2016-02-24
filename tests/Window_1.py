# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 14:00:45 2016

@author: Jee-Bee for jBae (c) 2016
"""

import numpy as np


class Window:  # (object):
    """Class of different Window types"""
    def __init__(self, N):  # , alpha, beta, gamma, p):
        self.N = N
        print("in Init")
        print(self.N)

    def triwind(self):
        print("in Function")
        w = np.zeros(self.N)
        x = np.zeros(self.N)
        for idx in range(int(self.N)):
            w[idx] = 1 - abs((idx - ((self.N - 1) / 2))/(self.N / 2))
            x[idx] = idx
        return (w, x)

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
