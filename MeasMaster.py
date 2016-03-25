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
        #QtGui.QWidget.__init__(self, parent)  # PyQt4
        super(Meas, self).__init__(parent)  #pyQt5
        self.ui = Ui_MeasMain()
        self.ui.setupUi(self)
        self.ui.setupUi
        #self.ui.setupUi(MeasMain)
        self.ui.retranslateUi(self)

        # self.ui.setWindowIcon(QtWidgets.QIcon('MeasLogoSm.png'))
        # self.ui.setWindowTitle("Meas Sound Measurement Tool")

        self.ui.progressBar.setProperty("value", 1)
        
        # measExit = self.ui.menuJBae_Meas.addAction(self.ui.actionExit)
        # measExit.triggered.connect(self.Exit)

#    def showmeas(self):
#        self.child_wind = Ui_MeasMain()
#        self.ui_MeasMain.retranslateUI.setWindowTitle("Meas Sound Measurement Tool")
#        self.child_wind.show()

# http://stackoverflow.com/questions/36180552/linking-pyqt-files-dont-relate/
    def Exit(self):
        choice = QtWidgets.QMessageBox.question(self, 'Exit Meas',
                    "Are You sure to Leave Meas?",
                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:
            self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    measapp = Meas()
    measapp.show()
    sys.exit(app.exec_())
