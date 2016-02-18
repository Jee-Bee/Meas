# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 16:45:59 2016

@author: Jee-Bee jBae (c) 2016
"""

from scipy.io import wavfile
from numpy import arange
import matplotlib.pylab as plt
from scripts import RMS, Transform, OctaveBands
#import RMS as RMS

import sounddevice as sd

import numpy as np


# Samples for internal use only. Just test data for test Results
#[fs,data] = wavfile.read('15 Sample 15Sec.wav')
[fs,data] = wavfile.read("09 Sample 15sec.wav")#,dtype=float)
data = data[2048:2048+4096:]

data = data.astype(float)/(2**15)


t = arange(0,len(data)/fs,1/fs)


#rmssig = RMS(data)
rmssig = RMS.RMS(data)

#crestsig = Crest(data) 
crest = RMS.Crest(data)


#if len(t)< 100000:
##    mpl.RcParams()
#    plt.rcParams['agg.path.chunksize'] = 10000

#
# FFT calculation
[F,DATA] = Transform.FFT(data,fs)
[F,RMSSIG] = Transform.FFT(rmssig,fs)


plt.figure()
plt.subplot(2,1,1), plt.plot(t,data)
plt.subplot(2,1,1), plt.plot(t,rmssig)
plt.subplot(2,1,2), plt.plot(F,DATA)
plt.subplot(2,1,2), plt.plot(F,RMSSIG)
#plt.draw
plt.show()

sd.play(data,fs)

#compwar = Crest(data)
#print(compwar)
#sd.wait()

#sd.stop()

from scripts.DefaultFigures import Time, SpecMag, SpecPh
plt.figure()
Time(t, data)
plt.figure()
SpecMag(F,DATA)



#Tertsband test
#Small Tesst audio


N = int(4096)

[fs,data] = wavfile.read("../09 Sample 15sec.wav")#,dtype=float)
t = np.arange(0,N/fs,1/fs)
data = data[2048:2048+N:]
data = np.reshape(np.delete(data,0, 1),len(data))
[F,DATA] = Transform.FFT(data,fs)
DATA = abs(DATA[len(DATA)/2::])
F = F[len(F)/2::]

(tertsF, tertsA) = OctaveBands.Octave3(DATA,F)

# Show curves for narrow bands and 1/3 octave bands.
plt.figure()
plt.semilogx(F,DATA,'k-')#,'linewidth',2)
plt.semilogx(tertsF,tertsA,'ro','MarkerSize',10)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Sound absorption coefficient')
plt.legend('Narrow bands','1/3 octave bands',4)
