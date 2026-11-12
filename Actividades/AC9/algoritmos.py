from collections import deque
from generador_laberintos import generar_laberinto

def bfs(grafo, inicio, meta):
    """
    Encuentra el camino más corto.
    Utiliza el diccionario "padres"
    para recordar qué nodo
    fue el que descubrió al nodo actual
    Luego se puede usar reconstruir_camino
    para encontrar el camino
    desde el final al origen y darlo vuelta
    """
    cola = deque([inicio])
    padres = {inicio: None}

    while cola:
        actual = cola.popleft()
        if actual == meta:
            return reconstruir_camino(padres, meta)

        for vecino in grafo.vecinos(actual):
            if vecino not in padres:
                padres[vecino] = actual
                cola.append(vecino)
            
    # Si no se encuentra la meta, se retorna camino vacío
    return []


def dfs(grafo, inicio, meta):
    """
    Encuentra el camino usando DFS.
    Utiliza el diccionario "padres"
    para recordar qué nodo
    fue el que descubrió al nodo actual
    Luego se puede usar reconstruir_camino
    para encontrar el camino
    desde el final al origen y darlo vuelta
    """
    stack = [inicio]
    padres = {inicio: None}

    while stack:
        actual = stack.pop()
        if actual == meta:
            return reconstruir_camino(padres, meta)

        for vecino in reversed(grafo.vecinos(actual)):
            if vecino not in padres:
                padres[vecino] = actual
                stack.append(vecino)

    # Si no se encuentra la meta, se retorna camino vacío
    return []

def reconstruir_camino(padres, meta):
    """
    Reconstruye el camino desde la meta
    hasta el nodo de inicio
    usando el diccionario "padres"
    """
    if meta not in padres:
        return []
    camino = []
    actual = meta
    while actual is not None:
        camino.append(actual)
        actual = padres[actual]
    return list(reversed(camino))


if __name__ == "__main__":
    # Generar laberinto con una sola solucion (densidad 1)
    laberinto = generar_laberinto(10, 1.0)

    # Usar BFS
    solucion = bfs(*laberinto)
    print(len(solucion))

    # Usar DFS
    solucion = dfs(*laberinto)
    print(len(solucion))

    # Generar laberinto sin muros (densidad 0)
    laberinto = generar_laberinto(10, 0.0)

    # Usar BFS
    solucion = bfs(*laberinto)
    print(len(solucion))

    # Usar DFS
    solucion = dfs(*laberinto)
    print(len(solucion))
