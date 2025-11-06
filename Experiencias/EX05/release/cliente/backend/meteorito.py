from PyQt5.QtCore import pyqtSignal, QMutex, QThread
from random import randint
import time
import parametros as p


class Meteorito(QThread):
    identificador = 0

    def __init__(
        self,
        x: int,
        y: int,
        mutex: QMutex,
        senal_fin_meteorito: pyqtSignal,
        senal_mover: pyqtSignal,
    ) -> None:
        super().__init__()

        self.id = Meteorito.identificador
        Meteorito.identificador += 1
        self.mutex = mutex
        self.x = x
        self.y = y
        self.senal_mover = senal_mover
        self.senal_fin_meteorito = senal_fin_meteorito
        self._destruido = False
        self._distancia_a_recorrer = randint(p.DISTANCIA_MINIMA, p.DISTANCIA_MAXIMA)

    def run(self) -> None:
        """
        Método encargado de mover constantemente el meteorito hacia abajo.
        Si llega a una posición indicada en "p.POSICION_Y", entonces llegó
        a la ciudad y hay que notificar que debe ser destruido junto con
        reducir la población de la ciudad.
        Solo 1 meteorito a la vez puede chocar con la ciudad.

        En este método hay 1 error 😱.
        TODO: Ronda 4.2
        """
        print(f"[BACK] Soy meteorito {self.id} y comienzo mi caída")
        while not self.destruido:
            time.sleep(p.TIEMPO_CAIDA_METEORO)
            self.y += self._distancia_a_recorrer
            self.senal_mover.emit(self.id, self.x, self.y)

            if self.y >= p.POSICION_Y:
                # Desaparecer haciendo daño
                self._destruido = True

                # Solo 1 meteorito notifica que debe hacer daño al mismo tiempo
                self.mutex.lock()
                self.senal_fin_meteorito.emit(self.id, True)

    @property
    def destruido(self) -> bool:
        return self._destruido

    @destruido.setter
    def destruido(self, destruido: bool) -> None:
        """
        Setter encargado de notificar cuando es necesario
        eliminar el meteorito
        """
        if destruido is True:
            self._destruido = destruido

            # Desaparecer sin hacer daño
            self.senal_fin_meteorito.emit(self.id, False)

    @property
    def centro_x(self) -> int:
        return self.x + 15

    @property
    def centro_y(self) -> int:
        return self.y + 192
