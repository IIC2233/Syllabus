from collections import namedtuple


Pelicula = namedtuple('Pelicula', 'id_pelicula, titulo, director, estreno, rating')
Genero = namedtuple('Genero', 'genero, id_pelicula')


def imprimir_peliculas(generador_peliculas, k=float('inf')):
    print(f'{"Título":^25} | {"Director":^20} | {"Año estreno":^11} | {"Rating promedio":^15}')
    print(f'{"-" * 25} | {"-" * 20} | {"-" * 11} | {"-" * 15}')
    for pelicula in generador_peliculas:
        print(f'{pelicula.titulo:<25} | {pelicula.director:<20} | {pelicula.estreno:>11} | {pelicula.rating:>15}')

        k -= 1
        if not k:
            print(f'{"⋮":^25}')
            return


def imprimir_generos(generador_generos, k=float('inf')):
    print(f'{"Género":^9} | {"ID Pelicula":^11}')
    print(f'{"-" * 9} | {"-" * 11}')
    for genero in generador_generos:
        print(f'{genero.genero:<9} | {genero.id_pelicula:>11}')

        k -= 1
        if not k:
            print(f'{"⋮":^9}')
            return


def imprimir_peliculas_genero(generador_peliculas_generos, k=float('inf')):
    print(f'{"Título":^25} | {"Director":^20} | {"Año estreno":^11} | {"Rating promedio":^15}\t{"Género":^9} | {"ID Pelicula":^11}')
    print(f'{"-" * 25} | {"-" * 20} | {"-" * 11} | {"-" * 15}\t{"-" * 9} | {"-" * 11}')
    for pelicula, genero in generador_peliculas_generos:
        print(f'{pelicula.titulo:<25} | {pelicula.director:<20} | {pelicula.estreno:>11} | {pelicula.rating:>15}\t{genero.genero:<9} | {genero.id_pelicula:>11}')

        k -= 1
        if not k:
            print(f'{"⋮":^25}')
            return
