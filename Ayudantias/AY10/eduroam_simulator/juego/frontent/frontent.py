import sys
from os.path import join
import os

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QPixmap, QTransform, QKeyEvent
from PyQt5.QtCore import Qt, QThread, pyqtSignal,QPoint, QTimer, QMutex, pyqtSignal, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QSoundEffect, QMediaContent


class Dino(QLabel):
    def __init__(self, ventana):
        super().__init__(ventana)

        #Cargo las 3 imagenes 
        self.sprites = [QPixmap(f"frontent/img/dino{num+1}.png") for num in range(3)]
        self.setPixmap(self.sprites[0])

        # Geometria del dinosaurio
        self.setGeometry(100,600,100,100)
        self.setScaledContents(True)
        self.imagen = 0

        # Thread encargado de cambiar el sprite
        self.thread_mover = QTimer()
        self.thread_mover.timeout.connect(self.cambiar_imagen)
        self.thread_mover.start(100)
        
        # Es False si perdemos
        self.seguimos = False

        # Lock para que no saltes 2 veces
        self.lock_salto = QMutex()



    def cambiar_imagen(self):
        # 10 veces por segundo, cambio la imagen de mi dinosaurio para que mueva
        # Las patitas
        if self.seguimos:
            self.imagen += 1
            self.setPixmap(self.sprites[self.imagen % 3])


    def saltar(self):
        # -----Explicacion------
        # Cada vez que apreto el espacio un thread se genera en el dinosaurio
        # El problema es que si 2 thread están haciendolo saltar simultaneamente
        # Entran en conflicto y el dinosaurio empieza a volar
        # Por eso se comprueba el QMutex con trylock, si es positivo hago saltar al dinosaurio
        # Sino simplemente paso de largo



        # Compruebo si el lock está pedido
        respuesta = self.lock_salto.tryLock()

        if respuesta:
            self.altura_salto = 300     
            self.velocidad = 8         
            self.subiendo = True        
            self.y_inicial = self.y()   
            self.timer_salto = QTimer()
            self.timer_salto.timeout.connect(self._animar_salto)
            self.timer_salto.start(10)
        else:
            return
        

    def _animar_salto(self):
        # se encarga de mover el dinosaurio hacia arriba hasta alcanzar la altura de salto
        # Luego lo hace bajar

        y_actual = self.y()
        
        if self.subiendo:
            nuevo_y = y_actual - self.velocidad
            if self.y_inicial - nuevo_y >= self.altura_salto:
                self.subiendo = False
        else:
            nuevo_y = y_actual + self.velocidad
            if nuevo_y >= self.y_inicial:
                nuevo_y = self.y_inicial
                self.lock_salto.unlock()
                self.timer_salto.stop()

        self.move(self.x(), nuevo_y)

class Gato(QLabel):
    def __init__(self, ventana):
        super().__init__(ventana)
        pixmap = QPixmap("frontent/img/gato.png")

        # La foto del gato mira hacia el otro lado, No habia otra en google :(
        # Así que la damos vuelta
        transform = QTransform().scale(-1, 1)
        pixmap_reflejado = pixmap.transformed(transform)

        # Seteamos el pixmap
        self.setPixmap(pixmap_reflejado)
        self.setGeometry(2000, 600, 100, 100)
        self.setScaledContents(True)
        self.mover = True


        #Thread que mueve el gato a la izquierda
        self.thread_mover = QTimer()
        self.thread_mover.timeout.connect(self.mover_izquierda)
        self.thread_mover.start(16)
        
        # Es False si perdemos
        self.seguimos = True
    
    def mover_izquierda(self):
        if self.seguimos:
            if self.mover:
                # Accedo a la posicion donde está
                pos = self.pos()
                pos_x = pos.x()
                pos_y = pos.y()

                # Muevo un poquito
                nuevo_x = pos_x - 8
                self.move(nuevo_x, pos_y)

            if nuevo_x <= -100:
                # Si tenemos que supera cierta barrera hacemos que se detenga
                self.seguimos = False
        else:
            # Si un gato está detenido borramos el thread que lo mueve
            self.thread_mover.stop()

