import os
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QProgressBar


class VentanaPantalla(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.inicializa_gui()

    def inicializa_gui(self) -> None:
        '''
        Definimos las dimensiones y posición de la ventana.
        Además se llaman las distintas funciones que se utilizan
        para inicializar la GUI.

        Descomenta cada función a medida que lo consideres necesario.
        '''
        self.posicion = (100, 100)
        self.porte = (640, 360)
        self.setGeometry(*self.posicion, *self.porte)
        self.setWindowTitle('Pantalla')

        self.generar_widgets()
        # self.agregar_estilo()

    def generar_widgets(self) -> None:
        '''
        Genera y posiciona los distintos widgets que serán
        utilizados en la pantalla:
        - Imagen y texto del canal actual.
        - Barra de progreso y texto con el volumen actual.
        '''
        self.imagen = QLabel('', self)
        self.imagen.setGeometry(0, 0, *self.porte)

        self.canal = QLabel('Canal: #0', self)
        self.canal.move(20, 20)

        self.volumen = QLabel('Volumen: 0', self)
        self.volumen.move(20, self.porte[1] - 30)

        self.volumen_barra = QProgressBar(self, textVisible=False)
        self.volumen_barra.resize(100, 15)
        self.volumen_barra.move(120, self.porte[1] - 30)

    def agregar_estilo(self) -> None:
        '''
        Agrega estilo a los distintos componentes de la ventana.
        '''
        # Agregamos un poco de estilo a los labels
        self.canal.setStyleSheet('''
            color: white;
            background: black;
        ''')
        self.volumen.setStyleSheet('''
            color: white;
            background: black;
        ''')

    def actualizar_volumen(self, nuevo_volumen: int) -> None:
        '''
        A partir del número recibido, actualiza la barra de progreso y
        el texto que muestran el volumen.
        
        TODO PARTE 2.2.a: Falta actualizar el texto.
        '''
        # Actualizamos el valor de la barra del volumen.
        self.volumen_barra.setValue(nuevo_volumen)

    def actualizar_canal(self, nuevo_canal: int) -> None:
        '''
        A partir del número recibido, actualiza la imagen y el texto
        que muestran el canal.
        
        TODO PARTE 2.2.b: Completa el método para lograr lo anterior.
        '''
        pass

    def prender_apagar(self, encendido: bool) -> None:
        '''
        Dependiendo de si la tele se prende o apaga,
        muestra o esconde la ventana.
        '''
        if encendido:
            self.show()
        else:
            self.hide()


if __name__ == '__main__':
    def hook(type, value, traceback) -> None:
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])
    ventana = VentanaPantalla()
    ventana.show()

    # PARTE 2.2: Código para probar los métodos actualizar_volumen y
    # actualizar_canal sin depender del backend.
    ventana.actualizar_volumen(10)
    ventana.actualizar_canal(2)

    sys.exit(app.exec())
