from collections import namedtuple

Posicion = namedtuple("Posicion", ["fila", "columna"])

class Tablero:
    """
    Maneja la lógica del tablero y movimiento
    """

    def __init__(self, grilla: list[list[str]], inicio: Posicion) -> None:
        """
        Inicializa el tablero dada la grilla y la posicion inicial
        """
        pass

    def mover(self, posicion: Posicion, direccion: str) -> Posicion:
        """
        Recibe una posicion (fila, columna) y una direccion
        "ARRIBA", "ABAJO", "IZQUIERDA" o "DERECHA".
        Retorna la nueva posicion si el movimiento es valido.
        
        Lanza:
        - KeyError cuando la dirección no existe
        - IndexError si se sale de la grilla
        - ValueError si se intenta pasar por un muro (@)
        """
        pass
            
