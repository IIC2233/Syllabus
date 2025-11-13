from collections import defaultdict, deque
from typing import Optional

import pandas as pd
import re


def cargar_sismos(path_archivo: str) -> pd.DataFrame:
    '''
    Lee el contenido del archivo entregado y lo transforma en un
    DataFrame compuesto de 7 campos (Fecha y hora local, Magnitud Ms,
    Magnitud Mw, Profundidad, Efecto, Coordenadas, Ubicación), donde 
    - 'Fecha y hora local' es un objeto de tipo datetime
    - 'Ubicación' es una lista de strings
    '''
    # TODO: Parte I


def filtrar_sismos_magnitud(df: pd.DataFrame, magnitud: float,
                            operacion: Optional[str] = '>') -> pd.DataFrame:
    '''
    Recibe un DataFrame y filtra todos los sismos que su ``Magnitud Ms'' cumpla
    la magnitud y operación recibidas como input.
    '''
    # TODO: Parte II


def estadisticas_efectos(df: pd.DataFrame) -> pd.Series:
    '''
    Recibe un DataFrame y obtiene el porcentaje correspondiente a
    los distintos tipos de Efecto que puede tener un Sismo.
    '''
    # TODO: Parte II


def crear_grafo_ubicaciones(df: pd.DataFrame) -> dict[set]:
    '''
    Recibe un DataFrame y retorna un grafo formado a partir de
    la información contenida en la columna 'Ubicación'.
    '''
    # TODO: Parte III

def ubicacion_tuvo_sismo_mar(grafo: dict[set], ubicacion: str) -> bool:
    '''
    Recibe un grafo representado mediante un diccionario de adyacencia, y
    una ubicación correspondiente a uno de los nodos de dicho grafo.
    Retorna un booleano que indica si desde dicha ubicación ha presentado
    sismos en el mar.
    '''
    # TODO: Parte III


def limpiar_header_corrompido(header: str) -> str:
    '''
    Recibe un texto corrompido y elimina todos los elementos correspondiente a
    la corrupción. 
    '''
    # TODO: Parte IV


if __name__ == '__main__':
    path_sismos = 'sismos.csv'

    print('\nParte I: Cargar la información')
    df_sismos = cargar_sismos(path_sismos)
    print(df_sismos.head(5))

    print('\nParte II: Consultas Sismos')
    input('Aprieta ENTER para continuar')

    print('\nFiltrar Sismos por magnitud')
    print(filtrar_sismos_magnitud(df_sismos, 8.0, '>'))

    print('\nEstadísticas de los Efectos de los Sismos')
    print(estadisticas_efectos(df_sismos))

    print('\nParte III: Grafo de ubicaciones')
    input('Aprieta ENTER para continuar')

    print('\nGrafo')
    grafo_ubicaciones = crear_grafo_ubicaciones(df_sismos)
    print(grafo_ubicaciones)

    print('\nRevisar si ubicaciones han tenido Sismos en el Mar')
    input('Aprieta ENTER para continuar')
    print('Magallanes:', ubicacion_tuvo_sismo_mar(grafo_ubicaciones, 'Magallanes'))
    print('Tamarugal:', ubicacion_tuvo_sismo_mar(grafo_ubicaciones, 'Tamarugal'))
    print('Chile:', ubicacion_tuvo_sismo_mar(grafo_ubicaciones, 'Chile'))
    print('Metropolitana:', ubicacion_tuvo_sismo_mar(grafo_ubicaciones, 'Metropolitana'))


    print('\nParte IV: Repara el Header corrompido usando Regex')
    input('Aprieta ENTER para continuar')
    header_corrompido = '*+1Fe321chaKSNM234 y ho32%%&#$ra loc?#a432lOIJSN'
    header_reparado = limpiar_header_corrompido(header_corrompido)
    print('- Original:', header_corrompido)
    print('- Reparado:', header_reparado)
