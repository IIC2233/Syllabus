from tablero import Tablero, Posicion

def imprimir_tablero_con_posicion(tablero: Tablero, posicion: Posicion) -> str:
    """
    Retorna un string que representa el tablero,
    marcando la posicion actual con una 'X'
    """

    filas = []

    for i, fila in enumerate(tablero.grilla):
        fila_str = []

        for j, valor in enumerate(fila):
            if Posicion(fila=i, columna=j) == posicion:
                fila_str.append("X")
            else:
                fila_str.append(valor)

        filas.append(" ".join(fila_str))

    print("\n".join(filas))