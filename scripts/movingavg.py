# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 15:29:56 2016

@author: enjbwink
"""
# Simple Moving Average
# https://en.wikipedia.org/wiki/Moving_average

# Simple Moving Averege
# https://en.wikipedia.org/wiki/Moving_average
#       1   P_m + P_(m-1) + ... P_(m-(n-1))   1   n-1
# SMA = - * ------------------------------- = -   SUM p_(m-i)
#       n                 n                   n   i=0

def sma(x,npa):
    sma = np.zeros(len(x))    
    if int(npa) % 2 == 0 :
        npa = int(npa-1)
    for idx1 in range(len(x)):  # calculate mean/ average
        npasum = 0
        for idx2 in range(int(npa)):  # check for zeros
            npaidx = idx2 - np.floor(npa/2)
            if (idx1 + npaidx) <0:             
                npasum = npasum + 0
            elif (idx1 + npaidx) >=len(x):
                npasum = npasum + 0
            else:
                npasum = npasum + x[idx1+npaidx]
        sma[idx1]= npasum/npa
    return (sma)

# Cumelative Moving Average

#def sma(x,npa):
#    sma = np.zeros(len(x))    
#    if int(npa) % 2 == 0 :
#        npa = int(npa-1)
#    for idx1 in range(len(x)):  # calculate mean/ average
#        npasum = 0
#        for idx2 in range(int(npa)):  # check for zeros
#            npaidx = idx2 - np.floor(npa/2)
#            if (idx1 + npaidx) <0:             
#                npasum = npasum + 0
#            elif (idx1 + npaidx) >=len(x):
#                npasum = npasum + 0
#            else:
#                npasum = npasum + x[idx1+npaidx]
#        sma[idx1]= npasum/npa
#    return (sma)

# Weighted Moving Average

#def sma(x,npa):
#    sma = np.zeros(len(x))    
#    if int(npa) % 2 == 0 :
#        npa = int(npa-1)
#    for idx1 in range(len(x)):  # calculate mean/ average
#        npasum = 0
#        for idx2 in range(int(npa)):  # check for zeros
#            npaidx = idx2 - np.floor(npa/2)
#            if (idx1 + npaidx) <0:             
#                npasum = npasum + 0
#            elif (idx1 + npaidx) >=len(x):
#                npasum = npasum + 0
#            else:
#                npasum = npasum + x[idx1+npaidx]
#        sma[idx1]= npasum/npa
#    return (sma)


# Exponential Moving Average

#def sma(x,npa):
#    sma = np.zeros(len(x))    
#    if int(npa) % 2 == 0 :
#        npa = int(npa-1)
#    for idx1 in range(len(x)):  # calculate mean/ average
#        npasum = 0
#        for idx2 in range(int(npa)):  # check for zeros
#            npaidx = idx2 - np.floor(npa/2)
#            if (idx1 + npaidx) <0:             
#                npasum = npasum + 0
#            elif (idx1 + npaidx) >=len(x):
#                npasum = npasum + 0
#            else:
#                npasum = npasum + x[idx1+npaidx]
#        sma[idx1]= npasum/npa
#    return (sma)

###############################################################
#a = np.array([2.,3.,1.,2.,2.,3.,1.,3.,1.,1.])
#smaval = sma(a,3)
#smahand = np.array([5./3, 6./3, 6./3, 5./3, 7./3, 6./3, 7./3, 5./3, 5./3, 2./3])
#
#for idx in range(len(smaval)):
#    print(smaval[idx], smahand[idx])
