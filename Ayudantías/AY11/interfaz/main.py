import sys 

from PyQt6.QtWidgets import QApplication

from backend import Verificador
from frontend import VentanaLogin, VentanaImagen


if __name__ == "__main__":

    def hook(type, value, traceback) -> None:
        print(type)
        print(traceback)

    sys.__excepthook__ = hook

    app = QApplication([])

    backend = Verificador()
    ventana_login = VentanaLogin()
    ventana_imagen = VentanaImagen()

    ventana_login.senal_verificar_contrasena.connect(
        backend.verificar_contrasena
    )

    backend.senal_respuesta_verificacion.connect(
        ventana_login.recibir_resultado_verificacion
    )

    ventana_login.senal_abrir_ventana_imagen.connect(
        ventana_imagen.show
    )

    ventana_login.show()

    sys.exit(app.exec())