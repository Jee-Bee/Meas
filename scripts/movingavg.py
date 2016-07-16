# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 15:29:56 2016

@author: enjbwink
"""
import numpy as np
# Simple Moving Average
# https://en.wikipedia.org/wiki/Moving_average

# Simple Moving Averege
# https://en.wikipedia.org/wiki/Moving_average
#       1   P_m + P_(m-1) + ... P_(m-(n-1))   1   n-1
# SMA = - * ------------------------------- = -   SUM p_(m-i)
#       n                 n                   n   i=0


def sma(x, npa):  # npa: Number P_Average = length Center point
    """
    input:
        x = an unavaraged array
        npa = Number P_Average and contain length Center point
    output:
        sma = the avaraged signal by a simple moving avarage filter.

    Simple Moving Average
    https://en.wikipedia.org/wiki/Moving_average

          1   P_m + P_(m-1) + ... P_(m-(n-1))   1   n-1
    SMA = - * ------------------------------- = -   SUM p_(m-i)
          n                 n                   n   i=0
    """
    sma = np.zeros(len(x))
    if int(npa) % 2 == 0:
        npa = int(npa - 1)
    for idx1 in range(len(x)):  # calculate mean/ average
        npasum = 0
        for idx2 in range(int(npa)):  # check for zeros
            npaidx = idx2 - np.floor(npa / 2)
            if (idx1 + npaidx) < 0:
                npasum = npasum + 0
            elif (idx1 + npaidx) >= len(x):
                npasum = npasum + 0
            else:
                npasum = npasum + x[idx1 + npaidx]
        sma[idx1] = npasum / npa
    return(sma)


# Cumelative Moving Average
def cma(x, n):
    """
    input:
        x = an unavaraged array
        n = length of n points over wich is avaraged
    output:
        cma = the avaraged signal by a cumelative moving avarage filter.

    Cumulative Moving Average
    https://en.wikipedia.org/wiki/Moving_average

            x_1 + x_2 + ... x_(n-1) + x_n                 x_(n+1) + n * CMA_n
    CMA_n = ----------------------------- and CMA_(n+1) = -------------------
                        n                                          n
    so
                x_(n+1) + n * CMA_n            x_(n+1) - CMA_n
    CMA_(n+1) = ------------------- or CMA_n + ---------------
                        n + 1                        n + 1

    TODO:
    - add when n = 0 is added n is the length of x
    """
    cma = np.zeros(n)
    cma_n = np.sum(x[0:n])/n  # calculate mean/ average
    if n == 0:
        print("this Have to be added later")
        pass  # return(cma)
    else:
        for idx in range(len(x)):
            cma[idx] = cma_n + (x[idx] - cma_n) / (n + 1)
        return (cma)

# Weighted Moving Average

#def sma(x,npa):
#    sma = np.zeros(len(x))
#    if int(npa) % 2 == 0:
#        npa = int(npa - 1)
#    for idx1 in range(len(x)):  # calculate mean / average
#        npasum = 0
#        for idx2 in range(int(npa)):  # check for zeros
#            npaidx = idx2 - np.floor(npa / 2)
#            if (idx1 + npaidx) < 0:
#                npasum = npasum + 0
#            elif (idx1 + npaidx) >= len(x):
#                npasum = npasum + 0
#            else:
#                npasum = npasum + x[idx1 + npaidx]
#        sma[idx1] = npasum / npa
#    return (sma)


# Exponential Moving Average

#def sma(x, npa):
#    sma = np.zeros(len(x))
#    if int(npa) % 2 == 0:
#        npa = int(npa - 1)
#    for idx1 in range(len(x)):  # calculate mean/ average
#        npasum = 0
#        for idx2 in range(int(npa)):  # check for zeros
#            npaidx = idx2 - np.floor(npa / 2)
#            if (idx1 + npaidx) < 0:
#                npasum = npasum + 0
#            elif (idx1 + npaidx) >= len(x):
#                npasum = npasum + 0
#            else:
#                npasum = npasum + x[idx1 + npaidx]
#        sma[idx1] = npasum / npa
#    return(sma)

###############################################################
#a = np.array([2., 3., 1., 2., 2., 3., 1., 3., 1., 1.])
#smaval = sma(a, 3)
#smahand = np.array([5./3, 6./3, 6./3, 5./3, 7./3, 6./3, 7./3, 5./3, 5./3, 2./3])
#
#for idx in range(len(smaval)):
#    print(smaval[idx], smahand[idx])
