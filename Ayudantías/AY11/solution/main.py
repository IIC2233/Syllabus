from PyQt6.QtWidgets import QApplication

import sys
import frontend
import backend


def hook(type_, value, traceback) -> None:
    sys.__excepthook__(type_, value, traceback)

sys.excepthook = hook

app = QApplication([])

login = backend.LogIn()
calculadora = backend.Calculadora()
ventana_login = frontend.VentanaLogIn()
ventana_calc = frontend.VentanaCalculadora()

# Login
ventana_login.signal_info_login.connect(
    login.recibir_login
)

login.login_result_signal.connect(
    ventana_login.recibir_resultado_login
)

# Abrir y cerrar calculadora
ventana_login.signal_abrir_calc.connect(
    ventana_calc.show
)

ventana_calc.signal_volver_login.connect(
    ventana_login.show
)

# Calculadora
ventana_calc.signal_boton.connect(
    calculadora.procesar_boton
)

ventana_calc.signal_borrar.connect(
    calculadora.eliminar
)

calculadora.signal_pantalla.connect(
    ventana_calc.actualizar_pantalla
)

calculadora.signal_resultado.connect(
    ventana_calc.actualizar_pantalla
)

ventana_login.show()
app.exec()