# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 13:04:25 2016

@author: Jee-Bee for jBae (c) 2016
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.jBae_Meas_0_15 import Ui_MeasMain
from ui import PrefMaster
from ui import FigMaster
from ui import MeasMaster
from resources.icons import *
import sys


# http://blog.abstractfactory.io/dynamic-signals-in-pyqt/
# http://stackoverflow.com/questions/26867723/how-to-call-a-python-script-on-button-click-using-pyqt
# http://stackoverflow.com/questions/14755305/open-a-gui-file-from-another-file-pyqt#14756580
# main window is child. this file mother file!!
class Meas(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        # QtGui.QWidget.__init__(self, parent)  # PyQt4
        super(Meas, self).__init__(parent)  # pyQt5
        self.ui = Ui_MeasMain()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./resources/icons/MeasLogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setWindowTitle("Meas Sound Measurement Tool")

        # make global variable for number of recordings:
        nRecordings = []
        global nRecordings
        nRecordings = 0

        # Menu bar
        # File Menu:
        self.ui.actionNew.triggered.connect(self.new_file)
        # self.ui.actionOpen.setText(_translate("MeasMain", "&Open"))
        self.ui.actionOpen.triggered.connect(self.open_file)
        # self.ui.actionOpen.setText(_translate("MeasMain", "&Open"))
        self.ui.actionSave.triggered.connect(self.save_file)
        # self.ui.actionSave.setText(_translate("MeasMain", "&Save"))
        self.ui.actionSave.triggered.connect(self.saveas_file)
        # self.ui.actionSave_as.setText(_translate("MeasMain", "&Save as"))
        self.ui.actionSave_All.triggered.connect(self.saveall_file)
        # self.ui.actionSave_All.setText(_translate("MeasMain", "&Save all"))
        self.ui.actionPreferences.triggered.connect(self.Preference_menu)
        # self.ui.actionPreferences.setText(_translate("MeasMain", "&Preferences"))
        self.ui.actionExit.triggered.connect(self.Exit)
        # self.ui.actionExit.setText(_translate("MeasMain", "&Quit"))

        # Edit Menu
        self.ui.actionDelete_Measurement.triggered.connect(self.Delete_Measurement)
        # self.ui.actionDelete_Measurement.setText(_translate("MeasMain", "&Delete"))
        # Top figure
        self.ui.actionHome_Top.triggered.connect(self.home_Top)
        self.ui.actionZoom_Top.triggered.connect(self.zoom_Top)
        self.ui.actionPan_Top.triggered.connect(self.pan_Top)
        self.ui.actionFig_Preferences_Top.triggered.connect(self.pref_Top)
        # Bottom figure
        self.ui.actionHome_Bottom.triggered.connect(self.home_Bottom)
        self.ui.actionZoom_Bottom.triggered.connect(self.zoom_Bottom)
        self.ui.actionPan_Bottom.triggered.connect(self.pan_Bottom)
        self.ui.actionFig_Preferences_Bottom.triggered.connect(self.pref_Bottom)

        # Measurement Menu:
        self.ui.actionRun_Measurent.triggered.connect(self.run_Measurement)
        self.ui.actionTest_Signal.triggered.connect(self.run_Test)

        # http://stackoverflow.com/questions/8687723/pyqthow-do-i-display-a-image-properly
        # self.ui.JbaeIcon = QtGui.QGraphicsPixmapItem()
        # logo jBae:
        jBae = QtGui.QPixmap('./resources/icons/jBaeLogo_0_1.png')
        jBae_Scaled = jBae.scaled(self.ui.jBaeLogo.size(), QtCore.Qt.KeepAspectRatio)
        self.ui.jBaeLogo.setPixmap(jBae_Scaled)
        # self.ui.jBaeLogo.scaledContents(True)
        self.ui.jBaeLogo.show()

        # date and time settings
        self.ui.dateTimeEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.ui.dateTimeEdit.setDate(QtCore.QDate.currentDate())
        self.ui.dateTimeEdit.setTime(QtCore.QTime.currentTime())
        
        # Figure buttons:
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./resources/icons/WrenchSm.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.ui.prefTop.setIcon(icon)
        self.ui.prefBottom.setIcon(icon)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./resources/icons/MagnifierSm.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.ui.zoomTop.setIcon(icon)
        self.ui.ZoomBottom.setIcon(icon)

        # Edit Icon wrong logo need to be double arrows
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./resources/icons/plusSm.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.ui.panTop.setIcon(icon)
        self.ui.panBottom.setIcon(icon)

        # Edit Icon wrong logo need to be double arrows
        # icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap("./resources/icons/PlusSm.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        # self.ui.homeTop.setIcon(icon)
        # self.ui.homeBottom.setIcon(icon)
        
        self.ui.homeTop.clicked.connect(self.home_Top)
        self.ui.zoomTop.clicked.connect(self.zoom_Top)
        self.ui.panTop.clicked.connect(self.pan_Top)
        self.ui.prefTop.clicked.connect(self.pref_Top)

        self.ui.homeBottom.clicked.connect(self.home_Bottom)
        self.ui.ZoomBottom.clicked.connect(self.zoom_Bottom)
        self.ui.panBottom.clicked.connect(self.pan_Bottom)
        self.ui.prefBottom.clicked.connect(self.pref_Bottom)

        # recordings toolbox pages
        # http://www.qtcentre.org/threads/23057-how-do-add-a-page-in-QToolBox
        self.ui.Recordings.setVisible(False)

        # test + run measurement
        self.ui.testSig.clicked.connect(self.run_Test)
        self.ui.runMeas.clicked.connect(self.run_Measurement)

# Menu:
    def new_file(self):
        Message = QtWidgets.QMessageBox.information(self, "Empty function!",
                                                    "This function Don\'t exist yet", QtWidgets.QMessageBox.Ok)
        return(Message)

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
        return(file)

#        self.editor()
#
#        with file:
#            text = file.read()
#            self.textEdit.setText(text)

    def Preference_menu(self):
        self.prefMenu = PrefMaster.runPref()
        self.prefMenu.show()


#     def Exit(self):
#         choice = QtGui.QMessageBox.question(self, 'Exit Meas',
#                     "Are You sure to Leave Meas?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
#         if choice == QtGui.QMessageBox.Yes:
#             sys.exit()
#         else:
#             pass


# http://stackoverflow.com/questions/36180552/linking-pyqt-files-dont-relate/
    def Exit(self):
        choice = QtWidgets.QMessageBox.question(self, 'Exit Meas',
                    "Are You sure to Leave Meas?",
                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:
            self.close()

# http://codeprogress.com/python/libraries/pyqt/showPyQTExample.php?key=QLCDNumberDigitalClock&index=409

    def Delete_Measurement(self):
        Message = QtWidgets.QMessageBox.information(self, "Empty function!",
                                                    "This function Don\'t exist yet", QtWidgets.QMessageBox.Ok)
        return(Message)

    # Pricture options

    def home_Top(self):
        Message = QtWidgets.QMessageBox.information(self, "Empty function!",
                                                    "This function Don\'t exist yet", QtWidgets.QMessageBox.Ok)
        return(Message)

    def zoom_Top(self):
        Message = QtWidgets.QMessageBox.information(self, "Empty function!",
                                                    "This function Don\'t exist yet", QtWidgets.QMessageBox.Ok)
        return(Message)

    def pan_Top(self):
        Message = QtWidgets.QMessageBox.information(self, "Empty function!",
                                                    "This function Don\'t exist yet", QtWidgets.QMessageBox.Ok)
        return(Message)

    def pref_Top(self):
        self.figMenu = FigMaster.runFig()
        self.figMenu.show()

    def home_Bottom(self):
        Message = QtWidgets.QMessageBox.information(self, "Empty function!",
                                                    "This function Don\'t exist yet", QtWidgets.QMessageBox.Ok)
        return(Message)

    def zoom_Bottom(self):
        Message = QtWidgets.QMessageBox.information(self, "Empty function!",
                                                    "This function Don\'t exist yet", QtWidgets.QMessageBox.Ok)
        return(Message)

    def pan_Bottom(self):
        Message = QtWidgets.QMessageBox.information(self, "Empty function!",
                                                    "This function Don\'t exist yet", QtWidgets.QMessageBox.Ok)
        return(Message)

    def pref_Bottom(self):
        self.figMenu = FigMaster.runFig()
        self.figMenu.show()

    def run_Measurement(self):
        self.measMenu = MeasMaster.runMeas()
        self.measMenu.show()
        global nRecordings
        if nRecordings == 0:
            self.ui.Recordings.setVisible(True)
            nRecordings += 1
        else:
            self.ui.Recordings(QtToolbox.addItem())

    def run_Test(self):
        Message = QtWidgets.QMessageBox.information(self, "Empty function!",
                                                    "This function Don\'t exist yet", QtWidgets.QMessageBox.Ok)
        return(Message)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    measgui = Meas()
    measgui.show()
    sys.exit(app.exec_())
