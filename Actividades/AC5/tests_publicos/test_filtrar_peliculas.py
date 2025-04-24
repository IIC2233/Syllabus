import unittest
import funciones

from typing import Generator
from utilidades import Pelicula
from tests_publicos.elementos_prohibidos import revisar_comandos_prohibidos


class TestFiltrarPeliculas(unittest.TestCase):

    def setUp(self):
        '''
        Función encargada de revisar que no se utilicen comandos prohibidos
        (while, for, list, dict, set, tuple) antes de ejecutar
        cada uno de los tests.
        '''
        revisar_comandos_prohibidos(funciones.filtrar_peliculas)
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

    def test_filtrar_peliculas_por_director(self):
        '''
        Se comprueba que la función "filtrar_peliculas" se aplique correctamente
        cuando solo se le entrega el nombre de un director. Se utilizan las películas
        de la variación 2 (generador_peliculas).
        '''

        datos = funciones.filtrar_peliculas(self.generador_peliculas(2), director='Christopher Nolan')
        peliculas = [
            Pelicula(4, 'The Dark Knight', 'Christopher Nolan', 2008, 9.0),
            Pelicula(6, 'Inception', 'Christopher Nolan', 2010, 8.8),
            Pelicula(16, 'Interstellar', 'Christopher Nolan', 2014, 8.6)
        ]
        self.assertIsInstance(datos, (filter, map, Generator))
        self.assertSequenceEqual(list(datos), peliculas)

    def test_filtrar_peliculas_por_rating_min(self):
        '''
        Se comprueba que la función "filtrar_peliculas" se aplique correctamente
        cuando solo se le entrega un rating mínimo. Se utilizan las películas
        de la variación 1 (generador_peliculas).
        '''

        datos = funciones.filtrar_peliculas(self.generador_peliculas(1), rating_min=8.0)
        peliculas = [
            Pelicula(5, 'Fight Club', 'David Fincher', 1999, 8.8)
        ]
        self.assertIsInstance(datos, (filter, map, Generator))
        self.assertSequenceEqual(list(datos), peliculas)

    def test_filtrar_peliculas_por_rating_max(self):
        '''
        Se comprueba que la función "filtrar_peliculas" se aplique correctamente
        cuando solo se le entrega un rating máximo. Se utilizan las películas
        de la variación 1 (generador_peliculas).
        '''

        datos = funciones.filtrar_peliculas(self.generador_peliculas(1), rating_max=7.7)
        peliculas = [
            Pelicula(20, 'The Social Network', 'David Fincher', 2010, 7.7)
        ]
        self.assertIsInstance(datos, (filter, map, Generator))
        self.assertSequenceEqual(list(datos), peliculas)

    def test_filtrar_peliculas_por_rating_max_y_min(self):
        '''
        Se comprueba que la función "filtrar_peliculas" se aplique correctamente
        cuando solo se le entrega un rating máximo y mínimo. Se utilizan las
        películas de la variación 2 (generador_peliculas).
        '''

        datos = funciones.filtrar_peliculas(self.generador_peliculas(2), rating_max=8.7, rating_min=8.6)
        peliculas = [
            Pelicula(7, 'The Matrix', 'Lana Wachowski', 1999, 8.7),
            Pelicula(8, 'Goodfellas', 'Martin Scorsese', 1990, 8.7),
            Pelicula(16, 'Interstellar', 'Christopher Nolan', 2014, 8.6),
        ]
        self.assertIsInstance(datos, (filter, map, Generator))
        self.assertSequenceEqual(list(datos), peliculas)

    def test_filtrar_peliculas_por_rating_max_y_director(self):
        '''
        Se comprueba que la función "filtrar_peliculas" se aplique correctamente
        cuando solo se le entrega un rating máximo y director. Se utilizan las
        películas de la variación 2 (generador_peliculas).
        '''

        datos = funciones.filtrar_peliculas(self.generador_peliculas(2), rating_max=8.4, director='Martin Scorsese')
        peliculas = [
            Pelicula(21, 'The Wolf of Wall Street', 'Martin Scorsese', 2013, 8.2)
        ]
        self.assertIsInstance(datos, (filter, map, Generator))
        self.assertSequenceEqual(list(datos), peliculas)

    def test_filtrar_peliculas_por_rating_min_y_director(self):
        '''
        Se comprueba que la función "filtrar_peliculas" se aplique correctamente
        cuando solo se le entrega un rating máximo y director. Se utilizan las
        películas de la variación 2 (generador_peliculas).
        '''

        datos = funciones.filtrar_peliculas(self.generador_peliculas(2), rating_min=8.4, director='Martin Scorsese')
        peliculas = [
            Pelicula(8, 'Goodfellas', 'Martin Scorsese', 1990, 8.7),
            Pelicula(13, 'The Departed', 'Martin Scorsese', 2006, 8.5),
        ]
        self.assertIsInstance(datos, (filter, map, Generator))
        self.assertSequenceEqual(list(datos), peliculas)

    def test_filtrar_peliculas_todo(self):
        '''
        Se comprueba que la función "filtrar_peliculas" se aplique correctamente
        cuando solo se le entrega el nombre de un director, un rating mínimo y un rating máximo.
        Se utilizan las películas de la variación 2 (generador_peliculas).
        '''

        datos = funciones.filtrar_peliculas(self.generador_peliculas(2), director='Martin Scorsese', rating_min=8.5, rating_max=9.0)
        peliculas = [
            Pelicula(8, 'Goodfellas', 'Martin Scorsese', 1990, 8.7),
            Pelicula(13, 'The Departed', 'Martin Scorsese', 2006, 8.5)
        ]
        self.assertIsInstance(datos, (filter, map, Generator))
        self.assertSequenceEqual(list(datos), peliculas)

    def test_filtrar_peliculas_vacio(self):
        '''
        Se comprueba que la función "filtrar_peliculas" se aplique correctamente
        y retorne vacío cuando corresponde. Se utilizan las películas de la
        variación 1 (generador_peliculas).
        '''

        datos = funciones.filtrar_peliculas(self.generador_peliculas(1), director='Lana Wachowski', rating_min=8.5, rating_max=9.0)
        self.assertIsInstance(datos, (filter, map, Generator))
        self.assertSequenceEqual(list(datos), [])
