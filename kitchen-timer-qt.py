'''
Yet another Kitchen Timer prog, this time using PySide2,
the python/Qt bindings module and Designer-qt5
'''
# Import PySide2 classes
import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from QtPyTimer import Ui_MainWindow, QTimer
import subprocess

CMD = ["/usr/bin/aplay", "-q", "chime.wav"]

class MainWindow(QMainWindow, Ui_MainWindow, QTimer):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #self.show()
        self.h = 0
        self.m = 0
        self.s = 0
        self.CountDownText = " "
        self.toolButtonStartStop.setCheckable(True)
        self.toolButtonStartStop.clicked.connect(self.start_stop)
        self.count_down_timer = QTimer(self)
        self.count_down_timer.timeout.connect(self.update_timer)


    def update_countdown_label(self):
        self.CountDownText = f"{self.h:0>2}:{self.m:0>2}:{self.s:0>2}"
        self.labelCountDown.setText(self.CountDownText)
    

    def start_stop(self):
        b = self.toolButtonStartStop.isChecked()
        if b is True:
            self.h = self.spinBoxHours.value()
            self.m = self.spinBoxMinutes.value()
            self.s = self.spinBoxSeconds.value()
            self.update_countdown_label()
            self.count_down_timer.start(1000)
        else:
            self.h = self.m = self.s = 0
            self.update_countdown_label()
            self.count_down_timer.stop()


    def update_timer(self):
        self.update_countdown_label()
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
            self.update_countdown_label()
            self.start_stop()
            # ALERT GOES HERE
            subprocess.run(CMD, shell=False)

# class MainWindow

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("QtPyTimer")

    window = MainWindow()
    window.show()

    app.exec_()

if __name__ == "__main__":
    main()
