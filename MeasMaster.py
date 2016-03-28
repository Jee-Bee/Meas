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
        self.ui.retranslateUi(self)
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../resources/icons/MeasLogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #Meas.QtWidgets.QMainWindow.setWindowTitle("Meas Sound Measurement Tool")
        #Meas.setWindowIcon(icon)
        # self.ui.setWindowTitle("Meas Sound Measurement Tool")
        
        # Menu bar
        self.ui.actionNew.triggered.connect(self.new_file)
        #self.ui.actionOpen.setText(_translate("MeasMain", "&Open"))
        self.ui.actionOpen.triggered.connect(self.open_file)
        #self.ui.actionOpen.setText(_translate("MeasMain", "&Open"))
        self.ui.actionSave.triggered.connect(self.save_file)
        #self.ui.actionSave.setText(_translate("MeasMain", "&Save"))
        self.ui.actionSave.triggered.connect(self.saveas_file)
        #self.ui.actionSave_as.setText(_translate("MeasMain", "&Save as"))
        self.ui.actionSave_All.triggered.connect(self.saveall_file)
        #self.ui.actionSave_All.setText(_translate("MeasMain", "&Save all"))
        self.ui.actionPreferences.triggered.connect(self.Preference_menu)
        #self.ui.actionPreferences.setText(_translate("MeasMain", "&Preferences"))
        self.ui.actionExit.triggered.connect(self.Exit)
        #self.ui.actionExit.setText(_translate("MeasMain", "&Quit"))

# http://stackoverflow.com/questions/8687723/pyqthow-do-i-display-a-image-properly
#        self.ui.JbaeIcon = QtGui.QGraphicsPixmapItem()


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
        #comboBox.activated[str].connect(self.style_choice)

        self.ui.lengthSelect.addItem("128")
        self.ui.lengthSelect.addItem("256")
        self.ui.lengthSelect.addItem("512")
        self.ui.lengthSelect.addItem("1024")
        self.ui.lengthSelect.addItem("2048")
#        self.ui.lengthSelect.addItem("1024")
        #comboBox.activated[str].connect(self.style_choice)
        
        self.ui.SweepsSelect.addItem("1")
        self.ui.SweepsSelect.addItem("2")
        self.ui.SweepsSelect.addItem("3")
        self.ui.SweepsSelect.addItem("5")
        self.ui.SweepsSelect.addItem("7")
        self.ui.SweepsSelect.addItem("9")
        # comboBox.activated[str].connect(self.style_choice)
        
        self.ui.progressBar.setProperty("value", 1)
        self.ui.dateTimeEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.ui.dateTimeEdit.setDate(QtCore.QDate.currentDate())
        self.ui.dateTimeEdit.setTime(QtCore.QTime.currentTime())

# Menu:
    def new_file(self):
        pass

# Save is now same as Save as. Futerure release Save change after known file
# else save goes thru save as
    def save_file(self):
        name = QtWidgets.QFileDialog.getSaveFileName(self, 'save File')
        file = open(name, 'w')
        # text = self.textEdit.toPlainText()
        # file.write(text)
        file.close()

    def saveas_file(self):
        name = QtWidgets.QFileDialog.getSaveFileName(self, 'save File')
        file = open(name, 'w')
        # text = self.textEdit.toPlainText()
        # file.write(text)
        file.close()

    def saveall_file(self):
        name = QtWidgets.QFileDialog.getSaveFileName(self, 'save File')
        file = open(name, 'w')
        # text = self.textEdit.toPlainText()
        # file.write(text)
        file.close()

    def open_file(self):
        name = QtWidgets.QFileDialog.getOpenFileName(self, 'open File')
        file = open(name, 'r')

#        self.editor()
#
#        with file:
#            text = file.read()
#            self.textEdit.setText(text)

    def Preference_menu(self):
        pass

# http://stackoverflow.com/questions/36180552/linking-pyqt-files-dont-relate/
    def Exit(self):
        choice = QtWidgets.QMessageBox.question(self, 'Exit Meas',
                    "Are You sure to Leave Meas?",
                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:
            self.close()

# http://codeprogress.com/python/libraries/pyqt/showPyQTExample.php?key=QLCDNumberDigitalClock&index=409




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    measgui = Meas()
    measgui.show()
    sys.exit(app.exec_())
