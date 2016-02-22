# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 12:26:12 2015

@author: Jee-Bee for jBae (c)
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
from mpl_toolkits.mplot3d import Axes3D
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

class defaultFigures():

    def __init__(self, signalx, signaly, signalz):
#        if len(unit) <= 3:
#            self.unit = unit
#        else:
#            print ("Unit vector is too long")
        self.signalx = signalx
        self.signaly = signaly
        self.signalz = signalz
#        pass


    def Time(self):  #,dimension):  # Dimension is unit type as V(olt) W(att), etc
        plt.plot(self.signalx, self.signaly)
        plt.xlabel('time [s]')  # or sample number
        plt.ylabel('voltage [mV]')  # auto add unit here
        plt.title('')
        plt.grid(True)
        plt.show()
    
    
    def SpecMag(self):  # ,dimension):  # Dimension is unit type as V(olt) W(att), etc
        plt.plot(plt.plot(self.signalx, self.signaly))
        plt.xlabel('frequency [Hz]')  # or frequency bin
        plt.ylabel('voltage [mV]')  # auto add unit here
        plt.title(' ')  # set title
        plt.grid(True)
        plt.show()

    def SpecPh (self):  # ,dimension):  # Dimension is unit type as V(olt) W(att), etc
        plt.plot(plt.plot(self.signalx, self.signaly))
        plt.xlabel('frequency [Hz]')  # or frequency bin
        plt.ylabel('phase [deg]')  # or add radians
        plt.title(' ')  # Set title
        plt.grid(True)
        plt.show()

    def Bode (self,dimension):  # Dimension is unit type as V(olt) W(att), etc
        [m,n] = np.size(self.signaly)
#        magnitude
        plt.subplot(2, 1, 1), plt.plot(self.signalx, self.signaly)
        plt.xlabel('Frequency [Hz]')  # Or sample number
        plt.ylabel('voltage [mV]')  # auto add unit here
        plt.title(' ')  # set title
        plt.grid(True)
#        phase
        plt.subplot(2, 1, 2), plt.plot(self.signalx, self.signaly)
        plt.xlabel('Frequency [Hz]')  # Or sample number
        plt.ylabel('Phase (deg)')  # Or Radians
        plt.title(' ')  # set title
        plt.grid(True)
        plt.show()

    def Spect (self,dimension):  # Dimension is unit type as V(olt) W(att), etc
        Axes3D.plot_surface(self.signalx, self.signaly, self.signalz)
        plt.xlabel('time [s]') # Or Sample number
        plt.ylabel('Frequency [Hz]') # Or Freq Bins number
        plt.zlabel('voltage [mV]') # auto add unit here
        plt.title(' ')  # set title
        plt.grid(True)
        plt.show()

    def water(self, *argv):  # Dimension is unit type as V(olt) W(att), etc
#        http://matplotlib.org/examples/mplot3d/polys3d_demo.html
        Axes3D.plot_surface(self.signalx, self.signaly, self.signalz)  # till better funcion
        plt.xlabel('time [s]') # Or Sample number
        plt.ylabel('Frequency [Hz]') # Or Freq Bins number
        plt.zlabel('voltage [mV]') # auto add unit here
        plt.title(' ')  # set title
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