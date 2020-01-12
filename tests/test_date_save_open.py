# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 12:26:11 2016

@author: Jee-Bee for jBae (c) 2016
"""

# Check garbage collector interface:
# https://docs.python.org/3.4/library/gc.html

# test datum
import datetime as dt
import numpy as np

# TODO
# Use Enumerate to make arrays/ dictionatys of values/ arrays
# one set of values add to dictionarus at the end.
# make remove function and recalculate enumerate number sequence


# http://stackoverflow.com/questions/7999935/python-datetime-to-string-without-microsecond-component
# http://stackoverflow.com/questions/7588511/format-a-datetime-into-a-string-with-milliseconds
timenow = dt.datetime.now().strftime("%Y%m%dT%H%M%S")


# test save file with date name

# some dummy vars
f = np.array([20, 350])
fs = 44100
T = 20

t = np.arange(0, T, 1/fs)
sig = np.sin(2 * np.pi * (f[1] - f[0]) / T * t)

# http://stackoverflow.com/questions/11553721/using-a-string-variable-as-a-variable-name
# http://stackoverflow.com/questions/2220699/whats-the-difference-between-eval-exec-and-compile-in-python

# Timestamp
exec("timeStamp" + timenow + " = timenow")

exec("f" + timenow + " = f")
exec("fs" + timenow + " = fs")
exec("T" + timenow + " = T")
exec("sig" + timenow + " = sig")
# exec("sigtype" + timenow + " = sigtype")
exec("m" + timenow + " = sig")  # for now Measurement = signal
# exec("itterations" + timenow + " = itterations")
# exec("wintype" + timenow + " = wintype")
# exec("winlength" + timenow + " = winlength")
# exec("F" + timenow + " = F")  # for now FFT frequency range
# exec("M" + timenow + " = M")  # for now FFT Measurement = signal
# exec("H0" + timenow + " = H0")  # for now FFT Transfer function
# exec("ir" + timenow + " = ir")  # for now impulse response
# exec("irmethod" + timenow + " = irmoethod")  # not implemented
# add optional spectra how to ??
# add measurements units
# save figures only


ts_names = []
for name in locals():
    if "timeStamp" in name:
        ts_names.append(name)
        print(name, eval(name))


for name in ts_names:
    dummy = dict()
    for locname in locals():
        # if "save_data" + str(eval(name))) in locname:
        if str(eval(name)) in locname and (locname != "save_data" + eval(name)):
            # print("Yes")
            print(name, locname, len(eval(name)))
            dummy[str(locname[0:-len(eval(name))])] = eval(locname)
        # else:
            # print("No")
    exec("save_data" + eval(name) + " = dummy")


all_data = dict()
for name in locals():
    if "save_data" in name:
        all_data[str(eval(name))] = eval(name)

sd_names = []
for name in locals():
    if "save_data" in name:
        sd_names.append(name)

# save multiple vars
from tempfile import TemporaryFile
measout = TemporaryFile()
np.save("measout", all_data)

measout_names = TemporaryFile()
np.savez("measout_names", eval(str(sd_names)))

#
# -------------- temp code from here --------------
#

# timenow = dt.datetime.now().replace(microsecond=0).isoformat()
# timenow = dt.datetime.now()
# timenow = timenow.replace(microsecond=0)
# time = timenow.isoformat()

# http://stackoverflow.com/questions/633127/viewing-all-defined-variables
# for name in vars():  #.keys():
#     print(name)
# and
# for value in vars().values():
#     print(value)


# existing_vars = locals()
# for dict in temp_vars:
#     if dict.name
#     print(dict)
