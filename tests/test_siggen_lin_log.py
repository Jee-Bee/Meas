# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 07:53:07 2016

@author: winkelk
"""

from scripts.SigGen import SigGen
#import scripts.SigGen

f = [10, 1000]  # [Hz] frequency
T = 5  # [sec] time
fs = 44100

t_lin, lin = SigGen.SigGen('ChirpLin', f, T, fs)
t_log, log = SigGen.SigGen('ChirpLog', f, T, fs)
