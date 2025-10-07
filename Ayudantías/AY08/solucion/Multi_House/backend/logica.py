from PyQt5.QtCore import QObject, pyqtSignal


class Procesador(QObject):
    senal_puede_entrar = pyqtSignal(bool)

    def __init__(self):
        super().__init__()

    def nueva_contrasena(self, nueva: str):
        self.contrasena = nueva

    def verificar_acceso(self, input: str):
        if input == self.contrasena:
            self.senal_puede_entrar.emit(True)
        else:
            self.senal_puede_entrar.emit(False)
