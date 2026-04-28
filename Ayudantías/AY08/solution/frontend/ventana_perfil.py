from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (
    QGridLayout,
    QLabel,
    QPushButton,
    QWidget,
)

from backend.backend import obtener_path_icon, obtener_biografia, obtener_stories


class VentanaPerfil(QWidget):

    # Señal para volver a la ventana de los perfiles
    senal_volver_perfiles = pyqtSignal()
    senal_ver_historias = pyqtSignal(str)
    senal_abrir_perfil = pyqtSignal(str)

    def __init__(self, usuario) -> None:
        super().__init__()
        self.usuario = usuario
        self.path_icon = obtener_path_icon(usuario)
        self.biografia = obtener_biografia(usuario)
        self.historias = obtener_stories(usuario)

        self.setWindowTitle(f"Usuario {self.usuario}")
        self.setGeometry(600, 180, 320, 200)
        self.inicializar_gui()

    def inicializar_gui(self) -> None:
        # Botón para levantar la señal y volver a la ventana de los perfiles
        self.boton_volver = QPushButton("Volver a perfiles")
        self.boton_volver.clicked.connect(self.senal_volver_perfiles.emit)

        self.boton_historias = QPushButton("Ver historias")
        self.boton_historias.clicked.connect(
            lambda _, u=self.usuario: self.senal_ver_historias.emit(u))

        self.label_usuario = QLabel(self.usuario)
        self.label_biografia = QLabel(self.biografia)
        self.inicializar_icon()

        grid = QGridLayout()
        grid.addWidget(self.boton_volver, 0, 0, 1, 1)
        grid.addWidget(self.widget_icon, 1, 0, 4, 1)
        grid.addWidget(self.boton_historias, 5, 0, 1, 1)
        grid.addWidget(self.label_usuario, 2, 1, 1, 1)
        grid.addWidget(self.label_biografia, 3, 1, 1, 1)

        self.setLayout(grid)

    def inicializar_icon(self) -> None:
        self.widget_icon = QLabel("")
        self.widget_icon.setFixedSize(110, 90)
        self.widget_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)

        pixmap = QPixmap(self.path_icon)
        self.widget_icon.setText("")
        self.widget_icon.setPixmap(
            pixmap.scaled(
                110,
                90,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
        )
