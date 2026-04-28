from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class VentanaHistoria(QWidget):

    senal_anterior_historia = pyqtSignal(str)
    senal_siguiente_historia = pyqtSignal(str)
    senal_salir_historia = pyqtSignal(str)

    def __init__(self, usuario: str, path: str):
        super().__init__()
        self.usuario = usuario
        self.path = path

        # Nombre y geometria de la ventana
        self.setWindowTitle(f'Historias de {usuario}')
        self.setGeometry(600, 180, 320, 200)
        self.inicializar_gui()

    def inicializar_gui(self):
        ''' Inicializa los elementos graficos de la ventana '''
        # TODO Parte 2: 
        #      - Crear el widget que muestre la foto de la historia
        #      - Crear botones para desplazarse entre las historias posteadas
        #      - Crear un layout para distribuir los widgets

        self.boton_salir = QPushButton("Salir", self)
        self.boton_salir.clicked.connect(lambda _, u=self.usuario:
                                         self.senal_salir_historia.emit(u))

        # TODO Parte 2: eliminar este layout y crear uno adecuado para 
        #               distribuir los widgets
        layout = QVBoxLayout()
        layout.addWidget(self.boton_salir)

    def inicializar_foto(self):
        self.widget_foto = QLabel("")
        self.widget_foto.setFixedSize(600, 450)
        self.widget_foto.setAlignment(Qt.AlignmentFlag.AlignCenter)

        pixmap = QPixmap(self.path)
        self.widget_foto.setText("")
        self.widget_foto.setPixmap(
            pixmap.scaled(
                600,
                450,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
        )
