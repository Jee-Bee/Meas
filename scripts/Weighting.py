# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 13:06:54 2016

@author: Jee-Bee for jBae (c) 2016
"""

import numpy as np

# RX are the values of the different weighted 

class Weighting():
    """ Default Weighting Class 
    Hole class based on Wikipedia"""
    def __init__(self, F):
        self.F = F

class A-Weighting(Weighting):
    """ A - Weighting Class - See  IEC 61672:2003 """
    def __init__(self, F):
        self.F = F
    
    def Weighting_RA(self):
        Ra = (12200 ** 2 * self.F ** 4) / ((self.F ** 2 + 20.6 ** 2) * np.sqrt((self.F ** 2 + 107.7 ** 2) * (self.F ** 2 + 737.9 ** 2)) * (self.F ** 2 + 12200 ** 2))
        return(Ra)

    def A_weighting(self, AS):
        Ra = Weighting_RA(self.F)
        A = 2 + 20 *np.log10(Ra) * AS
        return(A)


class B-Weighting(Weighting):
    """ B - Weighting Class - See  IEC 61672:2003 """
    def __init__(self, F):
        self.F = F

    def Weighting_RB(self):
        Rb = (12200 ** 2 * self.F ** 3) / ((self.F ** 2 + 20.6 ** 2) * np.sqrt((self.F ** 2 + 158.5 ** 2)) * (self.F ** 2 + 12200 ** 2))
        return(Rb)

    def B_weighting(self, AS):
        Rb = Weighting_RB(self.F)
        B = 0.17 + 20 *np.log10(Rb) * AS
        return(B)

class C-Weighting(Weighting):
    """ C - Weighting Class - See  IEC 61672:2003 """
    def __init__(self, F):
        self.F = F

    def Weighting_RC(self.F):
        Rc = (12200 ** 2 * self.F ** 2) / ((self.F ** 2 + 20.6 ** 2) * (self.F ** 2 + 12200 ** 2))
        return(Rc)

    def C_weighting(self, AS):
        Rc = Weighting_RC(self.F)
        C = 0.06+ 20 * np.log10(Rc) * AS
        return(C)

class D-Weighting(Weighting):
    """ D - Weighting Class - See  IEC 61672:2003 """
    def __init__(self, F):
        self.F = F

    def h_f(self):
        h = ((1037918.48 - self.F ** 2 ) ** 2 + 1080768.16 * self.F ** 2) / ((9837328 - self.F ** 2) ** 2 + 11723776 * self.F ** 2)
        return(h)

    def Weighting_RD(self):
        h = h_f(self.F)
        Rd = (self.F / 6.8966888496476 * 10 ** (-5)) * np.sqrt(h / ((self.F ** 2 + 79919.29) * (self.F ** 2 + 1345600)))
        return(Rd)

    def D_weighting(self, AS):
        Rd = Weighting_RD(self.F)
        D = 20 * np.log10(Rd) * AS
        return(D)
