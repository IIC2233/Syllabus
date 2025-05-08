from PyQt5.QtCore import QObject, pyqtSignal


# PARTE 2.3.a Para poder hacer que la clase ControladorLogico use señales y
# se conecte con los otros componentes del programa, debe heredar se QObject.
class ControladorLogico(QObject):
    # PARTE 2.3.b La señal_volumen contiene un carácter NO ascii en su definición.
    # Se cambia el nombre del atributo de clase para que no incluya la "ñ".
    senal_volumen = pyqtSignal(int)
    senal_canal = pyqtSignal(int)
    senal_encendido = pyqtSignal(bool)
    senal_empezar = pyqtSignal()

    def __init__(self) -> None:
        super().__init__()
        self._volumen = 20
        self._canal = 1
        self.prendido = True

    @property
    def volumen(self) -> int:
        return self._volumen

    @volumen.setter
    def volumen(self, valor: int) -> None:
        if valor < 0:
            valor = 0
        elif valor > 100:
            valor = 100

        self._volumen = valor

    @property
    def canal(self) -> int:
        return self._canal

    @canal.setter
    def canal(self, valor: int) -> None:
        self._canal = valor % 10

    def cambiar_volumen(self, cambio: str) -> None:
        if not self.prendido:
            print('La tele está apagada, no se puede cambiar el volumen')
            return

        print('Cambiando volumen:', cambio)
        if cambio == '+':
            self.volumen += 10
        elif cambio == '-':
            self.volumen -= 10
        self.actualizar_volumen()

    def cambiar_canal(self, cambio: str) -> None:
        if not self.prendido:
            print('La tele está apagada, no se puede cambiar el canal')
            return

        print('Cambiando canal:', cambio)
        if cambio == '+':
            self.canal += 1
        elif cambio == '-':
            self.canal -= 1
        else:
            self.canal = int(cambio)

        self.actualizar_canal()

    def actualizar_volumen(self) -> None:
        print('Avisando nuevo volumen:', self.volumen)
        self.senal_volumen.emit(self.volumen)

    def actualizar_canal(self) -> None:
        print('Avisando nuevo canal:', self.canal)
        self.senal_canal.emit(self.canal)

    def prender_apagar(self) -> None:
        self.prendido = not self.prendido
        if self.prendido:
            print('Prendiendo tele')
        else:
            print('Apagando tele')
        self.senal_encendido.emit(self.prendido)

    def empezar(self) -> None:
        self.actualizar_canal()
        self.actualizar_volumen()
        self.senal_empezar.emit()
