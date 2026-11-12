import random
from collections import namedtuple
from grafo import Grafo

Laberinto = namedtuple("Laberinto", ["grafo", "inicio", "meta"])


def vecinos_cuadricula(celda: tuple, tamano: int) -> list:
    """
    Retorna los vecinos de una celda dentro de una cuadrícula
    de tamano x tamano.

    Orden: arriba, derecha, abajo, izquierda.
    """
    fila, columna = celda

    candidatos = [
        (fila - 1, columna),
        (fila, columna + 1),
        (fila + 1, columna),
        (fila, columna - 1)
    ]

    vecinos = []
    for f, c in candidatos:
        if 0 <= f < tamano and 0 <= c < tamano:
            vecinos.append((f, c))

    return vecinos


def buscar_raiz(padres: dict, nodo: tuple) -> tuple:
    """
    Encuentra el representante del conjunto al que pertenece un nodo.
    Utiliza compresión de caminos.
    """
    if padres[nodo] != nodo:
        padres[nodo] = buscar_raiz(padres, padres[nodo])

    return padres[nodo]


def unir_conjuntos(padres: dict, rangos: dict, nodo_1: tuple, nodo_2: tuple) -> bool:
    """
    Une los conjuntos de dos nodos si pertenecen a componentes distintas.
    Retorna True si se realizó la unión y False en caso contrario.
    """
    raiz_1 = buscar_raiz(padres, nodo_1)
    raiz_2 = buscar_raiz(padres, nodo_2)

    if raiz_1 == raiz_2:
        return False

    if rangos[raiz_1] < rangos[raiz_2]:
        padres[raiz_1] = raiz_2
    elif rangos[raiz_1] > rangos[raiz_2]:
        padres[raiz_2] = raiz_1
    else:
        padres[raiz_2] = raiz_1
        rangos[raiz_1] += 1

    return True


def generar_laberinto(
    tamano: int,
    densidad: float = 0.25
) -> Laberinto:
    """
    Input:
    - tamano: entero mayor o igual a 2 que define el largo y ancho.
    - densidad: float entre 0 y 1 que controla la cantidad de
      paredes internas.

    Construye primero un árbol de expansión aleatorio utilizando
    Kruskal sobre una cuadrícula de tamano x tamano.

    Luego agrega conexiones adicionales con probabilidad (1 - densidad).

    'densidad' controla paredes internas, NO celdas bloqueadas.
    Todas las celdas son transitables y la meta siempre es alcanzable.
    """
    if tamano < 2:
        raise ValueError("tamano debe ser al menos 2")

    if not 0 <= densidad <= 1:
        raise ValueError("densidad debe estar entre 0 y 1")

    grafo = Grafo()

    inicio = (0, 0)
    meta = (tamano - 1, tamano - 1)

    padres = {}
    rangos = {}
    aristas = []

    # Crear nodos y conjuntos independientes.
    for fila in range(tamano):
        for columna in range(tamano):
            nodo = (fila, columna)

            grafo.agregar_nodo(nodo)
            padres[nodo] = nodo
            rangos[nodo] = 0

            # Agregar las posibles aristas sin duplicarlas.
            for vecino in vecinos_cuadricula(nodo, tamano):
                if nodo < vecino:
                    aristas.append((nodo, vecino))

    # Mezclar aleatoriamente las aristas.
    random.shuffle(aristas)

    # Kruskal: construir un árbol de expansión.
    for nodo_1, nodo_2 in aristas:
        if unir_conjuntos(padres, rangos, nodo_1, nodo_2):
            grafo.agregar_arista(nodo_1, nodo_2)

    # Agregar conexiones adicionales con probabilidad (1 - densidad).
    for nodo_1, nodo_2 in aristas:
        if nodo_2 not in grafo.vecinos(nodo_1):
            if random.random() < 1 - densidad:
                grafo.agregar_arista(nodo_1, nodo_2)

    return Laberinto(grafo, inicio, meta)

if __name__ == "__main__":
    # Como usar el generador de Laberintos:

    # Generar un laberinto dado un tamaño y densidad
    laberinto = generar_laberinto(20, 0.2)
    
    # Cada laberinto viene con su grafo, inicio y meta
    grafo = laberinto.grafo
    inicio = laberinto.inicio
    meta = laberinto.meta

    print(len(grafo))
    print(inicio)
    print(meta)





