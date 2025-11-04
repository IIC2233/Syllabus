from PyQt5.QtWidgets import QApplication
from backend.cliente import Cliente
from frontend.ventanas import VentanaInicio, VentanaJuego, VentanaFinal
import sys

def hook(type_, value, traceback):
    print(type_)
    print(traceback)

sys.__excepthook__ = hook

app = QApplication(sys.argv)

cliente = Cliente("localhost", 8080)
ventana_inicio = VentanaInicio()
ventana_juego = VentanaJuego()
ventana_final = VentanaFinal()

cliente.senal_inicio.connect(ventana_inicio.hide)
cliente.senal_inicio.connect(ventana_juego.show)

cliente.senal_jugador.connect(ventana_juego.modificar_jugador)
cliente.senal_actualizar_tablero.connect(ventana_juego.modificar_casilla)
cliente.senal_turno.connect(ventana_juego.modificar_turno)
cliente.senal_fin.connect(ventana_final.mostrar)
ventana_juego.senal_click_label.connect(cliente.jugar)

ventana_inicio.show()
cliente.setup_listo()

sys.exit(app.exec())