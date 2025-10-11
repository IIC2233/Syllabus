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

    # Acá el código presenta 4 errores:
    # a) ControladorLogico no es un QObject, por lo que no se pueden
    #    conectar las señales.
    # b) La señal "señal_volumen" del ControladorLogico contiene
    #    un carácter no ascii.
    # c) La señal "senal_empezar" del ControladorLogico se conecta a los
    #    métodos "show" ya ejecutados, por lo que no permite que
    #    se vean las ventanas.
    # d) La señal "senal_volumen" de VentanaControlRemoto está definida para
    #    recibir un int, pero es llamada recibiendo un str.

    control_remoto.senal_encendido.connect(controlador_logico.prender_apagar)
    control_remoto.senal_volumen.connect(controlador_logico.cambiar_volumen)
    control_remoto.senal_canal.connect(controlador_logico.cambiar_canal)

    controlador_logico.senal_volumen.connect(pantalla.actualizar_volumen)
    controlador_logico.senal_canal.connect(pantalla.actualizar_canal)
    controlador_logico.senal_encendido.connect(pantalla.prender_apagar)

    # PARTE 2.3.c: Al conectar la señal con el método show de la VentanaPantalla
    # y la VentanaControlRemoto, debemos asegurarnos de utilizar la referencia al método.
    controlador_logico.senal_empezar.connect(pantalla.show)
    controlador_logico.senal_empezar.connect(control_remoto.show)

    # Empezamos la ejecución del programa
    controlador_logico.empezar()

    sys.exit(app.exec())
