#!/usr/bin/env python

"""
Yet another Kitchen Timer prog, this time using PySide2,
the python/Qt bindings module and Designer-qt5
"""
# This file is in the public domain -- author Gunkslinger@github.com 2024

import sys
import datetime as dt
import threading
from pathlib import Path
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QStyle, QListWidget, QListWidgetItem
from QtPyTimerUI2 import Ui_MainWindow, FinishDialog
from kitchen_timer_config import KitchenTimerConfig
from chime import play_chime
from presets import Presets

class MainWindow(QMainWindow, Ui_MainWindow, QTimer):
    ''' MainWindow class '''

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.h = self.m = self.s = 0

        self.presetsToolButton.clicked.connect(self.openPresets)
        self.presetslistWidget = Presets(self)
        self.presetslistWidget.hide()
        self.presetName = ""
        self.toolButtonStartStop.setCheckable(True)
        self.toolButtonStartStop.clicked.connect(self.start_stop)

        self.count_down_timer = QTimer(self)
        self.count_down_timer.timeout.connect(self.update_timer)

        self.spinBoxHours.clearFocus()
        self.spinBoxMinutes.clearFocus()
        self.spinBoxSeconds.clearFocus()

        self.count_down_text: str
        self.appname: str
        self.now = dt.datetime.today()
        self.labelDate.setText("Finish time: " + self.now.strftime("%b %d, %Y %I:%M:%S %p"))


    def openPresets(self):
        self.presetslistWidget.show()

    def set_app_name(self, name: str):
        '''Set app name'''
        self.appname = name
        self.setWindowTitle(self.appname)

    def update_countdown_label(self):
        ''' Update countdown label '''
        self.count_down_text = f"{self.h:0>2}:{self.m:0>2}:{self.s:0>2}"
        self.labelCountDown.setText(self.count_down_text)
        self.setWindowTitle(self.count_down_text)
        self.labelCountDown.repaint()

    def set_finish_label(self):
        ''' Put finish label text together and display it '''
        self.now = dt.datetime.today()
        self.delt = dt.timedelta(hours=self.spinBoxHours.value(), minutes=self.spinBoxMinutes.value(),seconds=self.spinBoxSeconds.value())
        self.finish_time = self.now + self.delt
        if len(self.presetName):
            presetFinish = f"{self.presetName} finish time: "
        else:
            presetFinish = "Finish time: "
        self.labelDate.setText(presetFinish + self.finish_time.strftime("%b %d, %Y %I:%M:%S %p"))

    def start_stop(self):
        ''' Toggle start/stop button slot '''
        b = self.toolButtonStartStop.isChecked()
        if b is True:
            self.h = self.spinBoxHours.value()
            self.m = self.spinBoxMinutes.value()
            self.s = self.spinBoxSeconds.value()
            self.update_countdown_label()
            self.toolButtonStartStop.setText("STOP".center(6))
            self.toolButtonStartStop.setStyleSheet(
                "background-color: rgb(120, 45, 45)"  # red stop button
            )
            self.set_finish_label()
            self.count_down_timer.start(1000)
        else:
            self.h = self.m = self.s = 0
            self.update_countdown_label()
            self.toolButtonStartStop.setText("START".center(7))
            self.toolButtonStartStop.setStyleSheet(  # plain start button
                "background-color: "
            )  # blank resets to default color
            self.setWindowTitle(self.appname)
            self.count_down_timer.stop()

    def update_timer(self):
        ''' update timer slot '''
        if self.s > 0:
            self.s -= 1

        elif self.m > 0:
            self.m -= 1
            self.s = 59

        elif self.h > 0:
            self.h -= 1
            self.m = 59
            self.s = 59
            
        self.update_countdown_label()

        if self.h + self.m + self.s == 0:  # It's the fiiinal countdownnnn!!
            self.toolButtonStartStop.setChecked(False)
            self.start_stop()
            thread = threading.Thread(target=play_chime)
            thread.start()
            d = FinishDialog(self.presetName)
            d.exec()

# class MainWindow


def main():
    ''' entry '''
    app = QApplication(sys.argv)
    app.setApplicationName("QtPyTimer")
    kconf = KitchenTimerConfig()
    kqss = kconf.get_timer_qss()
    app.setStyleSheet(Path(kqss).read_text())
    window = MainWindow()
    window.set_app_name(app.applicationName())
    window.show()

    app.exec()


if __name__ == "__main__":
    main()
