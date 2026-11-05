import sys
from PyQt6.QtWidgets import QApplication

import parametros as p
from backend import Logica
from frontend import VentanaInicio, VentanaJuego


if __name__ == '__main__':
    def hook(type_, value, traceback) -> None:
        # Imprimimos el error con el hook original de Python. Al instalar
        # nuestro propio sys.excepthook, PyQt no cierra el programa
        sys.__excepthook__(type_, value, traceback)

    sys.excepthook = hook

    app = QApplication([])

    logica = Logica(p.HOST, p.PORT)
    ventana_inicio = VentanaInicio()
    ventana_juego = VentanaJuego()

    ventana_inicio.senal_unirse.connect(logica.unirse)

    logica.senal_vi_avisar.connect(ventana_inicio.mostrar_aviso)
    logica.senal_vi_habilitar.connect(ventana_inicio.habilitar)
    logica.senal_vi_cerrar.connect(ventana_inicio.hide)

    logica.senal_vj_empezar.connect(ventana_juego.empezar)
    logica.senal_vj_actualizar_marcador.connect(ventana_juego.actualizar_marcador)
    logica.senal_vj_actualizar_reloj.connect(ventana_juego.actualizar_reloj)
    logica.senal_vj_terminar.connect(ventana_juego.terminar)

    # Completar: conexiones que faltan y cierre de la conexión al salir

    # Solo para el bonus
    ventana_juego.senal_pausa.connect(logica.pedir_pausa)
    ventana_juego.senal_revancha.connect(logica.pedir_revancha)
    logica.senal_vj_pausa.connect(ventana_juego.mostrar_pausa)
    logica.senal_vj_aviso_revancha.connect(ventana_juego.mostrar_aviso_revancha)
    logica.senal_vj_mostrar_revancha.connect(ventana_juego.mostrar_boton_revancha)

    if not logica.conectar_a_servidor():
        sys.exit(1)

    ventana_inicio.show()
    sys.exit(app.exec())
