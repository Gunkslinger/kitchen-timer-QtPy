'''
Yet another Kitchen Timer prog, this time using PySlide2,
the python/Qt bindings module and Designer-qt5
'''
# Import PySide2 classes
import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from QtPyTimer import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow): #Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.spinBoxHours.valueChanged.connect(self.spinH)
        self.spinBoxMinutes.valueChanged.connect(self.spinM)
        self.spinBoxSeconds.valueChanged.connect(self.spinS)
        self.toolButtonStartStop.setCheckable(True)
        self.toolButtonStartStop.clicked.connect(lambda: self.pressedit(0))

    def spinH(self):
        print("Hours spun! ", self.spinBoxHours.value())

    def spinM(self):
        print("Minutes spun! ", self.spinBoxMinutes.value())

    def spinS(self):
        print("Seconds spun! ", self.spinBoxSeconds.value())

    def pressedit(self, n):
        print("Start/Stop PRESSED: ", self.toolButtonStartStop.isChecked())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("QtPyTimer")

    window = MainWindow()
    app.exec_()