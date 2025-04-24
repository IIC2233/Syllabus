import unittest
import funciones

from utilidades import Pelicula
from tests_publicos.elementos_prohibidos import revisar_comandos_prohibidos


class TestFiltrarTitulos(unittest.TestCase):

    def setUp(self):
        '''
        Función encargada de revisar que no se utilicen comandos prohibidos
        (while, for, list, dict, set, tuple) antes de ejecutar
        cada uno de los tests.
        '''
        revisar_comandos_prohibidos(funciones.filtrar_titulos)
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

    def test_filtrar_titulo(self):
        '''
        Se comprueba que la función "filtrar_titulos" se aplique correctamente
        y luego retorne, como str, las películas que cumplen el filtro. Variación 1.
        '''

        respuesta = funciones.filtrar_titulos(self.generador_peliculas(1), 'David Fincher', 8, 9.0)
        self.assertIsInstance(respuesta, str)
        self.assertEqual(respuesta, 'Fight Club')

    def test_filtrar_titulo_1(self):
        '''
        Se comprueba que la función "filtrar_titulos" se aplique correctamente
        y luego retorne, como str, las películas que cumplen el filtro. Variación 2
        '''
        datos = funciones.filtrar_titulos(self.generador_peliculas(2), 'Christopher Nolan', 8.5, 9.2)
        self.assertIsInstance(datos, str)

        peliculas = ['The Dark Knight', 'Inception', 'Interstellar']
        self.assertCountEqual(datos.split(", "), peliculas)

    def test_filtrar_titulo_2(self):
        '''
        Se comprueba que la función "filtrar_titulos" se aplique correctamente
        y luego retorne, como str, las películas que cumplen el filtro. Variación 1
        '''

        respuesta = funciones.filtrar_titulos(self.generador_peliculas(1), 'David Fincher', 1, 7.7)
        self.assertIsInstance(respuesta, str)
        self.assertEqual(respuesta, 'The Social Network')

    def test_filtrar_titulo_3(self):
        '''
        Se comprueba que la función "filtrar_titulos" se aplique correctamente
        y luego retorne, como str, las películas que cumplen el filtro. Variación 2
        '''

        datos = funciones.filtrar_titulos(self.generador_peliculas(2), 'Martin Scorsese', 8.5, 9.0)
        self.assertIsInstance(datos, str)

        peliculas = ['Goodfellas', 'The Departed']
        self.assertCountEqual(datos.split(", "), peliculas)

    def test_filtrar_titulos_sin_peliculas(self):
        '''
        Se comprueba que la función "filtrar_titulos" retorne str vacio cuando no hay peliculas
        en el generador
        '''

        respuesta = funciones.filtrar_titulos(self.generador_peliculas(5), 'Lana Wachowski', 8.5, 9.0)
        self.assertIsInstance(respuesta, str)
        self.assertEqual(respuesta, '')

    def test_filtrar_titulos_filtro_vacio(self):
        '''
        Se comprueba que la función "filtrar_titulos" retorne str vacio cuando no
        queda ninguna película post filtrar.
        '''

        respuesta = funciones.filtrar_titulos(self.generador_peliculas(1), 'Lana Wachowski', 8.5, 9.0)
        self.assertIsInstance(respuesta, str)
        self.assertEqual(respuesta, '')
