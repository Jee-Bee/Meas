import sys
import numpy as np
import matplotlib.pylab as plt

#fs = 512
#t = plt.arange(0.0, 2.0, 1/fs)
#s = plt.sin(250*plt.pi*t)
#plt.plot(t, s)
#
#plt.xlabel('time (s)')
#plt.ylabel('voltage (mV)')
#plt.title('About as simple as it gets, folks')
#plt.grid(True)
## plt.savefig("test.png")
#plt.show()

#
# ----------- From Here Overlab characteristics function ---------------------
#


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


def OC(Window_Type, percent):
    r = percent/100
    N = 1024
    (dummy, w) = hanwind(N)
    oc_num = np.sum(w * w.T + (1 - r) * N)
    oc_denum = np.sum(w ** 2)
    oc = oc_num / oc_denum
    return (oc)


def Overlap_Characterestics(Window_type, Window_Length):
    #    Calculate AF = Min/Max
    #    Calculate PF
    #    Calculate OC
    #    See 395068 Window Document:
    #       Spectrum and spectral density estimation by the Discrete Fourier
    #       transform (DFT), including a comprehensive list of window
    #       functions and some new at-top windows.
    N = Window_Length  # Window Length
    nW = int(N/8)
#    Overlab = 64  # [%]
    (dummy, win) = hanwind(N)
    af = []
    for Overlab_var in range(1, N+1):
        #    Overlab_var = Overlab / 100
        y = np.zeros(np.round(nW * N - (nW - 1) * Overlab_var))
        for idx in range(nW):
            idxl = round(idx * N - idx * Overlab_var)
            idxu = round((idx + 1) * N - idx * Overlab_var)
            y[idxl:idxu] = y[idxl:idxu] + win
        locmin = np.r_[True, y[1:] < y[:-1]] & np.r_[y[:-1] < y[1:], 
                       True] | np.r_[True, y[1:] == y[:-1]] & np.r_[
                        y[:-1] < y[1:], True] | np.r_[True,
                        y[1:] < y[:-1]] & np.r_[y[:-1] == y[1:], True]
        # Max value
        locmax = np.r_[True, y[1:] > y[:-1]] & np.r_[y[:-1] > y[1:],
                           True] | np.r_[True, y[1:] == y[:-1]] & np.r_[
                           y[:-1] > y[1:], True] | np.r_[True,
                           y[1:] > y[:-1]] & np.r_[y[:-1] == y[1:], True]
        minval = []
#        minidx = []
        maxval = []
#        maxidx = []
        temp = []
        for idx in range(len(locmin)):
            if locmin[idx] == True:
                if y[idx] != 0:
                    minval = np.append(minval, y[idx])
                    # minidx = np.append(minidx, idx)
                temp = np.append(temp, minval, axis=1)
            if locmax[idx] == True:
                maxval = np.append(maxval, y[idx])
                # maxidx = np.append(maxidx, idx)
        if minval != []:
            af = np.append(af, np.min(minval) / np.max(maxval))
        else:
            af = np.append(af, np.NaN)
    percent = np.linspace(0, 100, N)
    return (percent, af) #, temp)


def ROV(self, Window_type):
    # Input are values from Input characteresitcs
    pass

# https://terpconnect.umd.edu/~toh/spectrum/PeakFindingandMeasurement.htm
# https://gist.github.com/endolith/250860
[xaxis, yaxis] = Overlap_Characterestics([], 1024)
# http://stackoverflow.com/questions/4624970/finding-local-maxima-minima-with-numpy-in-a-1d-numpy-array

plt.plot(xaxis, yaxis)
