# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 13:06:54 2016

@author: Jee-Bee for jBae (c) 2016
"""

import numpy as np
# from src import measerror #import MeasError
from src.checks import istuple



# RX are the values of the different weightings
class weighting():
    """ Default Weighting Class:
    Whole class based equations writen on Wikipedia 2016
    see: https://en.wikipedia.org/wiki/A-weighting"""
    def __init__(self):
        pass


# class AWeighting(Weighting):
#    """ A - Weighting Class - See  IEC 61672:2003 """
#    def __init__(self):
#        pass

    def weightingRA(self, F):
        """
        Input:
            F = frequency array
        Output:
            Ra = Weighting function result in amplitude spectrum
        see: https://en.wikipedia.org/wiki/A-weighting
        """
        Ra = (12200 ** 2 * F ** 4) / ((F ** 2 + 20.6 ** 2) * np.sqrt((F ** 2 + 107.7 ** 2) * (F ** 2 + 737.9 ** 2)) * (F ** 2 + 12200 ** 2))
        return(Ra)

    def Aweighting(self, F, AS):
        """
        Input:
            F = frequency array
            AS = Amplitude spectrum as is
        Output:
            A = Weighting amplitude spectrum

        A-Weighting follows the inverse equal loudness curve of 40 dB(40 Phon).
        A weighted Amplide spectrum is corrected with 2.00 dB for ensure
        normalisation at 1000 Hz
        see: https://en.wikipedia.org/wiki/A-weighting
        """
        print("in weighting")
        if istuple(AS) is True:
            print("tuple A")
            AMP = AS[0]
            PHI = AS[1]
            F_shape = np.shape(F)
            AMP_shape = np.shape(AMP)
            if F_shape == AMP_shape:
                pass
            else:
                raise ValueError("Dimensions `F` and `As` Are not equal in length")
            if len(AMP_shape) == 1:
                Ra = self.weightingRA(F)
                A = 2 + 20 * np.log10(Ra) * AMP
                return(F, A, PHI)
            elif len(AMP_shape) == 2:
                if AMP_shape[0] < AMP_shape[1]:
                    pass
                elif AMP_shape[0] > AMP_shape[1]:
                    AMP = AMP.T
                    PHI = PHI.T
                    F = F.T
                A = []
                Ra = self.weightingRA(F[0])
                for chan in AMP_shape[0]:
                    if chan == 0:
                        A = np.append(A, 2 + 20 * np.log10(Ra) * AMP[chan])
                    else:
                        A = np.vstack((A, 2 + 20 * np.log10(Ra) * AMP[chan]))
                return(F, A, PHI)
            else:
                raise MeasError.SizeError("Dimensions `F` and `As` Are not equal in length")
        elif np.iscomplex(AS).any() is True:
            print("complex A")
            F_shape = np.shape(F)
            AS_shape = np.shape(AS)
            if F_shape == AMP_shape:
                pass
            else:
                raise ValueError("Dimensions `F` and `As` Are not equal in length")
            if len(AS_shape) == 1:
                N = len(F)/2
                F = F[:N]
                AMP = np.abs(AS[1:N])
                PHI = np.arctan(np.real(AS[1:N])/np.imag(AS[1:N]))
                Ra = self.weightingRA(F)
                A = 2 + 20 * np.log10(Ra) * AMP
                print("Dimensions of spectra are changed")
                return(F, A, PHI)
            elif len(AS_shape) == 2:
                if AS_shape[0] < AS_shape[1]:
                    N = AS_shape[1]/2
                    F = F.T[1:N].T
                    AMP = np.abs(AS.T[1:N]).T
                    PHI = np.arctan(np.real(AS.T[1:N])/np.imag(AS.T[1:N])).T
                elif AS_shape[0] > AS_shape[1]:
                    F = F[1:N].T
                    AMP = np.abs(AS[1:N]).T
                    PHI = np.arctan(np.real(AS[1:N])/np.imag(AS[1:N])).T
                A = []
                Ra = self.weightingRA(F[0])
                for chan in AMP_shape[0]:
                    if chan == 0:
                        A = np.append(A, 2 + 20 * np.log10(Ra) * AMP[chan])
                    else:
                        A = np.vstack((A, 2 + 20 * np.log10(Ra) * AMP[chan]))
                print("Dimensions of spectra are changed")
                return(F, A, PHI)
            else:
                raise MeasError.SizeError("Dimensions `F` and `As` Are not equal in length")

    def weightingRB(self, F):
        """
        Input:
            F = frequency array
        Output:
            Rb = Weighting function result in amplitude spectrum
        see: https://en.wikipedia.org/wiki/A-weighting
        """
        Rb = (12200 ** 2 * F ** 3) / ((F ** 2 + 20.6 ** 2) *
                        np.sqrt((F ** 2 + 158.5 ** 2)) * (F ** 2 + 12200 ** 2))
        return(Rb)

    def Bweighting(self, F, AS):
        """
        Input:
            F = frequency array
            AS = Amplitude spectrum as is
        Output:
            B = Weighting amplitude spectrum

        B-Weighting follows the inverse equal loudness curve of 70 dB(70 Phon).
        B weighted Amplide spectrum is corrected with 0.17 dB for ensure
        normalisation at 1000 Hz
        see: https://en.wikipedia.org/wiki/A-weighting
        """
        if istuple(AS) is True:
            AMP = AS[0]
            PHI = AS[1]
            F_shape = np.shape(F)
            AMP_shape = np.shape(AMP)
            if F_shape == AMP_shape:
                pass
            else:
                raise ValueError("Dimensions `F` and `As` Are not equal in length")
            if len(AMP_shape) == 1:
                Rb = self.weightingRB(F)
                B = 0.17 + 20 * np.log10(Rb) * AS
                return(F, B, PHI)
            elif len(AMP_shape) == 2:
                if AMP_shape[0] < AMP_shape[1]:
                    pass
                elif AMP_shape[0] > AMP_shape[1]:
                    AMP = AMP.T
                    PHI = PHI.T
                    F = F.T
                B = []
                Rb = self.weightingRB(F[0])
                for chan in AMP_shape[0]:
                    if chan == 0:
                        B = np.append(B, 0.17 + 20 * np.log10(Rb) * AMP[chan])
                    else:
                        B = np.vstack((B, 0.17 + 20 * np.log10(Rb) * AMP[chan]))
                return(F, B, PHI)
            else:
                raise MeasError.SizeError("Dimensions `F` and `As` Are not equal in length")
        elif np.iscomplex(AS).any() is True:
            F_shape = np.shape(F)
            AS_shape = np.shape(AS)
            if F_shape == AMP_shape:
                pass
            else:
                raise ValueError("Dimensions `F` and `As` Are not equal in length")
            if len(AS_shape) == 1:
                N = len(F)/2
                F = F[:N]
                AMP = np.abs(AS[1:N])
                PHI = np.arctan(np.real(AS[1:N])/np.imag(AS[1:N]))
                Rb = self.weightingRB(F)
                B = 0.17 + 20 * np.log10(Rb) * AMP
                print("Dimensions of spectra are changed")
                return(F, B, PHI)
            elif len(AS_shape) == 2:
                if AS_shape[0] < AS_shape[1]:
                    N = AS_shape[1]/2
                    F = F.T[1:N].T
                    AMP = np.abs(AS.T[1:N]).T
                    PHI = np.arctan(np.real(AS.T[1:N])/np.imag(AS.T[1:N])).T
                elif AS_shape[0] > AS_shape[1]:
                    F = F[1:N].T
                    AMP = np.abs(AS[1:N]).T
                    PHI = np.arctan(np.real(AS[1:N])/np.imag(AS[1:N])).T
                B = []
                Rb = self.weightingRB(F[0])
                for chan in AMP_shape[0]:
                    if chan == 0:
                        B = np.append(B, 0.17 + 20 * np.log10(Rb) * AMP[chan])
                    else:
                        B = np.vstack((B, 0.17 + 20 * np.log10(Rb) * AMP[chan]))
                print("Dimensions of spectra are changed")
                return(F, B, PHI)
            else:
                raise MeasError.SizeError("Dimensions `F` and `As` Are not equal in length")

    def weightingRC(self, F):
        """
        Input:
            F = frequency array
        Output:
            Rc = Weighting function result in amplitude spectrum
        see: https://en.wikipedia.org/wiki/A-weighting
        """
        Rc = (12200 ** 2 * F ** 2) / ((F ** 2 + 20.6 ** 2) *
                                      (F ** 2 + 12200 ** 2))
        return(Rc)

    def Cweighting(self, F, AS):
        """
        Input:
            F = frequency array
            AS = Amplitude spectrum as is
        Output:
            C = Weighting amplitude spectrum

        C-Weighting follows the inverse equal loudness curve of 100 dB
        (100 Phon).
        C weighted Amplide spectrum is corrected with 0.06 dB for ensure
        normalisation at 1000 Hz
        see: https://en.wikipedia.org/wiki/A-weighting
        """
        if istuple(AS) is True:
            AMP = AS[0]
            PHI = AS[1]
            F_shape = np.shape(F)
            AMP_shape = np.shape(AMP)
            if F_shape == AMP_shape:
                pass
            else:
                raise ValueError("Dimensions `F` and `As` Are not equal in length")
            if len(AMP_shape) == 1:
                Rc = self.weightingRC(F)
                C = 0.06 + 20 * np.log10(Rc) * AMP
                return(F, C, PHI)
            elif len(AMP_shape) == 2:
                if AMP_shape[0] < AMP_shape[1]:
                    pass
                elif AMP_shape[0] > AMP_shape[1]:
                    AMP = AMP.T
                    PHI = PHI.T
                    F = F.T
                C = []
                Rc = self.weightingRC(F[0])
                for chan in AMP_shape[0]:
                    if chan == 0:
                        C = np.append(C, 0.06 + 20 * np.log10(Rc) * AMP[chan])
                    else:
                        C = np.vstack((C, 0.06 + 20 * np.log10(Rc) * AMP[chan]))
                return(F, C, PHI)
            else:
                raise MeasError.SizeError("Dimensions `F` and `As` Are not equal in length")
        elif np.iscomplex(AS).any() is True:
            Rc = self.weightingRC(F)
            AS_shape = np.shape(AS)
            if F_shape == AMP_shape:
                pass
            else:
                raise ValueError("Dimensions `F` and `As` Are not equal in length")
            if len(AS_shape) == 1:
                N = len(F)/2
                F = F[:N]
                AMP = np.abs(AS[1:N])
                PHI = np.arctan(np.real(AS[1:N])/np.imag(AS[1:N]))
                Rc = self.weightingRC(F)
                C = 0.06 + 20 * np.log10(Rc) * AMP
                print("Dimensions of spectra are changed")
                return(F, C, PHI)
            elif len(AS_shape) == 2:
                if AS_shape[0] < AS_shape[1]:
                    N = AS_shape[1]/2
                    F = F.T[1:N].T
                    AMP = np.abs(AS.T[1:N]).T
                    PHI = np.arctan(np.real(AS.T[1:N])/np.imag(AS.T[1:N])).T
                elif AS_shape[0] > AS_shape[1]:
                    F = F[1:N].T
                    AMP = np.abs(AS[1:N]).T
                    PHI = np.arctan(np.real(AS[1:N])/np.imag(AS[1:N])).T
                C = []
                Rc = self.weightingRC(F[0])
                for chan in AMP_shape[0]:
                    if chan == 0:
                        C = np.append(C, 0.06 + 20 * np.log10(Rc) * AMP[chan])
                    else:
                        C = np.vstack((C, 0.06 + 20 * np.log10(Rc) * AMP[chan]))
                print("Dimensions of spectra are changed")
                return(F, C, PHI)
            else:
                raise MeasError.SizeError("Dimensions `F` and `As` Are not equal in length")

    def h_f(self, F):
        """
        Input:
            F = frequency array
        Output:
            h = a transferfunction not exactly known... no extra info
        see: https://en.wikipedia.org/wiki/A-weighting
        """
        h = ((1037918.48 - F ** 2) ** 2 + 1080768.16 * F ** 2) / (
                                (9837328 - F ** 2) ** 2 + 11723776 * F ** 2)
        return(h)

    def weightingRD(self, F):
        """
        Input:
            F = frequency array
        Output:
            Rd = Weighting function result in amplitude spectrum
        see: https://en.wikipedia.org/wiki/A-weighting
        """
        h = self.h_f(F)
        Rd = (F / 6.8966888496476 * 10 ** (-5)) * np.sqrt(h /
                                    ((F ** 2 + 79919.29) * (F ** 2 + 1345600)))
        return(Rd)

    def Dweighting(self, F, AS):
        """
        Input:
            F = frequency array
            AS = Amplitude spectrum as is
        Output:
            D = Weighting amplitude spectrum

        see: https://en.wikipedia.org/wiki/A-weighting
        """
        if istuple(AS) is True:
            AMP = AS[0]
            PHI = AS[1]
            F_shape = np.shape(F)
            AMP_shape = np.shape(AMP)
            if F_shape == AMP_shape:
                pass
            else:
                raise ValueError("Dimensions `F` and `As` Are not equal in length")
            if len(AMP_shape) == 1:
                Rd = self.weightingRD(F)
                D = 20 * np.log10(Rd) * AMP
                return(F, D, PHI)
            elif len(AMP_shape) == 2:
                if AMP_shape[0] < AMP_shape[1]:
                    pass
                elif AMP_shape[0] > AMP_shape[1]:
                    AMP = AMP.T
                    PHI = PHI.T
                    F = F.T
                D = []
                Rd = self.weightingRD(F[0])
                for chan in AMP_shape[0]:
                    if chan == 0:
                        D = np.append(D, 20 * np.log10(Rd) * AMP[chan])
                    else:
                        D = np.vstack((D, 20 * np.log10(Rd) * AMP[chan]))
                return(F, D, PHI)
            else:
                raise MeasError.SizeError("Dimensions `F` and `As` Are not equal in length")
        elif np.iscomplex(AS).any() is True:
            F_shape = np.shape(F)
            AS_shape = np.shape(AS)
            if F_shape == AMP_shape:
                pass
            else:
                raise ValueError("Dimensions `F` and `As` Are not equal in length")
            if len(AS_shape) == 1:
                N = len(F)/2
                F = F[:N]
                AMP = np.abs(AS[1:N])
                PHI = np.arctan(np.real(AS[1:N])/np.imag(AS[1:N]))
                Rd = self.weightingRD(F)
                D = 20 * np.log10(Rd) * AMP
                print("Dimensions of spectra are changed")
                return(F, D, PHI)
            elif len(AS_shape) == 2:
                if AS_shape[0] < AS_shape[1]:
                    N = AS_shape[1]/2
                    F = F.T[1:N].T
                    AMP = np.abs(AS.T[1:N]).T
                    PHI = np.arctan(np.real(AS.T[1:N])/np.imag(AS.T[1:N])).T
                elif AS_shape[0] > AS_shape[1]:
                    F = F[1:N].T
                    AMP = np.abs(AS[1:N]).T
                    PHI = np.arctan(np.real(AS[1:N])/np.imag(AS[1:N])).T
                D = []
                Rd = self.weightingRD(F[0])
                for chan in AMP_shape[0]:
                    if chan == 0:
                        D = np.append(D, 20 * np.log10(Rd) * AMP[chan])
                    else:
                        D = np.vstack((D, 20 * np.log10(Rd) * AMP[chan]))
                print("Dimensions of spectra are changed")
                return(F, D, PHI)
            else:
                raise MeasError.SizeError("Dimensions `F` and `As` Are not equal in length")
