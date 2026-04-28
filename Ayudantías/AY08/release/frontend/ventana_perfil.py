from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (
    QGridLayout,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QWidget,
)

# TODO Parte 3: ¿Cómo es el acoplamiento y cohesividad según este import?
from backend.backend import obtener_path_icon, obtener_biografia, obtener_stories


class VentanaPerfil(QWidget):

    # Señal para volver a la ventana de los perfiles
    senal_volver_perfiles = pyqtSignal()
    senal_ver_historias = pyqtSignal(str)
    senal_abrir_perfil = pyqtSignal(str)

    def __init__(self, usuario) -> None:
        super().__init__()
        self.usuario = usuario

        # Se inicializan:
        self.path_icon: str = obtener_path_icon(
            usuario)  # el path del icono del perfil
        # el texto de la biografia del perfil
        self.biografia: str = obtener_biografia(usuario)
        self.historias: list[str] = obtener_stories(
            usuario)  # los paths de las historias del perfil

        # Establecer el titulo y geometría de la ventana
        self.setWindowTitle(f"Usuario {self.usuario}")
        self.setGeometry(600, 180, 320, 200)
        self.inicializar_gui()

    def inicializar_gui(self) -> None:
        ''' Inicializa los elementos graficos de la ventana '''
        # TODO Parte 2:
        #      - Crear los widgets que muestren el nombre de usuario y biografía
        #      - Crear un layout para distribuir los widgets

        # Botón para levantar la señal y volver a la ventana de los perfiles
        self.boton_volver = QPushButton("Volver a perfiles")
        self.boton_volver.clicked.connect(self.senal_volver_perfiles.emit)

        self.boton_historias = QPushButton("Ver historias")
        self.boton_historias.clicked.connect(
            lambda _, u=self.usuario: self.senal_ver_historias.emit(u))

        # TODO Parte 2: eliminar este layout y crear uno adecuado para
        #               distribuir los widgets

        layout = QVBoxLayout()
        layout.addWidget(self.boton_volver)
        layout.addWidget(self.boton_historias)
        self.setLayout(layout)

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
