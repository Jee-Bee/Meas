# Test Script for signal generation and recording:

from scripts import interface, measerror
import sounddevice as sd
from scripts.measwarning import InterfaceWarning

# Soundcard information
(devinfo, devopt) = interface.InterfaceIO()
# print(devinfo, devopt)

try:
    import numpy as np
    import scripts.siggen as sg
    from scripts import transform, checks, weighting, repeat, spectraldistr
    # from importlib.machinery import SourceFileLoader
    import matplotlib.pyplot as plt
    # from scripts.DefaultFigures import Time, SpecMag, SpecPh
    from scripts.defaultfigures import *  # defaultFigures

    T = 5  # [s] T= Time in seconds
    f = (10, 350)  # [Hz] Frequency signal generation
    fs = 44100  # [Hz] fs = Samplerate
    repeats = 3

    RMS_res = True  # other option is 'False'
    crest_res = True  # other option is 'False'
    papr_res = True  # other option is 'False'

    weighting_filt = None  # oher options are the weightings 'A', 'B', 'C' and 'D'
    spectrum = 'AS'  # select spectrum type: AS; PS; SD and PSD respectivelijk
    # for Amplitude Spectrum; Power Spectrum; Spectral Density;
    # Power Spectral Density

    savename = _  # if you want to save the data add name here between " " if
                # not add underscore

    # WARNING:
    # FROM HERE START SCRIP DON EDIT ANYTHING WITHOUT KNOWLEDGE ABOUT MEAS!!

    f = np.array(f)
    (sigout, t) = sg.SigGen.SigGen('ChirpLog', f, T, fs)  # before testing signals etc
    sigout = checks.input_type(sigout)

    # Signal to soundcard

    sigout_rep, new_l = repeat.repSig(sigout, repeats, 2, fs, addzeros=True)

    # sd.default.device = 6  # [6, 1]
    # Simultanious play/ recording
    rec1 = sd.playrec(sigout_rep, fs, channels=2)
    sd.wait()
    # sd.stop()
