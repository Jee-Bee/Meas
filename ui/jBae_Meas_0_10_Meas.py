# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jBae_Meas_0_10_Meas.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets  # , QtGui

class Ui_measDialog(object):
    def setupUi(self, measDialog):
        measDialog.setObjectName("measDialog")
        measDialog.resize(287, 440)
        self.gridLayout_3 = QtWidgets.QGridLayout(measDialog)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridtime = QtWidgets.QGridLayout()
        self.gridtime.setObjectName("gridtime")
        self.dateEdit = QtWidgets.QDateEdit(measDialog)
        self.dateEdit.setMinimumSize(QtCore.QSize(140, 0))
        self.dateEdit.setReadOnly(False)
        self.dateEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateEdit.setObjectName("dateEdit")
        self.gridtime.addWidget(self.dateEdit, 0, 0, 1, 1)
        self.timeEdit = QtWidgets.QTimeEdit(measDialog)
        self.timeEdit.setMinimumSize(QtCore.QSize(65, 0))
        self.timeEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.timeEdit.setObjectName("timeEdit")
        self.gridtime.addWidget(self.timeEdit, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridtime, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(measDialog)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_3.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.gridfunc = QtWidgets.QGridLayout()
        self.gridfunc.setObjectName("gridfunc")
        self.LevelSend = QtWidgets.QSpinBox(measDialog)
        self.LevelSend.setMinimum(-192)
        self.LevelSend.setMaximum(0)
        self.LevelSend.setObjectName("LevelSend")
        self.gridfunc.addWidget(self.LevelSend, 1, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.endFreqLab = QtWidgets.QLabel(measDialog)
        self.endFreqLab.setObjectName("endFreqLab")
        self.gridLayout_2.addWidget(self.endFreqLab, 0, 0, 1, 1)
        self.endFreqSlid = QtWidgets.QSlider(measDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.endFreqSlid.sizePolicy().hasHeightForWidth())
        self.endFreqSlid.setSizePolicy(sizePolicy)
        self.endFreqSlid.setMinimumSize(QtCore.QSize(140, 0))
        self.endFreqSlid.setMaximum(100000)
        self.endFreqSlid.setOrientation(QtCore.Qt.Horizontal)
        self.endFreqSlid.setObjectName("endFreqSlid")
        self.gridLayout_2.addWidget(self.endFreqSlid, 1, 0, 1, 1)
        self.endFreqSpin = QtWidgets.QDoubleSpinBox(measDialog)
        self.endFreqSpin.setMinimumSize(QtCore.QSize(65, 0))
        self.endFreqSpin.setDecimals(0)
        self.endFreqSpin.setMaximum(100000.0)
        self.endFreqSpin.setProperty("value", 20000.0)
        self.endFreqSpin.setObjectName("endFreqSpin")
        self.gridLayout_2.addWidget(self.endFreqSpin, 1, 1, 1, 1)
        self.gridfunc.addLayout(self.gridLayout_2, 5, 0, 1, 2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.startFreqLab = QtWidgets.QLabel(measDialog)
        self.startFreqLab.setObjectName("startFreqLab")
        self.gridLayout.addWidget(self.startFreqLab, 0, 0, 1, 1)
        self.startFreqSlid = QtWidgets.QSlider(measDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startFreqSlid.sizePolicy().hasHeightForWidth())
        self.startFreqSlid.setSizePolicy(sizePolicy)
        self.startFreqSlid.setMinimumSize(QtCore.QSize(140, 0))
        self.startFreqSlid.setMaximum(100000)
        self.startFreqSlid.setOrientation(QtCore.Qt.Horizontal)
        self.startFreqSlid.setObjectName("startFreqSlid")
        self.gridLayout.addWidget(self.startFreqSlid, 1, 0, 1, 1)
        self.startFreqSpin = QtWidgets.QDoubleSpinBox(measDialog)
        self.startFreqSpin.setMinimumSize(QtCore.QSize(65, 0))
        self.startFreqSpin.setMaximum(100000.0)
        self.startFreqSpin.setProperty("value", 20.0)
        self.startFreqSpin.setObjectName("startFreqSpin")
        self.gridLayout.addWidget(self.startFreqSpin, 1, 1, 1, 1)
        self.gridfunc.addLayout(self.gridLayout, 4, 0, 1, 2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.repeatsLab = QtWidgets.QLabel(measDialog)
        self.repeatsLab.setObjectName("repeatsLab")
        self.verticalLayout_5.addWidget(self.repeatsLab)
        self.repeatsSel = QtWidgets.QComboBox(measDialog)
        self.repeatsSel.setMinimumSize(QtCore.QSize(140, 0))
        self.repeatsSel.setAccessibleDescription("")
        self.repeatsSel.setObjectName("repeatsSel")
        self.verticalLayout_5.addWidget(self.repeatsSel)
        self.gridfunc.addLayout(self.verticalLayout_5, 3, 0, 1, 1)
        self.Level_lab = QtWidgets.QLabel(measDialog)
        self.Level_lab.setObjectName("Level_lab")
        self.gridfunc.addWidget(self.Level_lab, 0, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.sigTypeLab = QtWidgets.QLabel(measDialog)
        self.sigTypeLab.setObjectName("sigTypeLab")
        self.verticalLayout_3.addWidget(self.sigTypeLab)
        self.sigTypeSel = QtWidgets.QComboBox(measDialog)
        self.sigTypeSel.setMinimumSize(QtCore.QSize(140, 0))
        self.sigTypeSel.setStatusTip("")
        self.sigTypeSel.setObjectName("sigTypeSel")
        self.verticalLayout_3.addWidget(self.sigTypeSel)
        self.gridfunc.addLayout(self.verticalLayout_3, 0, 0, 2, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lengthLab = QtWidgets.QLabel(measDialog)
        self.lengthLab.setObjectName("lengthLab")
        self.verticalLayout_4.addWidget(self.lengthLab)
        self.lengthSelect = QtWidgets.QComboBox(measDialog)
        self.lengthSelect.setMinimumSize(QtCore.QSize(140, 0))
        self.lengthSelect.setObjectName("lengthSelect")
        self.verticalLayout_4.addWidget(self.lengthSelect)
        self.gridfunc.addLayout(self.verticalLayout_4, 2, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridfunc, 2, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(measDialog)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_3.addWidget(self.progressBar, 3, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(measDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_3.addWidget(self.buttonBox, 4, 0, 1, 1)

        self.retranslateUi(measDialog)
        self.buttonBox.accepted.connect(measDialog.accept)
        self.buttonBox.rejected.connect(measDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(measDialog)

    def retranslateUi(self, measDialog):
        _translate = QtCore.QCoreApplication.translate
        measDialog.setWindowTitle(_translate("measDialog", "Dialog"))
        self.lineEdit.setText(_translate("measDialog", "Meas Comment here"))
        self.endFreqLab.setText(_translate("measDialog", "End Frequency"))
        self.endFreqSlid.setToolTip(_translate("measDialog", "Select End Frequency"))
        self.endFreqSpin.setToolTip(_translate("measDialog", "Set End Frequency"))
        self.startFreqLab.setText(_translate("measDialog", "Start Frequecy"))
        self.startFreqSlid.setToolTip(_translate("measDialog", "Select Start Frequency"))
        self.startFreqSpin.setToolTip(_translate("measDialog", "Set Start Frequency"))
        self.repeatsLab.setText(_translate("measDialog", "No Repeats"))
        self.repeatsSel.setToolTip(_translate("measDialog", "Select number of itterations"))
        self.Level_lab.setText(_translate("measDialog", "SoundLevel"))
        self.sigTypeLab.setText(_translate("measDialog", "Signal Type"))
        self.sigTypeSel.setToolTip(_translate("measDialog", "Select Signal Type"))
        self.lengthLab.setText(_translate("measDialog", "Length Signal"))
        self.lengthSelect.setToolTip(_translate("measDialog", "Select Length of Signal in k samples"))

