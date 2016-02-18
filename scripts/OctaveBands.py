# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 11:48:31 2016

@author: Jee-Bee for jBae (c) 2016
"""

#Made with help of: 
# http://apmr.matelys.com/Standards/OctaveBands.html
#and
# https://nl.wikipedia.org/wiki/Resolutie_(geluidsmeting)

#2DO:
#Octave
#1/n octave
#self calculating octave range
#self calculating freq bands/ check prefered if needed
#self asking for making plot or return to plot depends on direction...
#test current method

import numpy as np

def Octave(Measurement, fs, *argv):
    pass


def Octave3(Measurement,F):
#    The input parameters are:
#    o frequencies: frequency values 
#        (with a fixed of variable frequency step),
#    o measurements: acoustic absorption coefficent values
#        (corresponding to the frequency vector defined above).
#    
#    The output parameters are:
#    o one_third_freq: center frequencies of 1/3 octave bands,
#    o bands: values of the acoustic absorption coefficent in 1/3 bands
#    
#    First edition based on
#    Copyleft 2007-2011 luc.jaouen@matelys.com
#    cf. APMR on the web,
#    Standards/OctaveBands.html
#    for more information
    Freq_pref =  np.array([16, 20, 25,  31.5, 40, 50, 63, 80, 100, 125, 160, 200, 250,
                315, 400, 500, 630, 800, 1000, 1250, 1600, 2000, 2500, 3150, 4000, 
                5000, 6300, 8000, 10000, 12500, 16000, 20000])
    
    # Determine lower and upper limits of each 1/3 octave band
    freq3 = np.zeros(len(Freq_pref))
    bands3 = np.zeros((2,len(Freq_pref)))
    for a in range(len(Freq_pref)):
        freq3[a] = (1000*((2**(1/3)))**(a-19));
        bands3[0][a] = freq3[a]/2**(1/6)
        bands3[1][a] = freq3[a]*2**(1/6)
    
    # Compute the acoustic absorption coefficient per 1/3 octave band
    bands = []
    for a in range(np.size(bands3,1)):
        bands = np.append(bands,[0])
        idx = np.where( (F >= bands3[0][a]) & (F < bands3[1][a]) )
        idx = idx[0]
#        If we have no 'measurement' point in this band:
        if ( len(idx) == 0 ):
            print('Warning: no point found in band centered at %4.0f\n' % freq3[a])
#        If we have only 1 'measurement' point in this band:
        elif ( len(idx) == 1 ):
            print('Warning: only one point found in band centered at %4.0f\n' % freq3[a])
            bands[a] = Measurement[idx[0]]
#        If we have more than 1 'measurement' point in this band:
        elif ( len(idx) > 1 ):
            for b in range(len(idx)):
                bands[a] = bands[a] + ( F[idx[0]+b]-F[idx[0]+b-1] ) * abs( Measurement[idx[0]+b] + Measurement[idx[0]+b-1] ) / 2
            bands[a] = bands[a] / ( F[idx[len(idx)-1]] - F[idx[0]] )
    return (Freq_pref, bands)

#Small Tesst audio
from scipy.io import wavfile
from scipy.fftpack import fft, fftshift
import matplotlib.pylab as plt

N = int(4096)

[fs,data] = wavfile.read("../09 Sample 15sec.wav")#,dtype=float)
t = np.arange(0,N/fs,1/fs)
data = data[2048:2048+N:]
data = np.reshape(np.delete(data,0, 1),len(data))
DATAs = fftshift(fft(data))  # No fit
DATAs = abs(DATAs[len(DATAs)/2::])
DATA = fftshift(fft(data))  # No fit
DATA = abs(DATA[len(DATA)/2::])
F = np.linspace(-fs/2,fs/2,N)
F = F[len(F)/2::]

(tertsF, tertsA) = Octave3(DATAs,F)

# Show curves for narrow bands and 1/3 octave bands.
plt.figure()
plt.semilogx(F,DATAs,'k-')#,'linewidth',2)
plt.semilogx(tertsF,tertsA,'ro','MarkerSize',10)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Sound absorption coefficient')
plt.legend('Narrow bands','1/3 octave bands',4)


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

