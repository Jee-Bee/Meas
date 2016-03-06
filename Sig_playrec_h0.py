# Test Script for signal generation and recording:

import numpy as np
import scipy.signal as sig
#from importlib.machinery import SourceFileLoader

#sd = SourceFileLoader("sounddevice", "/usr/local/lib/python3.4/dist-packages2.7/sounddevice.py").load_module()
#foo.MyClass()
import sounddevice as sd
import matplotlib.pyplot as plt


T = 10  # [s] T= Time in seconds
f = (20, 20000)  # [Hz] Frequency signal generation
fs = 44100  # [Hz] fs = Samplerate

t = np.linspace(0, T - (1 / fs), T * fs)
sig = sig.chirp(t, 20, T, 20000, 'linear', 90)

# Signal to soundcard
# Soundcard information
devinfo = sd.query_devices()
print(devinfo)

# http://python-sounddevice.readthedocs.org/en/0.3.0/#

# playback array
sd.play(sig, fs)

# Record audio
#duration = 10  # seconds
#myrecording = sd.rec(duration * fs, samplerate=fs, channels=2)

# Simultanious play/ recording
#myrecording2 = sd.playrec(signal, fs, channels=2)

plt.plot(t, sig)
plt.show()

# 2Do
# https://pypi.python.org/pypi/kaching/0.3


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

