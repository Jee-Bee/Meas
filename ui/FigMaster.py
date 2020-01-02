# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 11:01:19 2016

@author: Jee-Bee for jBae (c) 2016
"""

import sys, os
from PyQt5 import QtGui, QtWidgets  # ,QtCore
from ui.jBae_Meas_0_10_Fig import Ui_Dialog  # @@@ Change name to Ui_MeasFig
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../resources/'))
from icons import *

def runFig():
    FigDialog = QtWidgets.QDialog() # @@@ Change name to Ui_MeasPref
    figpanel = Fig()
    return (figpanel)

class Fig(QtWidgets.QDialog):
    
    def __init__(self, parent=None):
        # QtGui.QWidget.__init__(self, parent)  # PyQt4
        super(Fig, self).__init__(parent)  #PyQt5
        self.ui=Ui_Dialog()  # @@@ Change name to Ui_MeasFig
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)

        # Window Icon
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../resources/icons/MeasLogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setWindowTitle("Meas Figure Settings")

        # plot title

        # plot type
        self.ui.plotTypeSel.addItem('time')
        self.ui.plotTypeSel.addItem('spectrum 2D')
        self.ui.plotTypeSel.addItem('Bode Plot')
        self.ui.plotTypeSel.addItem('waterfall')

        self.ui.plotTypeSel.activated[str].connect(self.plottype)

        # Units x, y, x
        # x, y, z have to be self filling settings. based on units in "unitdb"
        # for now filling with single "None"
        self.ui.xUnitSel.addItem('None')

        self.ui.xUnitSel.activated[str].connect(self.xUnit)

        self.ui.yUnitSel.addItem('None')

        self.ui.xUnitSel.activated[str].connect(self.yUnit)

        # add Z direction
        # self.ui.zUnitSel.addItem('None')

        # smoothing selector
        self.ui.smoothingSel.addItem('None')

        self.ui.smoothingSel.activated[str].connect(self.smoothing)

        # phase check
        # @@@ Rename different phase checks to their right names!!
        self.ui.phaseCheck.setChecked(False)
        self.ui.phaseCheck.clicked.connect(self.phaseWrap)

        self.ui.phaseCheck_2.setChecked(False)
        self.ui.phaseCheck_2.clicked.connect(self.full_half)

        self.ui.phaseCheck_3.setChecked(False)
        self.ui.phaseCheck_3.clicked.connect(self.lin_log)

        # rename to ...
        self.ui.phaseCheck_4.setChecked(False)
        self.ui.phaseCheck_4.clicked.connect(self.am_ph)

        # spec type sel
        self.ui.specTypeSel.addItem('Amplitude Spectrum')
        self.ui.specTypeSel.addItem('Power Spectrum')
        self.ui.specTypeSel.addItem('Spectral Density')
        self.ui.specTypeSel.addItem('Power Spectral Density')

        self.ui.plotTypeSel.activated[str].connect(self.spectype)

        # weighting check
        # add Weighting Type A, B, C, D
        self.ui.weightingCheck.setChecked(False)
        self.ui.weightingCheck.clicked.connect(self.weighting)

        #buttonBox:
        # see: http://stackoverflow.com/questions/35443399/pyqt-what-signal-does-my-standard-apply-button-emit-and-how-do-i-write-the-s
        # self.ui.buttonBox.accepted.clicked.connect(self.figOk)
        self.ui.buttonBox.accepted.connect(self.figOk)


    def plottype(self):
        Message = QtWidgets.QMessageBox.information(self, "Empty function!",
                                                    "This function Don\'t exist yet", QtWidgets.QMessageBox.Ok)
        return(Message)

    def xUnit(self):
        Message = QtWidgets.QMessageBox.information(self, "Empty function!",
                                                    "This function Don\'t exist yet", QtWidgets.QMessageBox.Ok)
        return(Message)

    def yUnit(self):
        Message = QtWidgets.QMessageBox.information(self, "Empty function!",
                                                    "This function Don\'t exist yet", QtWidgets.QMessageBox.Ok)
        return(Message)

    def smoothing(self):
        Message = QtWidgets.QMessageBox.information(self, "Empty function!",
                                                    "This function Don\'t exist yet", QtWidgets.QMessageBox.Ok)
        return(Message)

    def full_half(self):
        Message = QtWidgets.QMessageBox.information(self, "Empty function!",
                                                    "This function (full_half) Don\'t exist yet", QtWidgets.QMessageBox.Ok)
        self.ui.phaseCheck_4.setChecked(False)
        return(Message)

    def am_ph(self):
        Message = QtWidgets.QMessageBox.information(self, "Empty function!",
                                                    "This function(am_ph) Don\'t exist yet", QtWidgets.QMessageBox.Ok)
        self.ui.phaseCheck_2.setChecked(False)
        return(Message)

    def lin_log(self):
        Message = QtWidgets.QMessageBox.information(self, "Empty function!",
                                                    "This function(op1_op2) Don\'t exist yet", QtWidgets.QMessageBox.Ok)
        self.ui.phaseCheck_3.setChecked(False)
        return(Message)

    def phaseWrap(self):
        Message = QtWidgets.QMessageBox.information(self, "Empty function!",
                                                    "This function(op3_op4) Don\'t exist yet", QtWidgets.QMessageBox.Ok)
        self.ui.phaseCheck.setChecked(False)
        return(Message)

    def spectype(self):
        Message = QtWidgets.QMessageBox.information(self, "Empty function!",
                                                    "This function Don\'t exist yet", QtWidgets.QMessageBox.Ok)

    def weighting(self):
        Message = QtWidgets.QMessageBox.information(self, "Empty function!",
                                                    "This function Don\'t exist yet", QtWidgets.QMessageBox.Ok)
        self.ui.weightingCheck.setChecked(False)
        return(Message)

    def figCancel(self):
        Message = QtWidgets.QMessageBox.information(self, "Empty function!",
                                                    "This function Don\'t exist yet", QtWidgets.QMessageBox.Ok)
        return(Message)

    def figOk(self):
        Message = QtWidgets.QMessageBox.information(self, "Empty function!",
                                                    "This function Don\'t exist yet", QtWidgets.QMessageBox.Ok)
        return(Message)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # FigDialog = QtWidgets.QDialog() # @@@ Change name to Ui_MeasPref
    # figgui = Fig()
    figgui = runFig()
    figgui.show()
    sys.exit(app.exec_())
