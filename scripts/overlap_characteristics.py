import sys
import numpy as np
import matplotlib.pyplot as plt
from Window import Window
if sys.version_info.major <3:
    from __future__ import division

def OC(Window_Type, percent, *args, **kwargs):
    # See: http://www.recordingblogs.com/sa/tabid/88/Default.aspx?topic=Overlap+correlation
    r = percent/100
    N = 1024
    if kwargs == {}:
        if Window_Type == "coswind":
            dummy, w = Window.coswind(N)
        elif Window_Type == "gausswind":
            dummy, w = Window.gausswind(N)
        elif Window_Type == "gengausswind":
            if len(args) == 2:
                dummy, w = Window.gengausswind(N, args[1], args[2])
            else:
                raise TypeError(“2 Adidional args are needed but not given")
        elif Window_Type == "genhamwind":
            if len(args) == 2:
                dummy, w = Window.genhamwind(N, args[1], args[2])
            else:
                raise TypeError(“2 Adidional args are needed but not given")
        elif Window_Type == "hamwind":
            dummy, w = Window.hamwind(N)
        elif Window_Type == "hanwind":
            dummy, w = Window.hanwind(N)
        elif Window_Type == "partzwind":
            dummy, w = Window.partzwind(N)
        elif Window_Type == "rectwind":
            dummy, w = Window.rectwind(N)
        elif Window_Type == "triwind":
            dummy, w = Window.triwind(N)
        elif Window_Type == "Tukeywind":
            dummy, w = Window.Tukeywind(N)
    elif kwargs['WindowSet'] == 'window':
        w = Window_Type
    else:
        (dummy, w) = Window.hanwind(N)
    oc_num = []
    for idx in range(int(r * len(w))):
        oc_num = np.append(oc_num, w[idx] * w[idx + (1 - r) * len(w)])
    oc = oc_num.sum() / np.sum(w ** 2)
    return (oc)


def ROV(af, oc):
    # Input are values from Input characteresitcs
    N = len(af)
    rovidx = np.argmax(af / oc)
    rov = 100 / N * (rovidx - 1)
    return(rov, rovidx)


# a * idx + b (in log_2)
# if N = 1024, N/8 = 128; N = 2 ** 10; 8 = 2 ** 3; 128 = 2 ** 7
# idx[0] = a*0 + b = 2; b = 2
# idx[N] = a*N + 2 = 7; a = 5 / N
def Overlap_Characterestics(Window_type, Window_Length):
    """Calculate AF = Min/Max
       Calculate PF
       Calculate OC
       See 395068 Window Document:
           Spectrum and spectral density estimation by the Discrete Fourier
           transform (DFT), including a comprehensive list of window
           functions and some new at-top windows.
    """
    N = Window_Length  # Window Length
    (dummy, win) = hanwind(N)
    af = []
#    pf = []
    oc = []
    for Overlab_var in range(1, N+1):
        nW = 3 + 2 ** np.int(Overlab_var * (np.log2(N) - 5) / N)  # - 3 - 2 = 1/8 N max & 2 min
        #    Overlab_var = Overlab / 100
        y = np.zeros(np.round(nW * N - (nW - 1) * Overlab_var))
        idx = 1
        idxl = 0
        idxu = N
        while idx < nW:
            y[idxl:idxu] = y[idxl:idxu] + win
            idxl += (N - Overlab_var)
            idxu += (N - Overlab_var)
            idx +=1
        # Min value
        locmin = np.r_[True, y[1:] < y[:-1]] & np.r_[y[:-1] < y[1:],
                       True] | np.r_[True, y[1:] == y[:-1]] & np.r_[
                        y[:-1] < y[1:], True] | np.r_[True,
                        y[1:] < y[:-1]] & np.r_[y[:-1] == y[1:], True]
        # Max value
        locmax = np.r_[True, y[1:] > y[:-1]] & np.r_[y[:-1] > y[1:],
                           True] | np.r_[True, y[1:] == y[:-1]] & np.r_[
                           y[:-1] > y[1:], True] | np.r_[True,
                           y[1:] > y[:-1]] & np.r_[y[:-1] == y[1:], True]
        minaf = []
        maxaf = []
        for idx in range(len(locmin)):
            if locmin[idx] == True:
                if y[idx] != 0:
                    minaf = np.append(minaf, y[idx])
#                    minap = np.append(minap, y[idx] ** 2)
            if locmax[idx] == True:
                maxaf = np.append(maxaf, y[idx])
#                maxap = np.append(maxap, y[idx] ** 2)
        if minaf != []:
            af = np.append(af, minaf.min() / maxaf.max())
#            pf = np.append(pf, minap.min() / maxap.max())
        else:
            af = np.append(af, np.NaN)
#            pf = np.append(pf, np.NaN)
        oc = np.append(oc, OC(win, 100 / N * Overlab_var, WindowSet='window'))
    (rov, rovidx) = ROV(af, oc)
    percent = np.linspace(0, 100, N)
    return (percent, af, oc, rov)  # pf ,oc)


# https://terpconnect.umd.edu/~toh/spectrum/PeakFindingandMeasurement.htm
# https://gist.github.com/endolith/250860
[xaxis, afval, ocval, index] = Overlap_Characterestics([], 1024)
# http://stackoverflow.com/questions/4624970/finding-local-maxima-minima-with-numpy-in-a-1d-numpy-array

plt.plot(xaxis, afval, xaxis, ocval)
# plt.arrow(index, ocval[index], 0, afval[index] - ocval[index])

#For loop
#1 loops, best of 3: 16.2 s per loop
#C:/Users/enjbwink/Documents/python/temp_ovr.py:57: RuntimeWarning: divide by zero encountered in true_divide
#  rovidx = np.argmax(af / oc)

# while
#1 loops, best of 3: 16.2 s per loop
#C:/Users/enjbwink/Documents/python/temp_ovr.py:57: RuntimeWarning: divide by zero encountered in true_divide
#  rovidx = np.argmax(af / oc)

#while +:
#1 loops, best of 3: 9.94 s per loop
#C:/Users/enjbwink/Documents/python/temp_ovr.py:58: RuntimeWarning: divide by zero encountered in true_divide
#  rovidx = np.argmax(af / oc)
