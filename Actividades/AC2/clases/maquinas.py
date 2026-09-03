from clases.fabrica import Caja, CajaRechazadaError
from utils import codigo_valido


class MaquinaInspeccion:
    def __init__(self, peso_maximo: float) -> None:
        self.peso_maximo = peso_maximo

    def inspeccionar(self, caja: Caja) -> None:
        # TODO (Parte 3): completar este método.
        pass
