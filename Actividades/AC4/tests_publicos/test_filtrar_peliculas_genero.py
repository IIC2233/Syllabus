import unittest
import funciones

from utilidades import Pelicula, Genero
from tests_publicos.elementos_prohibidos import revisar_comandos_prohibidos


class TestFiltrarPeliculasGenero(unittest.TestCase):

    def setUp(self):
        '''
        Función encargada de revisar que no se utilicen comandos prohibidos
        (while, for, list, dict, set, tuple) antes de ejecutar
        cada uno de los tests.
        '''
        revisar_comandos_prohibidos(funciones.filtrar_peliculas_por_genero)
        return super().setUp()

    def generador_peliculas(self, variacion):
        '''
        Función generadora que retorna distintas instancias de película.
        '''

        if variacion == 1:
            yield Pelicula(5, 'Fight Club', 'David Fincher', 1999, 8.8)
            yield Pelicula(20, 'The Social Network', 'David Fincher', 2010, 7.7)
        elif variacion == 2:
            yield Pelicula(4, 'The Dark Knight', 'Christopher Nolan', 2008, 9.0)
            yield Pelicula(5, 'Fight Club', 'David Fincher', 1999, 8.8)
            yield Pelicula(6, 'Inception', 'Christopher Nolan', 2010, 8.8)
            yield Pelicula(7, 'The Matrix', 'Lana Wachowski', 1999, 8.7)
            yield Pelicula(8, 'Goodfellas', 'Martin Scorsese', 1990, 8.7)
            yield Pelicula(13, 'The Departed', 'Martin Scorsese', 2006, 8.5)
            yield Pelicula(16, 'Interstellar', 'Christopher Nolan', 2014, 8.6)
            yield Pelicula(21, 'The Wolf of Wall Street', 'Martin Scorsese', 2013, 8.2)
        elif variacion == 3:
            yield Pelicula(13, 'The Departed', 'Martin Scorsese', 2006, 8.5)
            yield Pelicula(16, 'Interstellar', 'Christopher Nolan', 2014, 8.6)
            yield Pelicula(21, 'The Wolf of Wall Street', 'Martin Scorsese', 2013, 8.2)

    def generador_generos(self, variacion):
        '''
        Función generadora que retorna distintas instancias de genero.
        '''

        if variacion == 1:
            yield Genero('Drama', 5)
            yield Genero('Drama', 20)
        elif variacion == 2:
            yield Genero('Action', 4)
            yield Genero('Drama', 4)
            yield Genero('Crime', 4)
            yield Genero('Drama', 5)
            yield Genero('Action', 6)
            yield Genero('Drama', 6)
            yield Genero('Action', 7)
            yield Genero('Sci-Fi', 7)
            yield Genero('Biography', 8)
            yield Genero('Crime', 8)
            yield Genero('Drama', 8)
            yield Genero('Crime', 13)
            yield Genero('Drama', 13)
            yield Genero('Adventure', 16)
            yield Genero('Drama', 16)
            yield Genero('Sci-Fi', 16)
            yield Genero('Comedy', 21)
            yield Genero('Crime', 21)
            yield Genero('Drama', 21)
        elif variacion == 3:
            yield Genero('Action', 4)
            yield Genero('Drama', 5)
            yield Genero('Sci-Fi', 7)
            yield Genero('Biography', 8)

    def test_filtrar_por_genero_1(self):
        '''
        Se comprueba que la función "filtrar_peliculas_por_genero" obtiene y filtrar
        los pares película-genero, cuando se le entrega un genero de película.
        Se utilizan las películas de la variación 1 (generador_peliculas) y los generos
        de la variación 1 (generador_generos).
        '''

        datos = funciones.filtrar_peliculas_por_genero(self.generador_peliculas(1), self.generador_generos(1), 'Drama')
        resultado_esperado = [
            (Pelicula(5, 'Fight Club', 'David Fincher', 1999, 8.8), Genero('Drama', 5)),
            (Pelicula(20, 'The Social Network', 'David Fincher', 2010, 7.7), Genero('Drama', 20))
        ]
        self.assertSequenceEqual(list(datos), resultado_esperado)

    def test_filtrar_por_genero_2(self):
        '''
        Se comprueba que la función "filtrar_peliculas_por_genero" obtiene y filtrar
        los pares película-genero, cuando se le entrega un genero de película.
        Se utilizan las películas de la variación 2 (generador_peliculas) y los generos
        de la variación 2 (generador_generos).
        '''

        datos = funciones.filtrar_peliculas_por_genero(self.generador_peliculas(2), self.generador_generos(2), 'Comedy')
        resultado_esperado = [
            (Pelicula(21, 'The Wolf of Wall Street', 'Martin Scorsese', 2013, 8.2), Genero('Comedy', 21))
        ]
        self.assertSequenceEqual(list(datos), resultado_esperado)

    def test_filtrar_por_genero_none(self):
        '''
        Se comprueba que la función "filtrar_peliculas_por_genero" obtiene y filtrar
        los pares película-genero, cuando no se entrega un genero de película.
        Se utilizan las películas de la variación 2 (generador_peliculas) y los generos
        de la variación 3 (generador_generos).
        '''

        datos = funciones.filtrar_peliculas_por_genero(self.generador_peliculas(2), self.generador_generos(3))
        resultado_esperado = [
            (Pelicula(4, 'The Dark Knight', 'Christopher Nolan', 2008, 9.0), Genero('Action', 4)),
            (Pelicula(5, 'Fight Club', 'David Fincher', 1999, 8.8), Genero('Drama', 5)),
            (Pelicula(7, 'The Matrix', 'Lana Wachowski', 1999, 8.7), Genero('Sci-Fi', 7)),
            (Pelicula(8, 'Goodfellas', 'Martin Scorsese', 1990, 8.7), Genero('Biography', 8))
        ]
        self.assertSequenceEqual(list(datos), resultado_esperado)

    def test_filtrar_por_genero_vacio_1(self):
        '''
        Se comprueba que la función "filtrar_peliculas_por_genero" retorna vacío,
        cuando no hay películas del genero indicado.
        Se utilizan las películas de la variación 1 (generador_peliculas) y los generos
        de la variación 1 (generador_generos).
        '''

        datos = funciones.filtrar_peliculas_por_genero(self.generador_peliculas(1), self.generador_generos(1), 'Comedy')
        self.assertSequenceEqual(list(datos), [])

    def test_filtrar_por_genero_vacio_2(self):
        '''
        Se comprueba que la función "filtrar_peliculas_por_genero" retorna vacío,
        cuando los generadores de películas y generos no tiene pares con el mismo id.
        Se utilizan las películas de la variación 1 (generador_peliculas) y los generos
        de la variación 1 (generador_generos).
        '''

        datos = funciones.filtrar_peliculas_por_genero(self.generador_peliculas(3), self.generador_generos(3))
        self.assertSequenceEqual(list(datos), [])
