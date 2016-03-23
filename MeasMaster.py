# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 13:04:25 2016

@author: Jee-Bee for jBae (c) 2016
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.jBae_Meas_0_15 import Ui_MeasMain
from resources.icons import *
import sys


# http://blog.abstractfactory.io/dynamic-signals-in-pyqt/
# http://stackoverflow.com/questions/26867723/how-to-call-a-python-script-on-button-click-using-pyqt
# http://stackoverflow.com/questions/14755305/open-a-gui-file-from-another-file-pyqt#14756580
# main window is child. this file mother file!!
class Meas(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        #QtGui.QWidget.__init__(self, parent)
        super(Meas, self).__init__(parent)
        self.ui = Ui_MeasMain()
        self.ui.setupUi(self)
        # self.ui.setWindowIcon(QtWidgets.QIcon('MeasLogoSm.png'))

#    def showmeas(self):
#        self.child_wind = Ui_MeasMain()
#        self.ui_MeasMain.setupUi.actionExit = QtWidgets.QAction(MeasMain)
#        self.ui_MeasMain.retranslateUI.setWindowTitle("Meas Sound Measurement Tool")
#        self.child_wind.show()

    def exit(self):
        choice = QtGui.QMessageBox.question(self, 'Exit Meas',
                    "Are You sure to Leave Meas?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    measapp = Meas()
    measapp.show()
    sys.exit(app.exec_())