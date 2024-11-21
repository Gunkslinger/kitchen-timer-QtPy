from PySide6.QtCore import QRect, Qt
from PySide6.QtWidgets import (QWidget, QListWidget, QLineEdit, QPushButton,
                                QHBoxLayout, QVBoxLayout, QSpinBox)
from kitchen_timer_config import KitchenTimerConfig

class Presets(QWidget):
    def __init__(self, mw):
        super().__init__()
        self.main_win = mw
        self.resize(240, 120)
        self.setWindowTitle("Presets")
        self.setLayout(QVBoxLayout())
        self.listWidget = QListWidget(self)
        self.listWidget.itemDoubleClicked.connect(self.doubleClick)
        self.layout().addWidget(self.listWidget)
        self.newbutton = QPushButton("New")
        self.newbutton.clicked.connect(self.newPresetButton)
        self.editbutton = QPushButton("Edit")
        self.editbutton.clicked.connect(self.editPresetButton)
        self.removebutton = QPushButton("Remove")
        self.removebutton.clicked.connect(self.removePresetButton)
        self.closebutton = QPushButton("Close")
        self.closebutton.clicked.connect(self.closePresetButton)
        self.butgrp = QHBoxLayout()
        self.butgrp.addWidget(self.newbutton)
        self.butgrp.addWidget(self.editbutton)
        self.butgrp.addWidget(self.removebutton)
        self.butgrp.addWidget(self.closebutton)
        self.layout().addLayout(self.butgrp)
        self.cur_hours = 0
        self.cur_minutes = 0
        self.cur_seconds = 0

        self.kconf = KitchenTimerConfig()
        self.presetsPath = self.kconf.get_timer_presets()
        print(self.presetsPath)
        with open(self.presetsPath, 'r') as prefile:
            for line in prefile:
                self.listWidget.addItem(line.rstrip())

    def doubleClick(self):
        self.curItem = self.listWidget.currentItem().text().split()
        self.curTime= self.curItem[len(self.curItem) - 1].split(":")
        self.main_win.spinBoxHours.setValue(int(self.curTime[0]))
        self.main_win.spinBoxMinutes.setValue(int(self.curTime[1]))
        self.main_win.spinBoxSeconds.setValue(int(self.curTime[2]))


    def newPresetButton(self):
        self.newDia = QWidget()
        self.newDia.setWindowTitle("New Preset")
        self.newDia.resize(400, 200)
        self.newPresetMainLayout = QVBoxLayout()
        self.newDia.setLayout(self.newPresetMainLayout)

        self.nameText = QLineEdit("name")

        self.newSpinButLayout = QHBoxLayout()
        self.newPresetMainLayout.addWidget(self.nameText)

        self.spinh = QSpinBox()
        self.spinh.setRange(0, 23)
        self.spinh.setAlignment(Qt.AlignCenter)
        self.spinh.setSuffix(" hours")
        self.spinh.setValue(self.cur_hours)
        self.newSpinButLayout.addWidget(self.spinh)

        self.spinm = QSpinBox()
        self.spinm.setRange(0, 59)
        self.spinm.setAlignment(Qt.AlignCenter)
        self.spinm.setSuffix(" mins")
        self.spinm.setValue(self.cur_minutes)
        self.newSpinButLayout.addWidget(self.spinm)

        self.spins = QSpinBox()
        self.spins.setRange(0, 59)
        self.spins.setAlignment(Qt.AlignCenter)
        self.spins.setSuffix(" secs")
        self.spins.setValue(self.cur_seconds)
        self.newSpinButLayout.addWidget(self.spins)

        self.newPresetMainLayout.addLayout(self.newSpinButLayout)

        self.cancelOkLayout = QHBoxLayout()
        self.cancelButton = QPushButton("Cancel")
        self.cancelButton.clicked.connect(lambda: self.newDia.close())
        
        self.OkButton = QPushButton("Ok")
        self.OkButton.clicked.connect(self.newOkClicked)

        self.cancelOkLayout.addWidget(self.cancelButton)
        self.cancelOkLayout.addWidget(self.OkButton)

        self.newPresetMainLayout.addLayout(self.cancelOkLayout)
        self.newDia.show()

    def newOkClicked(self):
        self.listWidget.addItem(f"{self.nameText.text()} {self.spinh.value()}:{self.spinm.value()}:{self.spins.value()}")
        # Set spinBoxes in main window
        self.main_win.spinBoxHours.setValue(self.spinh.value())
        self.main_win.spinBoxMinutes.setValue(self.spinm.value())
        self.main_win.spinBoxSeconds.setValue(self.spins.value())

        self.newDia.close()

    def editPresetButton(self):
        self.editDia = QWidget()
        self.editDia.setWindowTitle(f"Edit Preset: {self.listWidget.currentItem().text()}")
        self.editDia.resize(500, 200)
        self.editPresetMainLayout = QVBoxLayout()
        self.editDia.setLayout(self.editPresetMainLayout)

        self.curItem = self.listWidget.currentItem().text().split()
        self.curTime= self.curItem[len(self.curItem) - 1].split(":")

        self.editNameText = ""
        for text in self.listWidget.currentItem().text():
            for ch in text:
                if ch.isdigit() is False:
                    if ch == ":": break
                    self.editNameText += ch
                else: break
        self.nameLineEdit = QLineEdit(self.editNameText.rstrip())

        self.editSpinButLayout = QHBoxLayout()
        self.editPresetMainLayout.addWidget(self.nameLineEdit)

        self.spinh = QSpinBox()
        self.spinh.setRange(0, 23)
        self.spinh.setAlignment(Qt.AlignCenter)
        self.spinh.setSuffix(" hours")
        self.spinh.setValue(int(self.curTime[0]))
        self.editSpinButLayout.addWidget(self.spinh)

        self.spinm = QSpinBox()
        self.spinm.setRange(0, 59)
        self.spinm.setAlignment(Qt.AlignCenter)
        self.spinm.setSuffix(" mins")
        self.spinm.setValue(int(self.curTime[1]))
        self.editSpinButLayout.addWidget(self.spinm)

        self.spins = QSpinBox()
        self.spins.setRange(0, 59)
        self.spins.setAlignment(Qt.AlignCenter)
        self.spins.setSuffix(" secs")
        self.spins.setValue(int(self.curTime[2]))
        self.editSpinButLayout.addWidget(self.spins)

        self.editPresetMainLayout.addLayout(self.editSpinButLayout)

        self.cancelOkLayout = QHBoxLayout()
        self.cancelButton = QPushButton("Cancel")
        self.cancelButton.clicked.connect(lambda: self.editDia.close())
        
        self.OkButton = QPushButton("Ok")
        self.OkButton.clicked.connect(self.editOkClicked)

        self.cancelOkLayout.addWidget(self.cancelButton)
        self.cancelOkLayout.addWidget(self.OkButton)

        self.editPresetMainLayout.addLayout(self.cancelOkLayout)
        self.editDia.show()

    def editOkClicked(self):
        self.index = self.listWidget.row(self.listWidget.currentItem())
        self.editItem = self.listWidget.takeItem(self.index)
        self.listWidget.insertItem(self.index, f"{self.nameLineEdit.text()} {self.spinh.value()}:{self.spinm.value()}:{self.spins.value()}")

        print(self.index)
        self.editDia.close()

    def removePresetButton(self):
        selectedItems = self.listWidget.selectedItems()
        for item in selectedItems:
                self.listWidget.takeItem(self.listWidget.row(item))
    
    def closePresetButton(self):
        with open(self.presetsPath, "w") as file:
            file.truncate()
            for i in range(self.listWidget.count()):
                file.write(f"{self.listWidget.item(i).text()}\n")
        self.close()
