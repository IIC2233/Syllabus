import funciones
import unittest

from os import remove
from typing import Generator
from utilidades import Pelicula


class TestCargarDatos(unittest.TestCase):
    '''
    Test orientado a comprobar las funciones:
    - cargar_peliculas
    - cargar_generos
    '''

    data_peliculas = [
        # peliculas_1.csv
        'id,titulo,director,año_estreno,rating_promedio\n'
        '20,The Social Network,David Fincher,2010,7.7',
        # peliculas_2.csv
        'id,titulo,director,año_estreno,rating_promedio\n'
        '14,The Lion King,Roger Allers,1994,8.5\n'
        '15,The Avengers,Joss Whedon,2012,8.0\n'
        '16,Interstellar,Christopher Nolan,2014,8.6\n'
        '17,Gone with the Wind,Victor Fleming,1939,8.1\n'
        '18,Casablanca,Michael Curtiz,1942,8.5\n'
        '19,The Great Gatsby,Baz Luhrmann,2013,7.2',
        # peliculas_3.csv
        'id,titulo,director,año_estreno,rating_promedio\n'
        '7,The Matrix,Lana Wachowski,1999,8.7\n'
        '8,Goodfellas,Martin Scorsese,1990,8.7\n'
        '9,Schindler\'s List,Steven Spielberg,1993,8.9',
        # peliculas_4.csv
        'id,titulo,director,año_estreno,rating_promedio\n'
        '1,The Shawshank Redemption,Frank Darabont,1994,9.3\n'
        '2,The Godfather,Francis Ford Coppola,1972,9.2\n'
        '3,Pulp Fiction,Quentin Tarantino,1994,8.9\n'
        '4,The Dark Knight,Christopher Nolan,2008,9.0\n'
        '5,Fight Club,David Fincher,1999,8.8\n'
        '6,Inception,Christopher Nolan,2010,8.8\n'
        '10,Forrest Gump,Robert Zemeckis,1994,8.8\n'
        '11,The Silence of the Lambs,Jonathan Demme,1991,8.6\n'
        '12,The Lord of the Rings: The Fellowship of the Ring,Peter Jackson,2001,8.8\n'
        '13,The Departed,Martin Scorsese,2006,8.5'
    ]

    @classmethod
    def setUpClass(cls):
        '''
        Al inicio de la ejecución de los tests se crean los archivos
        necesarios para comprobar las función que cargan datos.
        '''

        for i, data in enumerate(cls.data_peliculas):
            with open(f'peliculas_{i + 1}.csv', 'w', encoding="UTF-8") as file:
                file.write(data)

    @classmethod
    def tearDownClass(cls):
        '''
        Al finalizar la ejecución de los tests se eliminan
        los archivos creados anteriormente.
        '''

        for i in range(len(cls.data_peliculas)):
            remove(f'peliculas_{i + 1}.csv')

    def test_cargar_peliculas_1(self):
        '''
        Se comprueba que la función "cargar_peliculas" cargue correctamente
        las peliculas del archivo "peliculas_1.csv". Se puede revisar el contenido
        del archivo en el atributo de clase "data_peliculas".
        '''

        datos = funciones.cargar_peliculas('peliculas_1.csv')

        # Verificar tipo de dato pedido
        self.assertIsInstance(datos, Generator)
        lista_datos = list(datos)

        # Verificar resultados
        pelicula = Pelicula(20, 'The Social Network', 'David Fincher', 2010, 7.7)
        self.assertSequenceEqual(lista_datos[0], pelicula)
        self.assertSequenceEqual(lista_datos[-1], pelicula)

    def test_cargar_peliculas_2(self):
        '''
        Se comprueba que la función "cargar_peliculas" cargue correctamente
        las películas del archivo "peliculas_2.csv". Se puede revisar el contenido
        del archivo en el atributo de clase "data_peliculas".
        '''

        datos = funciones.cargar_peliculas('peliculas_2.csv')

        # Verificar tipo de dato pedido
        self.assertIsInstance(datos, Generator)
        lista_datos = list(datos)

        # Verificar resultados
        pelicula_1 = Pelicula(14, 'The Lion King', 'Roger Allers', 1994, 8.5)
        pelicula_2 = Pelicula(15, 'The Avengers', 'Joss Whedon', 2012, 8.0)
        pelicula_3 = Pelicula(16, 'Interstellar', 'Christopher Nolan', 2014, 8.6)
        pelicula_4 = Pelicula(17, 'Gone with the Wind', 'Victor Fleming', 1939, 8.1)
        pelicula_5 = Pelicula(18, 'Casablanca', 'Michael Curtiz', 1942, 8.5)
        pelicula_6 = Pelicula(19, 'The Great Gatsby', 'Baz Luhrmann', 2013, 7.2)
        self.assertSequenceEqual(lista_datos[0], pelicula_1)
        self.assertSequenceEqual(lista_datos[1], pelicula_2)
        self.assertSequenceEqual(lista_datos[2], pelicula_3)
        self.assertSequenceEqual(lista_datos[3], pelicula_4)
        self.assertSequenceEqual(lista_datos[4], pelicula_5)
        self.assertSequenceEqual(lista_datos[5], pelicula_6)

    def test_cargar_peliculas_3(self):
        '''
        Se comprueba que la función "cargar_peliculas" cargue correctamente
        las películas del archivo "peliculas_3.csv". Se puede revisar el contenido
        del archivo en el atributo de clase "data_peliculas".
        '''

        datos = funciones.cargar_peliculas('peliculas_3.csv')

        # Verificar tipo de dato pedido
        self.assertIsInstance(datos, Generator)
        lista_datos = list(datos)

        # Verificar resultados
        pelicula_1 = Pelicula(7, 'The Matrix', 'Lana Wachowski', 1999, 8.7)
        pelicula_2 = Pelicula(8, 'Goodfellas', 'Martin Scorsese', 1990, 8.7)
        pelicula_3 = Pelicula(9, 'Schindler\'s List', 'Steven Spielberg', 1993, 8.9)
        self.assertSequenceEqual(lista_datos[0], pelicula_1)
        self.assertSequenceEqual(lista_datos[1], pelicula_2)
        self.assertSequenceEqual(lista_datos[2], pelicula_3)

    def test_cargar_peliculas_4(self):
        '''
        Se comprueba que la función "cargar_peliculas" cargue correctamente
        las películas del archivo "peliculas_4.csv". Se puede revisar el contenido
        del archivo en el atributo de clase "data_peliculas".
        '''

        datos = funciones.cargar_peliculas('peliculas_4.csv')

        # Verificar tipo de dato pedido
        self.assertIsInstance(datos, Generator)
        lista_datos = list(datos)

        # Verificar resultados
        pelicula_2 = Pelicula(2, 'The Godfather', 'Francis Ford Coppola', 1972, 9.2)
        pelicula_13 = Pelicula(13, 'The Departed', 'Martin Scorsese', 2006, 8.5)
        self.assertSequenceEqual(lista_datos[1], pelicula_2)
        self.assertSequenceEqual(lista_datos[-1], pelicula_13)
