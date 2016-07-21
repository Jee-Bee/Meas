# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 09:25:38 2016

@author: Jee-Bee for jBae (c) 2016
"""

from scipy.signal import *


def HannWwind(N):
    wind = hann(N)
    return wind

def GaussWind(N):
    pass


