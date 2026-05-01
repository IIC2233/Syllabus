from __future__ import annotations
from utils import NodoLigadoAbstracto

class NodoLigado(NodoLigadoAbstracto):
    def insertar(self, other: NodoLigado) -> NodoLigado:
        pass

    def remover(self, id: int) -> NodoLigado | None:
        pass

    def buscar(self, id: int) -> NodoLigado | None:
        pass