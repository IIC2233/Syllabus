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
        self.setWindowTitle(f'Historias de {usuario}')
        self.setGeometry(600, 180, 320, 200)
        self.inicializar_gui()

    def inicializar_gui(self):
        self.inicializar_foto()
        self.boton_anterior = QPushButton("Anterior")
        self.boton_anterior.clicked.connect(lambda _, u=self.usuario:
                                            self.senal_anterior_historia.emit(u))

        self.boton_siguiente = QPushButton("Siguiente")
        self.boton_siguiente.clicked.connect(lambda _, u=self.usuario:
                                             self.senal_siguiente_historia.emit(u))

        self.boton_salir = QPushButton("Salir")
        self.boton_salir.clicked.connect(lambda _, u=self.usuario:
                                         self.senal_salir_historia.emit(u))

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.boton_anterior)
        h_layout.addWidget(self.boton_salir)
        h_layout.addWidget(self.boton_siguiente)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.widget_foto)

        self.setLayout(v_layout)

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
