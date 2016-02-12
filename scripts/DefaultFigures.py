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

import numpy as np
import matplotlib.pylab as plt
#import matplotlib as mpl
#http://matplotlib.org/api/mlab_api.html

# what variable needed:
# Signal x axis (t[sec]/ t_samples[-]/ F[Hz]/ Freuencynr[-] / Quefrecy[?])
# Signal y axis (t[sec]/ f[Hz]/Amp [db /V /V RMS / ... ], angle deg/rad)
# Limit X axis
# Limit Y axis
# Label X Axis
# Label Y axis
# Label Z axis
# Title
# Save Yes no + sizes

#http://matplotlib.org/users/shell.html
##create big-expensive-figure
#ioff()      # turn updates off
#title('now how much would you pay?')
#xticklabels(fontsize=20, color='green')
#draw()      # force a draw
#savefig('alldone', dpi=300)
#close()
#ion()      # turn updating back on
#plot(rand(20), mfc='g', mec='r', ms=40, mew=4, ls='--', lw=3)

# save figure:
#plt.savefig("test.png")

def Time (timear,signal):  #,dimension):  # Dimension is unit type as V(olt) W(att), etc
    plt.plot(timear, signal)    
    plt.xlabel('time (s)')
    plt.ylabel('voltage (mV)')
    plt.title('About as simple as it gets, folks')
    plt.grid(True)
    plt.show()


def SpecMag (F,SIGNAL):  #,dimension):  # Dimension is unit type as V(olt) W(att), etc
    plt.plot(F, SIGNAL)    
    plt.xlabel('frequency (Hz)')
    plt.ylabel('voltage (mV)')
    plt.title('About as simple as it gets, folks')
    plt.grid(True)
    plt.show()

def SpecPh (F,SIGNAL):  #,dimension):  # Dimension is unit type as V(olt) W(att), etc
    plt.plot(F, SIGNAL)    
    plt.xlabel('frequency (Hz)')
    plt.ylabel('phase (deg)')
    plt.title('About as simple as it gets, folks')
    plt.grid(True)
    plt.show()

def Bode (bodear,signal,dimension):  # Dimension is unit type as V(olt) W(att), etc
    [m,n] = np.size(bodear)
    plt.plot(bodear, signal)    
    plt.xlabel('time (s)')
    plt.ylabel('voltage (mV)')
    plt.title('About as simple as it gets, folks')
    plt.grid(True)
    plt.show()

def Spect (specar,signal,dimension):  # Dimension is unit type as V(olt) W(att), etc
    plt.plot(specar, signal)    
    plt.xlabel('time (s)')
    plt.ylabel('voltage (mV)')
    plt.title('About as simple as it gets, folks')
    plt.grid(True)
    plt.savefig("test.png")
    plt.show()

def water (waterar,signal,dimension):  # Dimension is unit type as V(olt) W(att), etc
    plt.plot(waterar, signal)    
    plt.xlabel('time (s)')
    plt.ylabel('voltage (mV)')
    plt.title('About as simple as it gets, folks')
    plt.grid(True)
    plt.show()


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
