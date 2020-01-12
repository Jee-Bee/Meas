# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 12:43:07 2016

@author: Jee-Bee for jBae (c) 2016
"""
import numpy as np
import numpy.fft as fft
import numpy.random as rand
import matplotlib.pyplot as plt

def create_noise(shape, show_figure=True):
    rbin = rand.binomial(1, 0.5, shape)
    rexp = rand.exponential(1, shape)
    rnor = rand.normal(1, 1, shape)
    rpow = rand.power(1, shape)
    rran = rand.rand(shape)
    runi = rand.uniform(0, 1, shape)
    if show_figure is True:
        fign = plt.figure()
        axn1 = fign.add_subplot(2, 3, 1)
        axn1.hist(rbin)
        axn1.title.set_text('Binominaal')
        axn2 = fign.add_subplot(2, 3, 2)
        axn2.hist(rexp)
        axn2.title.set_text('Exponential')
        axn3 = fign.add_subplot(2, 3, 3)
        axn3.hist(rnor)
        axn3.title.set_text('Normal')
        axn4 = fign.add_subplot(2, 3, 4)
        axn4.hist(rpow)
        axn4.title.set_text('Power')
        axn5 = fign.add_subplot(2, 3, 5)
        axn5.hist(rran)
        axn5.title.set_text('Rand')
        axn6 = fign.add_subplot(2, 3, 6)
        axn6.hist(runi)
        axn6.title.set_text('Uniform')
        fign.show()
    return(rbin, rexp, rnor, rpow, rran, runi)


def noise_spectrum(rbin, rexp, rnor, rpow, rran, runi, show_figure=True):
    # create real, imag spectrum
    fbin = fft.fft(rbin)
    fexp = fft.fft(rexp)
    fnor = fft.fft(rnor)
    fpow = fft.fft(rpow)
    fran = fft.fft(rran)
    funi = fft.fft(runi)
    # change to magnitude and phase
    magbin = np.abs(fbin)
    phbin = np.angle(fbin, deg=True)
    magexp = np.abs(fexp)
    phexp = np.angle(fexp, deg=True)
    magnor = np.abs(fnor)
    phnor = np.angle(fnor, deg=True)
    magpow = np.abs(fpow)
    phpow = np.angle(fpow, deg=True)
    magran = np.abs(fran)
    phran = np.angle(fran, deg=True)
    maguni = np.abs(funi)
    phuni = np.angle(funi, deg=True)
    if show_figure is True:
        figf = plt.figure()
        axf1 = figf.add_subplot(2, 1, 1)
        axf1.loglog(magbin)
        axf1.loglog(magexp)
        axf1.loglog(magnor)
        axf1.loglog(magpow)
        axf1.loglog(magran)
        axf1.loglog(maguni)
        axf1.title.set_text('Magnitude spectrum noise')
        axf2 = figf.add_subplot(2, 1, 2)
        axf2.semilogx(phbin)
        axf2.semilogx(phexp)
        axf2.semilogx(phnor)
        axf2.semilogx(phpow)
        axf2.semilogx(phran)
        axf2.semilogx(phuni)
        axf2.title.set_text('phase spectrum noise')
        figf.show()


if __name__ == "__main__":
    noise_length = 2048
    rbin, rexp, rnor, rpow, rran, runi = create_noise(noise_length)
    noise_spectrum(rbin, rexp, rnor, rpow, rran, runi)
