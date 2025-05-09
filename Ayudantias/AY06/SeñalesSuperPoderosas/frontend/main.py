import os
from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QWidget, QLabel, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal

# Ventana principal
class VentanaPrincipal(QWidget):
    senal_label_seleccionado = pyqtSignal(QLabel)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_gui()

    # Función que setea nuestra GUI
    def init_gui(self):
        # Layout principal
        vlayout = QVBoxLayout()

        self.setWindowTitle("Main")
        self.setGeometry(0, 0, 500, 500)

        # número: botón
        self.botones = {}
        # número: imagen
        self.labels = {}

        # Abrimos las 4 imágenes
        for image in range(4):
            # Layout horizontal, tendrá la imagen y su botón
            hlayout = QHBoxLayout()
            ruta = os.path.join("SeñalesSuperPoderosas", "imagenes", f"image_{image}.png")

            # Seteamos la imagen
            label = QLabel()
            imagen = QPixmap(ruta)
            label.setPixmap(imagen)

            # Configuramos el botón
            boton = QPushButton(str(image), self)
            boton.clicked.connect(self.crear_handler(image))

            # Añadimos ambos Widgets al layout horizontal
            hlayout.addWidget(label)
            hlayout.addWidget(boton)

            # Finalmente añadimos este layout al principal
            vlayout.addLayout(hlayout)

            # Seteamos los diccionarios
            self.botones[image] = boton
            self.labels[image] = label

        # Seteamos el layout principal
        self.setLayout(vlayout)

    def mostrar(self):
        self.show()

    # Esta función genera un handler específico para cada botón presionado, 
    # que ejecutará la acción correspondiente dependiendo del número del botón.

    def crear_handler(self, num):
        def handler():
            self.boton_presionado(num)
        return handler

    # Definimos el comportamiento al presionar un botón
    def boton_presionado(self, numero):
        print(f"Botón {numero} presionado.")
        self.senal_label_seleccionado.emit(self.labels[numero])
        self.hide()

# Ventana secundaria
class VentanaSecundario(QWidget):
    senal_mostrar_principal = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_gui()
        
    def init_gui(self):
        self.setGeometry(500, 0, 200, 200)
        self.layout = QVBoxLayout()

        self.nuevo_label = QLabel()
        self.boton = QPushButton("Regresar", self)
        self.boton.clicked.connect(self.regresar)

        self.layout.addWidget(self.nuevo_label)
        self.layout.addWidget(self.boton)
        self.setLayout(self.layout)

    # Podemos cambiar la imagen siempre que queramos usando setPixmap sobre el mismo label
    def mostrar_imagen(self, label):
        self.nuevo_label.setPixmap(label.pixmap())
        self.show()

    # Al clickear el botón, mandamos la señal para que se muestre la ventana principal y se esconda la secundaria
    def regresar(self):
        self.senal_mostrar_principal.emit()
        self.hide()
