# This file is in the public domain -- author Gunkslinger@github.com 2024

import re
from PySide6.QtCore import QRect, Qt
from PySide6.QtWidgets import (QWidget, QListWidget, QLineEdit, QPushButton,
                                QHBoxLayout, QVBoxLayout, QSpinBox)
from kitchen_timer_config import KitchenTimerConfig

class Presets(QWidget):
    def __init__(self, mw):
        super().__init__()
        self.main_win = mw
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
        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.addWidget(self.newbutton)
        self.buttonLayout.addWidget(self.editbutton)
        self.buttonLayout.addWidget(self.removebutton)
        self.buttonLayout.addWidget(self.closebutton)
        self.layout().addLayout(self.buttonLayout)
        self.dirty = False
        self.kconf = KitchenTimerConfig()
        self.presetsPath = self.kconf.get_timer_presets()
        with open(self.presetsPath, 'r') as prefile:
            for line in prefile:
                self.listWidget.addItem(line.rstrip())
        self.resize(240, 40 * self.listWidget.count())
        print (self.listWidget.count())
                
    def getPresetName(self):
        ''' Get the selected preset. Use re to split on 4 spaces and return 1st in list. '''
        return re.split(r"    ", self.listWidget.currentItem().text())[0]

    def doubleClick(self):
        ''' Use the given preset '''
        self.curItem = self.listWidget.currentItem().text().split()
        self.curTime = self.curItem[len(self.curItem) - 1].split(":")
        self.main_win.spinBoxHours.setValue(int(self.curTime[0]))
        self.main_win.spinBoxMinutes.setValue(int(self.curTime[1]))
        self.main_win.spinBoxSeconds.setValue(int(self.curTime[2]))
        self.main_win.presetName = self.getPresetName()
        self.main_win.set_finish_label()

    def newPresetButton(self):
        ''' Create a new preset '''
        self.newDia = QWidget()
        self.newDia.setWindowTitle("New Preset")
        self.newDia.resize(400, 200)
        self.newPresetMainLayout = QVBoxLayout()
        self.newDia.setLayout(self.newPresetMainLayout)

        self.nameText = QLineEdit("name")
        self.nameText.setSelection(0, 4)

        self.newSpinButLayout = QHBoxLayout()
        self.newPresetMainLayout.addWidget(self.nameText)

        self.spinh = QSpinBox()
        self.spinh.setRange(0, 23)
        self.spinh.setAlignment(Qt.AlignCenter)
        self.spinh.setSuffix(" hours")
        self.spinh.setValue(self.main_win.spinBoxHours.value())
        self.newSpinButLayout.addWidget(self.spinh)

        self.spinm = QSpinBox()
        self.spinm.setRange(0, 59)
        self.spinm.setAlignment(Qt.AlignCenter)
        self.spinm.setSuffix(" mins")
        self.spinm.setValue(self.main_win.spinBoxMinutes.value())
        self.newSpinButLayout.addWidget(self.spinm)

        self.spins = QSpinBox()
        self.spins.setRange(0, 59)
        self.spins.setAlignment(Qt.AlignCenter)
        self.spins.setSuffix(" secs")
        self.spins.setValue(self.main_win.spinBoxSeconds.value())
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
        ''' Save the newly created preset '''
        self.dirty = True
        self.listWidget.addItem(f"{self.nameText.text()}    {self.spinh.value()}:{self.spinm.value()}:{self.spins.value()}")
        # Set spinBoxes in main window
        self.main_win.spinBoxHours.setValue(self.spinh.value())
        self.main_win.spinBoxMinutes.setValue(self.spinm.value())
        self.main_win.spinBoxSeconds.setValue(self.spins.value())

        #TODO here? Restart timer if running? Either that or don't change main_win spinbox values (above). Not sure.

        self.newDia.close()

    def editPresetButton(self):
        ''' Edit the currently selected preset '''
        self.editDia = QWidget()
        self.editDia.setWindowTitle(f"Edit Preset: {self.listWidget.currentItem().text()}")
        self.editDia.resize(500, 200)
        self.editPresetMainLayout = QVBoxLayout()
        self.editDia.setLayout(self.editPresetMainLayout)

        self.curItem = self.listWidget.currentItem().text().split()
        self.curTime = self.curItem[len(self.curItem) - 1].split(":")

        self.editNameText = self.getPresetName()
        self.nameLineEdit = QLineEdit(self.getPresetName())

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
        ''' Insert the edited preset back into the list and mark the list be saved '''
        self.dirty = True
        self.index = self.listWidget.row(self.listWidget.currentItem())
        self.editItem = self.listWidget.takeItem(self.index)
        self.listWidget.insertItem(self.index, f"{self.nameLineEdit.text()}    {self.spinh.value()}:{self.spinm.value()}:{self.spins.value()}")

        self.editDia.close()

    def removePresetButton(self):
        ''' The Remove preset button slot '''
        self.dirty = True
        selectedItems = self.listWidget.selectedItems()
        for item in selectedItems:
                self.listWidget.takeItem(self.listWidget.row(item))
        #self.resize(240, 40 * self.listWidget.count())

    
    def closePresetButton(self):
        ''' The Close button slot '''
        if self.dirty == True:
            with open(self.presetsPath, "w") as file:
                print("truncating and writing" + self.presetsPath)
                file.truncate()
                for i in range(self.listWidget.count()):
                    file.write(f"{self.listWidget.item(i).text()}\n")
    
        self.dirty = False
        self.close()
