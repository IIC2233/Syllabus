from __future__ import annotations

from clases.fabrica import Caja, Registro


class Nodo:
    def __init__(self, valor: Caja | Registro) -> None:
        self.valor = valor
        self.siguiente = None

    def __repr__(self) -> str:
        return f"Nodo[{self.valor!r}]"


class ListaLigada:
    def __init__(self) -> None:
        self.cabeza = None
        self.cola = None
        self.largo = 0

    def agregar(self, valor: Caja | Registro) -> None:
        # TODO (Parte 1): completar este método.
        pass

    def retirar_primera(self) -> Caja | Registro:
        # TODO (Parte 1): completar este método.
        pass

    def __len__(self) -> int:
        return self.largo

    def __iter__(self) -> IteradorListaLigada:
        # TODO (Parte 2): completar este método.
        pass


class IteradorListaLigada:
    def __init__(self, cabeza: Nodo | None) -> None:
        # TODO (Parte 2): completar este método.
        pass

    def __iter__(self) -> IteradorListaLigada:
        # TODO (Parte 2): completar este método.
        pass

    def __next__(self) -> Caja | Registro:
        # TODO (Parte 2): completar este método.
        pass
