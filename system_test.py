# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 20:07:58 2016

@author: Jee-Bee for jBae (c) 2016
"""


# Initial test for testing system.
# unix or OSX or windows...

import sys
import os

if sys.platform.startswith('linux'):
    currentdir = os.path.dirname(os.path.realpath(__file__))
    pathtests = "tests/"
    pathscripts = "scripts/"
elif sys.platform.startswith('win32'):
    pass
elif sys.platform.startswith('cygwin'):
    currentdir = os.path.dirname(os.path.realpath(__file__))
    pathtests = "tests\"
    pathscripts = "scripts\"
elif sys.platform.startswith('darwin'):
    pass


# Run script from path


#runningscript = "noise_test.py"
runningscript = "simple_plot.py"