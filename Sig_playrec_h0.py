# Test Script for signal generation and recording:

from scripts import Interface
import sounddevice as sd
from scripts.MeasWarning import InterfaceWarning

# Soundcard information
(devinfo, devopt) = Interface.InterfaceIO()
# print(devinfo, devopt)

try:
    import numpy as np
    import scripts.SigGen as sg
    from scripts import Transform, Conversion, Weighting, Repeat
    #from importlib.machinery import SourceFileLoader
    import matplotlib.pyplot as plt
    #from scripts.DefaultFigures import Time, SpecMag, SpecPh
    from scripts.DefaultFigures import *  # defaultFigures


    T = 5  # [s] T= Time in seconds
    f = (10, 350)  # [Hz] Frequency signal generation
    fs = 44100  # [Hz] fs = Samplerate
    repeats = 3 
    RMS_res = True  # other option is 'False'
    crest_res = True  # other option is 'False'
    papr_res = True  # other option is 'False'

    f = np.array(f)
    (sigout, t) = sg.SigGen.SigGen('ChirpLog', f, T, fs)  # before testing signals etc
    sigout = Conversion.input_type(sigout)

    # Signal to soundcard

    sigout_rep, new_l = Repeat.repSig(sigout, repeats, 2, fs, addzeros=True)

    # sd.default.device = 6  # [6, 1]
    # Simultanious play/ recording
    rec1 = sd.playrec(sigout_rep, fs, channels=2)
    sd.wait()
#    print(dtype(rec1))
    rec1 = Conversion.input_type(rec1)  # @ Comment till fixed...

    rec1 = rec1.T[0]

    # averaging from here:
    rec1_avg = Repeat.repAvg(rec1, repeats)

    sigout, new_l = Repeat.repSig(sigout, 1, 2, fs, addzeros=True)
    t = np.arange(0, len(sigout)) / fs

    # add RMS Crest and PAPR as optional processing
    if (RMS_res is True) or (crest is True) or (papr is true):
        from scripts import RMS

        if RMS_res is True:
            sigout = RMS.RMS(sigout)   # return RMS value of stard signal
            rec1_avg = RMS.RMS(rec1_avg)   # return RMS value of measurment
        if crest_res is True:
            sigout_crest = RMS.Crest(sigout_avg)
            rec1_crest = RMS.Crest(rec1_avg)
            print(asigout_crest, rec1_crest)
        if papr_res is True:
            sigout_papr = RMS.PAPR(sigout)
            rec1_papr = RMS.PAPR(rec1_avg)

    # sd.stop()
    (F_amph, REC1_amp, REC1_phi) = Transform.FFT(rec1_avg, fs, spectrum='AmPh')
    # (F, REC1) = Transform.FFT(rec1, fs)

    # Transfer function:
#    (F, SIGOUT_amp, SIGOUT_phi, F_1) = Transform.FFT(sigout, fs, spectrum='AmPh')
    (F, SIGOUT) = Transform.FFT(sigout, fs)

    (H1) = Transform.Transfer(rec1_avg, sigout, fs)  # Rebuild Transfer for ...
    # ... adding two allready calculated spectra

    # Weighted FFT
    AW = Weighting.AWeighting()  # temporary off
    AW_REC1 = AW.A_Weighting(F_amph, REC1_amp)   # temporary off

    # Impulse Response:
    (IR, fs_ir, T_ir) = Transform.ImpulseResponse(H1, F)  # temporary off
    # Create Var out from IR in To Do List!!

    if len(t) > 100000:
        # mpl.RcParams()
        plt.rcParams['agg.path.chunksize'] = 10000

    # Time plot
    plt.figure()
    timeplt = default2D(t, sigout)
    timeplt.Time()
    timeplt = default2D(t, rec1_avg)
    timeplt.Time()
    plt.axis([4.98, 5, -1, 1])

    # plot half frequency spectrum
    plt.figure()
    specplt = default2D(F_amph, REC1_amp)
    specplt.SpecMag()

    # plot full transferfunction
    plt.figure()
    specplt = default2D(F, H1)
    specplt.SpecMag()

    # Impulse response plot
    # check this on proper recording!!
    t_ir = np.arange(0,T_ir,1/fs)
    plt.figure()
    timeplt = default2D(t_ir, IR)
    timeplt.Time()
except MeasError.InterfaceError:
    InterfaceWarning("cant play and record at same time")  #, "Sigplayrec.py", 64):


try:
    np.savez("Convtest", sigout, rec1, fs, SIGOUT, REC1)
except NameError:
    NameError("Name allready excist or whatever... as long as it works...")


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
