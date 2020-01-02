# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 13:04:25 2016

@author: Jee-Bee for jBae (c) 2016
"""

import sys, os
from PyQt5 import QtGui, QtWidgets  # , QtCore
# from ui.jBae_Meas_0_15 import Ui_MeasMain
from ui.jBae_Meas_0_15_Pref import Ui_Dialog  # @@@ Change name to Ui_MeasPref
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../resources/'))
from icons import *


def runPref():
    PrefDialog = QtWidgets.QDialog() # @@@ Change name to Ui_MeasPref
    prefpanel = Pref()
    return (prefpanel)

#http://stackoverflow.com/questions/1807299/open-a-second-window-in-pyqt
#http://stackoverflow.com/questions/26867723/how-to-call-a-python-script-on-button-click-using-pyqt
# main window is child. this file mother file!!
class Pref(QtWidgets.QDialog):
    def __init__(self, parent=None):
        # QtGui.QWidget.__init__(self, parent)  # PyQt4
        super(Pref, self).__init__(parent)  # pyQt5
        self.ui = Ui_Dialog() # @@@ Change name to Ui_MeasPref
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)

        # Window Icon
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../resources/icons/MeasLogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setWindowTitle("Meas Preferences")

        self.ui.interfaceUpdate.clicked.connect(self.interface_Update)

        # Default inputs
        # @ @ from function and from file
        self.ui.interfaceInput.addItem("None")

        self.ui.interfaceInput.activated[str].connect(self.interfaceI_Sel)


        # Default outputs
        # @ @ from function and from file
        self.ui.interfaceOutput.addItem("None")
        
        self.ui.interfaceOutput.activated[str].connect(self.interfaceO_Sel)

        # standard bit depth options
        self.ui.bitDepth.addItem("8")
        self.ui.bitDepth.addItem("12")
        self.ui.bitDepth.addItem("16")
        self.ui.bitDepth.addItem("20")
        self.ui.bitDepth.addItem("24")

        self.ui.bitDepth.activated[str].connect(self.bitDepth_Sel)

        # self.ui.bitDeptDither.checkState()  # for see if checkbox is checked
        self.ui.bitDeptDither.setChecked(False)
        # self.ui.bitDeptDither.isChecked()  # .connect(self.dither)
        self.ui.bitDeptDither.clicked.connect(self.dither)

        # Standard Fs  options
        self.ui.fsSel.addItem("8000")
        self.ui.fsSel.addItem("11025")
        self.ui.fsSel.addItem("12000")
        self.ui.fsSel.addItem("22050")
        self.ui.fsSel.addItem("24000")
        self.ui.fsSel.addItem("44100")
        self.ui.fsSel.addItem("48000")
        self.ui.fsSel.addItem("88200")
        self.ui.fsSel.addItem("96000")
        self.ui.fsSel.addItem("176400")
        self.ui.fsSel.addItem("192000")

        self.ui.fsSel.activated[str].connect(self.fs_Sel)

        # self.ui.fsStandard.checkState()  # for see if checkbox is checked
        self.ui.fsStandard.setChecked(False)
        self.ui.fsStandard.clicked.connect(self.fs_Standaard)

        self.ui.fsEdit.setText("44100")

        # Default buffersize
        # values from 2 ^ 5 to 2 ^ 12:
        self.ui.buffSizeSel.addItem("32")  # 2^5
        self.ui.buffSizeSel.addItem("64")  # 2^6
        self.ui.buffSizeSel.addItem("128")  # 2^7
        self.ui.buffSizeSel.addItem("256")  # 2^8
        self.ui.buffSizeSel.addItem("512")  # 2^9
        self.ui.buffSizeSel.addItem("1024")  # 2^10
        self.ui.buffSizeSel.addItem("2048")  # 2^11
        self.ui.buffSizeSel.addItem("4096")  # 2^12

        self.ui.buffSizeSel.activated[str].connect(self.buffSize_sel)

        self.ui.OverlapTest.clicked.connect(self.overlap_Test)

        # Default Windows
        self.ui.WindowSel.addItem("Rectangular")
        self.ui.WindowSel.addItem("Triangular")
        self.ui.WindowSel.addItem("Parzen")
        self.ui.WindowSel.addItem("Generized Hamming")
        self.ui.WindowSel.addItem("Hann")
        self.ui.WindowSel.addItem("Hamming")
        self.ui.WindowSel.addItem("Cosine")
        self.ui.WindowSel.addItem("Generized Gaussian")
        self.ui.WindowSel.addItem("Gaussian")
        self.ui.WindowSel.addItem("Tukey")

        self.ui.WindowSel.activated[str].connect(self.window_sel)

        self.ui.defFreqMinEdit.setText("20")
        self.ui.defFreqMaxEdit.setText("20000")

        # Default Stylesheet
        self.ui.styleSheetSel.addItem("Standard")
        self.ui.styleSheetSel.addItem("None")

        self.ui.styleSheetSel.activated[str].connect(self.styleSheet_sel)

    def interfaceI_Sel(self):
        Message = QtWidgets.QMessageBox.information(self, "Empty function!",
                                                    "This function Don\'t exist yet", QtWidgets.QMessageBox.Ok)

    def interfaceO_Sel(self):
        Message = QtWidgets.QMessageBox.information(self, "Empty function!",
                                                    "This function Don\'t exist yet", QtWidgets.QMessageBox.Ok)

    def interface_Update(self):
        Message = QtWidgets.QMessageBox.information(self, "Empty function!",
                                                    "This function Don\'t exist yet", QtWidgets.QMessageBox.Ok)

    def bitDepth_Sel(self):
        Message = QtWidgets.QMessageBox.information(self, "Empty function!",
                                                    "This function Don\'t exist yet", QtWidgets.QMessageBox.Ok)

    def dither(self):
        Message = QtWidgets.QMessageBox.information(self, "Empty function!",
                                                    "This function Don\'t exist yet", QtWidgets.QMessageBox.Ok)
        self.ui.bitDeptDither.setChecked(False)

    def fs_Sel(self):
        Message = QtWidgets.QMessageBox.information(self, "Empty function!",
                                                    "This function Don\'t exist yet", QtWidgets.QMessageBox.Ok)

    def buffSize_sel(self):
        Message = QtWidgets.QMessageBox.information(self, "Empty function!",
                                                    "This function Don\'t exist yet", QtWidgets.QMessageBox.Ok)


    def fs_Standaard(self):
        Message = QtWidgets.QMessageBox.information(self, "Empty function!",
                                                    "This function Don\'t exist yet", QtWidgets.QMessageBox.Ok)
        self.ui.fsStandard.setChecked(False)

    def window_sel(self):
        Message = QtWidgets.QMessageBox.information(self, "Empty function!",
                                                    "This function Don\'t exist yet", QtWidgets.QMessageBox.Ok)

    def overlap_Test(self):
        Message = QtWidgets.QMessageBox.information(self, "Empty function!",
                                                    "This function Don\'t exist yet", QtWidgets.QMessageBox.Ok)

    def styleSheet_sel(self):
        Message = QtWidgets.QMessageBox.information(self, "Empty function!",
                                                    "This function Don\'t exist yet", QtWidgets.QMessageBox.Ok)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    prefgui = runPref()
    prefgui.show()
    sys.exit(app.exec_())
