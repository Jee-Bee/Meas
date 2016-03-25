# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 13:04:25 2016

@author: Jee-Bee for jBae (c) 2016
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.jBae_Meas_0_15 import Ui_MeasMain
import sys


# http://stackoverflow.com/questions/14755305/open-a-gui-file-from-another-file-pyqt#14756580
# main window is child. this file mother file!!
class Meas(object):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        
#self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))

    def showmeas(self):
        self.child_wind = Ui_MeasMain()
        self.ui_MeasMain.setupUi.actionExit = QtWidgets.QAction(MeasMain)
        self.ui_MeasMain.retranslateUI.setWindowTitle("Meas Sound Measurement Tool")
        self.child_wind.show()

# http://stackoverflow.com/questions/36180552/linking-pyqt-files-dont-relate/
    def Exit(self):
        choice = QtWidgets.QMessageBox.question(self, 'Exit Meas',
                    "Are You sure to Leave Meas?",
                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:
            self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MeasMain = QtWidgets.QMainWindow()
    ui = Ui_MeasMain()
    ui.setupUi(MeasMain)
    MeasMain.show()
    sys.exit(app.exec_())
