from functools import reduce
from itertools import product
from typing import Generator

from utilidades import Pelicula, Genero


# ----------------------------------------------------------------------------
# Parte I: Cargar dataset
# ----------------------------------------------------------------------------

def cargar_peliculas(ruta: str) -> Generator:
    pass


# ----------------------------------------------------------------------------
# Parte II: Consultas sobre generadores
# ----------------------------------------------------------------------------


def obtener_directores(generador_peliculas: Generator) -> Generator:
    """
    Retorna un generador con el nombre de todos los directores.
    """
    return "COMPLETAR"


def obtener_str_titulos(generador_peliculas: Generator) -> str:
    """
    Genera un str con todos los títulos de las películas separados por ", ".
    """
    return "COMPLETAR"


def filtrar_peliculas(
    generador_peliculas: Generator,
    director: str | None = None,
    rating_min: float | None = None,
    rating_max: float | None = None,
) -> filter:
    """
    Filtra los elementos del generador de Películas según lo indicado en el input.
    """
    return "COMPLETAR"


def filtrar_titulos(
    generador_peliculas: Generator,
    director: str,
    rating_min: float,
    rating_max: float
) -> Generator:
    """
    Genera un str con todos los títulos de las películas separados
    por ", ". Solo se consideran las películas que tengan el mismo
    director que el indicado, tengan un rating igual o mayor al
    rating_min y un rating igual o menor al rating_max.
    """
    return "COMPLETAR"


def filtrar_peliculas_por_genero(
    generador_peliculas: Generator,
    generador_generos: Generator,
    genero: str | None = None,
) -> Generator:
    """
    Crea un generador con todas las combinaciones posibles entre
    el generador de películas y el generador de géneros.
    Después, filtra las pares obtenidos y mantiene únicamente
    los que presentan el mismo id de película.
    Finalmente, retorna una lista con todos los pares pertenecientes
    a la categoría indicada.
    """
    return "COMPLETAR"
