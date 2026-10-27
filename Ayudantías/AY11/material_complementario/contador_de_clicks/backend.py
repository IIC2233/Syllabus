from PyQt6.QtWidgets import (
    QWidget, QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, 
    QHBoxLayout, QGridLayout)

from PyQt6.QtCore import pyqtSignal, QObject

class Clicker(QObject):
    senal_aumentar = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.numero = 0

    def click(self):
        self.numero += 1
        print(self.numero)
        self.senal_aumentar.emit(self.numero)