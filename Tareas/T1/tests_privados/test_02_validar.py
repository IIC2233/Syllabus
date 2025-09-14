# Test numero: 2
import sys, os
import unittest

from tests_privados.timeout_function import timeout

from tablero import Tablero

sys.stdout = open(os.devnull, "w")

N_SECOND = 10

# Agregar metodo de comparar tableros para evitar hard-coding.
class TestValidar(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None
    

    @timeout(N_SECOND)
    def test_00_validar_True_1(self):
        """
        Valida un tablero 4x5 retorna True
        """
        
        tablero = [["1", "2", ".", "5", "8"],
                   ["3", ".", "1", "2", "6"],
                   ["2", "1", "3", ".", "6"],
                   ["6", "3", "4", "7", "."]]

        tablero_estudiante = Tablero()
        tablero_estudiante.tablero = tablero

        resultado_estudiante = tablero_estudiante.validar()

        self.assertIsNotNone(resultado_estudiante)
        self.assertTrue(resultado_estudiante)


    @timeout(N_SECOND)
    def test_01_validar_True_2(self):
        """
        
        """
        
        tablero = [
    ["2", ".", "1", "3", "1", ".", "7"],
    ["1", "2", ".", "1", "3", "2", "9"],
    [".", "1", "2", ".", "1", "3", "7"],
    ["3", ".", "1", "2", ".", "1", "7"],
    ["2", "1", ".", "2", "1", ".", "6"],
    ["8", "4", "4", "8", "6", "6", "."]
]

        tablero_estudiante = Tablero()
        tablero_estudiante.tablero = tablero

        resultado_estudiante = tablero_estudiante.validar()

        self.assertIsNotNone(resultado_estudiante)
        self.assertTrue(resultado_estudiante)


    @timeout(N_SECOND)
    def test_02_validar_True_3(self):
        """
        
        """
        
        tablero = [
    ["1", ".", "2", "1", ".", "3", "1", "2", ".", "1", "11"],
    ["2", "1", ".", "2", "1", ".", "2", ".", "1", "2", "11"],
    [".", "2", "1", ".", "2", "1", ".", "2", "1", ".", "9"],
    ["1", ".", "2", "1", ".", "2", "1", ".", "2", "1", "10"],
    ["2", "1", ".", "2", "1", ".", "2", "1", ".", "2", "11"],
    [".", "2", "1", ".", "2", "1", ".", "2", "1", ".", "9"],
    ["1", ".", "2", "1", ".", "2", "1", ".", "2", "1", "10"],
    ["2", "1", ".", "2", "1", ".", "2", "1", ".", "2", "11"],
    ["9", "7", "8", "9", "7", "9", "9", "8", "7", "9", "."]
]

        tablero_estudiante = Tablero()
        tablero_estudiante.tablero = tablero

        resultado_estudiante = tablero_estudiante.validar()

        self.assertIsNotNone(resultado_estudiante)
        self.assertTrue(resultado_estudiante)


    @timeout(N_SECOND)
    def test_03_validar_True_4(self):
        """
        
        """
        
        tablero = [
    ["X2", "1", ".", "2", "1", "4"],
    ["1", "X3", "2", ".", "1", "4"],
    [".", "2", "1", "X1", "2", "5"],
    ["2", ".", "1", "2", "X1", "5"],
    ["3", "3", "4", "4", "4", "."]
]

        tablero_estudiante = Tablero()
        tablero_estudiante.tablero = tablero

        resultado_estudiante = tablero_estudiante.validar()

        self.assertIsNotNone(resultado_estudiante)
        self.assertTrue(resultado_estudiante)


    @timeout(N_SECOND)
    def test_04_validar_True_5(self):
        """
        
        """
        
        tablero = [
    ["X1", "2", ".", "1", "1", ".", "1", "."],
    ["2", "X2", "1", ".", "2", "1", ".", "6"],
    [".", "1", "X3", "2", ".", "1", "2", "."],
    ["1", ".", "2", "X1", "2", ".", "1", "6"],
    ["2", "1", ".", "2", "X2", "1", ".", "."],
    [".", "2", "1", ".", "1", "X3", "2", "6"],
    ["1", ".", "2", "1", ".", "2", "X1", "6"],
    ["2", "1", ".", "2", "1", ".", "2", "8"],
    [".", "2", "1", ".", "2", "1", "1", "."],
    [".", "9", ".", "8", "9", ".", "9", "."]
]

        tablero_estudiante = Tablero()
        tablero_estudiante.tablero = tablero

        resultado_estudiante = tablero_estudiante.validar()

        self.assertIsNotNone(resultado_estudiante)
        self.assertTrue(resultado_estudiante)


    @timeout(N_SECOND)
    def test_05_validar_False_1(self):
        """
        
        """
        
        tablero = [
    ["1", ".", ".", "10"],
    [".", "2", "1", "15"],
    ["5", "8", "7", "."]
]

        tablero_estudiante = Tablero()
        tablero_estudiante.tablero = tablero

        resultado_estudiante = tablero_estudiante.validar()

        self.assertIsNotNone(resultado_estudiante)
        self.assertFalse(resultado_estudiante)


    @timeout(N_SECOND)
    def test_06_validar_False_2(self):
        """
        
        """
        
        tablero = [
    ["1", "2", ".", "1", "2", "20"],
    [".", "1", "2", ".", "1", "15"],
    ["2", ".", "1", "2", ".", "18"],
    ["1", "2", ".", "1", "2", "22"],
    [".", "1", "2", ".", "1", "12"],
    ["2", ".", "1", "2", ".", "25"],
    ["6", "6", "6", "6", "6", "."]
]

        tablero_estudiante = Tablero()
        tablero_estudiante.tablero = tablero

        resultado_estudiante = tablero_estudiante.validar()

        self.assertIsNotNone(resultado_estudiante)
        self.assertFalse(resultado_estudiante)


    @timeout(N_SECOND)
    def test_07_validar_False_3(self):
        """
        
        """
        
        tablero = [
        ["1", "2", "1", "2", "1", "2", "1", "5", "50"], 
        ["2", "1", "2", "1", "2", "4", "2", "1", "45"], 
        ["1", "2", "1", "2", "3", "2", "1", "2", "48"], 
        ["2", "1", "2", "1", "2", "1", "6", "1", "52"], 
        ["1", "2", "1", "7", "1", "2", "1", "2", "46"], 
        ["2", "1", "8", "1", "2", "1", "2", "1", "49"], 
        ["1", "9", "1", "2", "1", "2", "1", "2", "51"], 
        ["2", "1", "2", "1", "2", "1", "2", "1", "47"],
        ["1", "2", "1", "2", "1", "2", "1", "2", "53"],
        ["2", "1", "2", "1", "2", "1", "2", "1", "44"],
        ["15", "15", "15", "15", "15", "15", "15", "15", "."]
    ]

        tablero_estudiante = Tablero()
        tablero_estudiante.tablero = tablero

        resultado_estudiante = tablero_estudiante.validar()

        self.assertIsNotNone(resultado_estudiante)
        self.assertFalse(resultado_estudiante)


    @timeout(N_SECOND)
    def test_08_validar_False_4(self):
        """
        
        """

        tablero = [
    ["X1", "2", ".", "1", "25"],
    ["2", "X1", "2", "X7", "20"],
    [".", "2", "X1", "2", "18"],
    ["1", "12", "2", "X1", "15"],
    ["2", "X1", ".", "2", "22"],
    ["5", "5", "5", "5", "."]
]

        tablero_estudiante = Tablero()
        tablero_estudiante.tablero = tablero

        resultado_estudiante = tablero_estudiante.validar()

        self.assertIsNotNone(resultado_estudiante)
        self.assertFalse(resultado_estudiante)


    @timeout(N_SECOND)
    def test_09_validar_False_5(self):
        """
        
        """

        tablero = [
        ["X1", "2", "1", "8", "2", "1", "2", "X9", "1", "35"],
        ["2", "X1", "8", "2", "1", "X10", "1", "2", "8", "30"],
        ["1", "8", "X2", "1", "9", "2", "8", "1", "2", "28"],
        ["X8", "2", "1", "X2", "1", "8", "2", "X11", "1", "32"],
        ["2", "1", "8", "1", "X2", "1", "X12", "2", "8", "29"],
        ["1", "X8", "2", "8", "1", "X2", "1", "X13", "2", "31"],
        ["8", "2", "1", "2", "X14", "1", "X2", "1", "8", "33"],
        ["2", "1", "8", "1", "2", "8", "1", "X2", "1", "34"],
        ["1", "X9", "2", "8", "1", "2", "8", "1", "X2", "27"],
        ["2", "1", "8", "2", "8", "1", "2", "X10", "1", "30"],
        ["1", "8", "2", "1", "2", "X11", "1", "2", "8", "26"],
        ["X8", "2", "1", "8", "1", "2", "8", "1", "2", "28"],
        ["10", "9", "9", "9", "10", "9", "10", "10", "10", "."]
    ]
        tablero_estudiante = Tablero()
        tablero_estudiante.tablero = tablero

        resultado_estudiante = tablero_estudiante.validar()

        self.assertIsNotNone(resultado_estudiante)
        self.assertFalse(resultado_estudiante)


    @timeout(N_SECOND)
    def test_10_validar_True_6(self):
        """
        
        """

        tablero = [
            ["X2", "X13", "X4", "2"],
            ["X4", "X3", "X8", "4"],
            ["X3", "X12", "X5", "8"],
            ["X2", "X5", "X4", "9"],
            [".", "5", "7", "."]
        ]

        tablero_estudiante = Tablero()
        tablero_estudiante.tablero = tablero

        resultado_estudiante = tablero_estudiante.validar()

        self.assertIsNotNone(resultado_estudiante)
        self.assertFalse(resultado_estudiante)

    @timeout(N_SECOND)
    def test_11_validar_False_6(self):
        """
        
        """

        tablero = [
            [".", ".", ".", "10"],
            [".", ".", ".", "4"],
            [".", ".", ".", "6"],
            [".", ".", ".", "9"],
            [".", ".", ".", "8"],
            ["1", "3", "7", "."]
        ]

        tablero_estudiante = Tablero()
        tablero_estudiante.tablero = tablero

        resultado_estudiante = tablero_estudiante.validar()

        self.assertIsNotNone(resultado_estudiante)
        self.assertFalse(resultado_estudiante)