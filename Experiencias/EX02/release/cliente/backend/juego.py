from PyQt5.QtCore import QObject, pyqtSignal, QMutex
from backend.networking import Cliente
from backend.meteorito import Meteorito
import parametros as p


class Juego(QObject):
    senal_empezar_juego = pyqtSignal()
    senal_mover_meteorito = pyqtSignal(int, int, int)
    senal_aparecer_meteorito = pyqtSignal(int, int, int)
    senal_remover_meteorito = pyqtSignal(int)
    senal_fin_meteorito = pyqtSignal(int, bool)
    senal_actualizar_poblacion = pyqtSignal(str)

    def __init__(self, host: str, port: int) -> None:
        super().__init__()

        self.meteoritos = []
        self.mutex = QMutex()
        self.senal_fin_meteorito.connect(self.fin_meteorito)

        self.cliente = Cliente(port, host)
        self.cliente.senal_empezar_juego.connect(self.empezar_juego)
        self.cliente.senal_aparecer_meteorito.connect(self.aparecer_meteorito)
        self.cliente.senal_actualizar_poblacion.connect(self.actualizar_poblacion)
        self.cliente.start()

    def seleccionar_dificultad(self, dificultad: str) -> None:
        """
        Método encargado de avisar al servidor que empezó el juego
        """
        print(f"[BACK] Dificultad recibida: {dificultad}")
        mensaje = {
            "comando": "empezar",
            "data": {"rangos": [0, p.ANCHO_JUEGO], "dificultad": dificultad},
        }
        self.cliente.enviar_mensaje(mensaje)

    def empezar_juego(self):
        print("[BACK] El servidor avisó que hay que comenzar el juego")
        self.senal_empezar_juego.emit()

    def aparecer_meteorito(self, post_x: int) -> None:
        """
        Método encargado de crear la lógica de un meteorito y notificar al
        frontend que debe aparecer un nuevo meteorito.
        Luego empiece su ejecución y guarda el meteorito en memoria.

        En este método hay 2 errores 😱.
        TODO: Ronda 3.2 y 3.3
        """

        meteorito = Meteorito(
            x=post_x,
            y=-p.ALTURA_METEORO,
            mutex=self.mutex,
            senal_fin_meteorito=self.senal_fin_meteorito,
            senal_mover=self.senal_mover_meteorito,
        )
        print(f"[BACK] Creando nuevo meteorito con id={meteorito.id}")
        self.senal_aparecer_meteorito.emit(meteorito.id, meteorito.x, meteorito.y)

    def actualizar_poblacion(self, poblacion: int) -> None:
        if poblacion <= 0:
            self.senal_actualizar_poblacion.emit(
                "DCCiudad ha perdido todos sus ciudadanos"
            )
        else:
            self.senal_actualizar_poblacion.emit(
                f"DCCiudad tiene {poblacion} ciudadanos"
            )

    def fin_meteorito(self, id_meteorito: int, daño: bool) -> None:
        """
        Método encargado de gestionar el fin de un meteorito. Esto implica
        Avisar al frontend cuando hay que eliminar,
        reducir la población en caso que el meteorito haga daño
        y si no queda población, detener la caída de meteoritos

        En este método hay 1 error 😱.
        TODO: Ronda 4.1
        """
        print(f"[BACK] Meteorito {id_meteorito} será eliminado")

        if daño:  # Si hay daño, avisar al servidor
            mensaje = {"comando": "caer-meteorito"}
            self.cliente.enviar_mensaje(mensaje)

    def click_pantalla(self, x: int, y: int) -> None:
        """
        Método encargado de buscar el meteorito activo
        más cercano al click del mouse y si está dentro del radio esperado
        lo destruye.
        """
        print(f"[BACK] Presioné en {x},{y}")
        for meteorito in self.meteoritos:
            if not meteorito.destruido:  # Solo verificar meteoritos sin destruir
                diff_x = (x - meteorito.centro_x) ** 2
                diff_y = (y - meteorito.centro_y) ** 2
                distancia = (diff_x + diff_y) ** (1 / 2)
                if distancia < p.DISTANCIA_IMPACTO:
                    # Si el click es válido, se destruye el meteorito
                    meteorito.destruido = True

                    # Dejo de buscar más meteoritos porque ya destruí uno.
                    return