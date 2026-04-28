from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import (
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class VentanaInicio(QWidget):

    # Señal para enviar un str con la clave ingresada
    senal_enviar_clave = pyqtSignal(str)

    def __init__(self, titulo: str) -> None:
        super().__init__()
        self.setWindowTitle(titulo)
        self.setGeometry(550, 220, 360, 180)
        self.inicializar_gui()

    def inicializar_gui(self):
        # Layout vertical
        self.layout_principal = QVBoxLayout()

        # Widget con instrucciones
        self.label_instruccion = QLabel("Ingresa tu clave de acceso")
        self.layout_principal.addWidget(self.label_instruccion)

        # Widget que contiene el texto de la clave
        self.input_clave = QLineEdit()
        self.input_clave.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_clave.returnPressed.connect(self.enviar_clave)
        self.layout_principal.addWidget(self.input_clave)

        # Botón para enviar la clave
        self.boton_ingresar = QPushButton("Ingresar")
        self.boton_ingresar.clicked.connect(self.enviar_clave)
        self.layout_principal.addWidget(self.boton_ingresar)

        # Label que contiene el mensaje actual enviado por el backend
        self.label_estado = QLabel("")
        self.layout_principal.addWidget(self.label_estado)

        self.setLayout(self.layout_principal)

    def enviar_clave(self) -> None:
        """
        Emite una señal con el str de la clave ingresada
        """

        self.senal_enviar_clave.emit(self.input_clave.text())

    def mostrar_mensaje(self, mensaje: str) -> None:
        """
        Actualiza el label con un mensaje
        """
        self.label_estado.setText(mensaje)

    def limpiar_input(self) -> None:
        self.input_clave.clear()

    def limpiar_mensaje(self) -> None:
        self.label_estado.setText("")
