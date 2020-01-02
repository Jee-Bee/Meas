# -*- coding: utf8 -*-
"""
Created on Wed Mar  9 19:06:07 2016

@author: Jee-Bee for Jbae (c) 2016
"""
#import MeasWarning
from scripts.measerror import MeasError


class SigGen(object):
    def __init__(self):
        pass

    def varlist(self, var, length):
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
        # Creating signal generator:
        # Options gentype: Sine; Sawtooth; Triangle; Square PW; ...
        # White/Pink noise; Chirp; Poly Chirp
        # http://stackoverflow.com/questions/919680/can-a-variable-number-of-arguments-be-passed-to-a-function
        import numpy as np
        import scipy.signal as sig
        f = np.array(f)
        if gentype == "Sine":
            if SigGen.varlist(f, 1) == (True, True):
                f0 = f
                ps = fs / f  # samples per period
                periods = np.ceil(T * fs / ps)
                T = periods * ps / fs

                t = np.arange(0, T * fs)/fs
                Sig = np.sin(2 * np.pi * f0 * t)
                return(Sig, t)
            elif SigGen.varlist(f, 1) == (False, True):
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
            if SigGen.varlist(f, 1) == (True, True):
                f0 = f
                ps = fs / f  # samples per period
                periods = np.ceil(T * fs / ps)
                T = periods * ps / fs

                t = np.arange(0, T * fs)/fs
                Sig = sig.Sawtooth(2 * np.pi * f0 * t)
                return(Sig, t)
            elif SigGen.varlist(f, 1) == (False, True):
                f0 = f[0]
                ps = fs / f  # samples per period
                periods = np.ceil(T * fs / ps)
                T = periods * ps / fs

                t = np.arange(0, T * fs)/fs
                Sig = sig.Sawtooth(2 * np.pi * f0 * t)
                return(Sig, t)
            else:
                # Sig = []
                raise MeasError.EmptyError(sig, 'Nothing to return')
        elif gentype == 'Square':
            if SigGen.varlist(f, 1) == (True, True):
                f0 = f
                ps = fs / f  # samples per period
                periods = np.ceil(T * fs / ps)
                T = periods * ps / fs

                t = np.arange(0, T * fs)/fs
                Sig = sig.Square(2 * np.pi * f0 * t)
                return(Sig, t)
            elif SigGen.varlist(f, 1) == (False, True):
                f0 = f[0]
                ps = fs / f  # samples per period
                periods = np.ceil(T * fs / ps)
                T = periods * ps / fs

                t = np.arange(0, T * fs)/fs
                Sig = sig.Square(2 * np.pi * f0 * t)
                return(Sig, t)
            else:
                # Sig = []
                raise MeasError.EmptyError(sig, 'Nothing to return')
        elif gentype == 'Triangle':
            if SigGen.varlist(f, 1) == (True, True):
                f0 = f
                ps = fs / f  # samples per period
                periods = np.ceil(T * fs / ps)
                T = periods * ps / fs

                t = np.arange(0, T * fs)/fs
                Sig = sig.Sawtooth(2 * np.pi * f0 * t, width=0.5)
                return(Sig, t)
            elif SigGen.varlist(f, 1) == (False, True):
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
            from scripts.window import Window
            if SigGen.varlist(f, 2) == (True, True):
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
            Sig_unw = sig.chirp(t, f0, T, f1, 'linear', 90)  # unwindowed Signal
            # phi = (f0 * (f1 / f0) ** (t[-4:] / T)) % np.pi

            if factor_f < 2:
                # print error
                raise ValueError('variable f1 < as fs/2')
            elif round(factor_f, 0) < 3:
                wl = 2  # window lenght
                dsample = len(Sig_unw) % wl  # delta in samples between mod (x/windw length)
                dW = wl/2 # dW = delta Window
                # overlap = 0.5
            elif round(factor_f, 0) < 6:
                wl = 4  # window lenght
                dW = wl/2 # dW = delta Window
                # overlap = 0.5
            elif round(factor_f, 0) < 13:
                wl = 8  # window lenght
                dsample = len(Sig_unw) % wl  # delta in samples between mod (x/windw length)
                dW = wl/2 # dW = delta Window
                # overlap = 0.5
            else:
                wl = 16  # window lenght
                dsample = len(Sig_unw) % wl  # delta in samples between mod (x/windw length)
                dW = wl/2 # dW = delta Window
                # overlap = 0.5
            hanwindow = window(wl)  # window
            dummy, W = hanwindow.hanwind()
            dsample = len(Sig_unw) % wl  # delta in samples between mod (x/windw length)
            if dsample == 0:
                Sig = np.zeros(len(Sig_unw))
                # ul = np.arange((len(Sig_unw) - (wl - 1)) / 2) * 2
            else:
                Sig_unw = np.append(Sig_unw, np.zeros(wl - dsample))
                t = np.arange(0, len(Sig_unw))/fs
                Sig = np.zeros(len(Sig_unw))
            ul = np.arange((len(Sig_unw) - (wl - 1)) / dW) * dW # dW = delta Window
            it = np.nditer(np.int_(ul), flags=['buffered'], casting='same_kind')  # , 'external_loop'])
            for idx in it:
                Sig[idx:idx + wl] += Sig_unw[idx:idx + wl] * W
            return(Sig, t)
            # http://docs.scipy.org/doc/scipy-0.17.0/reference/generated/scipy.signal.chirp.html
        elif gentype == 'ChirpLog':
            # http://dsp.stackexchange.com/questions/30245/clicks-at-end-of-chirp-signal
            from scripts.window import Window
            if SigGen.varlist(f, 2) == (True, True):
                f0 = f[0]
                f1 = f[1]
            elif SigGen.varlist(f, 2) == (False, True):
                f0 = f[0]
                f1 = f[1]
            else:
                Sig = []
                raise MeasError.EmptyError(sig, 'Nothing to return')
            t = np.arange(0, T * fs)/fs

            factor_f = fs/f1  # factor fs/f1
            T = T - (np.ceil(factor_f) + 1) / fs
            Sig_unw = sig.chirp(t, f0, T, f1, 'linear', 90)  # unwindowed Signal
            # phi = (f0 * (f1 / f0) ** (t[-4:] / T)) % np.pi

            if factor_f < 2:
                # print error
                raise ValueError('variable f1 < as fs/2')
            elif round(factor_f, 0) < 3:
                wl = 2  # window lenght
                dsample = len(Sig_unw) % wl  # delta in samples between mod (x/windw length)
                dW = wl/2 # dW = delta Window
                # overlap = 0.5
            elif round(factor_f, 0) < 6:
                wl = 4  # window lenght
                dW = wl/2 # dW = delta Window
                # overlap = 0.5
            elif round(factor_f, 0) < 13:
                wl = 8  # window lenght
                dsample = len(Sig_unw) % wl  # delta in samples between mod (x/windw length)
                dW = wl/2 # dW = delta Window
                # overlap = 0.5
            else:
                wl = 16  # window lenght
                dsample = len(Sig_unw) % wl  # delta in samples between mod (x/windw length)
                dW = wl/2 # dW = delta Window
                # overlap = 0.5
            hanwindow = Window(wl)  # window
            dummy, W = hanwindow.hanwind()
            dsample = len(Sig_unw) % wl  # delta in samples between mod (x/windw length)
            if dsample == 0:
                Sig = np.zeros(len(Sig_unw))
                # ul = np.arange((len(Sig_unw) - (wl - 1)) / 2) * 2
            else:
                Sig_unw = np.append(Sig_unw, np.zeros(wl - dsample))
                t = np.arange(0, len(Sig_unw))/fs
                Sig = np.zeros(len(Sig_unw))
            ul = np.arange((len(Sig_unw) - (wl - 1)) / dW) * dW # dW = delta Window
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
            pass
        elif gentype == 'bnoise':  # Brown noise
            # integral of white noise
            # white noise with random ofset or something like that see wikipedia
            raise MeasError.FunctionError('Bnoise', 'Signal generator Not Implemented (Yet)')
        elif gentype == 'multitone':  # multi sine tone
            raise MeasError.FunctionError('Multitonee', 'Signal generator Not Implemented (Yet)')
        elif gentype == 'ChirpPoly':
            raise MeasError.FunctionError('ChirpPoly', 'Signal generator Not Implemented (Yet)')
            #poly= scipy.signal.sweep_poly(t, poly, phi=0)[source]
            # http://docs.scipy.org/doc/scipy-0.17.0/reference/generated/scipy.signal.sweep_poly.html#scipy.signal.sweep_poly
        else:
            raise MeasError.FunctionError([], 'No Valid Signal generator')

# SigGen.py
# Created by Jee-Bee for jBae 2015(c)
