#! /bin/python
'''
Yet another Kitchen Timer prog, this time using PySide2,
the python/Qt bindings module and Designer-qt5

NEW: Configuration file .QtTimer must go in $HOME

    player: audio player binary
    opts: options for player if needed
    file: audio files used for the chime sound
'''
# Import PySide2 classes
import sys
import os
from PySide2.QtWidgets import QApplication, QMainWindow
from QtPyTimer import Ui_MainWindow, QTimer
import subprocess
from chime import play_chime

#HOME = os.getenv("HOME")
#chime = config_from_json(HOME + "/.QtTimer", read_from_file=True)
#CMD = [chime.player, chime.opts, HOME + chime.file]


class MainWindow(QMainWindow, Ui_MainWindow, QTimer):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.h = 0
        self.m = 0
        self.s = 0
        self.CountDownText: str
        self.toolButtonStartStop.setCheckable(True)
        self.toolButtonStartStop.clicked.connect(self.start_stop)
        self.count_down_timer = QTimer(self)
        self.count_down_timer.timeout.connect(self.update_timer)


    def update_countdown_label(self):
        self.CountDownText = f"{self.h:0>2}:{self.m:0>2}:{self.s:0>2}"
        self.labelCountDown.setText(self.CountDownText)
        self.labelCountDown.repaint()

    def start_stop(self):
        b = self.toolButtonStartStop.isChecked()
        if b is True:
            self.h = self.spinBoxHours.value()
            self.m = self.spinBoxMinutes.value()
            self.s = self.spinBoxSeconds.value()
            self.update_countdown_label()
            self.toolButtonStartStop.setText("STOP".center(6))
            self.count_down_timer.start(1000)
        else:
            self.h = self.m = self.s = 0
            self.update_countdown_label()
            self.toolButtonStartStop.setText("START".center(7))
            self.count_down_timer.stop()


    def update_timer(self):
        if self.s > 0:
            self.s -= 1
            self.update_countdown_label()

        elif self.m > 0:
            self.m -= 1
            self.s = 59
            self.update_countdown_label()

        elif self.h > 0:
            self.h -= 1
            self.m = 59
            self.s = 59
            self.update_countdown_label()

        if self.h + self.m + self.s == 0:  # It's the fiiinal countdownnnn!!
            self.toolButtonStartStop.setChecked(False)
            self.start_stop()
            # ALERT GOES HERE
            play_chime()

            #c = subprocess.run(CMD, shell=False)
            #if c.returncode != 0:
            #    script = self.get_script_name()
            #    print(f"{script}: Error {c.returncode} in {c.args[0]} subproc ")

    def get_script_name(self):
        if hasattr(sys.modules[__name__], '__file__'):
            return os.path.splitext(os.path.basename(__file__))[0]
        return os.path.basename(sys.argv[0])


# class MainWindow

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("QtPyTimer")

    window = MainWindow()
    window.show()

    app.exec_()

if __name__ == "__main__":
    main()
