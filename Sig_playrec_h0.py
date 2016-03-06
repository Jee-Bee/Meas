# Test Script for signal generation and recording:

import numpy as np
#import scipy.signal as sig
import scripts.SigGen as sg
from scripts import Transform
#from importlib.machinery import SourceFileLoader
import sounddevice as sd
import matplotlib.pyplot as plt
#from scripts.DefaultFigures import Time, SpecMag, SpecPh
from scripts.DefaultFigures import *  # defaultFigures


T = 10  # [s] T= Time in seconds
f = (20, 20000)  # [Hz] Frequency signal generation
fs = 44100  # [Hz] fs = Samplerate


f = np.array(f)
(sigout, t) = sg.SigGen('Chirp', f, T, fs)  # before testing signals etc

# Signal to soundcard
# Soundcard information
devinfo = sd.query_devices()
print(devinfo)

# Simultanious play/ recording
rec = sd.playrec(sigout, fs, channels=2)
sd.wait()
#sd.stop()
rect = rec.T[0]
[F, REC] = Transform.FFT(rect, fs)

plt.figure()
timeplt = defaultFigures(t, rec, [])
timeplt.Time()
plt.figure()
specplt = defaultFigures(F, REC, [])
specplt.SpecMag()

# 2Do
# https://pypi.python.org/pypi/kaching/0.3

# http://python-sounddevice.readthedocs.org/en/0.3.0/#

# playback array
#sd.play(sig, fs)
#sd.wait()

# Record audio
#duration = 10  # seconds
#myrecording = sd.rec(duration * fs, samplerate=fs, channels=2)


"""
Demo of a simple plot with a custom dashed line.

A Line object's ``set_dashes`` method allows you to specify dashes with
a series of on/off lengths (in points).
"""
#import numpy as np
#import matplotlib.pyplot as plt
#
#
#x = np.linspace(0, 10)
#line, = plt.plot(t, sig, '--', linewidth=2)
#
#dashes = [10, 5, 100, 5]  # 10 points on, 5 off, 100 on, 5 off
#line.set_dashes(dashes)

#plt.show()

# Question stack overflow
# /usr/local/lib/python3.4/dist-packages2.7
# http://stackoverflow.com/questions/67631/how-to-import-a-module-given-the-full-path