class MiVentana(QWidget):
    senal_obtener_clasificador = pyqtSignal()
    senal_nombre = pyqtSignal(str)
    senal_publicar_puntaje = pyqtSignal(int)

    def __init__(self) -> None:
        super().__init__()
        
        self.gatos = []
        self.seguimos = False

        self.iniciar_gui()
        self.iniciar_sonidos()
        self.iniciar_threads()

        self.setFocusPolicy(Qt.StrongFocus)
        self.setFocus()

    def iniciar_threads(self):

        # Qthread que ve si perdemos
        self.timer_colision = QTimer()
        self.timer_colision.timeout.connect(self.revisar_colisiones)
        self.timer_colision.start(100)  # cada 100 ms

        # Thread que crea un nuevo gato cada 2 segundos
        self.mas_gatos()
        self.timer_mas_gatos = QTimer()
        self.timer_mas_gatos.timeout.connect(self.mas_gatos)
        self.timer_mas_gatos.start(2000)

        # Thread encargado de subir el puntaje
        self.timer_puntaje = QTimer()
        self.timer_puntaje.timeout.connect(self.sumar_puntaje)
        self.timer_puntaje.start(100)


        #Thread que consulta el clasificador
        # Se deja en un thread aparte debido a que request detiene todo, osea que 
        # Congelaria el código

        self.timer_mas_gatos = QTimer()
        self.timer_mas_gatos.singleShot(1000, self.consultar_clasificador)

    def iniciar_sonidos(self):

        # ------------------PRECAUCIÓN------------------------------
        # Notar que se utiliza QMediaPlayer Solamente porque son archivos .mp3
        # En caso de ser .wav se deberia utilizar QSoundEffect


        # Sonido de perder
        self.sonido_perder = QMediaPlayer(self)
        path = os.path.abspath(join("frontent", "sound", "die.mp3"))
        content = QMediaContent(QUrl.fromLocalFile(path))
        self.sonido_perder.setMedia(content)

        # Sonido de saltar
        self.sonido_saltar = QMediaPlayer(self)
        path = os.path.abspath(join("frontent", "sound", "jump.mp3"))
        content = QMediaContent(QUrl.fromLocalFile(path))
        self.sonido_saltar.setMedia(content)

        # Sonido Puntos
        self.sonido_puntos = QMediaPlayer(self)
        path = os.path.abspath(join("frontent", "sound", "point.mp3"))
        content = QMediaContent(QUrl.fromLocalFile(path))
        self.sonido_puntos.setMedia(content)

    def iniciar_gui(self):

        self.setGeometry(400, 400, 2000, 800)

        #Creamos la linea inferior
        label = QLabel(self)
        label.setGeometry(0, 700, 1000000, 10)
        label.setStyleSheet("background-color: black;")

        #Creamos nueestro dinosaurio
        self.dinosaurio = Dino(self)


        # Creamos el campo para ingresar nombre
        self.nombre = QLineEdit("Nombre", self)
        self.nombre.setGeometry(700, 350, 800, 100)
        self.nombre.setAlignment(Qt.AlignCenter)

        # Creamos el boton para iniciar la partida
        self.boton = QPushButton("Iniciar",self)
        self.boton.setGeometry(950, 450, 300, 100)
        self.boton.clicked.connect(self.iniciar)

        #Ranking
        self.label_ranking = QLabel(self)
        self.label_ranking.setGeometry(1550, 50, 400, 600)
        self.label_ranking.setStyleSheet("font-size: 20px; background-color: #EEE; border: 1px solid black;")
        self.label_ranking.setAlignment(Qt.AlignTop)
        self.label_ranking.setWordWrap(True)

        # Qlabel de puntaje
        self.puntaje = 0
        self.label_puntaje = QLabel(f"Puntaje: {self.puntaje}", self)
        self.label_puntaje.setStyleSheet("font-size: 20px; background-color: #EEE; border: 1px solid black;")
        self.label_puntaje.setGeometry(10, 10, 400, 50)

    def sumar_puntaje(self):
        if self.seguimos:
            self.puntaje += 100
            self.label_puntaje.setText(f"Puntaje: {self.puntaje}")
            if self.puntaje % 5000 == 0:
                # Aquí reproducimos un sonido de puntos
                self.sonido_puntos.play()

    def consultar_clasificador(self):
        self.senal_obtener_clasificador.emit()

    def revisar_colisiones(self):
        if self.seguimos:
            for gato in self.gatos:
                if gato.geometry().intersects(self.dinosaurio.geometry()):
                    self.perder()

    def perder(self):
        # Hacemos que todo se detenga
        self.seguimos = False
        self.dinosaurio.seguimos = False
        for gato in self.gatos:
            gato.hide()

        # Volvemos a sacar el boton de iniciar
        self.boton.show()
        
        # Publicamos los nuevos puntajes
        self.senal_publicar_puntaje.emit(self.puntaje)

        # Detenemos la aparición de los gatos
        self.timer_mas_gatos.stop()

        # Reproducimos el sonido correspondiente
        self.sonido_perder.play()    

    def mas_gatos(self):
        if self.seguimos:
            gato = Gato(self)
            gato.show()
            gato.seguimos = True
            self.gatos.append(gato)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key_Space:
            if self.seguimos:
                self.dinosaurio.saltar()
                self.sonido_saltar.play()

    def iniciar(self):
        self.puntaje = 0
        
        #Le decimos a todas las entidades que pueden iniciar su movimiento
        self.dinosaurio.seguimos = True
        self.seguimos = True
        self.gatos = []

        # Ocultamos la interfaz gráfica 
        self.boton.hide()
        self.nombre.hide()

        # Emito una señal al backend para que guarde el nombre
        self.senal_nombre.emit(self.nombre.text())
        
        #Iniciamos el timer encargado de generar más gatos
        self.timer_mas_gatos = QTimer()
        self.timer_mas_gatos.timeout.connect(self.mas_gatos)
        self.timer_mas_gatos.start(2000)

    def mostrar_clasificador(self, lista):
        lista_ordenada = sorted(lista, key=lambda x: x['puntaje'], reverse=True)
        ranking = "🏆 RANKING\n\n"
        for i, jugador in enumerate(lista_ordenada, start=1):
            ranking += f"{i}. {jugador['nombre']} - {jugador['puntaje']}\n"

        self.label_ranking.setText(ranking)
        


if __name__ == '__main__': 
    def hook(type, value, traceback) -> None:
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])
    ventana = MiVentana()  
    ventana.show()
    sys.exit(app.exec())
