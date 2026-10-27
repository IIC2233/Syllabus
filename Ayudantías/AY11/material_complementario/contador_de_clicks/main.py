from PyQt6.QtWidgets import QApplication

import sys
import frontend
import backend


def hook(type_, value, traceback) -> None:
    sys.__excepthook__(type_, value, traceback)

sys.excepthook = hook

app = QApplication([])

window = frontend.VentanaPrincipal()
clicker = backend.Clicker()

window.senal_boton.connect(clicker.click)
clicker.senal_aumentar.connect(window.actualizar)

window.show()

sys.exit(app.exec())