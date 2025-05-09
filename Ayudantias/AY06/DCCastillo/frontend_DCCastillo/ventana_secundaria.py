import sys
import os
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QPushButton, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal


class Secundaria(QWidget):
    
    senal_abrir_castillo = pyqtSignal()
    senal_dormir = pyqtSignal(str)
    
    def __init__(self,tipo,hora):
        
        super().__init__()
        self.tipo = tipo
        self.hora = hora
        if self.tipo == "Dormitorio":
            self.setWindowTitle("¡ Dormitorio !")
            # https://co.pinterest.com/pin/427279083400366800/ 
            imagen_ruta = os.path.join("imagenes_DCCastillo", "dormitorio_DCCastillo.jpg")
        elif self.tipo == "Baño":
            self.setWindowTitle("¡ Baño !")
            # https://www.freepik.es/fotos-premium/bano-inspirado-castillo-medieval_50628276.htm 
            imagen_ruta = os.path.join("imagenes_DCCastillo", "bano_DCCastillo.jpg")
        self.setGeometry(0, 0, 500, 500)    
        layout_vertical = QVBoxLayout()
        imagen = QPixmap(os.path.join(imagen_ruta))
        label_imagen = QLabel()
        label_imagen.setPixmap(imagen)
        boton_ir_castillo = QPushButton("Volver al Castillo", self)
        boton_ir_castillo.clicked.connect(self.volver)
        layout_vertical.addWidget(label_imagen)
        layout_vertical.addWidget(boton_ir_castillo)
        if self.tipo == "Dormitorio":
            boton_dormir = QPushButton("Dormir", self)
            boton_dormir.clicked.connect(self.dormir)
            layout_vertical.addWidget(boton_dormir)
        self.setLayout(layout_vertical)
        
    def volver(self):
        
        self.senal_abrir_castillo.emit()
        self.hide()
            
        
    def abrir_ventana(self,string):
        
        if string == self.tipo:
            self.show()
            
    def dormir(self):
        
        self.senal_dormir.emit(self.hora)
        
    def fue_dormir(self):
        
        self.close()