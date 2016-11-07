# Test Script for signal generation and recording:

T = 5  # [s] T= Time in seconds
f = (10, 350)  # [Hz] Frequency signal generation
fs = 44100  # [Hz] fs = Samplerate
nChannels = 'stereo'  # 'Mono'; 'Stereo' or int value
repeats = 3  # repeating the signal = Averaging the noise

RMS_res = True  # other option is 'False'
crest_res = True  # other option is 'False'
papr_res = True  # other option is 'False'

fftMethod = "FFT"  # optionals FFT or AS both same result.
# for spectrum AS does nothing
weighting_filt = None  # oher options are the weightings 'A', 'B', 'C' and 'D'
spectrum = "SD"  # select spectrum type: AS; PS; SD and PSD respectivelijk
# for Amplitude Spectrum; Power Spectrum; Spectral Density;
# Power Spectral Density

savename = _  # if you want to save the data add name here between " " if
            # not add underscore


# WARNING:
# ----------------------------------------------------------------------
# FROM HERE START SCRIP DON EDIT ANYTHING WITHOUT KNOWLEDGE ABOUT MEAS!!
try:
    import sys
    if sys.version_info.major <3:
        from __future__ import division
    import numpy as np
    # from importlib.machinery import SourceFileLoader
    import matplotlib.pyplot as plt
	import sounddevice as sd
    from src import interface, measerror
    from src.measwarning import InterfaceWarning
    import src.siggen as sg
    from src import transform, checks, weighting, repeat, spectraldistr
    # from src.DefaultFigures import Time, SpecMag, SpecPh
    from src.defaultfigures import *  # defaultFigures

    # Soundcard information
    (devinfo, devopt) = interface.interfaceIO()
    # print(devinfo, devopt)

    f = np.array(f)
    #(sigout, t) = sg.SigGen.SigGen('ChirpLog', f, T, fs)  # before testing signals etc
    # multi channel signal generation
    (sigout, si_sigout, t) = sg.mSigGen('ChirpLog', f, T, fs, nChannels, repeat=repeats, l0=2)
    sigout = checks.convertFloat(sigout)

    # Signal to soundcard

    # replaced by multi channel function
    sigout_rep = np.copy(sigout)
    #sigout_rep, new_l = repeat.srepeat(sigout, repeats, 2, fs, addzeros=True)

    # sd.default.device = 6  # [6, 1]
    # Simultanious play/ recording
    rec1 = sd.playrec(sigout_rep.T, fs, channels=2)
    sd.wait()
    # sd.stop()
