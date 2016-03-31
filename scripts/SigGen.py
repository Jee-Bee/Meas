# -*- coding: utf8 -*-
"""
Created on Wed Mar  9 19:06:07 2016

@author: Jee-Bee for Jbae (c) 2016
"""
#import MeasWarning
import scripts.MeasError


class SigGen(object):
    def __init__():
        pass

    def varlist(var, length):
        from numpy import array
        if len(array(var)) > length:
    #        msg =
            raise MeasWarning.DimWarning (length, 'list is to long only first ' + str(length) + ' paramerets will be used' )
            return(False, True)
        elif len(array(var)) < length:
            raise MeasWarning.DimWarning(length, 'list is to short ' + str(length) + ' is less than required')
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
        t = np.linspace(0, T - (1 / fs), T * fs)
        if gentype == "Sine":
            if varlist(f, 1) == (True, True):
                f0 = f
                Sig = np.sin(2 * np.pi * f0 * t)
            elif varlist(f, 1) == (False, True):
                f0 = f[0]
                Sig = np.sin(2 * np.pi * f0 * t)
            else:
                Sig = []
                raise MeasError.EmptyError(sig, 'Nothing to return')
        elif gentype == "Sawtooth":
            if varlist(f, 1) == (True, True):
                f0 = f
                Sig = sig.Sawtooth(2 * np.pi * f0 * t)
            elif varlist(f, 1) == (False, True):
                f0 = f[0]
                Sig = sig.Sawtooth(2 * np.pi * f0 * t)
            else:
                Sig = []
                raise MeasError.EmptyError(sig, 'Nothing to return')
        elif gentype == 'Square':
            if varlist(f, 1) == (True, True):
                f0 = f
                Sig = sig.Square(2 * np.pi * f0 * t)
            elif varlist(f, 1) == (False, True):
                f0 = f[0]
                Sig = sig.Square(2 * np.pi * f0 * t)
            else:
                Sig = []
                raise MeasError.EmptyError(sig, 'Nothing to return')
        elif gentype == 'Triangle':
            if varlist(f, 1) == (True, True):
                f0 = f
                Sig = sig.Sawtooth(2 * np.pi * f0 * t, width=0.5)
            elif varlist(f, 1) == (False, True):
                f0 = f[0]
                Sig = sig.Sawtooth(2 * np.pi * f0 * t, width=0.5)
            else:
                Sig = []
                raise MeasError.EmptyError(sig, 'Nothing to return')
        elif gentype == 'ChirpLin':
            if varlist(f, 2) == (True, True):
                f0 = f[0]
                f1 = f[1]
                Sig = sig.chirp(t, f0, T, f1, 'linear', 90)
            elif varlist(f, 2) == (False, True):
                f0 = f[0]
                f1 = f[1]
                Sig = sig.chirp(t, f0, T, f1, 'linear', 90)
            else:
                Sig = []
                raise MeasError.EmptyError(sig, 'Nothing to return')
            # http://docs.scipy.org/doc/scipy-0.17.0/reference/generated/scipy.signal.chirp.html
        elif gentype == 'ChirpLog':
            if varlist(f, 2) == (True, True):
                f0 = f[0]
                f1 = f[1]
                Sig = sig.chirp(t, f0, T, f1, 'logarithmic', 90)
            elif varlist(f, 2) == (False, True):
                f0 = f[0]
                f1 = f[1]
                Sig = sig.chirp(t, f0, T, f1, 'logarithmic', 90)
            else:
                Sig = []
                raise MeasError.EmptyError(sig, 'Nothing to return')
            # http://docs.scipy.org/doc/scipy-0.17.0/
        elif gentype == 'Wnoise':  # White Noise
            Sig = np.random.normal(0, 1, len(t))
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
        return(Sig, t)

# SigGen.py
# Created by Jee-Bee for jBae 2015(c)
