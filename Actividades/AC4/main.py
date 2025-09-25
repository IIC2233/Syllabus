from typing import Any
import funciones as f

from os.path import join
from utilidades import (Genero, imprimir_peliculas,
                        imprimir_generos, imprimir_peliculas_genero)


def cargar_generos() -> f.Generator:
    yield Genero('fantasía', 1)
    yield Genero('aventura', 1)
    yield Genero('drama', 1)
    yield Genero('acción', 2)
    yield Genero('Sci-Fi', 2)
    yield Genero('romance', 3)
    yield Genero('drama', 3)
    yield Genero('fantasía', 4)
    yield Genero('familia', 4)
    yield Genero('drama', 5)
    yield Genero('guerra', 5)
    yield Genero('fantasía', 6)
    yield Genero('aventura', 6)
    yield Genero('acción', 6)
    yield Genero('thriller', 7)
    yield Genero('psicológico', 7)
    yield Genero('Sci-Fi', 8)
    yield Genero('thriller', 8)
    yield Genero('fantasía', 9)
    yield Genero('aventura', 9)
    yield Genero('Sci-Fi', 10)
    yield Genero('fantasía', 10)


if __name__ == '__main__':
    RUTA_PELICULAS = join("archivos", "peliculas.csv")

    print("> Cargar películas:")
    imprimir_peliculas(f.cargar_peliculas(RUTA_PELICULAS))
    print()

    print("> Cargar géneros")
    imprimir_generos(cargar_generos(), 5)
    print()

    print("> Obtener directores:")
    generador_peliculas = f.cargar_peliculas(RUTA_PELICULAS)
    print(list(f.obtener_directores(generador_peliculas)))
    print()

    print("> Obtener string títulos")
    generador_peliculas = f.cargar_peliculas(RUTA_PELICULAS)
    print(f.obtener_str_titulos(generador_peliculas))
    print()

    print("> Filtrar películas (director=Hayao Miyazaki):")
    generador_peliculas = f.cargar_peliculas(RUTA_PELICULAS)
    imprimir_peliculas(
        f.filtrar_peliculas(generador_peliculas, director="Hayao Miyazaki")
    )
    print("\n> Filtrar películas (rating_min=8.1):")
    generador_peliculas = f.cargar_peliculas(RUTA_PELICULAS)
    imprimir_peliculas(f.filtrar_peliculas(generador_peliculas, rating_min=8.1))

    print("\n> Filtrar películas (rating_max=8.7):")
    generador_peliculas = f.cargar_peliculas(RUTA_PELICULAS)
    imprimir_peliculas(f.filtrar_peliculas(generador_peliculas, rating_max=8.7))
    print()

    print("\n> Filtrar películas (Hayao Miyazaki, rating_min=8.1, rating_max=8.7):")
    generador_peliculas = f.cargar_peliculas(RUTA_PELICULAS)
    imprimir_peliculas(f.filtrar_peliculas(generador_peliculas,
                                           director="Hayao Miyazaki",
                                           rating_min=8.1,
                                           rating_max=8.7))
    print()

    print("> Filtrar títulos (Hayao Miyazaki, rating_min=8.1, rating_max=8.7)")
    generador_peliculas = f.cargar_peliculas(RUTA_PELICULAS)
    print(f.filtrar_titulos(generador_peliculas, "Hayao Miyazaki", 8.1, 8.7))

    print("> Filtrar películas por género (fantasía)")
    generador_peliculas = f.cargar_peliculas(RUTA_PELICULAS)
    generador_generos = cargar_generos()
    imprimir_peliculas_genero(
        f.filtrar_peliculas_por_genero(
            generador_peliculas, generador_generos, "fantasía"
        )
    )
    print()
