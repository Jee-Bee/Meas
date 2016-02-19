# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 14:00:45 2016

@author: Jee-Bee for jBae (c) 2016
"""

import numpy as np

class Windows(object):
    
    def __init__(self, N):
        self.N = N
#        pass

# B slpine Windows:
# Rectangular: k = 1 (st order)
# Triangular: k = 2 (nd Order)
# Parzen: k = 4 (th order)

    def rectwind(N):
        w = np.ones(N)
        x = np.arange(0,N-1,1)
        return(w,x)

    def triwind(N):
        w=np.zeros(N)
        x=np.zeros(N)
        for idx in range(N):
            w[idx] = 1-abs((idx-((N-1)/2))/(N/2))
            x[idx] = idx
        return (w,x)

    def partzwind(N):
        w=np.zeros(int(N/2))
        x=np.zeros(int(N/2))
        for idx in range(int(N/2)):
            x[idx] = idx
            if (idx >= 0) and (idx <= (N/4)):
                w[idx] = 1-(6*(idx/(N/2))**2) * (1- abs(idx)/(N/2))
            elif(idx >= N/4) and (idx <= (N/2)):
                w[idx] = 2*(1- abs(idx)/(N/2))**3
        x = np.append(x,x +int(N/2));
        w = np.append(w[::-1],w)
        return (x,w)
##    if (idx < 3) == True:

#
# -----------------------------------------------------------------------------
#

    def genhamwind(N,alpha,beta):
        w=np.zeros(N)
        x=np.zeros(N)
        for idx in range(N):
            w[idx] = alpha - beta * np.cos((2*np.pi*idx)/(N-1))
            x[idx] = idx
        return (x,w)

    def hanwind(N):
        alpha = beta = 0.5
        [x,w] = genhamwind(N,alpha,beta)
        return (x,w)

    def hamwind(N):
        alpha =  0.53836
        beta = 1 - alpha
        [x,w] = genhamwind(N,alpha,beta)
        return (x,w)

#
# -----------------------------------------------------------------------------
#

    def coswind (N):
        w = np.zeros(N)
        x = np.zeros(N)
        alpha = 1  # rectangular window alpha = 0; cos window alpha = 1; Hann window alpha =2.
        for idx in range(N):
            w[idx] = np.cos((np.pi * idx/(N-1)) - np.pi/2)**alpha
            x[idx] = idx
        return (x,w)

#
# -----------------------------------------------------------------------------
#

    def gengausswind(N,sigma,p): 
        w = np.zeros(N)
        x= np.zeros(N)
        for idx in range(N):
            num = idx-(N-1)/2
            denum = sigma*(N-1)/2
            w[idx] = np.e**((-1/2)*( num/denum )**p )
            x[idx] = idx
        return (x,w)

    def gausswind(N): 
        sigma = 0.5
        p = 2
        [x,w] = gengausswind(N,sigma,p)
        return (x,w)

#
# -----------------------------------------------------------------------------
#

    def Tukeywind (N):
        w = np.zeros(N)
        x = np.zeros(N)
        alpha = 0.5
        for idx in range(N):
            if idx <= int(alpha*(N-1)/2):
               w[idx] = 1/2*(1 + np.cos(np.pi*(2*idx/(alpha * (N-1)) -1) ) )
               x[idx] = idx
            elif idx >= int(alpha*(N-1)/2) and idx <= int((N-1)*(1-alpha/2)):
                w[idx] = 1
                x[idx] = idx
            elif idx >= int((N-1)*(1-alpha/2)) and idx <= (N-1):
                w[idx] = 1/2*(1 + np.cos(np.pi*(2*idx/(alpha * (N-1)) - 2/alpha + 1) ) )
                x[idx] = idx
        return (x,w)


#
# -----------------------------------------------------------------------------
#

# Frome here calculate Overlab carcteristics:
    def Overlap_Characterestics(self, Window_type, accurency):
#        Calculate AF = Min/Max
#        Calculate PF
#        Calculate OC 
#        See 395068 Window Document: 
#            Spectrum and spectral density estimation by the Discrete Fourier
#            transform (DFT), including a comprehensive list of window
#            functions and some new at-top windows.
        pass
    
    def ROV (self, Window_type):
#        Input are values from Input characteresitcs
        pass
    