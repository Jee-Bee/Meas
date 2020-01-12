# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 19:31:40 2016

@author: Jee-Bee for jBae (c) 2016
"""

import numpy as np


T = 5
fs = 44100
F = np.arange(1/T, fs/2, 1 / T )
oct_array = OctaveN(np.abs(np.array(np.random.rand(T * fs / 2))), F)

#Small tests - delete later on:
#    a = np.array([[1 ,2], [3, 4], [5,6]])
#    a[1] = array([3,4])
#    a[1][1] = 4
#
#    for idx in range(len(a)):
#        print(a[idx][0])
#
#    b = np.where((a>=3) & (a<=5)) = (array([1, 1, 2], dtype=int64), array([0, 1, 0], dtype=int64))


#Example:
#T =3
#f = 1000 Hz #= basic frequency
#np.log10(1000/1) = 3
#np.log10(1000/(1/T)) = 3.477...
#
#np.log2(1000/(1/T)) = 11.55...
#but since formulation octave is:
#1000*2**(n/2) or 1000/2**(n/2)
#i need to compensate my factor 2 so...
#1000 / 2**((2*12)/2) = 0.244... is around 0.33 Hz what was the signal

# 1/n test = 1/24
