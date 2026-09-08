class Carta:
    def __eq__(self, otra) -> bool:
        return self.color == otra.color or self.numero == otra.numero


class IteradorManoCartas:
    def __init__(self, cabeza: Carta) -> None:
        self.mano = cabeza
        self.pozo = cabeza

    def __iter__(self) -> "IteradorManoCartas":
        return self

    def __next__(self) -> Carta:
        carta_anterior = None
        carta_actual = self.mano

        if carta_actual is None:
            raise StopIteration("No quedan cartas en el mazo")

        while carta_actual is not None:

            if carta_actual == self.pozo:

                if carta_actual is self.mano:
                    self.mano = carta_actual.siguiente

                if carta_anterior is not None:
                    carta_anterior.siguiente = carta_actual.siguiente

                self.pozo = carta_actual
                return carta_actual

            carta_anterior = carta_actual
            carta_actual = carta_actual.siguiente

        raise StopIteration("No se puede jugar ninguna carta")
