from typing import Self
from tablero import Tablero, Posicion
from copy import deepcopy

class CaminoIterator:
    """
    Clase iterador. Maneja la lógica de moverse por la grilla
    usando __next__ y __iter__. Ignora movimientos inválidos
    e imprime en cada iteración
    """

    def __init__(self, tablero: Tablero, movimientos: list[str]) -> None:
        """
        Guarda el tablero, la lista de movimientos. Agrega todo lo que estimes
        necesario
        """
        self.tablero = tablero
        self.movimientos = movimientos
        # Agrega lo que estimes necesario

    def __next__(self) -> Posicion:
        """
        Método que maneja la lógica de iterar. Maneja las
        excepciones y lógica para saltarte movimientos incorrectos
        y contar vidas
        """
        pass



class CaminoIterable:
    """
    Camino con movimientos para el tablero. Implementa
    __iter__, por lo que se puede iterar.
    """
    def __init__(self, tablero: Tablero, movimientos: list[str]) -> None:
        """
        Guarda el tablero y movimientos
        """
        self.tablero = tablero
        self.movimientos = movimientos

    def __iter__(self) -> CaminoIterator:
        """
        Retorna un iterador de camino
        """
        movimientos = deepcopy(self.movimientos)
        return CaminoIterator(self.tablero, movimientos)