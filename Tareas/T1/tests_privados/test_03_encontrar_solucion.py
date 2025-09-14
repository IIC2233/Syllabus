import os
import sys
import unittest
from tablero import Tablero
from tests_privados.timeout_function import timeout

sys.stdout = open(os.devnull, 'w')

N_SECOND = 20


class TestEncontrarSolucion(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_00_tablero_simple_uno(self):
        """
        Tablero de 3x3 que resolver
        """

        tablero = [
            ['1', '2', '4', '3'],
            ['1', '2', '6', '8'],
            ['1', '2', '4', '7'],
            ['.', '.', '10', '.']
            ]

        tablero_estudiante = Tablero()
        tablero_estudiante.cargar_tablero("tablero_11.txt")
        nuevo_tablero = tablero_estudiante.encontrar_solucion()
        tablero_original = tablero_estudiante.tablero
        estructura_estudiante = nuevo_tablero.tablero
        estructura_esperada = [
            ['1', '2', 'X4', '3'],
            ['X1', '2', '6', '8'],
            ['1', '2', '4', '7'],
            ['.', '.', '10', '.']
            ]

        self.assertIsInstance(nuevo_tablero, Tablero)
        self.assertEqual(tablero_original, tablero)
        self.assertListEqual(estructura_estudiante, estructura_esperada)
        self.assertIsNot(nuevo_tablero, tablero_estudiante)

    @timeout(N_SECOND)
    def test_01_tablero_simple_dos(self):
        """
        Tablero de 2x2 deshabilitando casi todo
        """

        tablero = [
            ['4', '2', '2'],
            ['3', '3', '0'],
            ['0', '2', '.']
            ]

        tablero_estudiante = Tablero()
        tablero_estudiante.cargar_tablero("tablero_12.txt")
        nuevo_tablero = tablero_estudiante.encontrar_solucion()
        tablero_original = tablero_estudiante.tablero
        estructura_estudiante = nuevo_tablero.tablero
        estructura_esperada = [
            ['X4', '2', '2'],
            ['X3', 'X3', '0'],
            ['0', '2', '.']
            ]

        self.assertIsInstance(nuevo_tablero, Tablero)
        self.assertListEqual(estructura_estudiante, estructura_esperada)
        self.assertEqual(tablero_original, tablero)
        self.assertIsNot(nuevo_tablero, tablero_estudiante)

    @timeout(N_SECOND)
    def test_02_tablero_medio(self):
        """
        Tablero de 4x6 deshabilitando varias casillas
        """

        tablero = [
            ['9', '.', '3', '2', '4', '.', '9'],
            ['2', '4', '.', '1', '6', '2', '8'],
            ['.', '7', '7', '.', '1', '2', '.'],
            ['1', '.', '6', '3', '.', '5', '9'],
            ['3', '4', '10', '.', '5', '7', '.']
            ]

        tablero_estudiante = Tablero()
        tablero_estudiante.cargar_tablero("tablero_13.txt")
        nuevo_tablero = tablero_estudiante.encontrar_solucion()
        tablero_original = tablero_estudiante.tablero
        estructura_estudiante = nuevo_tablero.tablero
        estructura_esperada = [
            ['X9', '.', '3', '2', '4', '.', '9'],
            ['2', '4', '.', 'X1', 'X6', '2', '8'],
            ['.', 'X7', '7', '.', '1', 'X2', '.'],
            ['1', '.', 'X6', '3', '.', '5', '9'],
            ['3', '4', '10', '.', '5', '7', '.']
            ]

        self.assertIsInstance(nuevo_tablero, Tablero)
        self.assertListEqual(estructura_estudiante, estructura_esperada)
        self.assertEqual(tablero_original, tablero)
        self.assertIsNot(nuevo_tablero, tablero_estudiante)

    @timeout(N_SECOND)
    def test_03_tablero_medio_varias_soluciones(self):
        """
        Tablero de 5x4, con tres soluciones
        """

        tablero = [
            ['5',  '3', '3', '5', '5'],
            ['2',  '5', '1',  '5', '6'],
            ['3',  '5',  '5', '1', '8'],
            ['5',  '5', '5', '5',  '10'],
            ['4',  '7', '1', '7',  '5'],
            ['12', '10', '2',  '10', '.']
        ]

        tablero_estudiante = Tablero()
        tablero_estudiante.cargar_tablero("tablero_14.txt")
        nuevo_tablero = tablero_estudiante.encontrar_solucion()
        tablero_original = tablero_estudiante.tablero
        estructura_estudiante = nuevo_tablero.tablero

        solucion1 = [
            ['X5',  'X3', 'X3', '5', '5'],
            ['X2',  'X5', '1',  '5', '6'],
            ['3',  '5',  'X5', 'X1', '8'],
            ['5',  '5', 'X5', '5',  '10'],
            ['4',  'X7', '1', 'X7',  '5'],
            ['12', '10', '2',  '10', '.']
        ]

        solucion2 = [
            ['5',  'X3', 'X3', 'X5', '5'],
            ['X2',  'X5', '1',  '5', '6'],
            ['3',  '5',  'X5', 'X1', '8'],
            ['X5',  '5', 'X5', '5',  '10'],
            ['4',  'X7', '1', 'X7',  '5'],
            ['12', '10', '2',  '10', '.']
        ]

        solucion3 = [
            ['X5', 'X3', 'X3', '5', '5'],
            ['X2', 'X5', '1', '5', '6'],
            ['3', '5', 'X5', 'X1', '8'],
            ['5', '5', 'X5', 'X5', '10'],
            ['4', 'X7', '1', 'X7', '5'],
            ['12', '10', '2', '10', '.']
            ]

        soluciones = [solucion1, solucion2, solucion3]

        self.assertIsInstance(nuevo_tablero, Tablero)
        self.assertIn(estructura_estudiante, soluciones)
        self.assertEqual(tablero_original, tablero)
        self.assertIsNot(nuevo_tablero, tablero_estudiante)

    @timeout(N_SECOND)
    def test_04_tablero_mediano_varios(self):
        """
        Tablero de 5x4 se deshabilita todo
        """

        tablero = [
            ["2", "2", "2", "1", "0"],
            ["1", "2", "1", "6", "0"],
            ["7", "2", "1", "7", "0"],
            ["6", "3", "2", "3", "0"],
            ["3", "4", "4", "2", "0"],
            ["0", "0", "0", "0", "."]
        ]

        tablero_estudiante = Tablero()
        tablero_estudiante.cargar_tablero("tablero_15.txt")
        nuevo_tablero = tablero_estudiante.encontrar_solucion()
        tablero_original = tablero_estudiante.tablero
        estructura_estudiante = nuevo_tablero.tablero
        estructura_esperada = [
            ["X2", "X2", "X2", "X1", "0"],
            ["X1", "X2", "X1", "X6", "0"],
            ["X7", "X2", "X1", "X7", "0"],
            ["X6", "X3", "X2", "X3", "0"],
            ["X3", "X4", "X4", "X2", "0"],
            ["0", "0", "0", "0", "."]
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
            ["1", "2", "4", "3", "5", "6", "0"],
            ["1", "2", "6", "3", "5", "6", "23"],
            ["1", "2", "4", "3", "5", "6", "21"],
            ["2", "4", "10", "6", "10", "12", "."]
            ]

        tablero_estudiante = Tablero()
        tablero_estudiante.cargar_tablero("tablero_16.txt")
        tablero_original = tablero_estudiante.tablero
        nuevo_tablero = tablero_estudiante.encontrar_solucion()
        estructura_estudiante = nuevo_tablero.tablero

        estructura_esperada = [
            ["X1", "X2", "X4", "X3", "X5", "X6", "0"],
            ["1", "2", "6", "3", "5", "6", "23"],
            ["1", "2", "4", "3", "5", "6", "21"],
            ["2", "4", "10", "6", "10", "12", "."]
            ]

        self.assertIsInstance(nuevo_tablero, Tablero)
        self.assertEqual(tablero_original, tablero)
        self.assertListEqual(estructura_estudiante, estructura_esperada)
        self.assertIsNot(nuevo_tablero, tablero_estudiante)

    @timeout(N_SECOND)
    def test_06_tablero_resuelto(self):
        """
        Tablero de 6x6, ya resuelto
        """

        tablero = [
            ['2', '6', '5', '2', '1', '16'],
            ['3', '2', '1', '2', '2', '10'],
            ['5', '7', '3', '1', '6', '22'],
            ['5', '1', '3', '7', '4', '20'],
            ['8', '2', '2', '7', '7', '26'],
            ['1', '2', '1', '5', '5', '14'],
            ['24', '20', '15', '24', '25', "."]
            ]

        tablero_estudiante = Tablero()
        tablero_estudiante.cargar_tablero("tablero_17.txt")
        nuevo_tablero = tablero_estudiante.encontrar_solucion()
        tablero_original = tablero_estudiante.tablero
        estructura_estudiante = nuevo_tablero.tablero

        estructura_esperada = [
            ['2', '6', '5', '2', '1', '16'],
            ['3', '2', '1', '2', '2', '10'],
            ['5', '7', '3', '1', '6', '22'],
            ['5', '1', '3', '7', '4', '20'],
            ['8', '2', '2', '7', '7', '26'],
            ['1', '2', '1', '5', '5', '14'],
            ['24', '20', '15', '24', '25', "."]
            ]
        self.assertIsInstance(nuevo_tablero, Tablero)
        self.assertListEqual(estructura_estudiante, estructura_esperada)
        self.assertEqual(tablero_original, tablero)
        self.assertIsNot(nuevo_tablero, tablero_estudiante)

    @timeout(N_SECOND)
    def test_07_tablero_grande_sin_solucion(self):
        """
        Tablero de 5x2 sin solucion
        """

        tablero = [
            ['.', '1', '0'],
            ['3', '2', '2'],
            ['1', '.', '1'],
            ['2', '4', '0'],
            ['2', '2', '3'],
            ['3', '3', '.']
            ]

        tablero_estudiante = Tablero()
        tablero_estudiante.cargar_tablero("tablero_18.txt")
        nuevo_tablero = tablero_estudiante.encontrar_solucion()
        tablero_original = tablero_estudiante.tablero

        self.assertIsNone(nuevo_tablero)
        self.assertListEqual(tablero_original, tablero)
        self.assertIsNot(nuevo_tablero, tablero_estudiante)

    @timeout(N_SECOND)
    def test_08_tablero_desactivar_columna(self):
        """
        Tablero de 5x4 que desactiva columna del medio
        """

        tablero = [
            ["5", "3", "3", "5", "13"],
            ["2", "5", "7", "5", "12"],
            ["3", "5", "5", "1", "9"],
            ["5", "5", "5", "5", "15"],
            ["6", "5", "1", "5", "16"],
            ["21", "23", ".", "21", "."]
        ]

        tablero_estudiante = Tablero()
        tablero_estudiante.cargar_tablero("tablero_19.txt")
        nuevo_tablero = tablero_estudiante.encontrar_solucion()
        tablero_original = tablero_estudiante.tablero
        estructura_estudiante = nuevo_tablero.tablero
        estructura_esperada = [
            ["5", "3", "X3", "5", "13"],
            ["2", "5", "X7", "5", "12"],
            ["3", "5", "X5", "1", "9"],
            ["5", "5", "X5", "5", "15"],
            ["6", "5", "X1", "5", "16"],
            ["21", "23", ".", "21", "."]
        ]

        self.assertIsInstance(nuevo_tablero, Tablero)
        self.assertListEqual(estructura_estudiante, estructura_esperada)
        self.assertEqual(tablero_original, tablero)
        self.assertIsNot(nuevo_tablero, tablero_estudiante)

    @timeout(N_SECOND)
    def test_09_coordenadas_erroneas(self):
        """
        Tablero de 5x4 que hay que desactivar intercalado
        """

        tablero = [
            ['17', '8', '9', '9', '17'],
            ['8', '11', '8', '5', '16'],
            ['3', '4', '8', '9', '13'],
            ['11', '2', '11', '1', '22'],
            ['9', '12', '9', '6', '18'],
            ['19', '.', '19', '.', '.']
            ]

        estructura_esperada = [
            ['X17', '8', 'X9', '9', '17'],
            ['8', 'X11', '8', 'X5', '16'],
            ['X3', '4', 'X8', '9', '13'],
            ['11', 'X2', '11', 'X1', '22'],
            ['X9', '12', 'X9', '6', '18'],
            ['19', '.', '19', '.', '.']
            ]

        tablero_estudiante = Tablero()
        tablero_estudiante.cargar_tablero("tablero_20.txt")
        nuevo_tablero = tablero_estudiante.encontrar_solucion()
        tablero_original = tablero_estudiante.tablero
        estructura_estudiante = nuevo_tablero.tablero

        self.assertIsInstance(nuevo_tablero, Tablero)
        self.assertListEqual(estructura_estudiante, estructura_esperada)
        self.assertEqual(tablero_original, tablero)
        self.assertIsNot(nuevo_tablero, tablero_estudiante)
