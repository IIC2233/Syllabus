import os
import sys
import unittest
from tablero import Tablero
from tests_publicos.timeout_function import timeout

sys.stdout = open(os.devnull, 'w')

N_SECOND = 10


class TestModificarCasilla(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_00_tablero_simple_deshabilitar(self):
        """
        Tablero de 3x2 deshabilitando una casilla
        """

        tablero_estudiante = Tablero()
        tablero_estudiante.cargar_tablero("t0.txt")

        cambio_estudiante = tablero_estudiante.modificar_casilla(1, 1)
        estructura_estudiante = tablero_estudiante.tablero
        estructura_esperada = [[
            [1, 2, 4],
            [1, "X2", 6],
            [1, 2, 4],
            [".", ".", "."]
            ],
            [
            ["1", "2", "4"],
            ["1", "X2", "6"],
            ["1", "2", "4"],
            [".", ".", "."]
            ]
        ]

        self.assertEqual(cambio_estudiante, True)
        self.assertIn(estructura_estudiante, estructura_esperada)

    @timeout(N_SECOND)
    def test_01_tablero_medio_dehabilitar(self):
        """
        Tablero de 5x6, se dehabilita una casilla al medio
        """

        tablero_estudiante = Tablero()
        tablero_estudiante.cargar_tablero("t1.txt")

        cambio_estudiante = tablero_estudiante.modificar_casilla(2, 3)
        estructura_estudiante = tablero_estudiante.tablero
        estructura_esperada = [
            [
                [1, 2, 4, 3, 5, 6],
                [1, 2, 6, 3, 5, 6],
                [1, 2, 4, "X3", 5, 6],
                [1, 2, 4, 3, 5, 6],
                [1, 2, 4, 3, 5, 6],
                [".", ".", 31, 41, ".", ".", "."]
            ],
            [
                ["1", "2", "4", "3", "5", "6", "."],
                ["1", "2", "6", "3", "5", "6", "17"],
                ["1", "2", "4", "X3", "5", "6", "32"],
                ["1", "2", "4", "3", "5", "6", "."],
                ["1", "2", "4", "3", "5", "6", "12"],
                [".", ".", "31", "41", ".", ".", "."]
            ]]

        self.assertEqual(cambio_estudiante, True)
        self.assertIn(estructura_estudiante, estructura_esperada)

    @timeout(N_SECOND)
    def test_02_tablero_grande_deshabilitar(self):
        """
        Tablero de 10x6, se deshabilita una casilla al medio
        """

        tablero_estudiante = Tablero()
        tablero_estudiante.cargar_tablero("t2.txt")

        cambio_estudiante = tablero_estudiante.modificar_casilla(6, 4)
        estructura_estudiante = tablero_estudiante.tablero
        estructura_esperada = [
            [
                ['.', 7, 17, 2, 8, 6, 12],
                [5, 10, 8, 10, 14, 16, '.'],
                [3, 13, '.', 13, 3, 4, 10],
                [16, 13, 5, 12, 5, 3, '.'],
                [9, 11, 13, 11, 1, 13, 4],
                [14, 12, 16, 5, 3, 8, 7],
                ['.', 9, '.', '.', 'X15', 16, 14],
                ['.', 7, 4, 5, '.', 14, 16],
                [6, '.', 9, 2, '.', '.', 3],
                [16, '.', 7, 3, 3, '.', '.'],
                [5, 9, 10, 15, 8, '.', "."]
                ],
            [
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
                ['5', '9', '10', '15', '8', '.', "."]]
        ]

        self.assertEqual(cambio_estudiante, True)
        self.assertIn(estructura_estudiante, estructura_esperada)

    @timeout(N_SECOND)
    def test_03_tablero_simple_habilitar(self):
        """
        Tablero de 2x2 habilitando una casilla
        """

        tablero_estudiante = Tablero()
        tablero_estudiante.cargar_tablero("t3.txt")
        cambio_estudiante = tablero_estudiante.modificar_casilla(1, 0)
        estructura_estudiante = tablero_estudiante.tablero
        estructura_esperada = [
            [
                [11, 14, 1],
                ['X16', 7, '.'],
                [9, 5, "."]
            ],
            [
                ['11', '14', '1'],
                ['X16', '7', '.'],
                ['9', '5', "."]
            ]
        ]

        self.assertEqual(cambio_estudiante, True)
        self.assertIn(estructura_estudiante, estructura_esperada)

    @timeout(N_SECOND)
    def test_04_tablero_medio_habilitar(self):
        """
        Tablero de 4x5 habilitando una casilla
        """

        tablero_estudiante = Tablero()
        tablero_estudiante.cargar_tablero("t4.txt")

        cambio_estudiante = tablero_estudiante.modificar_casilla(3, 4)
        estructura_estudiante = tablero_estudiante.tablero
        estructura_esperada = [
            [
                ['.', '.', 9, 3, 6, 7],
                [2, 13, 5, 10, '.', '.'],
                [6, 7, 7, 16, 6, '.'],
                [6, '.', 6, '.', 'X15', '.'],
                ['.', 14, 8, 5, 8, "."]
            ],
            [
                ['.', '.', '9', '3', '6', '7'],
                ['2', '13', '5', '10', '.', '.'],
                ['6', '7', '7', '16', '6', '.'],
                ['6', '.', '6', '.', 'X15', '.'],
                ['.', '14', '8', '5', '8', "."]
            ]
        ]

        self.assertEqual(cambio_estudiante, True)
        self.assertIn(estructura_estudiante, estructura_esperada)

    @timeout(N_SECOND)
    def test_05_grande_habilitar(self):
        """
        Tablero de 12x15 varios cambios
        """

        tablero_estudiante = Tablero()
        tablero_estudiante.cargar_tablero("t5.txt")

        cambio_estudiante = tablero_estudiante.modificar_casilla(4, 2)
        cambio_estudiante = tablero_estudiante.modificar_casilla(4, 6)
        cambio_estudiante = tablero_estudiante.modificar_casilla(3, 6)

        estructura_estudiante = tablero_estudiante.tablero
        estructura_esperada = [
            [
                [13, 9, '.', 8, 9, 5, 8, 13, 15, '.', '.', 7, 11, 8, 8, 6],
                ['.', '.', 4, 3, 5, '.', 7, 14, '.', 2, 1, 6, '.', 12, 8, 3],
                [14, 8, 3, '.', '.', '.', 17, 1, '.', '.', 3, 9, '.', 1, '.', 11],
                [5, 9, '.', '.', 10, 2, 'X8', '.', '.', '.', '.', 17, 9, 2, 7, 0],
                [4, 10, 'X6', '.', '.', '.', 'X7', '.', '.', 10, 2, 7, 9, '.', 2, 3],
                [12, 12, 7, 1, 8, '.', '.', 12, 3, '.', 5, 11, 12, 1, '.', 1],
                [4, 1, 16, 7, '.', 10, 3, '.', 13, '.', 15, 3, 1, '.', '.', '.'],
                [16, 8, 8, '.', 7, 2, 9, 8, '.', '.', 12, 11, 10, 8, 16, 3],
                [2, 4, 7, 16, 1, 3, 4, 4, 4, 1, 1, 14, 6, 1, '.', 2],
                ['.', '.', 17, 9, '.', 12, 2, 9, 1, 10, 13, '.', 1, 1, '.', 1],
                [10, '.', 8, '.', 5, '.', 10, 14, 12, 3, 2, 1, 16, 1, '.', '.'],
                ['.', 15, 5, 17, 8, 1, 9, 1, 5, '.', '.', 15, 11, 8, 4, 5],
                ['.', '.', '.', '.', 1, '.', 15, '.', '.', 14, '.', '.', 8, 8, '.', "."]
            ],
            [
                ['13', '9', '.', '8', '9', '5', '8', '13', '15', '.', '.', '7', '11', '8', '8', '6'],
                ['.', '.', '4', '3', '5', '.', '7', '14', '.', '2', '1', '6', '.', '12', '8', '3'],
                ['14', '8', '3', '.', '.', '.', '17', '1', '.', '.', '3', '9', '.', '1', '.', '11'],
                ['5', '9', '.', '.', '10', '2', 'X8', '.', '.', '.', '.', '17', '9', '2', "7", '0'],
                ['4', '10', 'X6', '.', '.', '.', 'X7', '.', '.', '10', '2', '7', '9', '.', '2', '3'],
                ['12', '12', '7', '1', '8', '.', '.', '12', '3', '.', '5', '11', '12', '1', '.', '1'],
                ['4', '1', '16', '7', '.', '10', '3', '.', '13', '.', '15', '3', '1', '.', '.', '.'],
                ['16', '8', '8', '.', '7', '2', '9', '8', '.', '.', '12', '11', '10', '8', '16', '3'],
                ['2', '4', '7', '16', '1', '3', '4', '4', '4', '1', '1', '14', '6', '1', '.', '2'],
                ['.', '.', '17', '9', '.', '12', '2', '9', '1', '10', '13', '.', '1', '1', '.', '1'],
                ['10', '.', '8', '.', '5', '.', '10', '14', '12', '3', '2', '1', '16', '1', '.', '.'],
                ['.', '15', '5', '17', '8', '1', '9', '1', '5', '.', '.', '15', '11', '8', '4', '5'],
                ['.', '.', '.', '.', '1', '.', '15', '.', '.', '14', '.', '.', '8', '8', '.', "."]
            ]
        ]

        self.assertEqual(cambio_estudiante, True)
        self.assertIn(estructura_estudiante, estructura_esperada)

    @timeout(N_SECOND)
    def test_06_tablero_simple_objetivo(self):
        """
        Tablero de 3x1, objetivo
        """

        tablero_estudiante = Tablero()
        tablero_estudiante.cargar_tablero("t6.txt")

        cambio_estudiante = tablero_estudiante.modificar_casilla(2, 1)
        estructura_estudiante = tablero_estudiante.tablero
        estructura_esperada = [[
            [6, 15],
            [3, '.'],
            [12, '.'],
            ['.', "."]
            ],
            [
            ['6', '15'],
            ['3', '.'],
            ['12', '.'],
            ['.', "."]
            ]]

        self.assertEqual(cambio_estudiante, False)
        self.assertIn(estructura_estudiante, estructura_esperada)

    @timeout(N_SECOND)
    def test_07_tablero_medio_objetivo(self):
        """
        Tablero de 5x5, se pide un str
        """

        tablero_estudiante = Tablero()
        tablero_estudiante.cargar_tablero("t7.txt")

        cambio_estudiante = tablero_estudiante.modificar_casilla("tres", "seis")
        estructura_estudiante = tablero_estudiante.tablero
        estructura_esperada = [
            [
                ['.', 12, '.', 13, '.', 6],
                ['.', 6, 6, 6, 13, '.'],
                [2, 15, '.', 14, 17, '.'],
                [4, 16, '.', 5, '.', '.'],
                [2, 12, 14, 11, 1, 4],
                ['.', 2, 13, '.', '.', "."]
            ],
            [
                ['.', '12', '.', '13', '.', '6'],
                ['.', '6', '6', '6', '13', '.'],
                ['2', '15', '.', '14', '17', '.'],
                ['4', '16', '.', '5', '.', '.'],
                ['2', '12', '14', '11', '1', '4'],
                ['.', '2', '13', '.', '.', "."]
            ]]

        self.assertEqual(cambio_estudiante, False)
        self.assertIn(estructura_estudiante, estructura_esperada)


    def test_08_tablero_grande_vacio(self):
        """
        Tablero de 10x10, casilla vacía
        """

        tablero_estudiante = Tablero()
        tablero_estudiante.cargar_tablero("t9.txt")
        cambio_estudiante = tablero_estudiante.modificar_casilla(2, 7)
        estructura_estudiante = tablero_estudiante.tablero
        estructura_esperada = [[
            ['.', 5, '.', '.', '.', 6, 1, 16, 3, 4, 14],
            ['.', '.', '.', 2, '.', '.', 12, 9, 16, 7, '.'],
            [10, 5, '.', '.', 14, 1, 11, '.', '.', 15, 6],
            [10, 12, 8, '.', 8, 2, '.', '.', 17, 9, '.'],
            [15, '.', 1, 13, '.', 11, 6, 14, '.', 1, 6],
            ['.', '.', 8, 14, 17, '.', '.', '.', '.', 5, '.'],
            [13, 16, 3, 3, '.', 13, '.', 9, '.', '.', 17],
            [15, '.', 3, 11, 12, 4, 4, 13, 16, 10, 6],
            ['.', 8, 15, 8, 13, '.', 17, '.', 16, 12, 13],
            [12, 17, 11, 12, '.', 14, 13, 7, '.', 9, 1],
            ['.', 5, 11, 10, 12, '.', 2, 12, '.', 11, "."]
            ],
            [
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
        ]

        self.assertEqual(cambio_estudiante, False)
        self.assertIn(estructura_estudiante, estructura_esperada)
