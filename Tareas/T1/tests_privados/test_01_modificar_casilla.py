import os
import sys
import unittest
from tablero import Tablero
from tests_privados.timeout_function import timeout

sys.stdout = open(os.devnull, 'w')

N_SECOND = 10


class TestModificarCasilla(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_00_tablero_simple_deshabilitar(self):
        """
        Tablero de 2x5 deshabilitando una casilla extrema
        """

        tablero_estudiante = Tablero()
        tablero_estudiante.cargar_tablero("tablero3.txt")

        cambio_estudiante = tablero_estudiante.modificar_casilla(1, 4)
        estructura_estudiante = tablero_estudiante.tablero
        estructura_esperada = [
            ['1', '3', '4', '3', '1', '9'],
            ['1', '3', '5', '2', 'X1', '10'],
            ['.', '3', '.', '.', '1', '.']
            ]

        self.assertEqual(cambio_estudiante, True)
        self.assertListEqual(estructura_estudiante, estructura_esperada)

    @timeout(N_SECOND)
    def test_01_tablero_medio_dehabilitar_habilitar(self):
        """
        Tablero de 5x6, se dehabilita y habilita la misma casilla
        """

        tablero_estudiante = Tablero()
        tablero_estudiante.cargar_tablero("t1.txt")

        cambio_estudiante = tablero_estudiante.modificar_casilla(2, 3)
        cambio_estudiante2 = tablero_estudiante.modificar_casilla(2, 3)
        estructura_estudiante = tablero_estudiante.tablero
        estructura_esperada = [
                ["1", "2", "4", "3", "5", "6", "."],
                ["1", "2", "6", "3", "5", "6", "17"],
                ["1", "2", "4", "3", "5", "6", "32"],
                ["1", "2", "4", "3", "5", "6", "."],
                ["1", "2", "4", "3", "5", "6", "12"],
                [".", ".", "31", "41", ".", ".", "."]
            ]

        self.assertTrue(cambio_estudiante)
        self.assertTrue(cambio_estudiante2)
        self.assertListEqual(estructura_estudiante, estructura_esperada)

    @timeout(N_SECOND)
    def test_02_tablero_grande_deshabilitar_habilitar(self):
        """
        Tablero de 10x6, se deshabilitan dos y se vuelve a habilitar una
        """

        tablero_estudiante = Tablero()
        tablero_estudiante.cargar_tablero("t2.txt")
        cambio_estudiante1 = tablero_estudiante.modificar_casilla(3, 2)
        cambio_estudiante2 = tablero_estudiante.modificar_casilla(6, 4)
        cambio_estudiante3 = tablero_estudiante.modificar_casilla(3, 2)
        estructura_estudiante = tablero_estudiante.tablero
        estructura_esperada = [
            ['.', '7', '17', '2', '8', '6', '12'],
            ['5', '10', '8', '10', '14', '16', '.'],
            ['3', '13', '.', '13', '3', '4', '10'],
            ['16', '13', '5', '12', '5', '3', '.'],
            ['9', '11', '13', '11', '1', '13', '4'],
            ['14', '12', '16', '5', '3', '8', '7'],
            ['.', '9', '.', '.', 'X15', '16', '14'],
            ['.', '7', '4', '5', '.', '14', '16'],
            ['6', '.', '9', '2', '.', '.', '3'],
            ['16', '.', '7', '3', '3', '.', '.'],
            ['5', '9', '10', '15', '8', '.', "."]
            ]

        self.assertTrue(cambio_estudiante1)
        self.assertTrue(cambio_estudiante2)
        self.assertTrue(cambio_estudiante3)
        self.assertListEqual(estructura_estudiante, estructura_esperada)

    @timeout(N_SECOND)
    def test_03_tablero_simple_cambios_permitidos_y_no(self):
        """
        Tablero de 2x2, se pide un cambio permitido y uno del objetivo
        """

        tablero_estudiante = Tablero()
        tablero_estudiante.cargar_tablero("t3.txt")
        cambio_estudiante1 = tablero_estudiante.modificar_casilla(1, 2)
        cambio_estudiante2 = tablero_estudiante.modificar_casilla(1, 1)
        estructura_estudiante = tablero_estudiante.tablero
        estructura_esperada = [
            ['11', '14', '1'],
            ['16', 'X7', '.'],
            ['9', '5', "."]
        ]

        self.assertFalse(cambio_estudiante1)
        self.assertTrue(cambio_estudiante2)
        self.assertListEqual(estructura_estudiante, estructura_esperada)

    @timeout(N_SECOND)
    def test_04_tablero_medio_deshabilitar_todo(self):
        """
        Tablero de 3x2, se deshabilita todo
        """

        tablero_estudiante = Tablero()
        tablero_estudiante.cargar_tablero("tab2.txt")
        cambios = []

        for i in range(3):
            for j in range(2):
                cambio = tablero_estudiante.modificar_casilla(i, j)
                cambios.append(cambio)

        for cambio in cambios:
            self.assertTrue(cambio, "todos los cambios son validos :(")

        estructura_estudiante = tablero_estudiante.tablero
        estructura_esperada = [
            ['X1', 'X4', '4'],
            ['X4', 'X2', '6'],
            ['X2', 'X2', '4'],
            ['6', '.', '.']
            ]

        self.assertListEqual(estructura_estudiante, estructura_esperada)

    @timeout(N_SECOND)
    def test_05_medio_puntito(self):
        """
        Tablero de 4x6 se intenta modificar un "."
        """

        tablero_estudiante = Tablero()
        tablero_estudiante.cargar_tablero("tab9.txt")

        cambio_estudiante = tablero_estudiante.modificar_casilla(2, 3)
        estructura_estudiante = tablero_estudiante.tablero
        estructura_esperada = [
            ['5', '.', '3', '2', '4', '.', '7'],
            ['2', '4', '.', '1', '6', '2', '5'],
            ['.', '3', '7', '.', '1', '2', '4'],
            ['1', '.', '2', '3', '.', '5', '6'],
            ['3', '3', '5', '.', '5', '2', '.']
            ]

        self.assertFalse(cambio_estudiante)
        self.assertListEqual(estructura_estudiante, estructura_esperada)

    @timeout(N_SECOND)
    def test_06_tablero_simple_objetivo(self):
        """
        Tablero de 12x15 se intentan varios objetivos
        """

        tablero_estudiante = Tablero()
        tablero_estudiante.cargar_tablero("t5.txt")

        cambio_estudiante1 = tablero_estudiante.modificar_casilla(12, 4)
        cambio_estudiante2 = tablero_estudiante.modificar_casilla(12, 6)
        cambio_estudiante3 = tablero_estudiante.modificar_casilla(3, 15)

        estructura_estudiante = tablero_estudiante.tablero
        estructura_esperada = [
            ['13', '9', '.', '8', '9', '5', '8', '13', '15', '.', '.', '7', '11', '8', '8', '6'],
            ['.', '.', '4', '3', '5', '.', '7', '14', '.', '2', '1', '6', '.', '12', '8', '3'],
            ['14', '8', '3', '.', '.', '.', '17', '1', '.', '.', '3', '9', '.', '1', '.', '11'],
            ['5', '9', '.', '.', '10', '2', '8', '.', '.', '.', '.', '17', '9', '2', "7", '0'],
            ['4', '10', '6', '.', '.', '.', '7', '.', '.', '10', '2', '7', '9', '.', '2', '3'],
            ['12', '12', '7', '1', '8', '.', '.', '12', '3', '.', '5', '11', '12', '1', '.', '1'],
            ['4', '1', '16', '7', '.', '10', '3', '.', '13', '.', '15', '3', '1', '.', '.', '.'],
            ['16', '8', '8', '.', '7', '2', '9', '8', '.', '.', '12', '11', '10', '8', '16', '3'],
            ['2', '4', '7', '16', '1', '3', '4', '4', '4', '1', '1', '14', '6', '1', '.', '2'],
            ['.', '.', '17', '9', '.', '12', '2', '9', '1', '10', '13', '.', '1', '1', '.', '1'],
            ['10', '.', '8', '.', '5', '.', '10', '14', '12', '3', '2', '1', '16', '1', '.', '.'],
            ['.', '15', '5', '17', '8', '1', '9', '1', '5', '.', '.', '15', '11', '8', '4', '5'],
            ['.', '.', '.', '.', '1', '.', '15', '.', '.', '14', '.', '.', '8', '8', '.', "."]
        ]

        self.assertFalse(cambio_estudiante1)
        self.assertFalse(cambio_estudiante2)
        self.assertFalse(cambio_estudiante3)
        self.assertListEqual(estructura_estudiante, estructura_esperada)

    @timeout(N_SECOND)
    def test_07_tablero_sin_parametros(self):
        """
        Tablero de 5x5, no se dan parámetros correctos
        """

        tablero_estudiante = Tablero()
        tablero_estudiante.cargar_tablero("t7.txt")

        cambio_estudiante = tablero_estudiante.modificar_casilla("!", "!")
        estructura_estudiante = tablero_estudiante.tablero
        estructura_esperada = [
                ['.', '12', '.', '13', '.', '6'],
                ['.', '6', '6', '6', '13', '.'],
                ['2', '15', '.', '14', '17', '.'],
                ['4', '16', '.', '5', '.', '.'],
                ['2', '12', '14', '11', '1', '4'],
                ['.', '2', '13', '.', '.', "."]
            ]

        self.assertFalse(cambio_estudiante)
        self.assertListEqual(estructura_estudiante, estructura_esperada)

    @timeout(N_SECOND)
    def test_08_tablero_grande_objetivo(self):
        """
        Tablero de 13x11, coordenadas incorrectas
        """

        tablero_estudiante = Tablero()
        tablero_estudiante.cargar_tablero("t8.txt")

        cambio_estudiante = tablero_estudiante.modificar_casilla(-8, -9)
        estructura_estudiante = tablero_estudiante.tablero
        estructura_esperada = [
            ["10", "9", "13", "17", "3", "13", "3", "6", "13", "10", ".", "8", "12", "8"],
            ["2", "10", "10", ".", "17", "6", "7", "5", "2", "3", "7", "3", "16", "11"],
            ["12", ".", "1", "14", "7", ".", "9", "16", "9", "17", ".", "16", "6", "."],
            ["4", "5", "7", "4", ".", "6", "7", "8", "11", "13", ".", ".", "5", "11"],
            ["12", "6", ".", "15", ".", ".", "1", "10", "3", "5", "1", ".", ".", "16"],
            ["8", "1", "6", ".", "16", ".", ".", "15", ".", "8", "5", ".", "15", "9"],
            ["10", "6", ".", ".", ".", ".", "10", "4", "4", ".", "7", "2", ".", "12"],
            ["17", "1", ".", "16", "9", "10", "17", "14", ".", "16", "6", ".", "8", "16"],
            ["13", "8", "17", "16", ".", ".", "6", "5", ".", ".", ".", "10", "13", "."],
            ["4", "13", "5", "8", "16", ".", "10", ".", "9", "7", ".", "17", "9", "."],
            ["1", "15", "15", "13", ".", "16", "13", "16", ".", ".", ".", "6", ".", "."],
            [".", ".", "9", ".", "4", "10", "1", "5", "11", ".", "5", "3", "9", "."],
            ["11", "14", ".", ".", "8", "8", "14", "12", ".", "10", "12", "15", "13", "3"],
            ["15", "8", "16", "7", "8", "5", "4", ".", "17", "13", "10", ".", ".", "."]
        ]

        self.assertFalse(cambio_estudiante)
        self.assertListEqual(estructura_estudiante, estructura_esperada)

    @timeout(N_SECOND)
    def test_09_tablero_grande_vacio(self):
        """
        Tablero de 10x10, casilla fuera del tablero
        """

        tablero_estudiante = Tablero()
        tablero_estudiante.cargar_tablero("t9.txt")
        cambio_estudiante = tablero_estudiante.modificar_casilla(22, 33)
        estructura_estudiante = tablero_estudiante.tablero
        estructura_esperada = [
            ['.', '5', '.', '.', '.', '6', '1', '16', '3', '4', '14'],
            ['.', '.', '.', '2', '.', '.', '12', '9', '16', '7', '.'],
            ['10', '5', '.', '.', '14', '1', '11', '.', '.', '15', '6'],
            ['10', '12', '8', '.', '8', '2', '.', '.', '17', '9', '.'],
            ['15', '.', '1', '13', '.', '11', '6', '14', '.', '1', '6'],
            ['.', '.', '8', '14', '17', '.', '.', '.', '.', '5', '.'],
            ['13', '16', '3', '3', '.', '13', '.', '9', '.', '.', '17'],
            ['15', '.', '3', '11', '12', '4', '4', '13', '16', '10', '6'],
            ['.', '8', '15', '8', '13', '.', '17', '.', '16', '12', '13'],
            ['12', '17', '11', '12', '.', '14', '13', '7', '.', '9', '1'],
            ['.', '5', '11', '10', '12', '.', '2', '12', '.', '11', "."]
            ]

        self.assertFalse(cambio_estudiante)
        self.assertListEqual(estructura_estudiante, estructura_esperada)