#    print(dtype(rec1))
    rec1 = checks.input_type(rec1)  # @ Comment till fixed...
    rec1 = rec1.T[0]

    # averaging from here:
    rec1 = repeat.repAvg(rec1, repeats)

    sigout, new_l = repeat.repSig(sigout, 1, 2, fs, addzeros=True)
    t = np.arange(0, len(sigout)) / fs

    # add RMS Crest and PAPR as optional processing
    if (RMS_res is True) or (crest is True) or (papr is true):
        from scripts import rms

        if RMS_res is True:
            sigout = rms.RMS(sigout)   # return RMS value of stard signal
            rec1 = rms.RMS(rec1)   # return RMS value of measurment
        if crest_res is True:
            sigout_crest = rms.Crest(sigout)
            rec1_crest = rms.Crest(rec1)
            print(sigout_crest, rec1_crest)
        if papr_res is True:
            sigout_papr = rms.PAPR(sigout)
            rec1_papr = rms.PAPR(rec1)
            print(sigout_papr, rec1_papr)

    if (weighting_filt is not None) and (spectrum is not None):
        (REC1_F, REC1_S, REC1_P) = transform.FFT(rec1, fs, spectrum='AmPh')
        # REC1_S = Amplitude Spectrum and REC1_P = phase
        # (F, REC1) = Transform.FFT(rec1, fs)

        (F, SIG_S) = transform.FFT(sigout, fs)
        SIG_F = F[1: len(F)/2]
        SIG_S = abs(SIG_S[1:len(SIG_S)/2])
        SIG_P = np.arctan2(np.real(SIG_S[1:len(SIG_S)/2]), np.imag(SIG_S[1:len(SIG_S)/2]))
        if weighting_filt is 'A':
            # Weighted FFT
            AW = weighting.AWeighting()  # temporary off
            REC1_S = AW.A_Weighting(REC1_F, REC1_S)   # temporary off
            SIG_S = AW.A_Weighting(SIG_F, SIG_S)
        elif weighting_filt is 'B':
            BW = weighting.BWeighting()  # temporary off
            REC1_S = BW.B_Weighting(REC1_F, REC1_S)   # temporary off
            SIG_S = BW.B_Weighting(SIG_F, SIG_S)
        elif weighting_filt is 'C':
            CW = weighting.CWeighting()  # temporary off
            REC1_S = CW.C_Weighting(REC1_F, REC1_S)   # temporary off
            SIG_S = CW.C_Weighting(SIG_F, SIG_S)
        elif weighting_filt is 'D':
            DW = weighting.DWeighting()  # temporary off
            REC1_S = DW.D_Weighting(REC1_F, REC1_S)   # temporary off
            SIG_S = DW.D_Weighting(SIG_F, SIG_S)
        else:
            raise ValueError("the value %s is not one of the options for weighting" % weighting_filt)

        if spectrum is 'AS':
            (_, REC1_S, REC1_P) = spectraldistr.AS((REC1_S, REC1_P))
            (_, SIG_S, SIG_P) = spectraldistr.AS((SIG_S, SIG_P))
        elif spectrum is 'PS':
            (_, REC1_S, REC1_P) = spectraldistr.PS((REC1_S, REC1_P))
            (_, SIG_S, SIG_P) = spectraldistr.PS((SIG_S, SIG_P))
        elif spectrum is 'SD':
            (_, REC1_S, REC1_P) = spectraldistr.SD((REC1_S, REC1_P))
            (_, SIG_S, SIG_P) = spectraldistr.SD((SIG_S, SIG_P))
        elif spectrum is 'PSD':
            (_, REC1_S, REC1_P) = spectraldistr.PSD((REC1_S, REC1_P))
            (_, SIG_S, SIG_P) = spectraldistr.PSD((SIG_S, SIG_P))
        else:
            raise ValueError("the value %s is not one of the options for spectrum" % weighting)

    elif weighting_filt is not None:
        (REC1_F, REC1_S, REC1_P) = transform.FFT(rec1, fs, spectrum='AmPh')
        # REC1_S = Amplitude Spectrum and REC1_P = phase
        # (F, REC1) = Transform.FFT(rec1, fs)

        # (F, SIGOUT_amp, SIGOUT_phi, F_1) = Transform.FFT(sigout, fs, spectrum='AmPh')
        (F, SIG_S) = transform.FFT(sigout, fs)
        SIG_F = F[1: len(F)/2]
        SIG_P = np.arctan2(np.real(SIG_S[1:len(SIG_S)/2]), np.imag(SIG_S[1:len(SIG_S)/2]))
        SIG_S = abs(SIG_S[1:len(SIG_S)/2])
        if weighting_filt is 'A':
            # Weighted FFT
            AW = weighting.AWeighting()  # temporary off
            REC1_S = AW.A_Weighting(REC1_F, REC1_S)   # temporary off
            SIG_S = AW.A_Weighting(SIG_F, SIG_S)
        elif weighting_filt is 'B':
            BW = weighting.BWeighting()  # temporary off
            REC1_S = BW.B_Weighting(REC1_F, REC1_S)   # temporary off
            SIG_S = BW.B_Weighting(SIG_F, SIG_S)
        elif weighting_filt is 'C':
            CW = weighting.CWeighting()  # temporary off
            REC1_S = CW.C_Weighting(REC1_F, REC1_S)   # temporary off
            SIG_S = CW.C_Weighting(SIG_F, SIG_S)
        elif weighting_filt is 'D':
            DW = weighting.DWeighting()  # temporary off
            REC1_S = DW.D_Weighting(REC1_F, REC1_S)   # temporary off
            SIG_S = DW.D_Weighting(SIG_F, SIG_S)
    elif spectrum is not None:
        (REC1_F, REC1_S, REC1_P) = transform.FFT(rec1, fs, spectrum='AmPh')
        # (F, REC1) = Transform.FFT(rec1, fs)
        # REC1_S = Amplitude Spectrum and REC1_P = phase

        (F, SIG_S, _) = transform.FFT(sigout, fs)
        SIG_F = F[1: len(F)/2]
        SIG_P = np.arctan2(np.real(SIG_S[1:len(SIG_S)/2]), np.imag(SIG_S[1:len(SIG_S)/2]))
        SIG_S = abs(SIG_S[1:len(SIG_S)/2])
        if spectrum is 'AS':
            (_, REC1_S, REC1_P) = spectraldistr.AS((REC1_S, REC1_P))
            #REC1_F = REC1_F[1:len(REC1_F)/2]
            (_, SIG_S, SIG_P) = spectraldistr.AS((SIG_S, SIG_P))
        elif spectrum is 'PS':
            (_, REC1_S, REC1_P) = spectraldistr.PS((REC1_S, REC1_P))
            #REC1_F = REC1_F[1:len(REC1_F)/2]
            (_, SIG_S, SIG_P) = spectraldistr.PS((SIG_S, SIG_P))
        elif spectrum is 'SD':
            (_, REC1_S, REC1_P) = spectraldistr.SD((REC1_S, REC1_P))
            #REC1_F = REC1_F[1:len(REC1_F)/2]
            (_, SIG_S, SIG_P) = spectraldistr.SD((SIG_S, SIG_P))
        elif spectrum is 'PSD':
            (_, REC1_S, REC1_P) = spectraldistr.PSD((REC1_S, REC1_P))
            #REC1_F = REC1_F[1:len(REC1_F)/2]
            (_, SIG_S, SIG_P) = spectraldistr.PSD((SIG_S, SIG_P))
    else:
        (REC1_F, REC1_S, REC1_P) = transform.FFT(rec1, fs, spectrum='AmPh')
        # (F, REC1) = Transform.FFT(rec1, fs)
        # (F, SIGOUT_amp, SIGOUT_phi, F_1) = Transform.FFT(sigout, fs, spectrum='AmPh')
        (SIG_F, SIG_S) = transform.FFT(sigout, fs)

    # Transfer function:
    (H1) = transform.Transfer(rec1, sigout, fs)  # Rebuild Transfer for ...
    # ... adding two allready calculated spectra

    # Impulse Response:
    (IR, fs_ir, T_ir) = transform.ImpulseResponse(H1, F)  # temporary off
    # Create Var out from IR in To Do List!!

    if len(t) > 100000:
        # mpl.RcParams()
        plt.rcParams['agg.path.chunksize'] = 10000

    # Time plot
    plt.figure()
    timeplt = default2D(t, sigout)
    timeplt.Time()
    timeplt = default2D(t, rec1)
    timeplt.Time()
    plt.axis([4.98, 5, -1, 1])

    # plot half frequency spectrum
    plt.figure()
#    specplt = default2D(REC1_F, REC1_S)
#    specplt.SpecMag()
    specplt = default2D(SIG_F, SIG_S)
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
except measerror.InterfaceError:
    InterfaceWarning("cant play and record at same time")  #, "Sigplayrec.py", 64):


try:
    np.savez(savename, sigout, rec1, fs, SIGOUT, REC1)
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
