# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jBae-Meas_0_1.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MeasMain(object):
    def setupUi(self, MeasMain):
        MeasMain.setObjectName("MeasMain")
        MeasMain.resize(1280, 800)
        MeasMain.setStyleSheet("font: 9pt \"SansSerif\";")
        self.measCentral = QtWidgets.QWidget(MeasMain)
        self.measCentral.setObjectName("measCentral")
        self.JbaeLogo = QtWidgets.QGraphicsView(self.measCentral)
        self.JbaeLogo.setGeometry(QtCore.QRect(30, 25, 281, 111))
        self.JbaeLogo.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        self.JbaeLogo.setObjectName("JbaeLogo")
        self.testSig = QtWidgets.QToolButton(self.measCentral)
        self.testSig.setGeometry(QtCore.QRect(40, 670, 120, 40))
        self.testSig.setObjectName("testSig")
        self.startMeas = QtWidgets.QToolButton(self.measCentral)
        self.startMeas.setGeometry(QtCore.QRect(200, 670, 120, 40))
        self.startMeas.setObjectName("startMeas")
        self.tabWidget = QtWidgets.QTabWidget(self.measCentral)
        self.tabWidget.setGeometry(QtCore.QRect(30, 170, 380, 490))
        self.tabWidget.setObjectName("tabWidget")
        self.newTab = QtWidgets.QWidget()
        self.newTab.setObjectName("newTab")
        self.sigLevel = QtWidgets.QDial(self.newTab)
        self.sigLevel.setGeometry(QtCore.QRect(250, 70, 50, 64))
        self.sigLevel.setStatusTip("")
        self.sigLevel.setAccessibleDescription("")
        self.sigLevel.setObjectName("sigLevel")
        self.layoutWidget = QtWidgets.QWidget(self.newTab)
        self.layoutWidget.setGeometry(QtCore.QRect(15, 30, 341, 371))
        self.layoutWidget.setObjectName("layoutWidget")
        self.signalPropGrid = QtWidgets.QGridLayout(self.layoutWidget)
        self.signalPropGrid.setContentsMargins(0, 0, 0, 0)
        self.signalPropGrid.setObjectName("signalPropGrid")
        self.signalTypeGrid = QtWidgets.QFormLayout()
        self.signalTypeGrid.setObjectName("signalTypeGrid")
        self.sigTypeLab = QtWidgets.QLabel(self.layoutWidget)
        self.sigTypeLab.setObjectName("sigTypeLab")
        self.signalTypeGrid.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.sigTypeLab)
        self.sigTypeSel = QtWidgets.QComboBox(self.layoutWidget)
        self.sigTypeSel.setMinimumSize(QtCore.QSize(162, 0))
        self.sigTypeSel.setStatusTip("")
        self.sigTypeSel.setObjectName("sigTypeSel")
        self.signalTypeGrid.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.sigTypeSel)
        self.signalPropGrid.addLayout(self.signalTypeGrid, 0, 0, 1, 1)
        self.LengthGrid = QtWidgets.QFormLayout()
        self.LengthGrid.setObjectName("LengthGrid")
        self.lengthLab = QtWidgets.QLabel(self.layoutWidget)
        self.lengthLab.setObjectName("lengthLab")
        self.LengthGrid.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lengthLab)
        self.lengthSelect = QtWidgets.QComboBox(self.layoutWidget)
        self.lengthSelect.setMinimumSize(QtCore.QSize(162, 0))
        self.lengthSelect.setObjectName("lengthSelect")
        self.LengthGrid.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lengthSelect)
        self.signalPropGrid.addLayout(self.LengthGrid, 1, 0, 1, 1)
        self.sweepGrid = QtWidgets.QFormLayout()
        self.sweepGrid.setObjectName("sweepGrid")
        self.sweepsLab = QtWidgets.QLabel(self.layoutWidget)
        self.sweepsLab.setObjectName("sweepsLab")
        self.sweepGrid.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.sweepsLab)
        self.SweepsSelect = QtWidgets.QComboBox(self.layoutWidget)
        self.SweepsSelect.setMinimumSize(QtCore.QSize(162, 0))
        self.SweepsSelect.setAccessibleDescription("")
        self.SweepsSelect.setObjectName("SweepsSelect")
        self.sweepGrid.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.SweepsSelect)
        self.signalPropGrid.addLayout(self.sweepGrid, 2, 0, 1, 1)
        self.startFreqGrid = QtWidgets.QFormLayout()
        self.startFreqGrid.setObjectName("startFreqGrid")
        self.startFreqLab = QtWidgets.QLabel(self.layoutWidget)
        self.startFreqLab.setObjectName("startFreqLab")
        self.startFreqGrid.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.startFreqLab)
        self.startFreqSlid_2 = QtWidgets.QSlider(self.layoutWidget)
        self.startFreqSlid_2.setMinimumSize(QtCore.QSize(162, 0))
        self.startFreqSlid_2.setMaximum(100000)
        self.startFreqSlid_2.setOrientation(QtCore.Qt.Horizontal)
        self.startFreqSlid_2.setObjectName("startFreqSlid_2")
        self.startFreqGrid.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.startFreqSlid_2)
        self.startFreqSpin = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.startFreqSpin.setMinimumSize(QtCore.QSize(100, 0))
        self.startFreqSpin.setMaximum(100000.0)
        self.startFreqSpin.setProperty("value", 20.0)
        self.startFreqSpin.setObjectName("startFreqSpin")
        self.startFreqGrid.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.startFreqSpin)
        self.signalPropGrid.addLayout(self.startFreqGrid, 3, 0, 1, 1)
        self.endFreqGrid = QtWidgets.QFormLayout()
        self.endFreqGrid.setObjectName("endFreqGrid")
        self.endFreqLab = QtWidgets.QLabel(self.layoutWidget)
        self.endFreqLab.setObjectName("endFreqLab")
        self.endFreqGrid.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.endFreqLab)
        self.endFreqSlid = QtWidgets.QSlider(self.layoutWidget)
        self.endFreqSlid.setMinimumSize(QtCore.QSize(162, 0))
        self.endFreqSlid.setMaximum(100000)
        self.endFreqSlid.setOrientation(QtCore.Qt.Horizontal)
        self.endFreqSlid.setObjectName("endFreqSlid")
        self.endFreqGrid.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.endFreqSlid)
        self.endFreqSpin = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.endFreqSpin.setMinimumSize(QtCore.QSize(100, 0))
        self.endFreqSpin.setMaximum(100000.0)
        self.endFreqSpin.setProperty("value", 20000.0)
        self.endFreqSpin.setObjectName("endFreqSpin")
        self.endFreqGrid.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.endFreqSpin)
        self.signalPropGrid.addLayout(self.endFreqGrid, 4, 0, 1, 1)
        self.layoutWidget.raise_()
        self.sigLevel.raise_()
        self.tabWidget.addTab(self.newTab, "")
        self.LoadTab = QtWidgets.QWidget()
        self.LoadTab.setObjectName("LoadTab")
        self.pushButton = QtWidgets.QPushButton(self.LoadTab)
        self.pushButton.setGeometry(QtCore.QRect(270, 20, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.LoadTab)
        self.lineEdit_3.setGeometry(QtCore.QRect(70, 20, 211, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.LoadTab)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 20, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.recMeasurements = QtWidgets.QToolBox(self.LoadTab)
        self.recMeasurements.setGeometry(QtCore.QRect(30, 70, 291, 351))
        self.recMeasurements.setObjectName("recMeasurements")
        self.measurement = QtWidgets.QWidget()
        self.measurement.setGeometry(QtCore.QRect(0, 0, 291, 235))
        self.measurement.setObjectName("measurement")
        self.recMeasurements.addItem(self.measurement, "")
        self.measurement2 = QtWidgets.QWidget()
        self.measurement2.setGeometry(QtCore.QRect(0, 0, 291, 235))
        self.measurement2.setObjectName("measurement2")
        self.recMeasurements.addItem(self.measurement2, "")
        self.measurement3 = QtWidgets.QWidget()
        self.measurement3.setObjectName("measurement3")
        self.recMeasurements.addItem(self.measurement3, "")
        self.measurement4 = QtWidgets.QWidget()
        self.measurement4.setObjectName("measurement4")
        self.recMeasurements.addItem(self.measurement4, "")
        self.tabWidget.addTab(self.LoadTab, "")
        self.Figures = QtWidgets.QGroupBox(self.measCentral)
        self.Figures.setGeometry(QtCore.QRect(400, 0, 871, 671))
        self.Figures.setObjectName("Figures")
        self.layoutWidget1 = QtWidgets.QWidget(self.Figures)
        self.layoutWidget1.setGeometry(QtCore.QRect(830, 570, 34, 91))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.figBottomGrid = QtWidgets.QFormLayout(self.layoutWidget1)
        self.figBottomGrid.setContentsMargins(0, 0, 0, 0)
        self.figBottomGrid.setObjectName("figBottomGrid")
        self.ViewPropBBottom = QtWidgets.QToolButton(self.layoutWidget1)
        self.ViewPropBBottom.setObjectName("ViewPropBBottom")
        self.figBottomGrid.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.ViewPropBBottom)
        self.ZoomBottom = QtWidgets.QToolButton(self.layoutWidget1)
        self.ZoomBottom.setObjectName("ZoomBottom")
        self.figBottomGrid.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.ZoomBottom)
        self.toolBottom = QtWidgets.QToolButton(self.layoutWidget1)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../resources/icons/WrenchSm.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.toolBottom.setIcon(icon)
        self.toolBottom.setObjectName("toolBottom")
        self.figBottomGrid.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.toolBottom)
        self.layoutWidget2 = QtWidgets.QWidget(self.Figures)
        self.layoutWidget2.setGeometry(QtCore.QRect(830, 260, 34, 91))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.figTopGrid = QtWidgets.QFormLayout(self.layoutWidget2)
        self.figTopGrid.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.figTopGrid.setContentsMargins(0, 0, 0, 0)
        self.figTopGrid.setObjectName("figTopGrid")
        self.ViewPropTop = QtWidgets.QToolButton(self.layoutWidget2)
        self.ViewPropTop.setObjectName("ViewPropTop")
        self.figTopGrid.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.ViewPropTop)
        self.zoomTop = QtWidgets.QToolButton(self.layoutWidget2)
        self.zoomTop.setObjectName("zoomTop")
        self.figTopGrid.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.zoomTop)
        self.toolTop = QtWidgets.QToolButton(self.layoutWidget2)
        self.toolTop.setObjectName("toolTop")
        self.figTopGrid.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.toolTop)
        self.layoutWidget3 = QtWidgets.QWidget(self.measCentral)
        self.layoutWidget3.setGeometry(QtCore.QRect(420, 680, 801, 27))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.progressBar = QtWidgets.QProgressBar(self.layoutWidget3)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout.addWidget(self.progressBar)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.layoutWidget3)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.horizontalLayout.addWidget(self.dateTimeEdit)
        self.layoutWidget4 = QtWidgets.QWidget(self.measCentral)
        self.layoutWidget4.setGeometry(QtCore.QRect(420, 40, 801, 621))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.figVert = QtWidgets.QVBoxLayout(self.layoutWidget4)
        self.figVert.setContentsMargins(0, 0, 0, 0)
        self.figVert.setObjectName("figVert")
        self.plotTop = QtWidgets.QGraphicsView(self.layoutWidget4)
        self.plotTop.setObjectName("plotTop")
        self.figVert.addWidget(self.plotTop)
        self.PlotBottom = QtWidgets.QGraphicsView(self.layoutWidget4)
        self.PlotBottom.setObjectName("PlotBottom")
        self.figVert.addWidget(self.PlotBottom)
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.Figures.raise_()
        self.JbaeLogo.raise_()
        self.testSig.raise_()
        self.startMeas.raise_()
        self.tabWidget.raise_()
        MeasMain.setCentralWidget(self.measCentral)
        self.menubar = QtWidgets.QMenuBar(MeasMain)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 23))
        self.menubar.setObjectName("menubar")
        self.menuJBae_Meas = QtWidgets.QMenu(self.menubar)
        self.menuJBae_Meas.setObjectName("menuJBae_Meas")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MeasMain.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MeasMain)
        self.statusbar.setObjectName("statusbar")
        MeasMain.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MeasMain)
        self.actionExit.setEnabled(True)
        self.actionExit.setObjectName("actionExit")
        self.actionSave = QtWidgets.QAction(MeasMain)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_All = QtWidgets.QAction(MeasMain)
        self.actionSave_All.setObjectName("actionSave_All")
        self.actionPreferences = QtWidgets.QAction(MeasMain)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionSave_As = QtWidgets.QAction(MeasMain)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionDelete_Measurement = QtWidgets.QAction(MeasMain)
        self.actionDelete_Measurement.setObjectName("actionDelete_Measurement")
        self.menuJBae_Meas.addAction(self.actionSave)
        self.menuJBae_Meas.addAction(self.actionSave_As)
        self.menuJBae_Meas.addAction(self.actionSave_All)
        self.menuJBae_Meas.addSeparator()
        self.menuJBae_Meas.addAction(self.actionPreferences)
        self.menuJBae_Meas.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionDelete_Measurement)
        self.menubar.addAction(self.menuJBae_Meas.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MeasMain)
        self.tabWidget.setCurrentIndex(1)
        self.recMeasurements.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MeasMain)
        MeasMain.setTabOrder(self.testSig, self.startMeas)
        MeasMain.setTabOrder(self.startMeas, self.lineEdit_3)
        MeasMain.setTabOrder(self.lineEdit_3, self.ViewPropBBottom)
        MeasMain.setTabOrder(self.ViewPropBBottom, self.tabWidget)
        MeasMain.setTabOrder(self.tabWidget, self.sigLevel)
        MeasMain.setTabOrder(self.sigLevel, self.sigTypeSel)
        MeasMain.setTabOrder(self.sigTypeSel, self.lengthSelect)
        MeasMain.setTabOrder(self.lengthSelect, self.SweepsSelect)
        MeasMain.setTabOrder(self.SweepsSelect, self.startFreqSlid_2)
        MeasMain.setTabOrder(self.startFreqSlid_2, self.endFreqSlid)
        MeasMain.setTabOrder(self.endFreqSlid, self.pushButton_2)
        MeasMain.setTabOrder(self.pushButton_2, self.toolTop)
        MeasMain.setTabOrder(self.toolTop, self.zoomTop)
        MeasMain.setTabOrder(self.zoomTop, self.ViewPropTop)
        MeasMain.setTabOrder(self.ViewPropTop, self.ZoomBottom)
        MeasMain.setTabOrder(self.ZoomBottom, self.toolBottom)
        MeasMain.setTabOrder(self.toolBottom, self.pushButton)
        MeasMain.setTabOrder(self.pushButton, self.dateTimeEdit)
        MeasMain.setTabOrder(self.dateTimeEdit, self.JbaeLogo)
        MeasMain.setTabOrder(self.JbaeLogo, self.PlotBottom)
        MeasMain.setTabOrder(self.PlotBottom, self.plotTop)

    def retranslateUi(self, MeasMain):
        _translate = QtCore.QCoreApplication.translate
        MeasMain.setWindowTitle(_translate("MeasMain", "Meas"))
        self.testSig.setToolTip(_translate("MeasMain", "Open Menu Test Signal"))
        self.testSig.setText(_translate("MeasMain", "Test Signal"))
        self.startMeas.setToolTip(_translate("MeasMain", "Start Measurement"))
        self.startMeas.setText(_translate("MeasMain", "Start Measurement"))
        self.sigLevel.setToolTip(_translate("MeasMain", "Set Volume Level"))
        self.sigTypeLab.setText(_translate("MeasMain", "Signal Type"))
        self.sigTypeSel.setToolTip(_translate("MeasMain", "Select Signal Type"))
        self.lengthLab.setText(_translate("MeasMain", "Length Signal"))
        self.lengthSelect.setToolTip(_translate("MeasMain", "Select Length of Signal in k samples"))
        self.sweepsLab.setText(_translate("MeasMain", "No Sweeps"))
        self.SweepsSelect.setToolTip(_translate("MeasMain", "Select number of itterations"))
        self.startFreqLab.setText(_translate("MeasMain", "Start Frequecy"))
        self.startFreqSlid_2.setToolTip(_translate("MeasMain", "Select Start Frequency"))
        self.startFreqSpin.setToolTip(_translate("MeasMain", "Set Start Frequency"))
        self.endFreqLab.setText(_translate("MeasMain", "End Frequency"))
        self.endFreqSlid.setToolTip(_translate("MeasMain", "Select End Frequency"))
        self.endFreqSpin.setToolTip(_translate("MeasMain", "Set End Frequency"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.newTab), _translate("MeasMain", "Create New"))
        self.pushButton.setText(_translate("MeasMain", "PushButton"))
        self.pushButton_2.setText(_translate("MeasMain", "PushButton"))
        self.recMeasurements.setItemText(self.recMeasurements.indexOf(self.measurement), _translate("MeasMain", "Page 1"))
        self.recMeasurements.setItemText(self.recMeasurements.indexOf(self.measurement2), _translate("MeasMain", "Page 2"))
        self.recMeasurements.setItemText(self.recMeasurements.indexOf(self.measurement3), _translate("MeasMain", "Page"))
        self.recMeasurements.setItemText(self.recMeasurements.indexOf(self.measurement4), _translate("MeasMain", "Page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.LoadTab), _translate("MeasMain", "Load Exist"))
        self.Figures.setTitle(_translate("MeasMain", "Figures"))
        self.ViewPropBBottom.setText(_translate("MeasMain", "..."))
        self.ZoomBottom.setText(_translate("MeasMain", "..."))
        self.toolBottom.setText(_translate("MeasMain", "..."))
        self.ViewPropTop.setText(_translate("MeasMain", "..."))
        self.zoomTop.setText(_translate("MeasMain", "..."))
        self.toolTop.setText(_translate("MeasMain", "..."))
        self.menuJBae_Meas.setTitle(_translate("MeasMain", "File"))
        self.menuEdit.setTitle(_translate("MeasMain", "Edit"))
        self.actionExit.setText(_translate("MeasMain", "Exit"))
        self.actionExit.setToolTip(_translate("MeasMain", "Exit Meas"))
        self.actionExit.setShortcut(_translate("MeasMain", "Ctrl+Q"))
        self.actionSave.setText(_translate("MeasMain", "Save"))
        self.actionSave.setToolTip(_translate("MeasMain", "Save Measurements"))
        self.actionSave.setShortcut(_translate("MeasMain", "Ctrl+S"))
        self.actionSave_All.setText(_translate("MeasMain", "Save All"))
        self.actionSave_All.setToolTip(_translate("MeasMain", "Save All Measurements"))
        self.actionSave_All.setShortcut(_translate("MeasMain", "Ctrl+Shift+S"))
        self.actionPreferences.setText(_translate("MeasMain", "Preferences"))
        self.actionPreferences.setToolTip(_translate("MeasMain", "Preferences Meas"))
        self.actionPreferences.setShortcut(_translate("MeasMain", "Ctrl+I"))
        self.actionSave_As.setText(_translate("MeasMain", "Save As"))
        self.actionSave_As.setToolTip(_translate("MeasMain", "Save Measurements As"))
        self.actionDelete_Measurement.setText(_translate("MeasMain", "Delete Measurement"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MeasMain = QtWidgets.QMainWindow()
    ui = Ui_MeasMain()
    ui.setupUi(MeasMain)
    MeasMain.show()
    sys.exit(app.exec_())

