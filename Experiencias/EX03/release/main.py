import re
import pandas as pd

from collections import deque
from functools import reduce


def interpretar_archivo_regex(path_archivo: str) -> list[dict]:
    '''
    Lee el contenido del archivo entregado, distingue los elementos de
    cada fila utilizando de regex y grupos de captura: id_gasto, monto, fecha.
    Retorna una lista de diccionarios con los 3 campos mencionados.
    '''
    # TODO: Parte I
    patron_id_gasto = r''
    patron_monto = r''
    patron_fecha = r''

    patron_fila = fr'({patron_id_gasto}|{patron_monto}|{patron_fecha}|;)+'

    info_archivo = []

    with open(path_archivo, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            # TODO: Parte I
            pass

    return info_archivo


def cargar_gastos(path_archivo: str) -> pd.DataFrame:
    '''
    Lee el contenido del archivo entregado y lo transforma en un
    DataFrame compuesto de 3 campos: id_gasto, monto, fecha
    '''
    info_archivo = interpretar_archivo_regex(path_archivo)

    # TODO: Parte II.a y II.d


def cargar_categorias(path_archivo: str) -> pd.DataFrame:
    '''
    Carga la información del archivo entregado y
    lo retorna como un DataFrame.
    '''
    # TODO: Parte II.b


def combinar_gastos_categorias(df_gastos: pd.DataFrame,
                               df_categorias: pd.DataFrame) -> pd.DataFrame:

    '''
    Retorna un DataFrame que contiene la información del DF de transacciones y
    el DF de categorías. Estos dos DF se asocian por medio del atributo "id_gasto".
    '''
    # El método "merge" nos permite combinar 2 DataFrames en 1, utilizando una
    # columna en común en común para asociar ambos DF.
    df = df_gastos.merge(df_categorias, on='id_gasto')
    return df


def describir_informacion(df: pd.DataFrame) -> None:
    '''
    Recibe un DataFrame y describimos su información.
    '''
    # TODO: Parte II.d


def crear_grafo_categorias(df: pd.DataFrame) -> dict[list]:
    '''
    A partir de la columna de "categorias" crea un grafo
    que une las distintas categorías y sub-categorías.
    NOTESE: Este es un grafo direccional.
    '''
    # TODO: Parte III.a

    for item_categorias in df['categorias']:
        categorias = item_categorias.split('>')

        pass



def recorrer_dfs(grafo: dict[list], nodo_inicial: str) -> None:
    '''
    Recorre el grafo utilizando la búsqueda por profundidad.
    '''
    visitados = set()
    pendientes = "Completar"  # TODO: Parte III.b

    while pendientes:
        nodo_actual = "Completar"  # TODO: Parte III.b

        if nodo_actual not in visitados:
            # Agregamos el nodo_actual al set de visitados.
            visitados.add(nodo_actual)
            # Agregamos sus vecinos a la lista de pendientes.
            vecinos_actuales = grafo[nodo_actual]
            pendientes += vecinos_actuales

        print('->', nodo_actual, end=' ')


def recorrer_bfs(grafo: dict[list], nodo_inicial: str) -> None:
    '''
    Recorre el grafo utilizando la búsqueda por amplitud.
    '''
    visitados = set()
    pendientes = "Completar"  # TODO: Parte III.b

    while pendientes:
        nodo_actual = "Completar"  # TODO: Parte III.b

        if nodo_actual not in visitados:
            # Agregamos el nodo_actual al set de visitados.
            visitados.add(nodo_actual)
            # Agregamos sus vecinos a la lista de pendientes.
            vecinos_actuales = grafo[nodo_actual]
            pendientes += vecinos_actuales

        print('->', nodo_actual, end=' ')



if __name__ == '__main__':
    path_gastos = 'gastos.csv'
    path_categorias = 'categorias.csv'

    print('Parte I: Interpretar archivo transacciones')
    input('Aprieta ENTER para continuar')
    print(interpretar_archivo_regex(path_gastos)[:3])

    print('\nParte II: Cargar la información')
    input('Aprieta ENTER para cargar las transacciones')
    df_gastos = cargar_gastos(path_gastos)
    print(df_gastos.head())

    print()
    input('Aprieta ENTER para cargar las categorías')
    df_categorias = cargar_categorias(path_categorias)
    print(df_categorias.head())

    print('\nParte II: Juntar la información')
    input('Aprieta ENTER para combinar ambos DataFrames')
    df_total = combinar_gastos_categorias(df_gastos, df_categorias)
    print(df_total.head())

    print('\nParte II: Describir información')
    input('Aprieta ENTER para continuar')
    describir_informacion(df_total)

    print('\nParte III: Crear grafo de categorias')
    input('Aprieta ENTER para continuar')
    grafo_categorias = crear_grafo_categorias(df_total)
    print(grafo_categorias)

    print('\nParte III: Recorrer grafo de categorias')
    input('Aprieta ENTER para recorrer con alg. DFS')
    recorrer_dfs(grafo_categorias, 'Categoria')

    print()
    input('Aprieta ENTER para recorrer con alg. BFS')
    recorrer_bfs(grafo_categorias, 'Categoria')
