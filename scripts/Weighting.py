# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 13:06:54 2016

@author: Jee-Bee for jBae (c) 2016
"""

import numpy as np

# RX are the values of the different weighted 


def Weighting_RA(f):
    Ra = (12200 ** 2 * f ** 4) / ((f ** 2 + 20.6 ** 2) * np.sqrt((f ** 2 + 107.7 ** 2) * (f ** 2 + 737.9 ** 2)) * (f ** 2 + 12200 ** 2))
    return(Ra)


def A_weighting(AS, f):
    Ra = Weighting_RA(f)
    A = 2 + 20 *np.log10(Ra) * AS
    return(A)


def Weighting_RB(f):
    Rb = (12200 ** 2 * f ** 3) / ((f ** 2 + 20.6 ** 2) * np.sqrt((f ** 2 + 158.5 ** 2)) * (f ** 2 + 12200 ** 2))
    return(Rb)


def B_weighting(AS, f):
    Rb = Weighting_RB(f)
    B = 0.17 + 20 *np.log10(Rb) * AS
    return(B)


def Weighting_RC(f):
    Rc = (12200 ** 2 * f ** 2) / ((f ** 2 + 20.6 ** 2) * (f ** 2 + 12200 ** 2))
    return(Rc)


def C_weighting(AS, f):
    Rc = Weighting_RC(f)
    C = 0.06+ 20 * np.log10(Rc) * AS
    return(C)


def h_f(f):
    h = ((1037918.48 - f ** 2 ) ** 2 + 1080768.16 * f ** 2) / ((9837328 - f ** 2) ** 2 + 11723776 * f ** 2)
    return(h)


def Weighting_RD(f):
    h = h_f(f)
    Rd = (f / 6.8966888496476 * 10 ** (-5)) * np.sqrt(h / ((f ** 2 + 79919.29) * (f ** 2 + 1345600)))
    return(Rd)


def D_weighting(AS, f):
    Rd = Weighting_RD(f)
    D = 20 * np.log10(Rd) * AS
    return(D)
