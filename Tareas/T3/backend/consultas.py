from typing import Generator, List, Tuple
from math import pi
from itertools import groupby, tee

from utilidades import (
    Astronauta,
    Nave,
    Tripulacion,
    Planeta,
    Mineral,
    PlanetaMineral,
    Mision,
    MisionMineral,
    radio_planeta
)


# Cargas 

def cargar_astronautas(path: str) -> Generator[Astronauta, None, None]:
    pass


def cargar_naves(path: str) -> Generator[Nave, None, None]:
    pass


def cargar_tripulaciones(path: str) -> Generator[Tripulacion, None, None]:
    pass


def cargar_planetas(path: str) -> Generator[Planeta, None, None]:
    pass


def cargar_minerales(path: str) -> Generator[Mineral, None, None]:
    pass


def cargar_planeta_minerales(path: str) -> Generator[PlanetaMineral, None, None]:
    pass


def cargar_mision(path: str) -> Generator[Mision, None, None]:
    pass


def cargar_materiales_mision(path: str) -> Generator[MisionMineral, None, None]:
    pass


# Consultas 1 generador

def naves_de_material(generador_naves: Generator[Nave, None, None], material: str) -> Generator[Nave, None, None]:
    pass


def misiones_desde_fecha(generador_misiones: Generator[Mision, None, None], fecha: str, inverso: bool) -> Generator[Mision, None, None]:
    pass


def naves_por_intervalo_carga(generador_naves: Generator[Nave, None, None], cargas: tuple[float, float]) -> Generator[Nave, None, None]:
    pass


def planetas_con_cantidad_de_minerales(generador_planeta_mineral: Generator[PlanetaMineral, None, None], id_mineral: int, cantidad_minima: int) -> List[int]:
    pass


def naves_astronautas_rango(generador_tripulacion: Generator[Tripulacion, None, None], rango: int, 
                            minimo_astronautas: int) -> Generator[Tuple[str, Generator], None, None]:
    pass


def cambiar_rango_astronauta(generador_tripulacion: Generator[Tripulacion, None, None], id_astronauta: int, rango_astronauta: int) -> Generator[Tripulacion, None, None]:
    pass


def encontrar_planetas_cercanos(generador_planetas: Generator[Planeta, None, None], x1: int, 
                                y1: int, x2: int, y2: int, cantidad: int | None = None) -> Generator[Planeta, None, None]:
    pass
 

# Consultas 2 generadores

def disponibilidad_por_planeta(generador_planeta_mineral: Generator[PlanetaMineral, None, None],
                               generador_planetas: Generator[Planeta, None, None], id_mineral: int) -> Generator[Tuple[str, int, float], None, None]:
    pass


def misiones_por_tipo_planeta(generador_misiones: Generator[Mision, None, None],
                              generador_planetas: Generator[Planeta, None, None], tipo: str) -> Generator[Mision, None, None]:
    pass


def naves_pueden_llevar(generador_naves: Generator[Nave, None, None], generador_planeta_mineral: Generator[PlanetaMineral, None, None], 
                        id_planeta: int) -> Generator[tuple[str, int, float], None, None]:
    pass
    

# Consultas 3 generadores

def planetas_por_estadisticas(generador_mineral: Generator[Mineral, None, None], generador_planeta_mineral: Generator[PlanetaMineral, None, None], 
                              generador_planeta: Generator[Planeta, None, None], moles_elemento_min: float, 
                              concentracion_molar_min: float, densidad_min: float) -> Generator[Planeta, None, None]:
    pass

def ganancias_potenciales_por_planeta(generador_minerales: Generator[Mineral, None, None], generador_planeta_mineral: Generator[PlanetaMineral, None, None], 
                                      generador_planetas: Generator[Planeta, None, None], precios: dict) -> dict:
    pass


def planetas_visitados_por_nave(generador_planetas: Generator[Planeta, None, None], generador_misiones: Generator[Mision, None, None], 
                                generador_tripulaciones: Generator[Tripulacion, None, None]) -> Generator[Tuple[str, str|None, int|None], None, None]:
    pass


def mineral_por_nave(generador_tripulaciones: Generator[Tripulacion, None, None], generador_misiones: Generator[Mision, None, None], 
                     generador_misiones_mineral: Generator[MisionMineral, None, None]) -> Generator[Tuple[str, float], None, None]:
    pass


def porcentaje_extraccion(generador_tripulacion: Generator[Tripulacion, None, None], generador_mision_mineral: Generator[MisionMineral, None, None], 
                          generador_planeta_mineral: Generator[PlanetaMineral, None, None], mision : Mision) -> Tuple[float, float]:
    pass


# Consultas 4 generadores

def resultado_mision(mision: Mision, generador_naves: Generator[Nave, None, None], generador_planeta_mineral: Generator[PlanetaMineral, None, None],
                     generador_tripulaciones: Generator[Tripulacion, None, None], generador_mision_mineral: Generator[MisionMineral, None, None]) -> Mision:
    pass
