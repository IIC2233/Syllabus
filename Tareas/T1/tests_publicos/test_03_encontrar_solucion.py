import os
import sys
import unittest
from tablero import Tablero
from tests_publicos.timeout_function import timeout

sys.stdout = open(os.devnull, 'w')

N_SECOND = 20


class TestEncontrarSolucion(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_00_tablero_simple_habiltar(self):
        """
        Tablero de 1x1 deshabilitando la casilla
        """

        tablero = [
            ["4", "0"],
            ["0", "."]
        ]

        tablero_estudiante = Tablero()
        tablero_estudiante.cargar_tablero("tab1.txt")
        nuevo_tablero = tablero_estudiante.encontrar_solucion()
        tablero_original = tablero_estudiante.tablero
        estructura_estudiante = nuevo_tablero.tablero
        estructura_esperada = [
            [
                ["X4", 0],
                [0, "."]
            ],
            [
                ["X4", "0"],
                ["0", "."]
            ]
        ]

        self.assertIsInstance(nuevo_tablero, Tablero)
        self.assertEqual(tablero_original, tablero)
        self.assertIn(estructura_estudiante, estructura_esperada)
        self.assertIsNot(nuevo_tablero, tablero_estudiante)

    @timeout(N_SECOND)
    def test_01_tablero_simple_deshabilitar(self):
        """
        Tablero de 3x2 deshabilitando una casilla
        """

        tablero = [
            ["1", "4", "4"],
            ["4", "2", "6"],
            ["2", "2", "4"],
            ["6", ".", "."]
            ]

        tablero_estudiante = Tablero()
        tablero_estudiante.cargar_tablero("tab2.txt")
        nuevo_tablero = tablero_estudiante.encontrar_solucion()
        tablero_original = tablero_estudiante.tablero
        estructura_estudiante = nuevo_tablero.tablero
        estructura_esperada = [[
            ["X1", 4, 4],
            [4, 2, 6],
            [2, 2, 4],
            [6, ".", "."]
            ],
            [
            ["X1", "4", "4"],
            ["4", "2", "6"],
            ["2", "2", "4"],
            ["6", ".", "."]
            ]
        ]

        self.assertIsInstance(nuevo_tablero, Tablero)
        self.assertIn(estructura_estudiante, estructura_esperada)
        self.assertEqual(tablero_original, tablero)
        self.assertIsNot(nuevo_tablero, tablero_estudiante)

    @timeout(N_SECOND)
    def test_02_tablero_simple_habilitar_dos(self):
        """
        Tablero de 4x4 deshabilitando dos casillas
        """

        tablero = [
            ["1", "4", "4", ".", "9"],
            ["4", "2", "6", "1", "7"],
            ["2", "2", "4", ".", "8"],
            ["6", ".", "2", "4", "6"],
            ["7", ".", "10", "5", "."]
            ]

        tablero_estudiante = Tablero()
        tablero_estudiante.cargar_tablero("tab3.txt")
        nuevo_tablero = tablero_estudiante.encontrar_solucion()
        tablero_original = tablero_estudiante.tablero
        estructura_estudiante = nuevo_tablero.tablero
        estructura_esperada = [
            [
                [1, 4, 4, ".", 9],
                [4, 2, "X6", 1, 7],
                [2, 2, 4, ".", 8],
                ["X6", ".", 2, 4, 6],
                [7, ".", 10, 5, "."]
            ],
            [
                ["1", "4", "4", ".", "9"],
                ["4", "2", "X6", "1", "7"],
                ["2", "2", "4", ".", "8"],
                ["X6", ".", "2", "4", "6"],
                ["7", ".", "10", "5", "."]
            ]
        ]

        self.assertIsInstance(nuevo_tablero, Tablero)
        self.assertIn(estructura_estudiante, estructura_esperada)
        self.assertEqual(tablero_original, tablero)
        self.assertIsNot(nuevo_tablero, tablero_estudiante)

    @timeout(N_SECOND)
    def test_03_tablero_mediano_habilitar(self):
        """
        Tablero de 4x2, solo se deshabilitan varios
        """

        tablero = [
            ['4',  '7',  '7'],
            ['3',   '5', '3'],
            ['.',   '9',  '9'],
            ['2',   '1',  '3'],
            ['5',   '17', '.']
            ]

        tablero_estudiante = Tablero()
        tablero_estudiante.cargar_tablero("tab4.txt")
        nuevo_tablero = tablero_estudiante.encontrar_solucion()
        tablero_original = tablero_estudiante.tablero
        estructura_estudiante = nuevo_tablero.tablero
        estructura_esperada = [
                ['X4',  '7',  '7'],
                ['3',   'X5', '3'],
                ['.',   '9',  '9'],
                ['2',   '1',  '3'],
                ['5',   '17', '.']
            ]

        self.assertIsInstance(nuevo_tablero, Tablero)
        self.assertListEqual(estructura_estudiante, estructura_esperada)
        self.assertEqual(tablero_original, tablero)
        self.assertIsNot(nuevo_tablero, tablero_estudiante)

    @timeout(N_SECOND)
    def test_04_tablero_mediano_varios(self):
        """
        Tablero de 2x5 varios cambios, habilitando y dehabilitando
        """

        tablero = [
            ['1',  '3', '8',  '2',  '4', '7'],
            ['3',  '5',  '1',  '9',  '.', '9'],
            ['4',  '5',  '.',  '2',  '4', '.']
            ]

        tablero_estudiante = Tablero()
        tablero_estudiante.cargar_tablero("tab5.txt")
        nuevo_tablero = tablero_estudiante.encontrar_solucion()
        tablero_original = tablero_estudiante.tablero
        estructura_estudiante = nuevo_tablero.tablero
        estructura_esperada = [
            ['1',  'X3', 'X8',  '2',  '4', '7'],
            ['3',  '5',  '1',  'X9',  '.', '9'],
            ['4',  '5',  '.',  '2',  '4', '.']
            ]

        self.assertIsInstance(nuevo_tablero, Tablero)
        self.assertListEqual(estructura_estudiante, estructura_esperada)
        self.assertEqual(tablero_original, tablero)
        self.assertIsNot(nuevo_tablero, tablero_estudiante)

    @timeout(N_SECOND)
    def test_05_tablero_medio_opciones(self):
        """
        Tablero de 3x6, con varias soluciones
        """

        tablero = [
            ["1", "2", "4", "3", "5", "6", "21"],
            ["1", "2", "6", "3", "5", "6", "20"],
            ["1", "2", "4", "3", "5", "6", "18"],
            [".", ".", "14", "6", ".", ".", "."]
            ]

        tablero_estudiante = Tablero()
        tablero_estudiante.cargar_tablero("tab6.txt")
        tablero_original = tablero_estudiante.tablero
        nuevo_tablero = tablero_estudiante.encontrar_solucion()
        estructura_estudiante = nuevo_tablero.tablero

        e4 = [
            ["1", "2", "4", "3", "5", "6", "21"],
            ["X1", "X2", "6", "3", "5", "6", "20"],
            ["1", "2", "4", "X3", "5", "6", "18"],
            [".", ".", "14", "6", ".", ".", "."]
            ]

        e5 = [
            ["1", "2", "4", "3", "5", "6", "21"],
            ["1", "2", "6", "X3", "5", "6", "20"],
            ["X1", "X2", "4", "3", "5", "6", "18"],
            [".", ".", "14", "6", ".", ".", "."]
            ]

        respuestas = [e4, e5]
        self.assertIsInstance(nuevo_tablero, Tablero)
        self.assertEqual(tablero_original, tablero)
        self.assertIn(estructura_estudiante, respuestas)
        self.assertIsNot(nuevo_tablero, tablero_estudiante)

    @timeout(N_SECOND)
    def test_06_tablero_grande_intercalar_todo(self):
        """
        Tablero de 4x5, se cambia todo
        """

        tablero = [
            ['.',  '2', '1',  '5', '1'],
            ['2',  '.',  '3', '2',  '4'],
            ['1', '1',  '.',  '1',  '2'],
            ['2',  '1',  '1',  '.',  '.']
            ]

        tablero_estudiante = Tablero()
        tablero_estudiante.cargar_tablero("tab7.txt")
        nuevo_tablero = tablero_estudiante.encontrar_solucion()
        tablero_original = tablero_estudiante.tablero
        estructura_estudiante = nuevo_tablero.tablero
        estructura_esperada = [
            ['.',  'X2', '1',  'X5', '1'],
            ['2',  '.',  'X3', '2',  '4'],
            ['X1', '1',  '.',  '1',  '2'],
            ['2',  '1',  '1',  '.',  '.']
            ]

        self.assertIsInstance(nuevo_tablero, Tablero)
        self.assertListEqual(estructura_estudiante, estructura_esperada)
        self.assertEqual(tablero_original, tablero)
        self.assertIsNot(nuevo_tablero, tablero_estudiante)

    @timeout(N_SECOND)
    def test_07_tablero_grande_solucionado(self):
        """
        Tablero de 5x2 que está listo
        """

        tablero = [
            ['.',  '1', '0'],
            ['3', '2',  '2'],
            ['1',  '.',  '1'],
            ['2', '4', '0'],
            ['2',  '1',  '3'],
            ['3',  '3',  '.']
            ]

        tablero_estudiante = Tablero()
        tablero_estudiante.cargar_tablero("tab8.txt")
        nuevo_tablero = tablero_estudiante.encontrar_solucion()
        tablero_original = tablero_estudiante.tablero
        estructura_estudiante = nuevo_tablero.tablero
        estructura_esperada = [
            ['.',  'X1', '0'],
            ['X3', '2',  '2'],
            ['1',  '.',  '1'],
            ['X2', 'X4', '0'],
            ['2',  '1',  '3'],
            ['3',  '3',  '.']
            ]

        self.assertIsInstance(nuevo_tablero, Tablero)
        self.assertListEqual(estructura_estudiante, estructura_esperada)
        self.assertListEqual(tablero_original, tablero)
        self.assertIsNot(nuevo_tablero, tablero_estudiante)

    @timeout(N_SECOND)
    def test_08_tablero_grande_habilitar(self):
        """
        Tablero de 4x6, varios pasos
        """

        tablero = [
            ['5', '.',   '3',   '2', '4',   '.',   '7'],
            ['2',  '4',  '.',   '1',  '6',  '2',   '5'],
            ['.',  '3',   '7',  '.',  '1',   '2',  '4'],
            ['1',  '.',   '2',   '3',  '.',   '5',  '6'],
            ['3',  '3',   '5',   '.',  '5',   '2',   '.']
            ]

        tablero_estudiante = Tablero()
        tablero_estudiante.cargar_tablero("tab9.txt")
        nuevo_tablero = tablero_estudiante.encontrar_solucion()
        tablero_original = tablero_estudiante.tablero
        estructura_estudiante = nuevo_tablero.tablero
        estructura_esperada = [
            ['X5', '.',   '3',   'X2', '4',   '.',   '7'],
            ['2',  'X4',  '.',   '1',  'X6',  '2',   '5'],
            ['.',  '3',   'X7',  '.',  '1',   'X2',  '4'],
            ['1',  '.',   '2',   '3',  '.',   'X5',  '6'],
            ['3',  '3',   '5',   '.',  '5',   '2',   '.']
            ]

        self.assertIsInstance(nuevo_tablero, Tablero)
        self.assertListEqual(estructura_estudiante, estructura_esperada)
        self.assertEqual(tablero_original, tablero)
        self.assertIsNot(nuevo_tablero, tablero_estudiante)

    @timeout(N_SECOND)
    def test_09_coordenadas_erroneas(self):
        """
        Tablero de 1x1 sin solucion
        """

        tablero = [
            ["1", "2"],
            ["1", "."]
            ]

        tablero_estudiante = Tablero()
        tablero_estudiante.cargar_tablero("tab10.txt")
        nuevo_tablero = tablero_estudiante.encontrar_solucion()
        tablero_original = tablero_estudiante.tablero

        self.assertIsNone(nuevo_tablero)
        self.assertEqual(tablero_original, tablero)
