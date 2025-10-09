import sys
from PyQt5.QtWidgets import QApplication

from backend.logica import ControladorLogico
from frontend.control_remoto import VentanaControlRemoto
from frontend.pantalla import VentanaPantalla


if __name__ == '__main__':
    def hook(type, value, traceback) -> None:
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])

    # Instanciamos las clases
    controlador_logico = ControladorLogico()
    control_remoto = VentanaControlRemoto()
    pantalla = VentanaPantalla()

    # Conectamos las señales
    # FIXME PARTE 2.3: Algunas señales y la conexión de las mismas presentan
    # errores, ejecuta el programa para identificar qué señales fallan
    # y posteriormente arreglarlas.

    control_remoto.señal_encendido.connect(controlador_logico.prender_apagar)
    control_remoto.senal_volumen.connect(controlador_logico.cambiar_volumen)
    control_remoto.senal_canal.connect(controlador_logico.cambiar_canal)

    controlador_logico.señal_volumen.connect(pantalla.actualizar_volumen)
    controlador_logico.senal_canal.connect(pantalla.actualizar_canal)
    controlador_logico.senal_encendido.connect(pantalla.prender_apagar)

    controlador_logico.senal_empezar.connect(pantalla.show())
    controlador_logico.senal_empezar.connect(control_remoto.show())

    # Empezamos la ejecución del programa
    controlador_logico.empezar()

    sys.exit(app.exec())
