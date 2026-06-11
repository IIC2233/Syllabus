import pandas as pd

from busqueda import buscar_dfs, buscar_bfs
from laberinto import Laberinto
from collections import namedtuple

# namestuple que indica el input de un experimento
Experimento = namedtuple("Experimento", ["alto", "ancho", "redundancia", "repeticiones"])

def correr_experimento(experimento: Experimento) -> pd.DataFrame:
    """
    TODO: Debes utilizar los parámetros del experimento
    para correr dfs las veces que se te indica y retornar
    un dataframe con los resultados.
    Las columnas del dataframe deben ser:
    - redundancia
    - visitados_ordenado
    - visitados_sin_ordenar
    - visitados_bfs
    - largo_ordenado
    - largo_sin_ordenar
    - largo_bfs
    y debe haber una fila por cada repetición del experimento
    """
    return pd.DataFrame([])

def normalizar_datos(datos: pd.DataFrame) -> None:
    """
    TODO: Agrega columnas normalizadas al dataframe dividiendo los resultados
    de nodos visitados y largo de ruta con respecto a lo obtenido por BFS.
    Nombras la nuevas columnas:
    - norm_visitados_ordenado
    - norm_visitados_sin_ordenar
    - norm_largo_ordenado
    - norm_largo_sin_ordenar
    """

if __name__ == "__main__":
    alto = 20
    ancho = 20
    redundancias = [0, 0.2, 0.4, 0.6, 0.8]
    repeticiones = 10

    dataframes = []
    for redundancia in redundancias:
        experimento = Experimento(
            alto,
            ancho,
            redundancia,
            repeticiones
        )
        dataframes.append(correr_experimento(experimento))

    resultados = pd.concat(dataframes, ignore_index=True)
    normalizar_datos(resultados)

    print(resultados.groupby("redundancia")[[
        "norm_visitados_ordenado",
        "norm_visitados_sin_ordenar",
        "norm_largo_ordenado",
        "norm_largo_sin_ordenar"
    ]].mean())