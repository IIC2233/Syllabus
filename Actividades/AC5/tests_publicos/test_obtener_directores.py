import unittest
import funciones

from typing import Generator
from utilidades import Pelicula
from tests_publicos.elementos_prohibidos import revisar_comandos_prohibidos


class TestObtenerDirectores(unittest.TestCase):

    def setUp(self):
        '''
        Función encargada de revisar que no se utilicen comandos prohibidos
        (while, for, list, dict, set, tuple) antes de ejecutar
        cada uno de los tests.
        '''
        revisar_comandos_prohibidos(funciones.obtener_directores)
        return super().setUp()

    def generador_peliculas(self, variacion):
        '''
        Función generadora que retorna distintas instancias de película.
        '''

        if variacion == 1:
            yield Pelicula(16, 'Interstelar', 'Christopher Nolan', 2014, 8.6)
        elif variacion == 2:
            yield Pelicula(8, 'Buenos muchachos', 'Martin Scorsese', 1990, 8.7)
            yield Pelicula(13, 'Los infiltrados', 'Martin Scorsese', 2006, 8.5)
        elif variacion == 3:
            yield Pelicula(5, 'El club de la pelea', 'David Fincher', 1999, 8.8)
            yield Pelicula(18, 'Casablanca', 'Michael Curtiz', 1942, 8.5)
            yield Pelicula(19, 'El Gran Gatsby', 'Baz Luhrmann', 2013, 7.2)
        elif variacion == 4:
            yield Pelicula(4, 'Batman: el caballero de la noche', 'Christopher Nolan', 2008, 9.0)
            yield Pelicula(17, 'Lo que el viento se llevo', 'Victor Fleming', 1939, 8.1)
            yield Pelicula(6, 'El origen', 'Christopher Nolan', 2010, 8.8)
            yield Pelicula(7, 'Matrix', 'Lana Wachowski', 1999, 8.7)
            yield Pelicula(5, 'El club de la pelea', 'David Fincher', 1999, 8.8)
            yield Pelicula(20, 'Red Social', 'David Fincher', 2010, 7.7)

    def test_obtener_directores_1(self):
        '''
        Se comprueba que la función "obtener_directores" obtenga correctamente un set
        con el nombre de los directores de las películas de la variación 1 (generador_peliculas).
        '''

        datos = funciones.obtener_directores(self.generador_peliculas(1))
        self.assertIsInstance(datos, (filter, map, Generator))

        self.assertCountEqual(list(datos), ['Christopher Nolan'])

    def test_obtener_directores_2(self):
        '''
        Se comprueba que la función "obtener_directores" obtenga correctamente un set
        con el nombre de los directores de las películas de la variación 2 (generador_peliculas).
        '''

        datos = funciones.obtener_directores(self.generador_peliculas(2))
        self.assertIsInstance(datos, (filter, map, Generator))

        lista_esperada = ['Martin Scorsese', 'Martin Scorsese']
        self.assertCountEqual(datos, lista_esperada)

    def test_obtener_directores_3(self):
        '''
        Se comprueba que la función "obtener_directores" obtenga correctamente un set
        con el nombre de los directores de las películas de la variación 3 (generador_peliculas).
        '''

        datos = funciones.obtener_directores(self.generador_peliculas(3))
        self.assertIsInstance(datos, (filter, map, Generator))

        lista_esperada = ['David Fincher', 'Michael Curtiz', 'Baz Luhrmann']
        self.assertCountEqual(list(datos), lista_esperada)

    def test_obtener_directores_4(self):
        '''
        Se comprueba que la función "obtener_directores" obtenga correctamente un set
        con el nombre de los directores de las películas de la variación 4 (generador_peliculas).
        '''

        datos = funciones.obtener_directores(self.generador_peliculas(4))
        self.assertIsInstance(datos, (filter, map, Generator))

        lista_esperada = ['Christopher Nolan', 'Victor Fleming', 'Christopher Nolan', 'Lana Wachowski', 'David Fincher', 'David Fincher']
        self.assertCountEqual(list(datos), lista_esperada)

    def test_obtener_directores_vacio(self):
        '''
        Se comprueba que la función "obtener_directores" cree correctamente un set vacío
        cuando no se le pasan películas.
        '''

        datos = funciones.obtener_directores(self.generador_peliculas(5))
        self.assertIsInstance(datos, (filter, map, Generator))

        self.assertCountEqual(list(datos), [])
