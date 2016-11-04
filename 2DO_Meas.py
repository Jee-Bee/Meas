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
# |_ time plot          5     22 Mar 2016 50%
# |_ Freq plot/ bode    5     22 Mar 2016 50%
# |_ spectrum time      4     22 Mar 2016 50% (Spectogram)
# |_ Waterfall          4
# |_ 1/n oct bar plot   0     
# |_ zero poles         1
# |_                    0
# |_ Live updating      2     (FuncAnimation in Matplotlib)
# Spectra (make Clasas??)
# |_ FFT/ DFT = AS = LS 5    12 Feb 2016
# |_ PS [W]             5
# |_ (A)SD = LSD        3  [V/sqrt(Hz)] (LSD = Linear Spectrum Denisty)
# |_ PSD [W/Hz]         5    20 Feb 2016
# |_ ESD [W*s/Hz]       3
# |_ ENBW (Effective Noise Band With)
# |_ Normalized Equivalent Noise BandWidth (See Window >> 395068.pdf)
# |_ 1/n bands                14 Feb 2016 (1/3 and 1/1 bands)
# V^2 * Hz−1 for the PSD and V^2*s * Hz−1 for the ESD (energy spectral density)
# |_ multi channel
# Transforms (make class)
# |_ Fourier FFT/ DFT   5    12 Feb 2016() just data no real/imag  or Amp phase; no smooting and windowing
#    |_ Wrap phase      3
#    |_ STFT
#    |_ compare different FFT tools:
#       - PyFFTW
#       - scikit-Cuda
#       - reikna (follow up of pyfft)
#       -- See http://stackoverflow.com/questions/6365623/improving-fft-performance-in-python
# |_ Laplace/ Z-trans   0
# |_ Transferfunction   2    12 Feb 2016 (No exeptions or extra parameters)
# |_ Impulse response   2    13 Mar 2016
# |_ Cepstrum           0
# |_ more options Discrete (Co)Sine Transform (DCT/DST) Hilbert transform ...
# ... Whas it tilbert an realtransform
# Measuremnets (class)
# |_ Add Class??
# |_ play/rec audio     5    30 Jan 2016
# |_ play/rec vibr      1
#   |_ pyVISA
#   |_ py-IVI
#   |_ see: ivifoundation.org
# |_Impact              1
#   |_ buffer wait      0
#   |_ gate
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
# |_ RMS                5       04 Feb 2016
# |_ peak finder        2
# |_ interpolation      2
# |_ avereiging         3
#   |_ SMA (Simple Moving Avg)  05 Feb 2016
#   |_ CMA (Cumalative)         22 Feb 2016
#   |_ WMA (Weighted)
#   |_ EMA (Exponential)
# |_ Windowfunction     4
#   |_ Overlap (spectrum)
#   |_ (Overlap correlation)   3 Mar 2016
#   |_ Recomend Overlab ROV    3 Mar 2016 (See Window >> 395068.pdf)
#   |_ Frequency bin calculations
#   |_ WOSA (Welch’s Overlapped Segmented Average) (See Window >> 395068.pdf)
# |_ Smoothing          3
# |_ Masking (Error at value level/ missing values... see numpy.mask)



# multi signal analysis ((sub class of transform/spectra))
# Mel Cepstrum Coefficents
# cross-correlation
# Convolution
# autocorrelation
# |_ http://dsp.stackexchange.com/questions/27451/the-difference-between-convolution-and-cross-correlation-from-a-signal-analysis
# Correlation Coefficient
# |_ http://dsp.stackexchange.com/questions/9797/cross-correlation-peak

# Signal quality
# |_ Crest factor       2     8 feb 2016
# (peak to peak versus avg noise)
# |_ THD
# |_ SNR
# |_ LSB (Least Significant Bit) 15 Feb 2016

# Diverse
# Dimesions             4 [Volt/ g/ Hz/ Pa/ mV etc Nob = Number of Bits]
# Phase direction       0
# group delay
# RT60
# Save Auto name date
# Weighting(A B C and D)     24 Feb 2016
# |_ FFT values         3    09 feb 2016
# |_ Transfer functions 1
# Buffer
# Filters ?
# ERROR                 4
# Linking folders       5   07 Feb 2016
# git Repository        5   05 Feb 2016
# Garbage Collector

# GUI  (Make class??)
# |_ layout             4    13 Mar 2016
# |_ Coupling Py        4
# |_ graphs if needed   0
# |_ Live update plot   2
# Defaults              2
# Version manager

# Moving targets detection
# Direction sound comming
