import sys
from PyQt6.QtWidgets import QApplication

from backend.backend import Logica
from frontend.frontend import Frontend


if __name__ == "__main__":
    def hook(type, value, traceback) -> None:
        print(type)
        print(traceback)

    sys.__excepthook__ = hook

    app = QApplication([])

    backend = Logica()

    perfiles = [
        "TransportesPirataCoyh",
        "YangTipsParaVidaGatuna",
        "VendoChoripan",
        "andresit00___",
        "dvillas28",
        "ChaseTM",
        "mskdancers",
        "Luna",
        "Pepa",
        "Rosadita27"
    ]

    frontend = Frontend(perfiles)

    # TODO Parte 1: Conectar señales frontend -> backend

    # TODO Parte 1: Conectar señales backend -> frontend

    frontend.mostrar()
    sys.exit(app.exec())
