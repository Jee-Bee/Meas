# -*- coding: utf8 -*-
"""
Created on Wed Mar  9 19:06:07 2016

@author: Jee-Bee for jBae (c) 2016
"""
#import MeasWarning
from src.measerror import MeasError


class SigGen(object):
    def __init__(self):
        super(SigGen, self).__init__(parent)


    def varlist(self, var, length):
        """varlist:
        var list checks the shape of an array compared with an expected length. The following situations are possible:
        array - var > than expected length
        array - var < than expected length
        array - var == to expected length"""
        from numpy import array
        self.var = var
        self.length = length
        if len(array(self.var)) > self.length:
    #        msg =
            # raise MeasWarning.DimWarning (length, 'list is to long only first ' + str(length) + ' paramerets will be used' )
            return(False, True)
        elif len(array(var)) < length:
            # raise MeasWarning.DimWarning(length, 'list is to short ' + str(length) + ' is less than required')
            return(False, False)
        else:
            return(True, True)
    
    # for generating sounds is time array not importand...
    # for generating plots is time array importand!!
    def SigGen(gentype, f, T, fs, *arg):
        """Creating signal generator:
        Options gentype: Sine; Sawtooth; Triangle; Square PW; ...
        White/Pink noise; Chirp; Poly Chirp"""
        # http://stackoverflow.com/questions/919680/can-a-variable-number-of-arguments-be-passed-to-a-function
        import numpy as np
        import scipy.signal as sig
        sg = SigGen()
        f = np.array(f)
        if gentype == "Sine":
            if sg.varlist(f, 1) == (True, True):
                f0 = f
                ps = fs / f  # samples per period
                periods = np.ceil(T * fs / ps)
                T = periods * ps / fs

                t = np.arange(0, T * fs)/fs
                Sig = np.sin(2 * np.pi * f0 * t)
                return(Sig, t)
            elif sg.varlist(f, 1) == (False, True):
                f0 = f[0]
                ps = fs / f  # samples per period
                periods = np.ceil(T * fs / ps)
                T = periods * ps / fs

                t = np.arange(0, T * fs)/fs
                Sig = np.sin(2 * np.pi * f0 * t)
                return(Sig, t)
            else:
                # Sig = []
                raise MeasError.EmptyError(sig, 'Nothing to return')
        elif gentype == "Sawtooth":
            if sg.varlist(f, 1) == (True, True):
                f0 = f
                ps = fs / f  # samples per period
                periods = np.ceil(T * fs / ps)
                T = periods * ps / fs

                t = np.arange(0, T * fs)/fs
                Sig = sig.Sawtooth(2 * np.pi * f0 * t, width=width)
                return(Sig, t)
            elif SigGen.varlist(f, 1) == (False, True):
                f0 = f[0]
                ps = fs / f  # samples per period
                periods = np.ceil(T * fs / ps)
                T = periods * ps / fs

                t = np.arange(0, T * fs)/fs
                Sig = sig.Sawtooth(2 * np.pi * f0 * t, width=width)
                return(Sig, t)
            else:
                # Sig = []
                raise MeasError.EmptyError(sig, 'Nothing to return')
        elif gentype == 'Square':
            if sg.varlist(f, 1) == (True, True):
                f0 = f
                ps = fs / f  # samples per period
                periods = np.ceil(T * fs / ps)
                T = periods * ps / fs

                t = np.arange(0, T * fs)/fs
                Sig = sig.Square(2 * np.pi * f0 * t, duty=duty)
                return(Sig, t)
            elif sg.varlist(f, 1) == (False, True):
                f0 = f[0]
                ps = fs / f  # samples per period
                periods = np.ceil(T * fs / ps)
                T = periods * ps / fs

                t = np.arange(0, T * fs)/fs
                Sig = sig.Square(2 * np.pi * f0 * t, duty=duty)
                return(Sig, t)
            else:
                # Sig = []
                raise MeasError.EmptyError(sig, 'Nothing to return')
        elif gentype == 'Triangle':
            if sg.varlist(f, 1) == (True, True):
                f0 = f
                ps = fs / f  # samples per period
                periods = np.ceil(T * fs / ps)
                T = periods * ps / fs

                t = np.arange(0, T * fs)/fs
                Sig = sig.Sawtooth(2 * np.pi * f0 * t, width=0.5)
                return(Sig, t)
            elif sg.varlist(f, 1) == (False, True):
                f0 = f[0]
                ps = fs / f  # samples per period
                periods = np.ceil(T * fs / ps)
                T = periods * ps / fs

                t = np.arange(0, T * fs)/fs
                Sig = sig.Sawtooth(2 * np.pi * f0 * t, width=0.5)
                return(Sig, t)
            else:
                # Sig = []
                raise MeasError.EmptyError(sig, 'Nothing to return')
        elif gentype == 'ChirpLin':
            from src.window import Window
            if sg.varlist(f, 2) == (True, True):
                f0 = f[0]
                f1 = f[1]
            elif SigGen.varlist(f, 2) == (False, True):
                f0 = f[0]
                f1 = f[1]
            else:
                # Sig = []
                raise MeasError.EmptyError(sig, 'Nothing to return')
            t = np.arange(0, T * fs)/fs

            factor_f = fs/f1  # factor fs/f1
            T = T - (np.ceil(factor_f) + 1) / fs
            # unwindowed Signal =
            Sig_unw = sig.chirp(t, f0, T, f1, 'linear', 90)
            # phi = (f0 * (f1 / f0) ** (t[-4:] / T)) % np.pi

            if factor_f < 2:
                # print error
                raise ValueError('variable f1 < as fs/2')
            elif round(factor_f, 0) < 3:
                wl = 2  # window length
                # overlap = 0.5
            elif round(factor_f, 0) < 6:
                wl = 4  # window length
                # overlap = 0.5
            elif round(factor_f, 0) < 13:
                wl = 8  # window length
                # overlap = 0.5
            else:
                wl = 16  # window length
                # overlap = 0.5
            hanwindow = Window(wl)  # window
            dummy, W = hanwindow.hanwind()
            dsample = len(Sig_unw) % wl  # delta in samples between mod (x/windw length)
            dW = wl / 2  # dW = delta Window
            if dsample == 0:
                Sig = np.zeros(len(Sig_unw))
                # ul = np.arange((len(Sig_unw) - (wl - 1)) / 2) * 2
            else:
                Sig_unw = np.append(Sig_unw, np.zeros(wl - dsample))
                t = np.arange(0, len(Sig_unw))/fs
                Sig = np.zeros(len(Sig_unw))
            ul = np.arange((len(Sig_unw) - (wl - 1)) / dW) * dW  # dW = delta Window
            it = np.nditer(np.int_(ul), flags=['buffered'], casting='same_kind')  # , 'external_loop'])
            for idx in it:
                Sig[idx:idx + wl] += Sig_unw[idx:idx + wl] * W
            return(Sig, t)
            # http://docs.scipy.org/doc/scipy-0.17.0/reference/generated/scipy.signal.chirp.html
        elif gentype == 'ChirpLog':
            # http://dsp.stackexchange.com/questions/30245/clicks-at-end-of-chirp-signal
            from src.window import Window
            if sg.varlist(f, 2) == (True, True):
                f0 = f[0]
                f1 = f[1]
            elif SigGen.varlist(f, 2) == (False, True):
                f0 = f[0]
                f1 = f[1]
            else:
                # Sig = []
                raise MeasError.EmptyError(sig, 'Nothing to return')
            t = np.arange(0, T * fs)/fs

            factor_f = fs/f1  # factor fs/f1
            T = T - (np.ceil(factor_f) + 1) / fs
            # unwindowed Signal =
            Sig_unw = sig.chirp(t, f0, T, f1, 'linear', 90)
            # phi = (f0 * (f1 / f0) ** (t[-4:] / T)) % np.pi

            if factor_f < 2:
                # print error
                raise ValueError('variable f1 < as fs/2')
            elif round(factor_f, 0) < 3:
                wl = 2  # window lenght
                # overlap = 0.5
            elif round(factor_f, 0) < 6:
                wl = 4  # window lenght
                # overlap = 0.5
            elif round(factor_f, 0) < 13:
                wl = 8  # window lenght
                # overlap = 0.5
            else:
                wl = 16  # window lenght
                # overlap = 0.5
            hanwindow = Window(wl)  # window
            dummy, W = hanwindow.hanwind()
            dsample = len(Sig_unw) % wl  # delta in samples between mod (x/windw length)
            dW = wl / 2  # dW = delta Window
            if dsample == 0:
                Sig = np.zeros(len(Sig_unw))
                # ul = np.arange((len(Sig_unw) - (wl - 1)) / 2) * 2
            else:
                Sig_unw = np.append(Sig_unw, np.zeros(wl - dsample))
                t = np.arange(0, len(Sig_unw))/fs
                Sig = np.zeros(len(Sig_unw))
            ul = np.arange((len(Sig_unw) - (wl - 1)) / dW) * dW  # dW = delta Window
            it = np.nditer(np.int_(ul), flags=['buffered'], casting='same_kind')  # , 'external_loop'])
            for idx in it:
                Sig[idx:idx + wl] += Sig_unw[idx:idx + wl] * W
            return(Sig, t)
            # http://docs.scipy.org/doc/scipy-0.17.0/
        elif gentype == 'Wnoise':  # White Noise
            t = np.arange(0, T * fs)/fs
            Sig = np.random.normal(0, 1, len(t))
            return(Sig, t)
        elif gentype == 'Pnoise':  # Pink noise
            raise MeasError.FunctionError('Pnoise', 'Signal generator Not Implemented (Yet)')
        elif gentype == 'bnoise':  # Brown noise
            # integral of white noise
            # white noise with random ofset oid... see wikipedia
            raise MeasError.FunctionError('Bnoise', 'Signal generator Not Implemented (Yet)')
        elif gentype == 'multitone':  # multi sine tone
            raise MeasError.FunctionError('Multitonee', 'Signal generator Not Implemented (Yet)')
        elif gentype == 'ChirpPoly':
            raise MeasError.FunctionError('ChirpPoly', 'Signal generator Not Implemented (Yet)')
            # poly= scipy.signal.sweep_poly(t, poly, phi=0)[source]
            # http://docs.scipy.org/doc/scipy-0.17.0/reference/generated/scipy.signal.sweep_poly.html#scipy.signal.sweep_poly
        else:
            raise MeasError.FunctionError([], 'No Valid Signal generator')

    def mSigGen(gentype, f, T, fs, channels, duty=0.5, width=0, repeat=None, l0=None, cascade=False, medthod=2):
        """mSigGen
        inputs:
            some inputs
        Outputs:
            Output
        Description"""
        import numpy as np
        from scripts.repeat import srepeat, mrepeat
        msig = SigGen(gentype, f, T, fs, duty=0.5, width=0)
        if channels is ('mono' or 'Mono'):
            # mono channel don't have cascade function...
            if (repeat is not None) and (l0 is not None):
                msig = srepeat(msig, repeat, l0, fs, addzeros=True)
            elif l0 is not None:
                msig = srepeat(msig, repeat, l0, fs, addzeros=False)
            else:
                pass
            return(msig)
        elif channels is ('stereo' or 'Stereo'):
            if cascade is True:
                if (repeat is not None) and (l0 is not None):
                    msig = mrepeat(msig, repeat, 2, l0, fs, addzeros=True)
                elif l0 is not None:
                    msig = mrepeat(msig, repeat, 2, l0, fs, addzeros=False)
                else:
                    pass
            elif cascade is False:
                if (repeat is not None) and (l0 is not None):
                    msig = srepeat(msig, repeat, l0, fs, addzeros=True)
                    msig = np.tile(msig, (2, 1))
                elif l0 is not None:
                    msig = srepeat(msig, repeat, l0, fs, addzeros=False)
                    msig = np.tile(msig, (2, 1))
                else:
                    pass
            else:
                pass
            return(msig)
        elif channels is int:
            # Migrate with stereo for less duplication...
            if cascade is True:
                # Create cascade/ serie of signals acc. the number of channels
                if (repeat is not None) and (l0 is not None):
                    msig = mrepeat(msig, repeat, channels, l0, fs, addzeros=True)
                elif l0 is not None:
                    msig = mrepeat(msig, repeat, channels, l0, fs, addzeros=False)
                else:
                    pass
            elif cascade is False:
                # Create cascade/ serie of signals acc. the number of channels
                if (repeat is not None) and (l0 is not None):
                    msig = srepeat(msig, repeat, l0, fs, addzeros=True)
                    msig = np.tile(msig, (channels, 1))
                elif l0 is not None:
                    msig = srepeat(msig, repeat, l0, fs, addzeros=False)
                else:
                    pass
            else:
                pass
            return(msig)
        else:
            raise ValueError("Channels can only handle int or 'mono' or 'stereo'")

# SigGen.py
# Created by Jee-Bee for jBae 2015-2016(c)
