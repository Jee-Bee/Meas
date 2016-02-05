# -*- coding: utf8 -*-
#
# Input parameters each function
#
# t: T + fs
# Sine: 1* f + t
# Saw: 1 * f + t
# square: 1* f + t + DC
# @ Triangle: 1 * f + t
# Chirp: 2 * f + t + T
# White Noise: t or T
# @ pink Noise: t or T ??
# @ brown Noise: t or T ??

def varlist (var,length):
    if len(var) > length:
#        msg = 
        raise OSError('list is to long only first '+ length +' paramerets will be used' )
        return False
    elif len(var) < length:
        raise OSError('list is to short '+ length +' is less than required' )
        return False
    else:
        return True
        

def SigGen(gentype, f, T, fs,*arg):
    # Creating signal generator:
    # Options gentype: Sine; Sawtooth; Triangle; Square PW; ...
    # White/Pink noise; Chirp; Poly Chirp
    # http://stackoverflow.com/questions/919680/can-a-variable-number-of-arguments-be-passed-to-a-function
    import numpy as np
    import scipy.signal as sig
    
    t = np.linspace(0, T - (1 / fs), T * fs)  
    
    if gentype == "Sine":
        if varlist == True:
            f0 = f
        elif varlist == False:
            f0 = f[0]
        Sig = np.sin(2 * np.pi * f0 * t)
    elif gentype == "Sawtooth":
        if varlist == True:
            f0 = f
        elif varlist == False:
            f0 = f[0]        
        Sig = sig.Sawtooth(2 * np.pi * f0 * t)
    elif gentype == 'Square':
        if varlist == True:
            f0 = f
        elif varlist == False:
            f0 = f[0]        
        Sig = sig.Square(2 * np.pi * f0 * t)
    elif gentype == 'Triangle':
        if varlist == True:
            f0 = f
        elif varlist == False:
            f0 = f[0]        
        Sig = sig.Sawtooth(2 * np.pi * f0 * t,width=0.5)
    elif gentype == 'Chirp':
        if varlist == True:
            break
        elif varlist == False:
            f0 = f[0]
            f1 = f[1]
        sig = sig.chirp(t, f0, T, f1, 'linear',90)
        # http://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.signal.chirp.html
    elif gentype == 'Wnoise':  # White Noise
        sig = np.random.normal(0,1,len(t))
    elif gentype == 'Pnoise':  # Pink noise
        pass
    elif gentype == 'bnoise':  # Brown noise
        # integral of white noise
        # white noise with random ofset or something like that see wikipedia
        pass 
    elif gentype == 'multitone':  # multi sine tone
        pass
    elif gentype == 'ChirpPoly':
        pass
        #poly= scipy.signal.sweep_poly(t, poly, phi=0)[source]
        # http://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.signal.sweep_poly.html#scipy.signal.sweep_poly
    else:
        raise OSError('No Valid Signal generator')
    return(Sig, t)

# SigGen.py
# Created by Jee-Bee for jBae 2015(c)