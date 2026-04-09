from tablero import Tablero, Posicion
from camino import CaminoIterable
from utils import imprimir_tablero_con_posicion

if __name__ == "__main__":
    # Inicializar tablero
    grilla = [
        [".", ".", "."],
        ["@", "@", "."],
        [".", ".", "."]
    ]
    inicio = Posicion(fila=0, columna=0)
    tablero = Tablero(grilla, inicio)


    ###### Parte 1:

    # # Movimiento correcto
    # tablero.mover(Posicion(fila=0, columna=0), "DERECHA")

    # # Movimiento hacia muro (Deberia levantar una excepcion)
    # tablero.mover(Posicion(fila=0, columna=0), "ABAJO")

    # # Movimiento hacia fuera del tablero (Deberia levantar una excepcion)
    # tablero.mover(Posicion(fila=0, columna=0), "ARRIBA")

    # # Movimiento no conocido (Deberia levantar una excepcion)
    # tablero.mover(Posicion(fila=0, columna=0), "DIAGONAL")

    ###### Parte 2
    # # Crear secuencia de movimientos (Muere)
    # movimientos = ["ARRIBA", "DERECHA", "DERECHA", "ABAJO", "IZQUIERDA", "ABAJO", "IZQUIERDA", "IZQUIERDA", "IZQUIERDA", "IZQUIERDA", "IZQUIERDA", "IZQUIERDA"]
    # camino = CaminoIterable(tablero, movimientos)

    # # Moverse en el tablero
    # imprimir_tablero_con_posicion(tablero, inicio)
    # for posicion in camino:
    #     imprimir_tablero_con_posicion(tablero, posicion)

