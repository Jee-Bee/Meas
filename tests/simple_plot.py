import matplotlib.pylab as plt
#from pylab import *

fs = 512
t = plt.arange(0.0, 2.0, 1/fs)
s = plt.sin(250*plt.pi*t)
plt.plot(t, s)

plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('About as simple as it gets, folks')
plt.grid(True)
plt.savefig("test.png")
plt.show()

#
# ----------- From Here Overlab characteristics function ---------------------
#
import sys
from ..scripts import Window
import numpy as np


def Overlap_Characterestics(Window_type, accurency):
#        Calculate AF = Min/Max
#        Calculate PF
#        Calculate OC 
#        See 395068 Window Document: 
#            Spectrum and spectral density estimation by the Discrete Fourier
#            transform (DFT), including a comprehensive list of window
#            functions and some new at-top windows.
    N = 1024  # Window Length
    Overlab = 50  # [%] 
    Overlab_var = Overlab/100 + 1
    hann = Window.hanwind(N)
    y= np.zeros(N* Overlab_var)
    y = y + hann
    x = np.arange(N*Overlab_var)
    return (x,y)
#    pass

 
def ROV (self, Window_type):
#        Input are values from Input characteresitcs
    pass


