# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jBae_Meas_0_15.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MeasMain(object):
    def setupUi(self, MeasMain):
        MeasMain.setObjectName("MeasMain")
        MeasMain.resize(800, 582)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MeasMain.sizePolicy().hasHeightForWidth())
        MeasMain.setSizePolicy(sizePolicy)
        MeasMain.setStyleSheet("font: 9pt \"SansSerif\";")
        self.measCentral = QtWidgets.QWidget(MeasMain)
        self.measCentral.setObjectName("measCentral")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.measCentral)
        self.gridLayout_3.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.jBaeLogo = QtWidgets.QLabel(self.measCentral)
        self.jBaeLogo.setMinimumSize(QtCore.QSize(240, 90))
        self.jBaeLogo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.jBaeLogo.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.jBaeLogo.setText("")
        self.jBaeLogo.setObjectName("jBaeLogo")
        self.gridLayout_3.addWidget(self.jBaeLogo, 0, 0, 1, 2)
        self.Plot_top = QtWidgets.QWidget(self.measCentral)
        self.Plot_top.setMinimumSize(QtCore.QSize(0, 240))
        self.Plot_top.setObjectName("Plot_top")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.Plot_top)
        self.verticalLayout_7.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.gridLayout_3.addWidget(self.Plot_top, 0, 2, 2, 1)
        self.FigTopLayout = QtWidgets.QVBoxLayout()
        self.FigTopLayout.setContentsMargins(9, 9, 9, 9)
        self.FigTopLayout.setSpacing(6)
        self.FigTopLayout.setObjectName("FigTopLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 180, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.FigTopLayout.addItem(spacerItem)
        self.homeTop = QtWidgets.QToolButton(self.measCentral)
        self.homeTop.setObjectName("homeTop")
        self.FigTopLayout.addWidget(self.homeTop)
        self.panTop = QtWidgets.QToolButton(self.measCentral)
        self.panTop.setObjectName("panTop")
        self.FigTopLayout.addWidget(self.panTop)
        self.zoomTop = QtWidgets.QToolButton(self.measCentral)
        self.zoomTop.setObjectName("zoomTop")
        self.FigTopLayout.addWidget(self.zoomTop)
        self.prefTop = QtWidgets.QToolButton(self.measCentral)
        self.prefTop.setObjectName("prefTop")
        self.FigTopLayout.addWidget(self.prefTop)
        self.gridLayout_3.addLayout(self.FigTopLayout, 0, 3, 2, 1)
        self.Recordings = QtWidgets.QToolBox(self.measCentral)
        self.Recordings.setObjectName("Recordings")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setGeometry(QtCore.QRect(0, 0, 240, 334))
        self.page_1.setObjectName("page_1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_1)
        self.gridLayout_2.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Recordings.addItem(self.page_1, "")
        self.gridLayout_3.addWidget(self.Recordings, 1, 0, 2, 2)
        self.Plot_bottom = QtWidgets.QWidget(self.measCentral)
        self.Plot_bottom.setMinimumSize(QtCore.QSize(0, 240))
        self.Plot_bottom.setObjectName("Plot_bottom")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.Plot_bottom)
        self.verticalLayout_6.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout_3.addWidget(self.Plot_bottom, 2, 2, 1, 1)
        self.FigBottomLayout = QtWidgets.QVBoxLayout()
        self.FigBottomLayout.setContentsMargins(9, 9, 9, 9)
        self.FigBottomLayout.setSpacing(6)
        self.FigBottomLayout.setObjectName("FigBottomLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 180, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.FigBottomLayout.addItem(spacerItem1)
        self.homeBottom = QtWidgets.QToolButton(self.measCentral)
        self.homeBottom.setObjectName("homeBottom")
        self.FigBottomLayout.addWidget(self.homeBottom)
        self.panBottom = QtWidgets.QToolButton(self.measCentral)
        self.panBottom.setObjectName("panBottom")
        self.FigBottomLayout.addWidget(self.panBottom)
        self.ZoomBottom = QtWidgets.QToolButton(self.measCentral)
        self.ZoomBottom.setObjectName("ZoomBottom")
        self.FigBottomLayout.addWidget(self.ZoomBottom)
        self.prefBottom = QtWidgets.QToolButton(self.measCentral)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../resources/icons/WrenchSm.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.prefBottom.setIcon(icon)
        self.prefBottom.setObjectName("prefBottom")
        self.FigBottomLayout.addWidget(self.prefBottom)
        self.gridLayout_3.addLayout(self.FigBottomLayout, 2, 3, 1, 1)
        self.testSig = QtWidgets.QToolButton(self.measCentral)
        self.testSig.setObjectName("testSig")
        self.gridLayout_3.addWidget(self.testSig, 3, 0, 1, 1)
        self.runMeas = QtWidgets.QToolButton(self.measCentral)
        self.runMeas.setObjectName("runMeas")
        self.gridLayout_3.addWidget(self.runMeas, 3, 1, 1, 1)
        self.DateTimeLayout = QtWidgets.QHBoxLayout()
        self.DateTimeLayout.setContentsMargins(9, 9, 9, 9)
        self.DateTimeLayout.setSpacing(6)
        self.DateTimeLayout.setObjectName("DateTimeLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.DateTimeLayout.addItem(spacerItem2)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.measCentral)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.DateTimeLayout.addWidget(self.dateTimeEdit)
        self.gridLayout_3.addLayout(self.DateTimeLayout, 3, 2, 1, 1)
        self.testSig.raise_()
        self.runMeas.raise_()
        self.jBaeLogo.raise_()
        self.Plot_top.raise_()
        self.Plot_bottom.raise_()
        self.Recordings.raise_()
        MeasMain.setCentralWidget(self.measCentral)
        self.menubar = QtWidgets.QMenuBar(MeasMain)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuMeasurements = QtWidgets.QMenu(self.menubar)
        self.menuMeasurements.setObjectName("menuMeasurements")
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
        self.actionOpen = QtWidgets.QAction(MeasMain)
        self.actionOpen.setObjectName("actionOpen")
        self.actionNew = QtWidgets.QAction(MeasMain)
        self.actionNew.setObjectName("actionNew")
        self.actionTest_Signal = QtWidgets.QAction(MeasMain)
        self.actionTest_Signal.setObjectName("actionTest_Signal")
        self.actionRun_Measurent = QtWidgets.QAction(MeasMain)
        self.actionRun_Measurent.setObjectName("actionRun_Measurent")
        self.actionHome_Top = QtWidgets.QAction(MeasMain)
        self.actionHome_Top.setObjectName("actionHome_Top")
        self.actionPan_Top = QtWidgets.QAction(MeasMain)
        self.actionPan_Top.setObjectName("actionPan_Top")
        self.actionZoom_Top = QtWidgets.QAction(MeasMain)
        self.actionZoom_Top.setObjectName("actionZoom_Top")
        self.actionFig_Preferences_Top = QtWidgets.QAction(MeasMain)
        self.actionFig_Preferences_Top.setObjectName("actionFig_Preferences_Top")
        self.actionHome_Bottom = QtWidgets.QAction(MeasMain)
        self.actionHome_Bottom.setObjectName("actionHome_Bottom")
        self.actionPan_Bottom = QtWidgets.QAction(MeasMain)
        self.actionPan_Bottom.setObjectName("actionPan_Bottom")
        self.actionZoom_Bottom = QtWidgets.QAction(MeasMain)
        self.actionZoom_Bottom.setObjectName("actionZoom_Bottom")
        self.actionFig_Preferences_Bottom = QtWidgets.QAction(MeasMain)
        self.actionFig_Preferences_Bottom.setObjectName("actionFig_Preferences_Bottom")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionSave_All)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPreferences)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionDelete_Measurement)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionHome_Top)
        self.menuEdit.addAction(self.actionPan_Top)
        self.menuEdit.addAction(self.actionZoom_Top)
        self.menuEdit.addAction(self.actionFig_Preferences_Top)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionHome_Bottom)
        self.menuEdit.addAction(self.actionPan_Bottom)
        self.menuEdit.addAction(self.actionZoom_Bottom)
        self.menuEdit.addAction(self.actionFig_Preferences_Bottom)
        self.menuMeasurements.addAction(self.actionTest_Signal)
        self.menuMeasurements.addAction(self.actionRun_Measurent)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuMeasurements.menuAction())

        self.retranslateUi(MeasMain)
        self.Recordings.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MeasMain)
        MeasMain.setTabOrder(self.runMeas, self.testSig)
        MeasMain.setTabOrder(self.testSig, self.panTop)
        MeasMain.setTabOrder(self.panTop, self.zoomTop)
        MeasMain.setTabOrder(self.zoomTop, self.prefTop)
        MeasMain.setTabOrder(self.prefTop, self.panBottom)
        MeasMain.setTabOrder(self.panBottom, self.ZoomBottom)
        MeasMain.setTabOrder(self.ZoomBottom, self.prefBottom)
        MeasMain.setTabOrder(self.prefBottom, self.dateTimeEdit)

    def retranslateUi(self, MeasMain):
        _translate = QtCore.QCoreApplication.translate
        MeasMain.setWindowTitle(_translate("MeasMain", "Meas"))
        self.homeTop.setText(_translate("MeasMain", "..."))
        self.panTop.setText(_translate("MeasMain", "..."))
        self.zoomTop.setText(_translate("MeasMain", "..."))
        self.prefTop.setText(_translate("MeasMain", "..."))
        self.Recordings.setItemText(self.Recordings.indexOf(self.page_1), _translate("MeasMain", "Page 1"))
        self.homeBottom.setText(_translate("MeasMain", "..."))
        self.panBottom.setText(_translate("MeasMain", "..."))
        self.ZoomBottom.setText(_translate("MeasMain", "..."))
        self.prefBottom.setText(_translate("MeasMain", "..."))
        self.testSig.setToolTip(_translate("MeasMain", "Open Menu Test Signal"))
        self.testSig.setText(_translate("MeasMain", "Test Signal"))
        self.runMeas.setToolTip(_translate("MeasMain", "Run Measurement"))
        self.runMeas.setText(_translate("MeasMain", "Run Measurement"))
        self.menuFile.setTitle(_translate("MeasMain", "&File"))
        self.menuEdit.setTitle(_translate("MeasMain", "&Edit"))
        self.menuMeasurements.setTitle(_translate("MeasMain", "&Measurements"))
        self.actionExit.setText(_translate("MeasMain", "&Quit"))
        self.actionExit.setIconText(_translate("MeasMain", "Quit"))
        self.actionExit.setToolTip(_translate("MeasMain", "Exit Meas"))
        self.actionExit.setShortcut(_translate("MeasMain", "Ctrl+Q"))
        self.actionSave.setText(_translate("MeasMain", "&Save"))
        self.actionSave.setIconText(_translate("MeasMain", "&Save"))
        self.actionSave.setToolTip(_translate("MeasMain", "Save Measurements"))
        self.actionSave.setShortcut(_translate("MeasMain", "Ctrl+S"))
        self.actionSave_All.setText(_translate("MeasMain", "Save All"))
        self.actionSave_All.setToolTip(_translate("MeasMain", "Save All Measurements"))
        self.actionSave_All.setShortcut(_translate("MeasMain", "Ctrl+Shift+S"))
        self.actionPreferences.setText(_translate("MeasMain", "&Preferences"))
        self.actionPreferences.setIconText(_translate("MeasMain", "&Preferences"))
        self.actionPreferences.setToolTip(_translate("MeasMain", "Preferences Meas"))
        self.actionPreferences.setShortcut(_translate("MeasMain", "Ctrl+I"))
        self.actionSave_As.setText(_translate("MeasMain", "Save As"))
        self.actionSave_As.setToolTip(_translate("MeasMain", "Save Measurements As"))
        self.actionDelete_Measurement.setText(_translate("MeasMain", "&Delete Measurement"))
        self.actionOpen.setText(_translate("MeasMain", "&Open"))
        self.actionOpen.setIconText(_translate("MeasMain", "&Open"))
        self.actionOpen.setShortcut(_translate("MeasMain", "Ctrl+O"))
        self.actionNew.setText(_translate("MeasMain", "&New"))
        self.actionNew.setIconText(_translate("MeasMain", "&New"))
        self.actionNew.setShortcut(_translate("MeasMain", "Ctrl+N"))
        self.actionTest_Signal.setText(_translate("MeasMain", "&Test Signal"))
        self.actionRun_Measurent.setText(_translate("MeasMain", "&Run Measurent"))
        self.actionHome_Top.setText(_translate("MeasMain", "Home Top"))
        self.actionPan_Top.setText(_translate("MeasMain", "Pan Top"))
        self.actionZoom_Top.setText(_translate("MeasMain", "Zoom Top"))
        self.actionFig_Preferences_Top.setText(_translate("MeasMain", "Fig Preferences Top"))
        self.actionHome_Bottom.setText(_translate("MeasMain", "Home Bottom"))
        self.actionPan_Bottom.setText(_translate("MeasMain", "Pan Bottom"))
        self.actionZoom_Bottom.setText(_translate("MeasMain", "Zoom Bottom"))
        self.actionFig_Preferences_Bottom.setText(_translate("MeasMain", "Fig Preferences Bottom"))

