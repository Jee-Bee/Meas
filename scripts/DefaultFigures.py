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

import matplotlib.pylab as plt
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

def time (timear,signal,dimension):
    plt.plot(timear, signal)    
    plt.xlabel('time (s)')
    plt.ylabel('voltage (mV)')
    plt.title('About as simple as it gets, folks')
    plt.grid(True)
    plt.savefig("test.png")
    plt.show()


def Freq (freqar,signal,dimension):
    plt.plot(freqar, signal)    
    plt.xlabel('time (s)')
    plt.ylabel('voltage (mV)')
    plt.title('About as simple as it gets, folks')
    plt.grid(True)
    plt.savefig("test.png")
    plt.show()

def bode (bodear,signal,dimension):
    plt.plot(bodear, signal)    
    plt.xlabel('time (s)')
    plt.ylabel('voltage (mV)')
    plt.title('About as simple as it gets, folks')
    plt.grid(True)
    plt.savefig("test.png")
    plt.show()

def Spect (specar,signal,dimension):
    plt.plot(specar, signal)    
    plt.xlabel('time (s)')
    plt.ylabel('voltage (mV)')
    plt.title('About as simple as it gets, folks')
    plt.grid(True)
    plt.savefig("test.png")
    plt.show()

def water (waterar,signal,dimension):
    plt.plot(waterar, signal)    
    plt.xlabel('time (s)')
    plt.ylabel('voltage (mV)')
    plt.title('About as simple as it gets, folks')
    plt.grid(True)
    plt.savefig("test.png")
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
