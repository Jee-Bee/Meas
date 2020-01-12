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
    pathscripts = "src/"
elif sys.platform.startswith('win32'):
    currentdir = os.path.dirname(os.path.realpath(__file__))
    pathtests = "tests\\"
    pathscripts = "src\\"
elif sys.platform.startswith('cygwin'):
    currentdir = os.path.dirname(os.path.realpath(__file__))
    pathtests = "tests\\"
    pathscripts = "src\\"
elif sys.platform.startswith('darwin'):
    pass


# Run script from path
from tests import print_script
print_script


from tests import simple_plot
simple_plot # figures don't work...

#runningscript = "noise_test.py"
#runningscript = "simple_plot.py"