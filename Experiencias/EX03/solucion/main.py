import re
import pandas as pd

from collections import deque
from functools import reduce


def interpretar_archivo_regex(path_archivo: str) -> list[dict]:
    '''
    Lee el contenido del archivo entregado, distingue los elementos de
    cada fila utilizando de regex y grupos de captura:
    - id_gasto: presenta 8 caracteres alfanuméricos
    - monto: empieza con el símbolo $ y presenta 1 o más dígitos
    - fecha: presenta el formato YYYY-MM-DD hh:mm
    Retorna una lista de diccionarios con los 3 campos mencionados.
    '''
    # TODO: Parte I
    # Definir regex con grupos de captura con nombre.
    patron_id_gasto = r'(?P<id_gasto>[a-zA-Z0-9]{8})'
    patron_monto = r'(?P<monto>\$\d+)'
    patron_fecha = r'(?P<fecha>\d{4}-\d{2}-\d{2} \d+:\d+)'

    # Juntar los 3 patrones en 1 gran patrón general.
    patron_fila = fr'({patron_id_gasto}|{patron_monto}|{patron_fecha}|;)+'

    info_archivo = []

    # Leer el archivo.
    with open(path_archivo, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            # TODO: Parte I
            # Clasificar los campos de cada línea y agregar el dict a la lista.
            match = re.fullmatch(patron_fila, linea.strip())
            info_linea = match.groupdict()
            info_archivo.append(info_linea)

    return info_archivo


def cargar_gastos(path_archivo: str) -> pd.DataFrame:
    '''
    Lee el contenido del archivo entregado y lo transforma en un
    DataFrame compuesto de 3 campos: id_gasto, monto, fecha.
    '''
    # Interpretamos el archivo.
    info_archivo = interpretar_archivo_regex(path_archivo)

    # TODO: Parte II.a
    # Generar el DataFrame.
    df = pd.DataFrame.from_dict(info_archivo)

    # TODO: Parte II.d
    # Actualizar valores.
    df['monto'] = df['monto'].str.replace('$', '').astype(int)
    df['fecha'] = pd.to_datetime(df['fecha'], format='%Y-%m-%d %H:%M')

    return df


def cargar_categorias(path_archivo: str) -> pd.DataFrame:
    '''
    Carga la información del archivo entregado y
    lo retorna como un DataFrame.
    '''
    # TODO: Parte II.b

    columnas = ['id_gasto', 'categorias']

    df = pd.read_csv(path_archivo, sep=';', encoding='utf-8',
                     names=columnas, header=None)
    return df


def combinar_gastos_categorias(df_gastos: pd.DataFrame,
                               df_categorias: pd.DataFrame) -> pd.DataFrame:

    '''
    Retorna un DataFrame que contiene la información del DF de transacciones y
    el DF de categorías. Estos dos DF se asocian por medio del atributo "id_gasto".
    '''
    # El método "merge" nos permite combinar 2 DataFrames en 1, utilizando una
    # columna en común en común para asociar ambos DF (argumento "on").
    df = df_gastos.merge(df_categorias, on='id_gasto')
    return df


def describir_informacion(df: pd.DataFrame) -> None:
    '''
    Recibe un DataFrame y describimos su información.
    '''
    # TODO: Parte II.d

    print('\nDimensiones:')
    print(df.shape)

    print('\nTipos de datos por columna:')
    print(df.dtypes)

    print('\nDescripción columnas numéricas:')
    print(df.describe())

    print('\nDescripción columnas categóricas (no numéricas):')
    print(df.describe(include=[object]))
    #     df.describe(exclude=[np.number])  # Operación equivalente.

    print('\nCategorías y sub-categorías')
    # Creamos una Serie con sets de categorías y sub-categorías.
    serie_categorias = df['categorias'].apply(lambda x: set(x.split('>')))

    # Opción 1: Los concatenamos usando la operación "union".
    total_categorias = set.union(*serie_categorias.tolist())

    # Opción 2: Utilizamos reduce y la operación "union" (|).
    total_categorias = reduce(lambda acc, c: acc | c, serie_categorias, set())

    # Opción 3: Iteramos sobre la Serie.
    total_categorias = set()
    for c in serie_categorias:
        total_categorias.update(c)

    print('- Cant. categorias:', len(total_categorias))
    print('- Valores:', total_categorias)


def crear_grafo_categorias(df: pd.DataFrame) -> dict[list]:
    '''
    A partir de la columna de "categorias" crea un grafo
    que une las distintas categorías y sub-categorías.
    NOTESE: Este es un grafo direccional.
    '''
    # TODO: Parte III.a
    lista_adyacencia = {}

    for item_categorias in df['categorias']:
        categorias = item_categorias.split('>')

        for i in range(len(categorias) - 1):
            # Obtenemos las categorias conectadas.
            nodo_actual = categorias[i]
            nodo_siguiente = categorias[i + 1]

            # Las agregamos al diccionario si no existen.
            if nodo_actual not in lista_adyacencia:
                lista_adyacencia[nodo_actual] = []
            if nodo_siguiente not in lista_adyacencia:
                lista_adyacencia[nodo_siguiente] = []

            # Generamos la conexión si no existe.
            if not nodo_siguiente in lista_adyacencia[nodo_actual]:
                lista_adyacencia[nodo_actual].append(nodo_siguiente)

    return lista_adyacencia


def recorrer_dfs(grafo: dict[list], nodo_inicial: str) -> None:
    '''
    Recorre el grafo utilizando la búsqueda por profundidad.
    '''
    # TODO: Parte III.b: Los pendientes son un stack.
    visitados = set()
    pendientes = [nodo_inicial]

    while pendientes:
        # TODO: Parte III.b: Obtenemos el último elemento del stack.
        nodo_actual = pendientes.pop(-1)

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
    # TODO: Parte III.b: Los pendientes son una cola.
    visitados = set()
    pendientes = deque([nodo_inicial])

    while pendientes:
        # TODO: Parte III.b: Obtenemos el primer elemento de la cola.
        nodo_actual = pendientes.popleft()

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

    print('\n')
    input('Aprieta ENTER para recorrer con alg. BFS')
    recorrer_bfs(grafo_categorias, 'Categoria')
