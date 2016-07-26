# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 13:06:54 2016

@author: Jee-Bee for jBae (c) 2016
"""

import numpy as np
from scripts import measerror #import MeasError


# RX are the values of the different weightings
class Weighting():
    """ Default Weighting Class
    Whole class based equations writen on Wikipedia 2016 
    see: https://en.wikipedia.org/wiki/A-weighting"""
    def __init__(self):
        pass


class AWeighting(Weighting):
    """ A - Weighting Class - See  IEC 61672:2003 """
    def __init__(self):
        pass

    def Weighting_RA(self, F):
        """
        Input:
            F = frequency array
        Output:
            Ra = Weighting function result in amplitude spectrum
        see: https://en.wikipedia.org/wiki/A-weighting
        """
        Ra = (12200 ** 2 * F ** 4) / ((F ** 2 + 20.6 ** 2) * np.sqrt((F ** 2 + 107.7 ** 2) * (F ** 2 + 737.9 ** 2)) * (F ** 2 + 12200 ** 2))
        return(Ra)

    def A_Weighting(self, F, AS):
        """
        Input:
            F = frequency array
            AS = Amplitude spectrum as is
        Output:
            A = Weighting amplitude spectrum

        A weighted Amplide spectrum is corrected with 2.00 dB for ensure
        normalisation at 1000 Hz
        see: https://en.wikipedia.org/wiki/A-weighting
        """
        if len(F) == len(AS):
            Ra = self.Weighting_RA(F)
            A = 2 + 20 * np.log10(Ra) * AS
            return(A)
        else:
            raise MeasError.SizeError("Dimensions `F` and `As` Are not equal in length")


class BWeighting(Weighting):
    """ B - Weighting Class - See  IEC 61672:2003 """
    def __init__(self):
        pass

    def Weighting_RB(self, F):
        """
        Input:
            F = frequency array
        Output:
            Rb = Weighting function result in amplitude spectrum
        see: https://en.wikipedia.org/wiki/A-weighting
        """
        Rb = (12200 ** 2 * F ** 3) / ((F ** 2 + 20.6 ** 2) * np.sqrt((F ** 2 + 158.5 ** 2)) * (F ** 2 + 12200 ** 2))
        return(Rb)

    def B_Weighting(self, F, AS):
        """
        Input:
            F = frequency array
            AS = Amplitude spectrum as is
        Output:
            B = Weighting amplitude spectrum

        B weighted Amplide spectrum is corrected with 0.17 dB for ensure
        normalisation at 1000 Hz
        see: https://en.wikipedia.org/wiki/A-weighting
        """
        if len(F) == len(AS):
            Rb = self.Weighting_RB(F)
            B = 0.17 + 20 * np.log10(Rb) * AS
            return(B)
        else:
            raise MeasError.SizeError("Dimensions `F` and `As` Are not equal in length")


class CWeighting(Weighting):
    """ C - Weighting Class - See  IEC 61672:2003 """
    def __init__(self):
        pass

    def Weighting_RC(self, F):
        """
        Input:
            F = frequency array
        Output:
            Rc = Weighting function result in amplitude spectrum
        see: https://en.wikipedia.org/wiki/A-weighting
        """
        Rc = (12200 ** 2 * F ** 2) / ((F ** 2 + 20.6 ** 2) * (F ** 2 + 12200 ** 2))
        return(Rc)

    def C_Weighting(self, F, AS):
        """
        Input:
            F = frequency array
            AS = Amplitude spectrum as is
        Output:
            C = Weighting amplitude spectrum

        C weighted Amplide spectrum is corrected with 0.06 dB for ensure
        normalisation at 1000 Hz
        see: https://en.wikipedia.org/wiki/A-weighting
        """
        if len(F) == len(AS):
            Rc = self.Weighting_RC(F)
            C = 0.06 + 20 * np.log10(Rc) * AS
            return(C)
        else:
            raise MeasError.SizeError("Dimensions `F` and `As` Are not equal in length")


class DWeighting(Weighting):
    """ D - Weighting Class - See  IEC 61672:2003 """
    def __init__(self):
        pass

    def h_f(self, F):
        """
        Input:
            F = frequency array
        Output:
            h = a transferfunction not exactly known... no extra info
        see: https://en.wikipedia.org/wiki/A-weighting
        """
        h = ((1037918.48 - F ** 2) ** 2 + 1080768.16 * F ** 2) / ((9837328 - F ** 2) ** 2 + 11723776 * F ** 2)
        return(h)

    def Weighting_RD(self, F):
        """
        Input:
            F = frequency array
        Output:
            Rd = Weighting function result in amplitude spectrum
        see: https://en.wikipedia.org/wiki/A-weighting
        """
        h = self.h_f(F)
        Rd = (F / 6.8966888496476 * 10 ** (-5)) * np.sqrt(h / ((F ** 2 + 79919.29) * (F ** 2 + 1345600)))
        return(Rd)

    def D_Weighting(self, F, AS):
        """
        Input:
            F = frequency array
            AS = Amplitude spectrum as is
        Output:
            D = Weighting amplitude spectrum

        see: https://en.wikipedia.org/wiki/A-weighting
        """
        if len(F) == len(AS):
            Rd = self.Weighting_RD(F)
            D = 20 * np.log10(Rd) * AS
            return(D)
        else:
            raise MeasError.SizeError("Dimensions `F` and `As` Are not equal in length")
