from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtCore import pyqtSignal, Qt

# Este label clickeable solo tiene fines estéticos. Pero puedes usar esta 
# plantilla para hacer un label que tenga una foto y además sea clickeable!

class LabelClickeable(QLabel):
    senal_click = pyqtSignal(int, int)

    def __init__(self, fil, col):
        super().__init__()
        self.fil = fil
        self.col = col
        self.setFixedSize(50, 50)
        self.setStyleSheet("background-color: lightblue; font-size: 40px;")
        self.setAlignment(Qt.AlignCenter)
    
    def mousePressEvent(self, event):
        self.senal_click.emit(self.fil, self.col)


class VentanaInicio(QWidget):
    senal_inicio = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana de inicio")
        self.setGeometry(20, 20, 200, 100)
        self.label = QLabel("Esperando oponente...", self)


class VentanaJuego(QWidget):
    senal_click_label = pyqtSignal(int, int)

    def __init__(self):
        super().__init__()
        self.init_gui()

    def init_gui(self):
        self.setWindowTitle("Ventana de juego")
        self.setGeometry(20, 20, 300, 300)

        self.label_jugador = QLabel('', self)
        self.label_turno = QLabel('', self)

        layout_principal = QHBoxLayout()
        v_layout_1 = QVBoxLayout()
        v_layout_1.addWidget(self.label_jugador)
        v_layout_1.addWidget(self.label_turno)
        layout_principal.addLayout(v_layout_1)

        v_layout_2 = QVBoxLayout()
        self.labels = []
        for fil in range(3):
            h_layout = QHBoxLayout()
            col_labels = []
            for col in range(3):
                label = LabelClickeable(fil, col)
                label.senal_click.connect(self.senal_click_label.emit)
                h_layout.addWidget(label)
                col_labels.append(label)
            v_layout_2.addLayout(h_layout)
            self.labels.append(col_labels)
        layout_principal.addLayout(v_layout_2)
        self.setLayout(layout_principal)

    def modificar_jugador(self, simbolo):
        self.label_jugador.setText(f"Jugador: {simbolo}")
    
    def modificar_casilla(self, fil, col, simbolo):
        self.labels[fil][col].setText(simbolo)
    
    def modificar_turno(self, simbolo):
        self.label_turno.setText(f"Turno: {simbolo}")
    

class VentanaFinal(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana Final")
        self.setGeometry(20, 20, 400, 100)
        self.label = QLabel("", self)
        self.label.setFixedSize(400, 100)
        self.label.setStyleSheet("font-size: 20px;")
        self.label.setAlignment(Qt.AlignCenter)
    
    def mostrar(self, simbolo, resultado):
        self.show()
        self.label.setText(f"jugador {simbolo}: {resultado}")
