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

# some dummy vars
import numpy as np

f = np.array([20, 350])
fs = 44100
T = 10

t = np.arange(0,T,1/fs)
sig = np.sin(2 * np.pi * (f[1] - f[0]) / T * t)

# http://stackoverflow.com/questions/11553721/using-a-string-variable-as-a-variable-name
foo = "bar"
exec(foo + " = sig")
print(len(bar))

timenow = "m" + timenow
# http://stackoverflow.com/questions/2220699/whats-the-difference-between-eval-exec-and-compile-in-python

exec(timenow + " = sig")
#eval(timenow + " = sig")
