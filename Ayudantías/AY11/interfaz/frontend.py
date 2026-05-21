from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
)


class VentanaLogin(QWidget):
    senal_verificar_contrasena = pyqtSignal(str)
    senal_abrir_ventana_imagen = pyqtSignal()

    def __init__(self) -> None:
        super().__init__()
        self.inicializar_gui()

    def inicializar_gui(self) -> None:
        self.setWindowTitle("Login")
        self.setGeometry(700, 300, 350, 180)

        self.label_instruccion = QLabel("Ingresa la contraseña:", self)
        self.label_instruccion.move(30, 20)

        self.input_contrasena = QLineEdit("", self)
        self.input_contrasena.setGeometry(30, 50, 280, 25)

        self.boton_ingresar = QPushButton("Ingresar", self)
        self.boton_ingresar.setGeometry(30, 85, 280, 30)
        self.boton_ingresar.clicked.connect(self.enviar_contrasena)

        self.label_resultado = QLabel("", self)
        self.label_resultado.setGeometry(30, 125, 280, 25)

    def enviar_contrasena(self) -> None:
        contrasena = self.input_contrasena.text()
        self.senal_verificar_contrasena.emit(contrasena)

    def recibir_resultado_verificacion(self, aprobado: bool, mensaje: str) -> None:
        self.label_resultado.setText(mensaje)
        self.label_resultado.resize(self.label_resultado.sizeHint())

        if aprobado:
            self.hide()
            self.senal_abrir_ventana_imagen.emit()


class VentanaImagen(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.inicializar_gui()

    def inicializar_gui(self) -> None:
        self.setWindowTitle("Imagen secreta")
        self.setGeometry(650, 250, 500, 400)

        self.label_imagen = QLabel(self)
        self.label_imagen.setGeometry(25, 25, 450, 300)

        pixmap = QPixmap("pepsi.jpg")
        pixmap = pixmap.scaled(
            450,
            300,
            Qt.AspectRatioMode.KeepAspectRatio
        )
        self.label_imagen.setPixmap(pixmap)