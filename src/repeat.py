# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 14:47:07 2016

@author: Jee-Bee for jBae (c) 2016
"""
# Repeat sweep } one function
# add zeros    }

# Average the n repeats to one sigle signal

import numpy as np


def addzeros(signal, l0, fs=None):
    """
    Input:
        sig
        l0 = length in samples or together with fs (sample frequency) time T
        fs(optional) = sample Frequency
    Output:
        repsig = repeated signal"""
    if fs is not None:
        zero_array = np.zeros(np.int(np.round(l0 * fs)))
    else:
        zero_array = np.zeros(np.int(l0))
    signalwzeros = np.append(signal, zero_array)
    return(signalwzeros)


def srepeat(sig, reps, l0=None, fs=None):
    """ Single repeat:
    Repeat signal n times. l0 is non None than zeros are added.
    Input:
        sig
        reps
        l0(Optional) = length in samples or if it an array T(length time) together
        with fs (sample frequency)
        fs(optional) = sample Frequency
    Output:
        repsig = repeated signal
        sing_length = length of signal
    """
    if l0 is not None:
        sigwzeros = addzeros(sig, l0, fs)
    repsig = np.tile(sig, reps)
    return(repsig, len(sig))


def repAvg(repeated_sig, repeats, l0=None):
    """
    Input:
        repeated_sig = measured repeated signal
        repeats = number of repeats
        l0(optional) = time between repeats... - Not implemented yet
    Output:
        averaged_sig = averaged signal
    TODO:
    - implement l0
    """
    arr_dim = repeated_sig.ndim
    if arr_dim == 1:
        averaged_sig = repeated_sig.reshape(repeats, -1).sum(axis=0) / repeats
        return(averaged_sig)
    else:
        print("be carefull dimension and layout arrray not tested!!")
        channels = repeated_sig.shape[0]  # of 1
        averaged_sig = repeated_sig.reshape(channels, repeats, -1).sum(axis=1) # check output of
        return(averaged_sig)


def mrepeat(sig, reps, channels, l0=None, fs=None, addzeros=False, method=1):
    if method == 1:
        # step 1: repeat chrip signal:
        rep_sig, l = srepeat(sig, reps, l0, fs, addzeros)
        msig = np.zeros((channels, channels * l))
        # step 2 place chirps in total lenght signal positions
        for channel in range(channels):
            msig[channel, channel * l: (channel + 1) * l] = rep_sig
    # method 2: chirps in channels; repeat all channels
    elif method == 2:
        sig, l = srepeat(sig, 1, l0, fs, addzeros)
        msig = np.zeros((channels, channels * len(sig)))
        # step 1 place chirps in single chirp positions
        for channel in range(channels):
            msig[channel, channel * l: (channel + 1) * l] = sig
        # step 2: repeat total signal set:
        msig = srepeat(sig, reps)
    else:
        raise ValueError("method should be a 1 or a 2")
    pass

# repeats = 2
# c = np.arange(6)
# d = c.reshape(repeats,-1)
# # c = array([0, 1, 2, 3, 4, 5])
# # d = array([[0, 1, 2],
# #            [3, 4, 5]])
# a=np.arange(12).reshape(-1,6)  # virtual 2 channels recorded
# a.shape  # = (2, 6)
# channels = a.shape[0]
# # array([[ 0,  1,  2,  3,  4,  5],
# #        [ 6,  7,  8,  9, 10, 11]])
# b = a.reshape(channels,repeats,-1)
# # b = array([[[ 0,  1,  2],
# #             [ 3,  4,  5]],
# #            [[ 6,  7,  8],
# #             [ 9, 10, 11]]])
