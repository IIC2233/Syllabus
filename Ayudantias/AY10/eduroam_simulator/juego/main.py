import sys
from PyQt5.QtWidgets import QApplication

from frontent.frontent import MiVentana
from backend.backend import Procesardor

if __name__ == '__main__': 
    def hook(type, value, traceback) -> None:
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])
    ventana = MiVentana() 
    procesador = Procesardor() 

    #Conectamos las señales
    ventana.senal_nombre.connect(procesador.nombre)
    ventana.senal_obtener_clasificador.connect(procesador.obtener_clasificador)
    ventana.senal_publicar_puntaje.connect(procesador.perder)

    procesador.senal_clasificador.connect(ventana.mostrar_clasificador)





    ventana.show()  
    sys.exit(app.exec())