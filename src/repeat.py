# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 14:47:07 2016

@author: Jee-Bee for jBae (c) 2016
"""
# Repeat sweep } one function
# add zeros    }

# Average the n repeats to one sigle signal

import numpy as np

def srepeat(sig, reps, l0=None, fs=None, addzeros=False):
    """
    Input:
        sig
        reps
        l0(Optional) = length in samples or if it an array T(length time) together
        with fs (sample frequency)
        fs(optional) = sample Frequency
        addzeros = True
    Output:
        repsig = repeated signal
        ursl = unrepeatedsignal length

    TODO:
    - Make ursl optional
    """
    if addzeros is True:
        if (l0 is None) and (fs is None):
            raise ValueError("if addzeros is True l0 AND fs can't be None")
        elif (fs is None) and l0 < 1024:
            raise ValueError("if addzeros is True and fsis None. l0 should be greather than 1024 samples")
        elif (fs is None) and l0 > 1024:
            sig = np.append(sig, np.zeros(l0))
            repsig = np.tile(sig, reps)
            return(repsig, len(sig))
        else:
            sig = np.append(sig, np.zeros(l0*fs))
            repsig = np.tile(sig, reps)
            return(repsig, len(sig))
    else:
        repsig = np.tile(sig, reps)
        return(repsig, len(sig))


def repAvg(repsig, reps, l0=None):
    """
    Input:
        repsig = measured repeated signal
        reps = number of repeats
        l0(optional) = time between repeats... - Not implemented yet
    Output:
        avgsig = averaged signal

    TODO:
    - implement l0
    """
    N = len(repsig)/reps  # signal Length singel signal
    avgsig = np.zeros(N)
    for idx in range(reps):
        avgsig += repsig[idx * N:(idx+1) * N]
    avgsig = avgsig / reps
    return(avgsig)


def mrepeat(sig, reps, channels, l0=None, fs=None, addzeros=False, method=1):
    if method == 1:
        # step 1: repeat chrip signal:
        rep_sig = srepeat(sig, reps, l0, fs, addzeros)
        msig = np.zeros((channels, channels * len(rep_sig)))
        l = len(rep_sig)
        # step 2 place chirps in total lenght signal positions
        for channel in range(channels):
            msig[channel, channel * l: (channel + 1) * l] = rep_sig
    # method 2: chirps in channels; repeat all channels
    elif method == 2:
        sig = srepeat(sig, 1, l0, fs, addzeros)
        l = len(sig)
        msig = np.zeros((channels, channels * len(sig)))
        # step 1 place chirps in single chirp positions
        for channel in range(channels):
            msig[channel, channel * l: (channel + 1) * l] = sig
        # step 2: repeat total signal set:
        msig = srepeat(sig, reps)
    else:
        raise ValueError("method should be a 1 or a 2")
    pass
