# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 16:45:59 2016

@author: Jee-Bee jBae (c) 2016
"""

from scipy.io import wavfile
from numpy import arange
import matplotlib.pylab as plt
from scripts import *
import RMS as RMS

import sounddevice as sd


#import numpy as np

#def RMS (sig):
#    if isinstance( sig, ( int ) ) == True:
#        sig_rms = sig/(2**15)
#        rmsarray = np.sqrt((1/len(sig_rms))*np.sum(sig_rms**2))*sig
#        return rmsarray
#    elif isinstance( sig, ( float ) ) == True:
#        rmsarray = np.sqrt((1/len(sig_rms))*np.sum(sig_rms**2))*sig
#        return rmsarray
#    return np.sqrt((1/len(sig))*np.sum(sig**2))*sig
#    return np.sqrt((1/len(sig_rms))*np.sum(sig_rms**2))*sig
#    return np.sqrt((1/len(sig))*np.sum(sig**2))

def Crest (sig):  # Crest Factor singe value from array
    rms = RMS(sig)
    peak = abs(sig)
    C = sum(peak/rms)/len(sig)
    return(peak, rms,C)
#    return (temp, C)


# Samples for internal use only. Just test data for test Results
#[fs,data] = wavfile.read('15 Sample 15Sec.wav')
[fs,data] = wavfile.read('09 Sample 15sec.wav')#,dtype=float)
data = data[2048:2048+4096:]

data = data.astype(float)/(2**15)


t = arange(0,len(data)/fs,1/fs)

#http://matplotlib.org/users/shell.html
#ioff()      # turn updates off
#title('now how much would you pay?')
#xticklabels(fontsize=20, color='green')
#draw()      # force a draw
#savefig('alldone', dpi=300)
#close()
#ion()      # turn updating back on
#plot(rand(20), mfc='g', mec='r', ms=40, mew=4, ls='--', lw=3)


#sinewave = np.sin(2*np.pi * 100 *t)
#rmssine = RMS(sinewave)
#[peak,rms,crestsine] = Crest(sinewave)
#
#C=peak/rms  # peak/rms is bij 0/0 NAN... Fix this

#plt.figure()
#plt.plot(t,sinewave,t,rmssine)
##plt.draw
#plt.show()

#rmssig = RMS(data)
rmssig = RMS.RMS(data)

#crestsig = Crest(data) 
[peak,rms,crestsig] = Crest(data)

#if len(t)< 100000:
##    mpl.RcParams()
#    plt.rcParams['agg.path.chunksize'] = 10000

plt.figure()
plt.plot(t,data)
#plt.show()
#plt.figure()
plt.plot(t,rmssig)
#plt.draw
plt.show()

sd.play(data,fs)

#compwar = Crest(data)
#print(compwar)
#sd.wait()

#sd.stop()
