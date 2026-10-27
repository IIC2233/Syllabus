import sys
from PyQt6.QtWidgets import (
    QWidget, QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, 
    QHBoxLayout, QGridLayout)

from PyQt6.QtCore import pyqtSignal


class VentanaPrincipal(QWidget):
    senal_boton = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.inicializar()

    def inicializar(self):
        self.setGeometry(500, 300, 500, 500)
        self.label = QLabel("Clicker App")
        self.btn = QPushButton("Click")
        self.cnt = QLabel("0")

        self.v = QVBoxLayout()
        self.v.addWidget(self.label)
        self.v.addWidget(self.cnt)
        self.v.addWidget(self.btn)
        self.btn.clicked.connect(self.senal_boton.emit)
        self.setLayout(self.v)

    def actualizar(self, valor):
        self.cnt.setText(str(valor))