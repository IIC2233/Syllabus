from laberinto import Laberinto, Celda
from collections import deque

def reconstruir_ruta(celda_padre: dict[Celda, Celda], fin: Celda) -> list[Celda]:
    """
    TODO: Dado el diccionario celda_padre, reconstruye la ruta
    hasta la celda "fin" y la retorna como una lista de celdas
    """
    return []


def buscar_dfs(inicio: Celda, fin: Celda, ordernar_conexiones: bool = False) -> tuple[list[Celda], set[Celda]]:
    """
    TODO: Altera el método de DFS para que:
    - termine al encontrar la celda "fin"
    - reconstruya la ruta de inicio a fin usando reconstruir_ruta
    - retorne la ruta y el set de celdas visitados
    - ordene las conexiones de las celdas cuando ordenar_conexiones sea igual a True
    """
    visitados = set()
    stack = [inicio]

    while len(stack) > 0:
        celda = stack.pop()
        if celda in visitados:
            continue
        visitados.add(celda)

        conexiones = celda.conexiones
        for vecino in conexiones:
            if vecino not in visitados:
                stack.append(vecino)

    return [], set()
    

def buscar_bfs(inicio: Celda, fin: Celda) -> tuple[list[Celda], set[Celda]]:
    """
    TODO: Altera el método de BFS para que:
    - termine al encontrar la celda "fin"
    - reconstruya la ruta de inicio a fin usando reconstruir_ruta
    - retorne la ruta y el set de celdas visitadas
    """
    visitados = set()
    queue = deque([inicio])

    while len(queue) > 0:
        celda = queue.popleft()
        if celda in visitados:
            continue
        visitados.add(celda)
        
        for vecino in celda.conexiones:
            if vecino not in visitados:
                queue.append(vecino)

    return [], set()
    

if __name__ == "__main__":
    laberinto = Laberinto(30, 30, 0.5)
    inicio = laberinto.obtener_celda(29, 29)
    fin = laberinto.obtener_celda(0, 0)
    laberinto.imprimir_laberinto()

    ##### DFS
    camino_ordenando, visitados_ordenando = buscar_dfs(inicio, fin, ordernar_conexiones = True)

    print("DFS ordenando:")
    print(f"Largo del camino {len(camino_ordenando)}")
    print(f"Celdas visitadas {len(visitados_ordenando)}")
    print("\n")

    camino_sin_ordenar, visitados_sin_ordenar = buscar_dfs(inicio, fin, ordernar_conexiones = False)

    print("DFS sin ordenar:")
    print(f"Largo del camino {len(camino_sin_ordenar)}")
    print(f"Celdas visitadas {len(visitados_sin_ordenar)}")
    print("\n")

    ##### BSF
    camino, visitados = buscar_bfs(inicio, fin)

    print("BFS")
    print(f"Largo del camino {len(camino)}")
    print(f"Celdas visitadas {len(visitados)}")