import os

from PyQt6.QtCore import Qt, QTimer, pyqtSignal
from PyQt6.QtGui import QKeyEvent, QPixmap
from PyQt6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QGridLayout
)

import parametros as p


class VentanaInicio(QWidget):
    senal_unirse = pyqtSignal(str)

    def __init__(self) -> None:
        super().__init__()
        self.inicializar_gui()

    def inicializar_gui(self) -> None:
        self.setGeometry(300, 300, 320, 140)
        self.setWindowTitle('DCCalabazaPong')

        self.line_edit_nombre = QLineEdit('', self)
        self.boton_jugar = QPushButton('&Jugar', self)
        self.boton_jugar.clicked.connect(self.unirse)
        self.label_aviso = QLabel('', self)

        grilla = QGridLayout()
        grilla.addWidget(QLabel('Nombre:'), 0, 0)
        grilla.addWidget(self.line_edit_nombre, 0, 1)
        grilla.addWidget(self.boton_jugar, 1, 0, 1, 2)
        grilla.addWidget(self.label_aviso, 2, 0, 1, 2)
        self.setLayout(grilla)

    def unirse(self) -> None:
        self.senal_unirse.emit(self.line_edit_nombre.text())

    def mostrar_aviso(self, texto: str) -> None:
        self.label_aviso.setText(texto)

    def habilitar(self, activo: bool) -> None:
        self.boton_jugar.setEnabled(activo)
        self.line_edit_nombre.setEnabled(activo)


