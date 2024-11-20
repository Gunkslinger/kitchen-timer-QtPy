from PySide6.QtCore import QRect, Qt
from PySide6.QtWidgets import (QWidget, QListWidget, QLineEdit, QPushButton,
                                QHBoxLayout, QVBoxLayout, QSpinBox)

class Presets(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(240, 120)
        self.setWindowTitle("Presets")
        self.setLayout(QVBoxLayout())
        self.listWidget = QListWidget(self)
        self.layout().addWidget(self.listWidget)
        self.newbutton = QPushButton("New")
        self.newbutton.clicked.connect(self.newPresetButton)
        self.editbutton = QPushButton("Edit")
        #if self.listWidget.currentItem() is not None:
        self.editbutton.setEnabled(False)
        self.removebutton = QPushButton("Remove")
        self.butgrp = QHBoxLayout()
        self.butgrp.addWidget(self.newbutton)
        self.butgrp.addWidget(self.editbutton)
        self.butgrp.addWidget(self.removebutton)
        self.layout().addLayout(self.butgrp)
        self.cur_hours = 0
        self.cur_minutes = 0
        self.cur_seconds = 0

    def newPresetButton(self):
        self.newDia = QWidget()
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
        self.OkButton = QPushButton("Ok")
        self.cancelOkLayout.addWidget(self.cancelButton)
        self.cancelOkLayout.addWidget(self.OkButton)
        
        # All of the buttons above need funcs to be connected to
        self.newPresetMainLayout.addLayout(self.cancelOkLayout)
        self.newDia.show()


