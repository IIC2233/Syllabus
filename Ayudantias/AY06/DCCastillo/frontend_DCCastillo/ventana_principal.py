import sys
import os
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QPushButton, QWidget, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal


class Castillo(QWidget):
    
    abrir_ventana = pyqtSignal(str)
    
    def __init__(self,*args,**kwargs):
        
        super().__init__(*args,**kwargs)
        self.setWindowTitle("¡ Castillo !")
        self.setGeometry(0, 0, 500, 500)
    
        # Crear el contenedor para los botones
        imagen_ruta = os.path.join("imagenes_DCCastillo", "lobby_DCCastillo.jpg")
        label_imagen = QLabel()
        pixeles = QPixmap(imagen_ruta)
        label_imagen.setPixmap(pixeles)
        label_imagen.setScaledContents(True)
        label_imagen.setFixedSize(500,500)
        layout_vertical = QVBoxLayout()
        
        # Creamos los botones
        
        boton_ir_dormitorio = QPushButton("Dormitorio", self)
        boton_ir_baño = QPushButton("Baño", self)
        boton_salir = QPushButton("Salir del Castillo", self)
        
        #Conectamos las señales
        
        boton_ir_dormitorio.clicked.connect(self.metodo_abrir_dormitorio)
        boton_ir_baño.clicked.connect(self.metodo_abrir_bano)
        boton_salir.clicked.connect(self.close)
        
        #Le añadimos un espaciado y añadimos los widgets
        layout_vertical.addStretch(1)
        layout_vertical.addWidget(label_imagen)
        layout_vertical.addWidget(boton_ir_dormitorio)
        layout_vertical.addWidget(boton_ir_baño)
        layout_vertical.addWidget(boton_salir)
        layout_vertical.addStretch(1)

        # Configurar el layout del contenedor
        
        self.setLayout(layout_vertical)
    
    #En el caso que se seleccione dormitorio en la ventana principal se abre 
    
    def metodo_abrir_dormitorio(self):
        self.hide()
        self.abrir_ventana.emit("Dormitorio") # Esta señal se emite a ambas ventanas

    #En el caso que se seleccione baño en la ventana principal se abre 
    def metodo_abrir_bano(self):
        
        self.hide()
        self.abrir_ventana.emit("Baño")
    
    #En el caso que se necesite abrir nuevamente
    def abrir_nuevamente(self):
        
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Castillo()
    ventana.show()
    sys.exit(app.exec())