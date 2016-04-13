# Test Script for signal generation and recording:

from scripts import Interface
import sounddevice as sd
from scripts.MeasWarning import InterfaceWarning

# Soundcard information
(devinfo, devopt) = Interface.InterfaceIO()
print(devinfo, devopt)

try:
    import numpy as np
    import scripts.SigGen as sg
    from scripts import Transform, Conversion, Weighting
    #from importlib.machinery import SourceFileLoader
    import matplotlib.pyplot as plt
    #from scripts.DefaultFigures import Time, SpecMag, SpecPh
    from scripts.DefaultFigures import *  # defaultFigures


    T = 5  # [s] T= Time in seconds
    f = (10, 350)  # [Hz] Frequency signal generation
    fs = 44100  # [Hz] fs = Samplerate

    f = np.array(f)
    (sigout, t) = sg.SigGen.SigGen('ChirpLog', f, T, fs)  # before testing signals etc
    sigout = Conversion.input_type(sigout)

    # Signal to soundcard

    # sd.default.device = 6  # [6, 1]
    # Simultanious play/ recording
    rec1 = sd.playrec(sigout, fs, channels=2)
    sd.wait()
#    print(dtype(rec1))
    rec1 = Conversion.input_type(rec1)  # @ Comment till fixed...

    rec1 = rec1.T[0]
    # sd.stop()
    (F, REC1) = Transform.FFT(rec1, fs)
    # Transfer function:
    (F, SIGOUT) = Transform.FFT(sigout, fs)

    (H1) = Transform.Transfer(rec1, sigout, fs)  # Rebuild Transfer for ...
    # ... adding two allready calculated spectra

    # Weighted FFT
    AW = Weighting.AWeighting()
    AW_REC1 = AW.A_Weighting(F, REC1)

    # Impulse Response:
    (IR, fs_dummy, T_dummy) = Transform.ImpulseResponse(H1, F)
    # Create Var out from IR in To Do List!!

    if len(t) > 100000:
        # mpl.RcParams()
        plt.rcParams['agg.path.chunksize'] = 10000

    plt.figure()
    timeplt = default2D(t, sigout)
    timeplt.Time()
    timeplt = default2D(t, rec1)
    timeplt.Time()
    plt.axis([4.98, 5,-1, 1])
    plt.figure()
    specplt = default2D(F, REC1)
    specplt.SpecMag()
except MeasError.InterfaceError:
    InterfaceWarning("cant play and record at same time")  #, "Sigplayrec.py", 64):
#    # len(devopt) == 0:
#    message = 'play and record a signal at the same time is not possible'
#except SystemError():
#    raise ("stupid thing")

# 2Do
# https://pypi.python.org/pypi/kaching/0.3

# http://python-sounddevice.readthedocs.org/en/0.3.0/#

# Question stack overflow
# /usr/local/lib/python3.4/dist-packages2.7
# http://stackoverflow.com/questions/67631/how-to-import-a-module-given-the-full-path
