# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QtPyTimer2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.12
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

# Converted to PySide6 and other tweaks done by hand
# THIS FILE WILL NOT BE REGENERATED AS IS by it's UI file. DO NOT OVERWRITE! Necessary tweaks will be lost

#MIT License

# Copyright (c) 2024 GunkSlinger

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from PySide6.QtCore import QMetaObject, QRect, Qt, QCoreApplication
from PySide6.QtGui import QFont, QCursor
from PySide6.QtWidgets import (QWidget, QLayout, QHBoxLayout, QVBoxLayout, QSpinBox, QToolBar,
                                QAbstractSpinBox, QToolButton, QSizePolicy, QLabel, QProgressBar,
                                QListWidget, QDialog, QDialogButtonBox, QLabel)
from datetime import datetime as dt


class FinishDialog(QDialog):
    def __init__(self, presetName):
        super().__init__()

        self.resize(250, 120)
        self.setLayout(QVBoxLayout())
        finlab = QLabel()
        self.now = dt.today()
        if len(presetName):
            self.preambleText = presetName + " finished"
        else:
            self.preambleText = "Timer Finished"

        finlab.setText(self.preambleText + " at: " + self.now.strftime("%b %d, %Y %I:%M:%S %p"))
        self.setWindowTitle(self.preambleText)
        ok_button = QDialogButtonBox(QDialogButtonBox.Ok)
        ok_button.accepted.connect(self.accept)

        self.layout().addWidget(finlab)
        self.layout().addWidget(ok_button)

    def accept(self):
        self.close()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        expnd = 200
        MainWindow.setFixedSize(600+expnd, 400)

        self.toolbar = QToolBar(u"Tool Bar", MainWindow)
        self.toolbar.setMovable(False)
        self.toolbar.setObjectName(u"toolBar")
        self.presetsToolButton = QToolButton(self.toolbar)
        self.presetsToolButton.setText(u"Presets")
        self.toolbar.addWidget(self.presetsToolButton)
        MainWindow.addToolBar(self.toolbar)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.spinButtonsHorizontalLayoutWidget = QWidget(self.centralwidget)
        self.spinButtonsHorizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.spinButtonsHorizontalLayoutWidget.setGeometry(QRect(0, 20, 541+expnd, 61))
        self.spinButtonsHorizontalLayout = QHBoxLayout(self.spinButtonsHorizontalLayoutWidget)
        self.spinButtonsHorizontalLayout.setObjectName(u"horizontalLayout")
        self.spinButtonsHorizontalLayout.setContentsMargins(10, 0, 10, 0)
        font = QFont()
        font.setBold(True)
        self.spinBoxHours = QSpinBox(self.spinButtonsHorizontalLayoutWidget)
        self.spinBoxHours.setObjectName(u"spinBoxHours")
        self.spinBoxHours.setFont(font)
        self.spinBoxHours.setAlignment(Qt.AlignCenter)

        self.spinButtonsHorizontalLayout.addWidget(self.spinBoxHours)

        self.spinBoxMinutes = QSpinBox(self.spinButtonsHorizontalLayoutWidget)
        self.spinBoxMinutes.setObjectName(u"spinBoxMinutes")
        self.spinBoxMinutes.setFont(font)
        self.spinBoxMinutes.setAlignment(Qt.AlignCenter)
        self.spinBoxMinutes.setMaximum(59)

        self.spinButtonsHorizontalLayout.addWidget(self.spinBoxMinutes)

        self.spinBoxSeconds = QSpinBox(self.spinButtonsHorizontalLayoutWidget)
        self.spinBoxSeconds.setObjectName(u"spinBoxSeconds")
        self.spinBoxSeconds.setFont(font)
        self.spinBoxSeconds.setAlignment(Qt.AlignCenter)
        self.spinBoxSeconds.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.spinBoxSeconds.setMaximum(59)

        self.spinButtonsHorizontalLayout.addWidget(self.spinBoxSeconds)

        self.startStopButtonHorizontalLayoutWidget = QWidget(self.centralwidget)
        self.startStopButtonHorizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget_2")
        self.startStopButtonHorizontalLayoutWidget.setGeometry(QRect(290, 100, 311+expnd, 80))
        self.startStopButtonHorizontalLayout = QHBoxLayout(self.startStopButtonHorizontalLayoutWidget)
        self.startStopButtonHorizontalLayout.setObjectName(u"horizontalLayout_2")
        self.startStopButtonHorizontalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.startStopButtonHorizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.toolButtonStartStop = QToolButton(self.startStopButtonHorizontalLayoutWidget)
        self.toolButtonStartStop.setObjectName(u"toolButtonStartStop")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButtonStartStop.sizePolicy().hasHeightForWidth())
        self.toolButtonStartStop.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamily(u"Crillee")
        font1.setPointSize(35)
        font1.setBold(False)
        self.toolButtonStartStop.setFont(font1)
        self.toolButtonStartStop.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButtonStartStop.setToolButtonStyle(Qt.ToolButtonTextOnly)

        self.startStopButtonHorizontalLayout.addWidget(self.toolButtonStartStop)

        self.countDownVerticalLayoutWidget = QWidget(self.centralwidget)
        self.countDownVerticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.countDownVerticalLayoutWidget.setGeometry(QRect(125, 190, 521, 81))
        self.countDownVerticalLayout = QVBoxLayout(self.countDownVerticalLayoutWidget)
        self.countDownVerticalLayout.setObjectName(u"verticalLayout")
        self.countDownVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.labelCountDown = QLabel(self.countDownVerticalLayoutWidget)
        self.labelCountDown.setObjectName(u"labelCountDown")
        font2 = QFont()
        font2.setPointSize(35)
        font2.setBold(True)
        self.labelCountDown.setFont(font2)
        self.labelCountDown.setAutoFillBackground(False)
        self.labelCountDown.setTextFormat(Qt.AutoText)
        self.labelCountDown.setAlignment(Qt.AlignCenter)

        self.countDownVerticalLayout.addWidget(self.labelCountDown)

        self.labelDateVerticalLayoutWidget = QWidget(self.centralwidget)
        self.labelDateVerticalLayoutWidget.setObjectName(u"verticalLayoutWidget_2")
        self.labelDateVerticalLayoutWidget.setGeometry(QRect(10, 270, 560+expnd, 75))
        self.labelDateVerticalLayout = QVBoxLayout(self.labelDateVerticalLayoutWidget)
        self.labelDateVerticalLayout.setObjectName(u"verticalLayout_2")
        self.labelDateVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.labelDate = QLabel(self.labelDateVerticalLayoutWidget)
        self.labelDate.setObjectName(u"labelDate")
        font3 = QFont()
        font3.setPointSize(15)
        self.labelDate.setFont(font3)
        self.labelDate.setAlignment(Qt.AlignCenter)

        self.labelDateVerticalLayout.addWidget(self.labelDate)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"QtPy Timer", None))
        self.spinBoxHours.setSuffix(QCoreApplication.translate("MainWindow", u"  hours", None))
        self.spinBoxMinutes.setSuffix(QCoreApplication.translate("MainWindow", u"  minutes", None))
        self.spinBoxSeconds.setSuffix(QCoreApplication.translate("MainWindow", u"  seconds", None))
        self.toolButtonStartStop.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.labelCountDown.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.labelDate.setText(QCoreApplication.translate("MainWindow", u"Today's Date + timer", None))
    # retranslateUi

