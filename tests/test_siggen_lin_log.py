# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 07:53:07 2016

@author: Jee-Bee for jBae (c) 2016
"""

from src.SigGen import SigGen
# import src.SigGen
import matplotlib.pyplot as plt

f = [10, 1000]  # [Hz] frequency
T = 5  # [sec] time
fs = 44100

t_lin, lin = SigGen.SigGen('ChirpLin', f, T, fs)
t_log, log = SigGen.SigGen('ChirpLog', f, T, fs)


if __name__ == "__main__":
    f = [10, 1000]  # [Hz] frequency
    T = 5  # [sec] time
    fs = 44100

    t_lin, lin = SigGen.SigGen('ChirpLin', f, T, fs)
    t_log, log = SigGen.SigGen('ChirpLog', f, T, fs)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(t_lin, lin, label='linear chirp')
    ax.plot(t_log, log, label='ligaritmic chirp')
    fig.legend(loc='best')
