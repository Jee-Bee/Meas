# Test Script for signal generation and recording:

import numpy as np
import scripts.SigGen as sg


T = 10  # [s] T= Time in seconds
f = (20, 20000)  # [Hz] Frequency signal generation
fs = 44100  # [Hz] fs = Samplerate

f = np.array(f)
(sigout, t) = sg.SigGen('ChirpLog', f, T, fs)  # before testing signals etc
sigout = Conversion.input_check(sigout)

try:
    from scripts import Transform, Interface, Conversion, Weighting
    #from importlib.machinery import SourceFileLoader
    import matplotlib.pyplot as plt
    #from scripts.DefaultFigures import Time, SpecMag, SpecPh
    from scripts.DefaultFigures import *  # defaultFigures
    import sounddevice as sd

    # Signal to soundcard
    # Soundcard information
    (devinfo, devopt) = Interface.InterfaceIO()
    print(devinfo, devopt)
 
    print(devopt)
    
    # sd.default.device = 6  # [6, 1]
    # Simultanious play/ recording
    rec = sd.playrec(sigout, fs, channels=2)
    sd.wait()
    rec = Conversion.input_check(rec)

    # sd.stop()
    rect = rec.T[0]
    (F, REC1) = Transform.FFT(rect, fs)
    # Transfer function:
    (F, SIGOUT) = Transform.FFT(sigout, fs)   
    
    (F, H1) = Transform.Transfer(rec1, sigout, fs)  # Rebuild Transfer for ...
    # ... adding two allready calculated spectra

    # Weighted FFT
    AW = Weightin(REC1)
    AW_REC1 = A-Weighting(REC1)

    # Impulse Response:
    (IR, fs_dummy, T_dummy) = Transform.ImpulseResponse(H, F1)
    # Create Var out from IR in To Do List!!

    plt.figure()
    timeplt = defaultFigures(t, rec, [])
    timeplt.Time()
    plt.figure()
    specplt = defaultFigures(F, REC, [])
    specplt.SpecMag()
except Exeption as len(devopt) == 0:
    print('play and record a signal at the same time is not possible')


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
