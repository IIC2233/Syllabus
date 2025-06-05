from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtGui import QFont, QPixmap, QMouseEvent, QKeyEvent
from PyQt5.QtCore import Qt, pyqtSignal, QUrl
from PyQt5.QtWidgets import QHBoxLayout, QWidget, QComboBox, QLabel, QPushButton
from os.path import abspath
import parametros as p


class VentanaInicio(QWidget):
    senal_seleccionar_dificultad = pyqtSignal(str)

    def __init__(self) -> None:
        """
        Creamos todos los elementos de la primera ventana.

        Este método tiene 1 error 😱.
        TODO: Ronda 2.3
        """
        super().__init__()
        self.setGeometry(200, 200, 400, 150)
        self.setWindowTitle("Selector Dificultad")

        # Creamos el selector que vamos a necesitar en nuestra ventana de Inicio
        self.selector_dificultad = QComboBox(self)

        # Usamos el parámetro DIFICULTAD para detectar obtener las diferentes opciones.
        self.selector_dificultad.addItems(p.DIFICULTAD)
        self.boton_ingresar = QPushButton("Empezar juego", self)

        # Creamos el layout de nuestra ventana y agregamos los elementos
        layout = QHBoxLayout()
        layout.addWidget(self.selector_dificultad)
        layout.addWidget(self.boton_ingresar)

        self.setLayout(layout)

    def enviar_info(self) -> None:
        """
        Método encargado de enviar la señal al backend sobre la dificultad
        seleccionada.
        """
        # Le avisamos al backend la dificultad mediante la señal.
        text = self.selector_dificultad.currentText()
        print(f"[FRONT] Enviar info --> {text}")
        self.senal_seleccionar_dificultad.emit(text)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        """
        Método encargado de detectar cuando oprimimos ENTER para hacer
        lo mismo que si hubiera oprimido el botón "Empezar juego"
        """
        print("[FRONT] Se presionó una tecla")
        if event.key() == Qt.Key.Key_Enter or event.key() == Qt.Key.Key_Return:
            self.enviar_info()


class VentanaJuego(QWidget):
    senal_click_pantalla = pyqtSignal(int, int)

    def __init__(self) -> None:
        super().__init__()
        # Tamaño de mi Ventana
        self.setGeometry(100, 100, p.ANCHO_JUEGO, p.ALTURA_JUEGO)

        # QLabel para el Background (imagen de fondo)
        self.background = QLabel(self)
        self.background.setPixmap(QPixmap(p.FONDO_PATH))
        self.background.setScaledContents(True)
        self.background.setGeometry(0, 0, p.ANCHO_JUEGO, p.ALTURA_JUEGO)

        # Importante el QLabel sea transparente a los eventos del mouse.
        self.background.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)

        # QLabel para la Vida
        self.label_vida = QLabel(self)
        self.label_vida.setFont(QFont("Arial", 17))
        self.label_vida.setGeometry(90, 10, 280, 50)
        self.label_vida.setStyleSheet("color: white")

        self.labels_meteorito = {}  # id: label
        # Defino la QPixmap para cada meteorito
        self.pixmap_meteorito = QPixmap(p.METEORO_PATH)

        # QLabel para la mira del disparo
        self.label_disparo = QLabel(self)
        self.label_disparo.setPixmap(QPixmap(p.MIRA_PATH))
        self.label_disparo.setScaledContents(True)
        self.label_disparo.setGeometry(-100, -100, 100, 100)

        self.media_player_mp3 = QMediaPlayer(self)
        path = abspath(p.SOUND_PATH)
        content = QMediaContent(QUrl.fromLocalFile(path))
        self.media_player_mp3.setMedia(content)
        self.media_player_mp3.setVolume(100)
        self.personalizarMouse()

    def personalizarMouse(self) -> None:
        """
        Este método se encarga de personalizar el mouse para que sea invisible,
        se detecte siempre su movimiento y los QLabel no interfieren an la detección
        de los eventos del mouse.
        """
        # Ventana pueda seguir en todo momento el movimiento del mouse y
        self.setMouseTracking(True)

        # Que el mouse sea invisible
        self.setCursor(Qt.CursorShape.BlankCursor)

        # El QLabel de la mira sea transparente a los eventos del mouse.
        self.label_disparo.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)

        # El QLabel con las vidas sea transparente a los eventos del mouse.
        self.label_vida.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)

    def empezar_juego(self) -> None:
        """
        Método encargado de reproducir la música y mostrar la ventana
        cuando empieza el juego.

        Este método tiene 1 error 😱.
        TODO: Ronda 3.1
        """
        print("[FRONT] Empezar juego")
        self.media_player_mp3.start()

        self.show()

    def mousePressEvent(self, event: QMouseEvent) -> None:
        """
        Método encargado de avisar al backend cada vez que presionamos
        con el mouse.
        """
        if event.button() == Qt.MouseButton.LeftButton:
            x = event.pos().x()
            y = event.pos().y()
            self.senal_click_pantalla.emit(x, y)

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        """
        Método encargado de mover visualmente la mira de disparo cada vez
        que se mueve el mouse
        """
        x = event.pos().x()
        y = event.pos().y()
        # Hacemos -50 para que la imagen esté centrada al mouse
        self.label_disparo.move(x - 50, y - 50)

    def actualizar_poblacion(self, texto: str) -> None:
        """
        Método encargado de actualizar la cantidad de vidas en la ventana
        """
        self.label_vida.setText(texto)
        self.label_vida.resize(self.label_vida.sizeHint())

    def aparecer_meteorito(self, id_meteorito: int, x: int, y: int) -> None:
        """
        Método encargado de generar visualmente un meteorito en la ventana
        """
        # Definir label de meteorito
        label = QLabel(self)
        label.setPixmap(self.pixmap_meteorito)
        label.setScaledContents(True)
        label.setGeometry(x, y, p.ANCHO_METEORO, p.ALTURA_METEORO)

        # Este QLabel sea transparente a los eventos del mouse.
        label.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)

        # Guardar QLabel en nuestro diccionario
        self.labels_meteorito[id_meteorito] = label

        # Asegurar que la mira de disparo sig sobre todo lo demás QLabel
        self.label_disparo.raise_()

        # Mostrar imagen
        label.show()

    def remover_meteorito(self, id_meteorito: int) -> None:
        """
        Método encargado de eliminar visualmente un meteorito en la ventana.
        En este caso, solo lo escondemos.

        Tarea para la casa: Investigar como eliminar elementos y
        no solo ocultarlos
        """
        self.labels_meteorito[id_meteorito].hide()

    def mover_meteorito(self, id_meteorito, x, y) -> None:
        """
        Método encargado de mover visualmente un meteorito en la ventana
        """
        label: QLabel = self.labels_meteorito[id_meteorito]
        label.move(x, y)
