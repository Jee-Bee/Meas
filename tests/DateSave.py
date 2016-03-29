# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 12:26:11 2016

@author: Jee-Bee for jBae (c) 2016
"""


# test datum
import datetime as dt

# http://stackoverflow.com/questions/7999935/python-datetime-to-string-without-microsecond-component
# http://stackoverflow.com/questions/7588511/format-a-datetime-into-a-string-with-milliseconds
timenow = dt.datetime.now().strftime("%Y%m%dT%H%M%S")

#timenow = dt.datetime.now().replace(microsecond=0).isoformat()
# timenow = dt.datetime.now()
# timenow = timenow.replace(microsecond=0)
# time = timenow.isoformat()


# test save file with date name
import numpy as np

Save_File = True

# some dummy vars
f = np.array([20, 350])
fs = 44100
T = 10


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
# eval(timenow + " = sig")
exec("m" + timenow + " = sig")  # for now Measurement = signal

#existing_vars = locals()
#for dict in temp_vars:
#    if dict.name 
#    print(dict)

#http://stackoverflow.com/questions/633127/viewing-all-defined-variables
for name in vars().keys():
    print(name)
#and
#for value in vars().values():
#    print(value)

if Save_File == True:
    print("\n")
    ts_names = []
    for name in dir():
        if "timeStamp" in name:
            ts_names.append(name)
            print(name)


    #for name in ts_names:
    #    print(exec(name))
    #    exec("save_data" + name + " = dict()")
    #    for locname in locals():
    #        if name in locals():
    #            exec("save_data" + name + ".append(name: name[0])")
    #            print(name)

    # save multiple vars
    #np.savez()
else:
    print("File Not Saved \n")