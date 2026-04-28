from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

# TODO Parte 3: ¿Cómo es el acoplamiento y cohesividad según este import?
from backend.backend import obtener_path_icon


class VentanaPerfiles(QWidget):

    # Señal que envía el nombre de usuario un perfil
    senal_abrir_perfil = pyqtSignal(str)

    # Senal que envía para indicar que se quiere volver a la ventana de inicio
    senal_volver_inicio = pyqtSignal()

    def __init__(self, perfiles: list[str]) -> None:
        super().__init__()
        self.perfiles = perfiles
        self.setWindowTitle("Perfiles")
        self.setGeometry(500, 140, 650, 420)
        self.inicializar_gui()

    def inicializar_gui(self) -> None:

        # Layout vertical para organizar los Widgets
        layout_principal = QVBoxLayout()

        titulo = QLabel("Selecciona un perfil")
        layout_principal.addWidget(titulo)

        # Grid para posicionar los perfiles
        grid = QGridLayout()
        for indice, usuario in enumerate(self.perfiles):
            fila = indice // 3
            columna = indice % 3
            grid.addWidget(self.crear_tarjeta_perfil(
                usuario), fila, columna)
        layout_principal.addLayout(grid)

        layout_inferior = QHBoxLayout()
        layout_inferior.addStretch()

        # Botón para volver a la ventana de Inicio
        boton_volver = QPushButton("Volver a inicio")
        boton_volver.clicked.connect(self.senal_volver_inicio.emit)

        layout_inferior.addWidget(boton_volver)
        layout_principal.addLayout(layout_inferior)

        self.setLayout(layout_principal)

    def crear_tarjeta_perfil(self, usuario: str) -> QFrame:

        icon_path = obtener_path_icon(usuario)
        tarjeta = QFrame()
        tarjeta.setFrameShape(QFrame.Shape.StyledPanel)
        layout_tarjeta = QVBoxLayout()

        icon = QLabel("")
        icon.setFixedSize(110, 90)

        pixmap = QPixmap(icon_path)
        icon.setText("")
        icon.setPixmap(
            pixmap.scaled(
                110,
                90,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
        )

        layout_tarjeta.addWidget(icon, alignment=Qt.AlignmentFlag.AlignCenter)

        label_usuario = QLabel(usuario)
        layout_tarjeta.addWidget(
            label_usuario, alignment=Qt.AlignmentFlag.AlignCenter)

        boton_abrir = QPushButton("Abrir perfil")
        boton_abrir.clicked.connect(
            lambda _, u=usuario: self.senal_abrir_perfil.emit(u))
        layout_tarjeta.addWidget(boton_abrir)

        tarjeta.setLayout(layout_tarjeta)
        return tarjeta
