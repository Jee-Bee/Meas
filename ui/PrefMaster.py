# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 13:04:25 2016

@author: Jee-Bee for jBae (c) 2016
"""

import sys, os
from PyQt5 import QtCore, QtGui, QtWidgets
# from ui.jBae_Meas_0_15 import Ui_MeasMain
from jBae_Meas_Pref_0_15 import Ui_Dialog  # @@@ Change name to Ui_MeasPref
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../resources/'))
import icons


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

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../resources/icons/MeasLogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setWindowTitle("Meas Preferences")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PrefDialog = QtWidgets.QDialog() # @@@ Change name to Ui_MeasPref
    prefgui = Pref()
    prefgui.show()
    sys.exit(app.exec_())
