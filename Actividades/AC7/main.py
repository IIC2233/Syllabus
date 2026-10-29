import sys
from PyQt6.QtWidgets import QApplication


if __name__ == '__main__':
    def hook(type_, value, traceback) -> None:
        # Imprimimos el error con el hook original de Python. Al instalar
        # nuestro propio sys.excepthook, PyQt no cierra el programa
        sys.__excepthook__(type_, value, traceback)

    sys.excepthook = hook

    app = QApplication([])
    
    sys.exit(app.exec())
