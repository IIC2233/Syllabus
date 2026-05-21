from PyQt6.QtCore import QObject, pyqtSignal


class Verificador(QObject):
    senal_respuesta_verificacion = pyqtSignal(bool, str)

    def __init__(self) -> None:
        super().__init__()
        self.contrasena_correcta = "amo iic2233"

    def verificar_contrasena(self, contrasena: str) -> None:
        if contrasena == self.contrasena_correcta:
            self.senal_respuesta_verificacion.emit(True, "Contraseña correcta")
        else:
            self.senal_respuesta_verificacion.emit(False, "Contraseña incorrecta")