#    print(dtype(rec1))
    rec1 = checks.convertFloat(rec1)  # @ Comment till fixed...
    rec1 = rec1.T[0]

    # averaging from here:
    rec1 = repeat.repAvg(rec1, repeats)

    # sigout, new_l = repeat.srepeat(sigout, 1, 2, fs, addzeros=True)
    t = np.arange(0, len(sigout)) / fs

    # add RMS Crest and PAPR as optional processing
    if (RMS_res is True) or (crest is True) or (papr is true):
        from src import rms
        if RMS_res is True:
            sigout = rms.mRMS(sigout)   # return RMS value of stard signal
            rec1 = rms.RMS(rec1)   # return RMS value of measurment
        if crest_res is True:
            sigout_crest = rms.mCrest(sigout)
            rec1_crest = rms.Crest(rec1)
            print(sigout_crest, rec1_crest)
        if papr_res is True:
            sigout_papr = rms.mPAPR(sigout)
            rec1_papr = rms.PAPR(rec1)
            print(sigout_papr, rec1_papr)

    # FFT method
    if (fftMethod is "fft") or (fftMethod is "FFT"):
        SI_F, SI_S, SI_P = transform.mFFT(si_sigout, fs)
        REC1_F, REC1_S, REC1_P = transform.mFFT(rec1, fs)
    elif (fftMethod is "as") or (fftMethod is "AS"):
        SI_F, SI_S, SI_P = spectraldistr.AS(si_sigout, fs)
        REC1_F, REC1_S, REC1_P = spectraldistr.AS(rec1, fs)

    AW = weighting.weighting()
    if weighting_filt is None:
        pass
    elif weighting_filt is "A":
        if np.iscomplex(REC1_S).any() is True:
            SI_F, SI_S, SI_P = AW.Aweighting(SI_F, SI_S)
            REC1_F, REC1_S, REC1_P = AW.Aweighting(REC1_F, REC1_S)
        else:
            SI_F, SI_S, SI_P = AW.Aweighting(SI_F, (SI_S, SI_P))
            REC1_F, REC1_S, REC1_P = AW.Aweighting(REC1_F, (REC1_S, REC1_P))
    elif weighting_filt is "B":
        if np.iscomplex(REC1_S).any() is True:
            SI_F, SI_S, SI_P = AW.Bweighting(SI_F, SI_S)
            REC1_F, REC1_S, REC1_P = AW.Bweighting(REC1_F, REC1_S)
        else:
            SI_F, SI_S, SI_P = AW.Bweighting(SI_F, (SI_S, SI_P))
            REC1_F, REC1_S, REC1_P = AW.Bweighting(REC1_F, (REC1_S, REC1_P))
    elif weighting_filt is "C":
        if np.iscomplex(REC1_S).any() is True:
            SI_F, SI_S, SI_P = AW.Cweighting(SI_F, SI_S)
            REC1_F, REC1_S, REC1_P = AW.Cweighting(REC1_F, REC1_S)
        else:
            SI_F, SI_S, SI_P = AW.Cweighting(SI_F, (SI_S, SI_P))
            REC1_F, REC1_S, REC1_P = AW.Cweighting(REC1_F, (REC1_S, REC1_P))
    elif weighting_filt is "D":
        if np.iscomplex(REC1_S).any() is True:
            SI_F, SI_S, SI_P = AW.Aweighting(SI_F, SI_S)
            REC1_F, REC1_S, REC1_P = AW.Aweighting(REC1_F, REC1_S)
        else:
            SI_F, SI_S, SI_P = AW.Aweighting(SI_F, (SI_S, SI_P))
            REC1_F, REC1_S, REC1_P = AW.Aweighting(REC1_F, (REC1_S, REC1_P))
    else:
        raise ValueError("input for Weighting Doesn Excist")

    if spectrum is None:
        pass
    elif (spectrum is "AS") or (spectrum is "as"):
        pass
    elif (spectrum is "PS") or (spectrum is "ps"):
        if np.iscomplex(REC1_S).any() is True:
            SI_F, SI_S, SI_P = spectraldistr.PS(SI_S, SI_F)
            REC1_F, REC1_S, REC1_P = spectraldistr.PS(REC1_S, REC1_F)
        else:
            SI_F, SI_S, SI_P = spectraldistr.PS((SI_S, SI_P), SI_F)
            REC1_F, REC1_S, REC1_P = spectraldistr.PS((REC1_S, REC1_P), REC1_F)
    elif (spectrum is "SD") or (spectrum is "sd"):
        if np.iscomplex(REC1_S).any() == True:
            SI_S, SI_P, SI_F = spectraldistr.SD(SI_S, SI_F)
            REC1_S, REC1_P, REC1_F = spectraldistr.SD(REC1_S, REC1_F)
        else:
            SI_F, SI_S, SI_P = spectraldistr.SD((SI_S, SI_P), SI_F)
            REC1_F, REC1_S, REC1_P = spectraldistr.SD((REC1_S, REC1_P), REC1_F)
    elif (spectrum is "PSD") or (spectrum is "psd"):
        if np.iscomplex(REC1_S).any() is True:
            SI_F, SI_S, SI_P  = spectraldistr.PSD(SI_S, SI_F)
            REC1_F, REC1_S, REC1_P = spectraldistr.PSD(REC1_S, REC1_F)
        else:
            SI_F, SI_S, SI_P = spectraldistr.PSD((SI_S, SI_P), SI_F)
            REC1_F, REC1_S, REC1_P = spectraldistr.PSD((REC1_S, REC1_P), REC1_F)
    else:
        raise ValueError("Input for Spectrums doesn't excist")

    # Transfer function:
    #print(np.shape(sigout))
    val = len(sigout.T)/3
    sigout_si = sigout.T[:val].T
    (H1, F) = transform.mTransfer(rec1, sigout_si, fs)  # Rebuild Transfer for ...
    # ... adding two allready calculated spectra

    # Impulse Response:
    (IR, fs_ir, T_ir) = transform.mImpulseResponse(H1, F)  # temporary off
    # Create Var out from IR in To Do List!!

#    if len(t) > 100000:
#        # mpl.RcParams()
#        plt.rcParams['agg.path.chunksize'] = 10000
#
#    # Time plot
#    plt.figure()
#    timeplt = default2D(t, sigout)
#    timeplt.Time()
#    timeplt = default2D(t, rec1)
#    timeplt.Time()
#    plt.axis([4.98, 5, -1, 1])
#
#    # plot half frequency spectrum
#    plt.figure()
##    specplt = default2D(REC1_F, REC1_S)
##    specplt.SpecMag()
#    specplt = default2D(SIG_F, SIG_S)
#    specplt.SpecMag()
#
#    # plot full transferfunction
#    plt.figure()
#    specplt = default2D(F, H1)
#    specplt.SpecMag()
#
#    # Impulse response plot
#    # check this on proper recording!!
#    t_ir = np.arange(0,T_ir,1/fs)
#    plt.figure()
#    timeplt = default2D(t_ir, IR)
#    timeplt.Time()
except measerror.InterfaceError:
    raise InterfaceWarning("cant play and record at same time")  #, "Sigplayrec.py", 64):


try:
    np.savez(savename, sigout, rec1, fs, SIGOUT, REC1)
except NameError:
    raise NameError("Name allready excist or whatever... as long as it works...")


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
