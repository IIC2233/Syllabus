from collections import deque
from datetime import datetime, timedelta

from parametros import (
    DURACION_SERVICIO,
    MENU,
    NOMBRES_COCINEROS,
    NUM_COCINEROS,
    PEDIDOS_POR_COCINERO,
)
from utilidades import log


class Pedido:
    """
    Un pedido de un cliente. NO MODIFICAR.
    """

    def __init__(self, id_pedido: int, plato: str) -> None:
        self.id_pedido = id_pedido
        self.plato = plato
        self.inicio = None
        self.entrega = None

    def __repr__(self) -> str:
        return f"Pedido #{self.id_pedido} ({self.plato})"


class Cocinero:
    """
    Un cocinero del restaurante. Atiende, de uno en uno, los pedidos que
    tiene asignados en su propia cola.
    """

    def __init__(self, nombre: str) -> None:
        super().__init__(name=nombre)
        self.nombre = nombre
        self.pedidos = deque()

    def asignar_pedido(self, pedido: Pedido) -> None:
        """Agrega un pedido al final de su cola. NO MODIFICAR."""
        self.pedidos.append(pedido)

    # COMPLETAR Parte 1


class Cocina:
    """
    Un servicio completo del restaurante, de la apertura al cierre.
    """

    # COMPLETAR: la estufa no alcanza para dos, y el registro de entregas
    # lo escriben todos los cocineros. Define aquí lo necesario para que
    # solo un cocinero a la vez pueda acceder a cada uno.

    def __init__(self, num_cocineros: int = NUM_COCINEROS,
                 pedidos_por_cocinero: int = PEDIDOS_POR_COCINERO,
                 duracion_servicio: float = DURACION_SERVICIO) -> None:
        self.duracion_servicio = duracion_servicio

        # COMPLETAR: los cocineros no deben empezar a trabajar antes de que
        # abra el restaurante, y deben saber cuándo la cocina cerró.

        self.cocineros = self.contratar_cocineros(num_cocineros)
        self.pedidos = self.recibir_pedidos(
            num_cocineros * pedidos_por_cocinero
        )
        self.repartir_pedidos()

    def contratar_cocineros(self, cantidad: int) -> dict[str, Cocinero]:
        """Crea los cocineros del turno. NO MODIFICAR."""
        cocineros: dict[str, Cocinero] = dict()
        for i in range(cantidad):
            nombre = NOMBRES_COCINEROS[i % len(NOMBRES_COCINEROS)]
            cocineros[nombre] = Cocinero(nombre)
        return cocineros

    def recibir_pedidos(self, cantidad: int) -> list[Pedido]:
        """Crea los pedidos de la noche. NO MODIFICAR."""
        return [
            Pedido(i + 1, MENU[i % len(MENU)]) for i in range(cantidad)
        ]

    def repartir_pedidos(self) -> None:
        """Reparte los pedidos entre los cocineros. NO MODIFICAR."""
        cocineros = list(self.cocineros.values())
        for i, pedido in enumerate(self.pedidos):
            cocineros[i % len(cocineros)].asignar_pedido(pedido)

    def cerrar_cocina(self) -> None:
        """Cierra la cocina para nuevos pedidos"""
        log("COCINA", "*** SE CIERRA LA COCINA: no se toman más pedidos ***")
        # COMPLETAR Parte 2

    def simular_servicio(self) -> tuple[dict[int, timedelta], list[Pedido]]:
        # COMPLETAR Parte 2
        pass
