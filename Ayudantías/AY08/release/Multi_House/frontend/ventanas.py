from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import pyqtSignal, QUrl
from PyQt5.QtGui import QPixmap, QMouseEvent, QKeyEvent
from os.path import join, exists
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QSlider)


class Inicio(QWidget):

    senal_nueva_contrasena = pyqtSignal(str)
    senal_ir_entrada = pyqtSignal()

    def __init__(self):
        super().__init__()
        # COMPLETAR 
        pass

    def establecer_contrasena(self):
        # COMPLETAR
        pass


class Entrada(QWidget):

    senal_ir_living = pyqtSignal()
    senal_emitir_contrasena = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Entrada de la Casa")
        self.setFixedSize(1000, 1000)

        layout = QVBoxLayout()

        label_instruccion = QLabel(
            "Haz clic en la puerta para poder ingresar la contraseña.")
        label_instruccion.setStyleSheet("font-size: 28px;")
        layout.addWidget(label_instruccion)

        # Imagen
        ruta_imagen = join("recursos", "entrada.jpg")
        if exists(ruta_imagen):
            label_img = QLabel()
            label_img.setPixmap(QPixmap(ruta_imagen))
            # Escala la imagen manteniendo la proporción
            label_img.setScaledContents(True)
            layout.addWidget(label_img)

        self.label_contrasena = QLabel(
            "Ingresa la contraseña para entrar a tu hogar, luego ENTER:")
        self.label_contrasena.setStyleSheet("font-size: 28px;")
        self.label_contrasena.hide()
        layout.addWidget(self.label_contrasena)

        self.input_contrasena = QLineEdit('', self)
        self.input_contrasena.setStyleSheet("font-size: 26px;")
        self.input_contrasena.hide()
        layout.addWidget(self.input_contrasena)

        self.setLayout(layout)

    def ir_living(self):
        self.hide()
        self.senal_ir_living.emit()

    def abrir_ventana(self):
        self.show()

    def mousePressEvent(self, event: QMouseEvent) -> None:
        # COMPLETAR
        pass

    def keyPressEvent(self, event: QKeyEvent) -> None:
        # COMPLETAR
        pass

    def recibir_verificacion(self, puede_entrar: bool):
        if puede_entrar:
            self.ir_living()
        else:
            self.label_contrasena.setText(
                "Contraseña incorrecta. Intenta de nuevo.")
        self.input_contrasena.clear()


class Living(QWidget):

    senal_volver_entrada = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Living")
        self.setGeometry(200, 100, 1000, 1000)

        layout = QVBoxLayout()

        boton_entrada = QPushButton("Volver a la Entrada")
        boton_entrada.setStyleSheet("font-size: 26px;")
        boton_entrada.clicked.connect(self.volver_entrada)
        layout.addWidget(boton_entrada)

        ruta_imagen = join("recursos", "living.jpg")
        if exists(ruta_imagen):
            self.label_img = QLabel()
            self.label_img.setPixmap(QPixmap(ruta_imagen))
            # Escala la imagen manteniendo la proporción
            self.label_img.setScaledContents(True)
            layout.addWidget(self.label_img)

        self.media_player_mp3 = QMediaPlayer(self)
        self.media_player_mp3.setMedia(QMediaContent(
            QUrl.fromLocalFile(join("recursos", "fiesta.mp3"))))
        self.media_player_mp3.setVolume(50)

        self.boton_play = QPushButton("Play")
        self.boton_play.clicked.connect(self.media_player_mp3.play)
        layout.addWidget(self.boton_play)

        self.boton_pause = QPushButton("Pause")
        self.boton_pause.clicked.connect(self.media_player_mp3.pause)
        layout.addWidget(self.boton_pause)

        self.boton_stop = QPushButton("Stop")
        self.boton_stop.clicked.connect(self.media_player_mp3.stop)
        layout.addWidget(self.boton_stop)

        self.slider_volumen = QSlider()
        self.slider_volumen.setOrientation(1)  # Horizontal
        self.slider_volumen.setRange(0, 100)
        self.slider_volumen.setValue(50)
        self.slider_volumen.valueChanged.connect(self.media_player_mp3.setVolume)
        layout.addWidget(self.slider_volumen)

        self.setLayout(layout)

    def volver_entrada(self):
        self.hide()
        self.senal_volver_entrada.emit()

    def abrir_ventana(self):
        self.show()
