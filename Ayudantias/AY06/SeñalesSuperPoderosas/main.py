# main.py
from backend import main
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    app = QApplication([])

    backend = main.Backend()
    backend.conectar()

    sys.exit(app.exec())
