# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 18:32:31 2016

@author: Jee-Bee for jBae (c) 2016
"""
import sys, os
from PyQt5 import QtCore, QtGui, QtWidgets
# from ui.jBae_Meas_0_15 import Ui_MeasMain
from ui.jBae_Meas_0_10_Meas import Ui_measDialog  
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../resources/'))
from icons import *


def runMeas():
    MeasDialog = QtWidgets.QDialog() 
    measpanel = Meas()
    return (measpanel)


class Meas(QtWidgets.QDialog):
    def __init__(self, parent=None):
        # QtGui.QWidget.__init__(self, parent)  # PyQt4
        super(Meas, self).__init__(parent)  # pyQt5
        self.ui = Ui_measDialog() 
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)

        # Window Icon
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../resources/icons/MeasLogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setWindowTitle("Meas Preferences")

# http://stackoverflow.com/questions/8687723/pyqthow-do-i-display-a-image-properly
#        self.ui.JbaeIcon = QtGui.QGraphicsPixmapItem()

        # Measurement Properties
        self.ui.sigTypeSel.addItem("Sine")
        self.ui.sigTypeSel.addItem("Sawtooth")
        self.ui.sigTypeSel.addItem("Square")
        self.ui.sigTypeSel.addItem("Triangle")
        self.ui.sigTypeSel.addItem("ChirpLin")
        self.ui.sigTypeSel.addItem("ChirpLog")
        self.ui.sigTypeSel.addItem("Wnoise")
        self.ui.sigTypeSel.addItem("Pnoise")
        self.ui.sigTypeSel.addItem("bnoise")
        self.ui.sigTypeSel.addItem("multitone")
        self.ui.sigTypeSel.addItem("ChirpPoly")
#        self.ui.sigTypeSel.addItem("")
        self.ui.sigTypeSel.activated[str].connect(self.signal)

        self.ui.lengthSelect.addItem("128")
        self.ui.lengthSelect.addItem("256")
        self.ui.lengthSelect.addItem("512")
        self.ui.lengthSelect.addItem("1024")
        self.ui.lengthSelect.addItem("2048")
#        self.ui.lengthSelect.addItem("1024")
        self.ui.lengthSelect.activated[str].connect(self.sweep_length)

        self.ui.SweepsSelect.addItem("1")
        self.ui.SweepsSelect.addItem("2")
        self.ui.SweepsSelect.addItem("3")
        self.ui.SweepsSelect.addItem("5")
        self.ui.SweepsSelect.addItem("7")
        self.ui.SweepsSelect.addItem("9")
        self.ui.SweepsSelect.activated[str].connect(self.sweep_iterations)

        #buttonBox:
        # see: http://stackoverflow.com/questions/35443399/pyqt-what-signal-does-my-standard-apply-button-emit-and-how-do-i-write-the-s
        self.ui.buttonBox.accepted.connect(self.measfOk)
        self.ui.buttonBox.rejected.connect(self.measCancel)


     # Signal Parameters
    def signal(self):
        Message = QtWidgets.QMessageBox.information(self, "Empty function!",
                                                    "This function Don\'t exist yet", QtWidgets.QMessageBox.Ok)

    def sweep_length(self):
        Message = QtWidgets.QMessageBox.information(self, "Empty function!",
                                                    "This function Don\'t exist yet", QtWidgets.QMessageBox.Ok)

    def sweep_iterations(self):
        Message = QtWidgets.QMessageBox.information(self, "Empty function!",
                                                    "This function Don\'t exist yet", QtWidgets.QMessageBox.Ok)

    def measCancel(self):
        choice = QtWidgets.QMessageBox.question(self, 'Exit Meas',
                    "Are You sure to Leave Meas?",
                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:
            self.close()

    # change to run
    def measOk(self):
        Message = QtWidgets.QMessageBox.information(self, "Empty function!",
                                                    "This function Don\'t exist yet", QtWidgets.QMessageBox.Ok)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    measgui = runMeas()
    measgui.show()
    sys.exit(app.exec_())
