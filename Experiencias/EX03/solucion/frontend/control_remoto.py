import sys
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QHBoxLayout, QVBoxLayout, QGridLayout,
)


class VentanaControlRemoto(QWidget):
    # PARTE 2.3.d La señal_volumen originalmente está definida como una pyqtSignal que recibe
    # un int, pero al momento de llamarla se le pasa un str.
    # Para no cambiar el flujo de llamado y recepción del str, se cambia el tipo de dato recibido
    # por la pyqtSignal.
    senal_volumen = pyqtSignal(str)
    senal_canal = pyqtSignal(str)
    senal_encendido = pyqtSignal()

    def __init__(self) -> None:
        super().__init__()
        self.inicializa_gui()

    def inicializa_gui(self) -> None:
        '''
        Llama las distintas funciones que se utilizan para inicializar la GUI.
        
        Descomenta cada función a medida que lo consideres necesario. 
        '''
        self.generar_botones()
        self.generar_layout()
        self.conectar_botones()
        self.agregar_estilo()

        self.setWindowTitle('Control remoto')
        self.move(800, 100)

    def generar_botones(self) -> None:
        '''
        Genera todos los botones que serán utilizados en el control remoto: 
        - encendido/apagado
        - +/- de volumen y canales 
        - números del 1 al 9 para los canales

        PARTE 1.1: Hay botones que faltan, ya sea por errores o porque no han
        sido creados, corrige el código para que se creen todos los botones.
        '''
        # Botón encendido/apagado
        # FIXME: Arreglar para que aparezca en el control.

        # PARTE 1.1.a: Faltaba agregar el 'self' para que el botón se vea en la ventana.
        self.on_off = QPushButton('On/Off', self)

        # Botones de volumen
        self.volumen = [
            QPushButton('+', self),
            QPushButton('-', self)
        ]

        # Botones de canales
        self.canales = [
            QPushButton('+', self),
            QPushButton('-', self),
        ]

        # Botones numéricos
        # TODO: Completa el listado de números,
        # para tener todos los números del 1 al 9.

        # PARTE 1.1.b: Creamos 9 botones y los agregamos a la lista de números.
        self.numeros = [
            QPushButton(f'{numero}', self) for numero in range(1, 10)
        ]

    def generar_layout(self) -> None:
        '''
        Genera el layout de la ventana y agrega los distintos
        elementos al mismo.

        El layout estará compuesto por un layout vertical que contendrá:
        1. El botón de encendido/apagado
        2. Un layout horizontal con los botones +/- del volumen y los canales.
        3. Una grilla de 3x3 con los botones numéricos.

        PARTE 1.2: Falta agregar los botones +/-.
        Revisa la función "generar_layout_subir_bajar".
        '''
        # Generamos el layout principal
        vbox = QVBoxLayout()

        # Generamos y rellenamos el layout secundario (horizontal)
        # TODO: Agrega los botones faltantes.

        # PARTE 1.2: Llamamos el método "generar_layout_subir_bajar" con
        # la lista de botones de volumen y la lista de botones de canales.
        hbox = QHBoxLayout()
        hbox.addLayout(self.generar_layout_subir_bajar(self.volumen, 'Vol'))
        hbox.addLayout(self.generar_layout_subir_bajar(self.canales, 'Canal'))

        # Agregamos los elementos al layout principal
        vbox.addWidget(self.on_off)
        vbox.addStretch()
        vbox.addLayout(hbox)
        vbox.addStretch()
        vbox.addLayout(self.generar_layout_numeros())
        vbox.addStretch()

        # Setteamos el layout
        self.setLayout(vbox)

    def generar_layout_subir_bajar(self, botones: list, texto: str) -> None:
        '''
        A partir de un par de botones y un texto, genera un layout
        vertical donde ubica los botones en los extremos y el texto al centro.
        '''
        texto = QLabel(texto, self)
        texto.setAlignment(Qt.AlignmentFlag.AlignCenter)

        vbox = QVBoxLayout()
        vbox.addWidget(botones[0])
        vbox.addWidget(texto)
        vbox.addWidget(botones[1])
        return vbox

    def generar_layout_numeros(self) -> None:
        '''
        A partir de los botones numéricos guardados en el atributo "numeros",
        genera un grid layout de 3x3 donde ubica los botones.
        '''
        # Creamos la grilla de los números
        grilla_numeros = QGridLayout()

        # Agregamos los botones a la grilla
        for pos, boton in enumerate(self.numeros):
            fila = pos // 3
            columna = pos % 3
            grilla_numeros.addWidget(boton, fila, columna)

        # Retornamos la grilla
        return grilla_numeros

    def agregar_estilo(self) -> None:
        '''
        Agrega estilo a los distintos componentes de la ventana.
        '''
        # Aplicamos estilo a los elementos
        self.setStyleSheet('''
            background: #2e2d2b;
            color:white;
        ''')
        self.on_off.setStyleSheet('''
            background: red;
            border-radius: 15px;
        ''')

        # Ajustamos el tamaño de los botones
        for boton in (*self.volumen, *self.canales, *self.numeros):
            boton.setMinimumWidth(boton.sizeHint().height())
        self.on_off.setFixedSize(50, 50)

        # Ajustamos el tamaño del control
        self.resize(50, 360)

    def conectar_botones(self) -> None:
        '''
        Conecta los botones a las funciones o señales que deben manejar los clicks:
        - Actualización del volumen: "actualizar_volumen"
        - Actualización del canal: "actualizar_canal"
        - Encender/apagar la tele: "senal_encendido"
        '''
        # Botones de volumen
        for boton in self.volumen:
            boton.clicked.connect(self.actualizar_volumen)

        # Botones de canales
        for boton in [*self.canales, *self.numeros]:
            boton.clicked.connect(self.actualizar_canal)

        # Botón apagado
        self.on_off.clicked.connect(self.senal_encendido.emit)

    def actualizar_canal(self) -> None:
        '''
        Identifica el botón que fue apretado y envía su 
        identificador (número, +, -) al Controlador Lógico.
        
        TODO PARTE 2.1.a: Completa el método para lograr lo anterior.
        '''
        sender = self.sender()
        identificador = sender.text()
        self.senal_canal.emit(identificador)

    def actualizar_volumen(self) -> None:
        '''
        Identifica el botón que fue apretado y envía su 
        identificador (+, -) al Controlador Lógico.
        
        TODO PARTE 2.1.b: Completa el método para lograr lo anterior.
        '''
        sender = self.sender()
        identificador = sender.text()
        self.senal_volumen.emit(identificador)


if __name__ == '__main__':
    def hook(type, value, traceback) -> None:
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])
    ventana = VentanaControlRemoto()
    ventana.show()
    sys.exit(app.exec())
