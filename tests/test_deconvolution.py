# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 18:22:57 2016
@author: Jee-Bee for jBae (c) 2016
"""

import numpy as np
from scipy.signal import chirp, convolve, deconvolve  # , hann # hanning window
from scipy.fftpack import fft, ifft
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# signal generating:
# ------------------

fs = 44100
T = 10
ws = 0.1

def harmonic_distorted_signals(plot_figure=True):
    t = np.arange(0, T, 1 / fs)

    sig1k = 1 * np.sin(2 * np.pi * 1000 * t)

    # 1k = 1
    # 2K = 0.2
    # 3K = 0.05
    # 4K = 0.01
    sig1kresp = 1 * np.sin(2 * np.pi * 1000 * t) + 0.2 * np.sin(2 * np.pi * 2000 * t
                    ) + 0.05 * np.sin(2 * np.pi * 3000 * t) + 0.01 * np.sin(2 * np.pi * 4000 * t)
    sig1kresp /= np.max(sig1kresp)

    # https://dsp.stackexchange.com/questions/5959/add-odd-even-harmonics-to-signal
    sig1kh = sig1k + np.tanh(sig1k)  # tanh() harmonic noise
    sig1kh /= np.max(sig1kh)
    # add x ^ 3, x^6 and or x^7 distortion to just for experiments

    if plot_figure is True:
        figt = plt.figure()
        axt = figt.add_subplot(1, 1, 1)
        axt.plot(t, sig1k, label='original')
        axt.plot(t, sig1kresp, label='with harmonic dist')
        axt.plot(t, sig1kh, label='with sinh() dist')
        #plt.axis([T-1, T,])
        axt.set_xlim(0.015, 0.025)
        figt.legend()
        figt.show()
    return(sig1k, sig1kresp, sig1kh)


def harmonic_distorded_fft(sig1k, sig1kresp, sig1kh, plot_figure=True, plot_spectogram=False):
    SIG1K = fft(sig1k)
    SIG1KRESP = fft(sig1kresp)
    SIG1KH = fft(sig1kh)  # sinh() noise

    # F = np.arange(-fs / 2, fs / 2, 1 / T)
    F = np.arange(0, fs, 1 / T)

    if plot_figure is True:
        figf = plt.figure()
        axf = figf.add_subplot(1, 1, 1)
        axf.plot(F, np.log10(np.abs(SIG1K)), label='original')
        axf.plot(F, np.log10(np.abs(SIG1KRESP)), label='with harmonic dist')
        axf.plot(F, np.log10(np.abs(SIG1KH)), label='with sinh() dist')
        axf.set_xlim(0, fs / 2)
        figf.legend()
        figf.show()

    if plot_spectogram is True:
        # Spectogram forwork
        SIG1KRESPS = np.zeros([np.round(T / ws).astype(int), np.round(fs * ws).astype(int)], dtype='complex')
        for idx in range(np.int(T/ws)):
            SIG1KRESPS[idx, :] = fft(sig1kresp[idx * np.round(fs * ws).astype(int): (idx + 1) * np.round(fs * ws).astype(int)])
            TS = np.arange(T / ws) * ws
            FS = np.arange(fs * ws) / ws
            FS, TS = np.meshgrid(FS, TS)

        fig1 = plt.figure()
        ax1 = fig1.add_subplot(111, projection="3d")
        ax1.plot_surface(TS, FS, np.abs(SIG1KRESPS), cmap="autumn_r", lw=0.5, rstride=1, cstride=1)
        ax1.azim = -90  # } set axit to top view
        ax1.elev = 90  # }
        fig1.show()


# deconvolution:
# --------------
# from scipy import fftpack
# from scipy import signal

def deconvolution_harmonic(sig1k, sig1kresp, sig1kh, plot_figure=True):
    deconvolved1kq, deconvolved1kr, = deconvolve(sig1k[1::], sig1kresp[1::])
# convolve()

    if plot_figure is True:
        figd = plt.figure()
        axd = figd.add_subplot(1, 1, 1)
        axd.plot(t[:-1:], deconvolved1kr, label='original')
        axd.axis([T-1, T,])
        axd.xlim(0, 0.2)
        figd.legend()
        figd.show()


# ----------------- Sweep -------------------------------------
# sig = chirp(t, 20, T, 1000)


# ----------------- Temp --------------------------------------
# http://stackoverflow.com/questions/35445424/surface-and-3d-contour-in-matplotlib
# fig = plt.figure()
# ax = fig.add_subplot(111, projection="3d")
# X, Y = np.mgrid[-2:2:60j, -1:1:30j]
# Z = np.sin(np.pi*X)*np.sin(np.pi * Y)
# ax.plot_surface(X, Y, Z, cmap="autumn_r", lw=0.5, rstride=1, cstride=1)

if __name__ == "__main__":
    sig1k_or, sig1k_custh, sig1k_sinh = harmonic_distorted_signals()
    harmonic_distorded_fft(sig1k_or, sig1k_custh, sig1k_sinh)
