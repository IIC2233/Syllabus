import sys
from PyQt5.QtWidgets import QApplication
from frontend.ventanas import VentanaInicio, VentanaJuego
from backend.juego import Juego


class ProtegeDCCity:
    def __init__(self, host: str, port: int) -> None:
        """
        Instanciamos todas las ventanas y clases necesarias
        """
        self.frontend_inicio = VentanaInicio()
        self.frontend_juego = VentanaJuego()
        self.backend = Juego(host, port)

    def conectar(self) -> None:
        """
        Conectamos todas las señales entre ventanas y backend

        En este método hay 2 errores 😱.
        TODO: Ronda 1.2 y 2.1
        """
        self.backend.senal_empezar_juego(self.frontend_juego.empezar_juego)

        # Frontend_juego notifica al backend cuando se hace click en pantalla
        self.frontend_juego.senal_click_pantalla.connect(self.backend.click_pantalla)

        # Backend notifica al frontend_juego cuando aparece, se mueve
        # y desaparece el meteorito
        self.backend.senal_aparecer_meteorito.connect(
            self.frontend_juego.aparecer_meteorito
        )
        self.backend.senal_mover_meteorito.connect(self.frontend_juego.mover_meteorito)
        self.backend.senal_remover_meteorito.connect(
            self.frontend_juego.remover_meteorito
        )

        # Backend notifica al frontend_juego cuando se cambia la población
        self.backend.senal_actualizar_poblacion.connect(
            self.frontend_juego.actualizar_poblacion
        )

    def iniciar(self) -> None:
        """
        Definimos qué sucede cuando empieza el juego. En este caso, que
        la ventana de inicio se muestre.

        En este método hay 1 error 😱.
        TODO: Ronda 1.3
        """
        self.frontend_inicio.show


if __name__ == "__main__":

    def hook(type_, value, traceback):
        print(type_)
        print(traceback)

    # sys.__excepthook__ = hook
    PORT = 4444 if len(sys.argv) < 2 else int(sys.argv[1])
    HOST = "localhost" if len(sys.argv) < 3 else sys.argv[2]

    app = QApplication([])
    juego = ProtegeDCCity(HOST, PORT)
    juego.conectar()
    juego.iniciar()

    sys.exit(app.exec())