class VentanaJuego(QWidget):
    senal_tecla = pyqtSignal(int, bool)
    # Solo para el bonus
    senal_pausa = pyqtSignal()
    senal_revancha = pyqtSignal()

    TECLAS = {Qt.Key.Key_W: -1, Qt.Key.Key_S: 1}

    def __init__(self) -> None:
        super().__init__()
        self.inicializar_gui()

    def inicializar_gui(self) -> None:
        alto_barra = 50
        self.setFixedSize(p.ANCHO_CANCHA, p.ALTO_CANCHA + alto_barra)
        self.setWindowTitle('DCCalabazaPong')

        # Barra superior
        self.label_nombre_izquierda = QLabel('', self)
        self.label_nombre_izquierda.setGeometry(15, 10, 200, 30)
        self.label_nombre_derecha = QLabel('', self)
        self.label_nombre_derecha.setGeometry(p.ANCHO_CANCHA - 215, 10, 200, 30)
        self.label_nombre_derecha.setAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
        )

        self.label_marcador = QLabel('0 - 0', self)
        self.label_marcador.setGeometry(p.ANCHO_CANCHA // 2 - 90, 10, 80, 30)
        self.label_marcador.setStyleSheet('font-size: 20px; font-weight: bold;')
        self.label_reloj = QLabel('', self)
        self.label_reloj.setGeometry(p.ANCHO_CANCHA // 2 + 20, 10, 80, 30)
        self.label_reloj.setStyleSheet('font-size: 20px;')

        # Cancha
        self.cancha = QLabel(self)
        self.cancha.setGeometry(0, alto_barra, p.ANCHO_CANCHA, p.ALTO_CANCHA)
        # Sin selector, los hijos de la cancha heredarían este fondo y los labels
        # de texto, aun vacíos, taparían a la pelota y a las paletas
        self.cancha.setObjectName('cancha')
        self.cancha.setStyleSheet('#cancha { background-color: #1e1e2e; }')

        y_inicial = (p.ALTO_CANCHA - p.ALTO_PALETA) // 2
        self.paletas = {}
        for lado, x in (
            ('izquierda', p.MARGEN_PALETA),
            ('derecha', p.ANCHO_CANCHA - p.MARGEN_PALETA - p.ANCHO_PALETA),
        ):
            paleta = QLabel(self.cancha)
            paleta.setGeometry(x, y_inicial, p.ANCHO_PALETA, p.ALTO_PALETA)
            paleta.setStyleSheet('background-color: white;')
            self.paletas[lado] = paleta

        self.pelota = QLabel(self.cancha)
        self.pelota.setGeometry(
            (p.ANCHO_CANCHA - p.TAMAÑO_PELOTA) // 2,
            (p.ALTO_CANCHA - p.TAMAÑO_PELOTA) // 2,
            p.TAMAÑO_PELOTA, p.TAMAÑO_PELOTA
        )
        self.pelota.setPixmap(QPixmap(os.path.join('assets', 'calabaza.png')))
        self.pelota.setScaledContents(True)

        # Texto sobre la cancha, para goles y fin de partida
        self.label_mensaje = QLabel('', self.cancha)
        self.label_mensaje.setGeometry(0, 60, p.ANCHO_CANCHA, 50)
        self.label_mensaje.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_mensaje.setStyleSheet('color: white; font-size: 26px;')

        # Solo para el bonus
        self.label_aviso = QLabel('', self.cancha)
        self.label_aviso.setGeometry(0, 170, p.ANCHO_CANCHA, 50)
        self.label_aviso.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_aviso.setStyleSheet('color: yellow; font-size: 26px;')

        self.boton_revancha = QPushButton('&Revancha', self.cancha)
        self.boton_revancha.setGeometry(p.ANCHO_CANCHA // 2 - 60, 120, 120, 34)
        self.boton_revancha.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.boton_revancha.clicked.connect(self.pedir_revancha)
        self.boton_revancha.hide()

        self.timer_mensaje = QTimer(self)
        # Completar: configuración de timer_mensaje

    def empezar(self, nombres: list, texto_reloj: str) -> None:
        self.label_nombre_izquierda.setText(nombres[0])
        self.label_nombre_derecha.setText(nombres[1])
        self.label_reloj.setText(texto_reloj)
        self.label_marcador.setText('0 - 0')
        self.timer_mensaje.stop()
        self.label_mensaje.clear()
        self.label_aviso.clear()
        self.boton_revancha.hide()
        self.boton_revancha.setEnabled(True)
        self.show()
        self.activateWindow()

    def actualizar_estado(self, x: int, y: int, izquierda: int, derecha: int) -> None:
        self.pelota.move(x, y)
        self.paletas['izquierda'].move(self.paletas['izquierda'].x(), izquierda)
        self.paletas['derecha'].move(self.paletas['derecha'].x(), derecha)

    def actualizar_marcador(self, goles_izquierda: int, goles_derecha: int) -> None:
        self.label_marcador.setText(f'{goles_izquierda} - {goles_derecha}')

    def actualizar_reloj(self, texto: str) -> None:
        self.label_reloj.setText(texto)

    def mostrar_mensaje_temporal(self, texto: str) -> None:
        # Completar: muestra un aviso temporal
        pass

    def terminar(self, texto: str) -> None:
        # Completar: muestra el mensaje final, que queda fijo en pantalla
        self.label_aviso.clear()
        self.boton_revancha.hide()

    def mostrar_pausa(self, activa: bool, nombre: str) -> None:
        # Solo para el bonus
        self.label_aviso.setText(f'Pausa de {nombre}' if activa else '')

    def mostrar_aviso_revancha(self, nombre: str) -> None:
        # Solo para el bonus
        self.label_aviso.setText(f'{nombre} quiere revancha')

    def mostrar_boton_revancha(self) -> None:
        # Solo para el bonus. terminar oculta este botón: emite la señal que
        # llega aquí después de terminar la partida, y solo con fin
        self.boton_revancha.show()

    def pedir_revancha(self) -> None:
        # Solo para el bonus
        self.boton_revancha.setEnabled(False)
        self.senal_revancha.emit()

    def keyPressEvent(self) -> None:
        # Completar: informa las teclas de movimiento presionadas
        # Bonus: informa la tecla de pausa
        pass

    def keyReleaseEvent(self, evento: QKeyEvent) -> None:
        if evento.key() in self.TECLAS and not evento.isAutoRepeat():
            self.senal_tecla.emit(self.TECLAS[evento.key()], False)
