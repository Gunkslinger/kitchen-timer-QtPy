# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QtPyTimer.ui'
## 
## Created by: Qt User Interface Compiler version 5.15.12
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import QMetaObject, QRect, Qt, QCoreApplication
from PySide2.QtGui import QFont, QCursor
from PySide2.QtWidgets import (QWidget, QLayout, QHBoxLayout, QVBoxLayout, QSpinBox,
                                QAbstractSpinBox, QToolButton, QSizePolicy, QLabel, QProgressBar)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(540, 300)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 541, 61))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 0, 10, 0)
        self.spinBoxHours = QSpinBox(self.horizontalLayoutWidget)
        self.spinBoxHours.setObjectName(u"spinBoxHours")
        font = QFont()
        font.setBold(True)
        self.spinBoxHours.setFont(font)
        self.spinBoxHours.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.spinBoxHours)

        self.spinBoxMinutes = QSpinBox(self.horizontalLayoutWidget)
        self.spinBoxMinutes.setObjectName(u"spinBoxMinutes")
        self.spinBoxMinutes.setFont(font)
        self.spinBoxMinutes.setAlignment(Qt.AlignCenter)
        self.spinBoxMinutes.setMaximum(59)

        self.horizontalLayout.addWidget(self.spinBoxMinutes)

        self.spinBoxSeconds = QSpinBox(self.horizontalLayoutWidget)
        self.spinBoxSeconds.setObjectName(u"spinBoxSeconds")
        self.spinBoxSeconds.setFont(font)
        self.spinBoxSeconds.setAlignment(Qt.AlignCenter)
        self.spinBoxSeconds.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.spinBoxSeconds.setMaximum(59)

        self.horizontalLayout.addWidget(self.spinBoxSeconds)

        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(120, 70, 311, 76))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.toolButtonStartStop = QToolButton(self.horizontalLayoutWidget_2)
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

        self.horizontalLayout_2.addWidget(self.toolButtonStartStop)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 190, 521, 81))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.labelCountDown = QLabel(self.verticalLayoutWidget)
        self.labelCountDown.setObjectName(u"labelCountDown")
        font2 = QFont()
        font2.setPointSize(35)
        font2.setBold(True)
        self.labelCountDown.setFont(font2)
        self.labelCountDown.setAutoFillBackground(False)
        self.labelCountDown.setTextFormat(Qt.AutoText)
        self.labelCountDown.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.labelCountDown)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(9, 299, 521, 74))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.labelDate = QLabel(self.verticalLayoutWidget_2)
        self.labelDate.setObjectName(u"labelDate")
        font3 = QFont()
        font3.setPointSize(15)
        self.labelDate.setFont(font3)
        self.labelDate.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.labelDate)

        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(10, 380, 519, 26))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.progressBar = QProgressBar(self.verticalLayoutWidget_3)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(10, 380, 517, 24))
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)
        #self.progressBar.setValue(24)
        self.progressBar.setStyleSheet(
                "background-color: rgb(120, 45, 45)"
        )
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"QtPy Timer", None))
        self.spinBoxHours.setSuffix(QCoreApplication.translate("MainWindow", u"  hours", None))
        self.spinBoxMinutes.setSuffix(QCoreApplication.translate("MainWindow", u"  minutes", None))
        self.spinBoxSeconds.setSuffix(QCoreApplication.translate("MainWindow", u"  seconds", None))
        self.toolButtonStartStop.setText(QCoreApplication.translate("MainWindow", u"START".center(7), None))
        self.labelCountDown.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
    # retranslateUi

