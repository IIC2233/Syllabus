import sys
from PyQt6.QtWidgets import (
    QWidget, QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, 
    QHBoxLayout, QGridLayout)

from PyQt6.QtCore import pyqtSignal

class VentanaLogIn(QWidget):
    signal_info_login = pyqtSignal(str, str)
    signal_abrir_calc = pyqtSignal()

    def __init__(self):
        super().__init__() # hereda las caracteristicas de la ventana
        self.inicializar_gui()

    def inicializar_gui(self):
        self.setGeometry(500, 200, 500, 500) # jueguen!!
        self.setWindowTitle("LogIn: pagina muy bacan que aprendi en IIC2233")

        self.mensaje = QLabel("Bienvenido a la ayudantia 11 de IIC2233", self)
        self.input_nombre = QLineEdit("Ingresa tu nombre")
        self.input_contrasena = QLineEdit("Ingresa tu contraseña")
        self.boton_continuar = QPushButton('&Continuar', self)
        self.boton_continuar.resize(self.boton_continuar.sizeHint())
        self.boton_continuar.clicked.connect(self.enviar_login)
        self.inicializar_layout()

    def inicializar_layout(self):
        vertical = QVBoxLayout()
        vertical.addStretch(1)
        vertical.addWidget(self.mensaje)
        vertical.addWidget(self.input_nombre)
        vertical.addWidget(self.input_contrasena)
        vertical.addWidget(self.boton_continuar)
        vertical.addStretch(1)

        horizontal = QHBoxLayout()
        horizontal.addStretch(1)
        horizontal.addLayout(vertical)
        horizontal.addStretch(1)

        self.setLayout(horizontal)

    def enviar_login(self):
        nombre = self.input_nombre.text()
        contrasena = self.input_contrasena.text()
        self.signal_info_login.emit(nombre, contrasena)

    def recibir_resultado_login(self, exito, mensaje):
        if not exito:
            self.mensaje.setText(mensaje)
            return
        self.mensaje.setText(mensaje)
        self.hide()
        self.signal_abrir_calc.emit()


class VentanaCalculadora(QWidget):
    
    signal_boton = pyqtSignal(str)
    signal_volver_login = pyqtSignal()
    signal_borrar = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.operacion_actual = ""
        self.inicializar_gui()

    def inicializar_gui(self):
        self.setGeometry(500, 200, 500, 500)
        self.setWindowTitle("Calculadora que calcula cosas geniales en IIC2233")

        self.operaciones = QLabel('', self)
        self.volver = QPushButton('Volver', self)
        self.borrar = QPushButton('Borrar', self)
        self.volver.clicked.connect(self.cerrar_sesion)
        self.borrar.clicked.connect(self.eliminar)

        elementos = [
            '7', '8', '9', '*',
            '4', '5', '6', '/',
            '1', '2', '3', '+',
            '0', '.', '=', '-',
        ]

        grilla = QGridLayout()
        for indice, elemento in enumerate(elementos):
            boton = QPushButton(elemento, self)
            boton.clicked.connect(
                lambda _, texto=elemento:
                self.signal_boton.emit(texto)
            )

            fila = indice // 4
            columna = indice % 4
            grilla.addWidget(boton, fila, columna)

        horizontal = QHBoxLayout()
        horizontal.addWidget(self.volver)
        horizontal.addWidget(self.borrar)
        horizontal.addStretch(5)
        vertical = QVBoxLayout()
        vertical.addLayout(horizontal)
        vertical.addWidget(self.operaciones)
        vertical.addLayout(grilla)
        self.setLayout(vertical)

    def eliminar(self):
        self.signal_borrar.emit()

    def actualizar_pantalla(self, texto):
        self.operaciones.setText(texto)

    def cerrar_sesion(self):
        self.hide()
        self.signal_volver_login.emit()