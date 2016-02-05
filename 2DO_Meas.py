# -*- coding: utf-8 -*-
# Priority
# 5 = High
# 4 = Medium/ High
# 3 = Medium
# 2 = Low/ Medium
# 1 = low
# 0 = undefined/ unknown


# 2Do List Meas:
# FUNCTION          PRIORITY  DATE FINISHED (DATE CHECKED)
# --------------------------------------------------------------------
# Signal generator  (Make Class??)  
# |_ Sine               5     6 Jan 2016
# |_ Chirp              5     6 Jan 2016
# |_ square + DC        5     6 Jan 2016(NO DC/ Duty Cycle)
# |_ Triangle           5     6 Jan 2016
# |_ Sawtooth           5     6 Jan 2016
# |_ White Noise        5     11 Jan 2016
# |_ Pink Noise         3
# |_ brown Noise        1
# |_ multitone          1
# |_ Polychirp          1
# Plots (class?)              
# |_ time plot          5
# |_ Freq plot/ bode    5
# |_ spectrum time      4
# |_ Waterfall          4
# |_ 1/n oct bar plot   0
# |_ zero poles         1
# |_                    0
# |_ Live updating      2     (FuncAnimation in Matplotlib)
# Spectra (make Clasas??)            
# |_ FFT/ DFT = AS      5
# |_ PS [W]             5
# |_ (A)SD [V/sqrt(Hz)] 3
# |_ PSD [W/Hz]         5 
# |_ ESD [W*s/Hz]       3
# V^2 * Hz−1 for the PSD and V^2*s * Hz−1 for the ESD (energy spectral density)
# |_ multi channel
# Transforms (make class)
# |_ Fourier FFT/ DFT   5
#    |_ Wrap phase      3
#    |_ STFT
# |_ Laplace/ Z-trans   0
# |_ Transferfunction   0
# |_ Impulse response   0
# |_ Cepstrum           0
# Measuremnets (class)
# |_ play/rec audio     5
# |_ play/rec vibr      1
# |_Impact              1
#   |_ buffer wait      0
#   |_ save impact      0
# |_ 2 channels         0
# |_ multi channel      0
# |_ sound device select4
#    |_ default selct   4

# Measurement Real Time(class)
# |_ play/rec audio     5
# |_ play/rec vibr      1
# |_ Real time          4
# |_ 2 channels         0
# |_ multi channel      0
# |_ Test signal        3


# Signal improve (sub class of transform/spectra)
# |_ RMS                5       4 - 01 - 2016
# |_ peak finder        2
# |_ avereiging         3
# |_ Windowfunction     4
# |_ Smoothing          3
# |_ Overlap (spectrum)

# multi signal analysis ((sub class of transform/spectra))
# Mel Cepstrum Coefficents 
# cross-correlation
# Convolution
# autocorrelation
# http://dsp.stackexchange.com/questions/27451/the-difference-between-convolution-and-cross-correlation-from-a-signal-analysis

# Signal quality
# |_ Crest factor 
# (peak to peak versus avg noise)
# |_ THD
# |_ SNR

# Diverse
# Dimesions             4 [Volt/ g/ Hz/ Pa/ mV etc]
# Phase direction       0
# group delay
# RT60
# Save Auto name date
# Weighting(A B C and D)
# Buffer
# Filters ?
# ERROR                 4
# Linking folders       5
# git Repository        5

# GUI  (Make class??)               
# |_ layout             0
# |_ button             0
# |_ graphs if needed   0
# |_ Live update plot   2
# Defaults              2


# Moving targets detection
# Direction sound comming
