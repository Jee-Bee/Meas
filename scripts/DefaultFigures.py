# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 12:26:12 2015

@author: Jee-Bee
"""

# FUNCTION           PRIORITY  DATE FINISHED
# ----------------------------------------------
# Plots               
# |_ time plot        5
# |_ Freq plot/ bode  5
# |_ spectrum time    4
# |_ Waterfall        4
# |_ 1/n oct bar plot
# |_ zero poles       1
# |_                  0
# |_ Live updating    2     (FuncAnimation in Matplotlib)

import from matplotlib.pylab plot
#import matplotlib as mpl
#http://matplotlib.org/api/mlab_api.html

# what variable needed:
# Signal x axis (t[sec]/ F[Hz])
# Signal y axis (t[sec]/ f[Hz]/Amp [db /V /V RMS / ... ])
# Limit X axis
# Limit Y axis
# Label X Axis
# Label Y axis
# Label Z axis
# Title
# Save Yes no + sizes

#

def time (timear,signal,dimension):
    plot(timear, signal)    
    xlabel('time (s)')
    ylabel('voltage (mV)')
    title('About as simple as it gets, folks')
    grid(True)
    savefig("test.png")
    show()


def Freq (freqar,signal,dimension):
    plot(Freqar, signal)    
    xlabel('time (s)')
    ylabel('voltage (mV)')
    title('About as simple as it gets, folks')
    grid(True)
    savefig("test.png")
    show()

def bode (bodear,signal,dimension):
    plot(bodear, signal)    
    xlabel('time (s)')
    ylabel('voltage (mV)')
    title('About as simple as it gets, folks')
    grid(True)
    savefig("test.png")
    show()

def Spect (Specar,signal,dimension):
    plot(specar, signal)    
    xlabel('time (s)')
    ylabel('voltage (mV)')
    title('About as simple as it gets, folks')
    grid(True)
    savefig("test.png")
    show()

def water (waterar,signal,dimension):
    plot(waterar, signal)    
    xlabel('time (s)')
    ylabel('voltage (mV)')
    title('About as simple as it gets, folks')
    grid(True)
    savefig("test.png")
    show()


#def zero (zeeroar,signal,dimension):
#    plot(zeroar, signal)    
#    xlabel('time (s)')
#    ylabel('voltage (mV)')
#    title('About as simple as it gets, folks')
#    grid(True)
#    savefig("test.png")
#    show()

# DefaultFigures.py
# Created by Jee-Bee for jBae 2016(c)
