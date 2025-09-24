# Test numero: 0
import sys, os
import unittest

from tests_privados.timeout_function import timeout

from tablero import Tablero

sys.stdout = open(os.devnull, "w")

N_SECOND = 10


class TestCargartablero(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None
    

    @timeout(N_SECOND)
    def test_00_cargar_tablero(self):
        """
        Carga un tablero 3x3 simple
        """

        tablero_esperado = [
            ["3", "1", "4"],
            ["5", ".", "."],
            [".", "1", "."]
        ]
        tablero_estudiante = Tablero()
        tablero_estudiante.cargar_tablero("tablero11.txt")
        
        self.assertIsNotNone(tablero_estudiante.tablero)
        self.assertListEqual(tablero_esperado, tablero_estudiante.tablero)
        
        
    @timeout(N_SECOND)
    def test_01_cargar_tablero(self):
        """
        Carga un tablero 3x4 simple
        """

        tablero_esperado = [
            ["1", "2", "3", "3"],
            ["4", "5", "6", "9"],
            ["5", "7", "9", "."]
        ]
        tablero_estudiante = Tablero()
        tablero_estudiante.cargar_tablero("tablero12.txt")
        
        self.assertIsNotNone(tablero_estudiante.tablero)
        self.assertListEqual(tablero_esperado, tablero_estudiante.tablero)
        

    @timeout(N_SECOND)
    def test_02_cargar_tablero(self):
        """
        Carga un tablero 6x6
        """

        tablero_esperado = [
            ["2", "3", ".", ".", "1", "6"],
            [".", "4", ".", "1", ".", "5"],
            ["1", ".", "2", "3", ".", "6"],
            [".", ".", "1", "2", ".", "3"],
            ["3", "1", ".", ".", "2", "6"],
            ["6", "8", "3", "6", "3", "."]
        ]
        tablero_estudiante = Tablero()
        tablero_estudiante.cargar_tablero("tablero13.txt")
        
        self.assertIsNotNone(tablero_estudiante.tablero)
        self.assertListEqual(tablero_esperado, tablero_estudiante.tablero)
        

    @timeout(N_SECOND)
    def test_03_cargar_tablero(self):
        """
        Carga un tablero 8x5
        """

        tablero_esperado = [
            ["1", "2", ".", "3", "6"],
            [".", "3", "2", "1", "6"],
            ["2", ".", "1", ".", "3"],
            ["3", "1", ".", ".", "4"],
            [".", "2", "2", "1", "5"],
            ["1", ".", ".", "3", "4"],
            ["2", "1", "3", ".", "6"],
            ["5", "6", "5", "8", "."]
        ]
        tablero_estudiante = Tablero()
        tablero_estudiante.cargar_tablero("tablero14.txt")
        
        self.assertIsNotNone(tablero_estudiante.tablero)
        self.assertListEqual(tablero_esperado, tablero_estudiante.tablero)
        

    @timeout(N_SECOND)
    def test_04_cargar_tablero(self):
        """
        Carga un tablero 9x9
        """

        tablero_esperado = [
            ["1", "8", ".", "4", "4", "8", "7", "2", "24"],
            ["1", "1", ".", ".", "5", "3", "3", "6", "15"],
            ["3", "2", "7", "4", "1", ".", "3", "5", "14"],
            ["9", "6", "2", "4", "2", "1", "3", "9", "12"],
            [".", "4", "1", "0", "9", "9", ".", "3", "14"],
            ["9", "3", ".", "2", "8", "9", "7", "9", "17"],
            ["3", "8", "2", "2", "1", "5", "6", "4", "14"],
            ["8", "4", "7", ".", "4", ".", "7", "6", "18"],
            ["1", "20", "12", "12", "21", "26", "25", "11", "."]
        ]
        tablero_estudiante = Tablero()
        tablero_estudiante.cargar_tablero("tablero15.txt")
        
        self.assertIsNotNone(tablero_estudiante.tablero)
        self.assertListEqual(tablero_esperado, tablero_estudiante.tablero)
        

    @timeout(N_SECOND)
    def test_05_cargar_tablero(self):
        """
        Carga un tablero 11x13
        """

        tablero_esperado = [
            ["1", "2", ".", "1", "3", "2", ".", ".", "1", "2", "1", "3", "17"],
            ["2", ".", "1", "2", "2", "1", "3", ".", ".", "1", "2", "1", "15"],
            [".", "3", "1", "1", "2", "2", "1", "2", ".", "3", "1", "2", "18"],
            ["3", "1", "2", ".", ".", "3", "1", "2", "1", "2", "1", ".", "16"],
            [".", "1", "3", "2", "1", ".", "2", "1", "3", "1", "2", "1", "17"],
            ["1", ".", "2", "1", "2", "3", "1", ".", "1", "2", "3", "1", "17"],
            ["2", "1", ".", "2", "1", "2", ".", "3", "1", "1", "2", "2", "17"],
            [".", "2", "1", "3", "2", "1", "2", "1", ".", "3", "1", "2", "18"],
            ["3", "1", "2", "1", ".", "2", "1", "2", "3", "1", "2", ".", "18"],
            ["1", "3", ".", "2", "1", "1", "2", "2", "1", ".", "3", "2", "18"],
            ["17", "16", "14", "15", "14", "15", "14", "12", "14", "15", "18", "14", "."]
        ]
        tablero_estudiante = Tablero()
        tablero_estudiante.cargar_tablero("tablero16.txt")
        
        self.assertIsNotNone(tablero_estudiante.tablero)
        self.assertListEqual(tablero_esperado, tablero_estudiante.tablero)
        

    @timeout(N_SECOND)
    def test_06_cargar_tablero(self):
        """
        Carga un tablero 6x4 todo vacio
        """

        tablero_esperado = [
            [".", ".", ".", "10"],
            [".", ".", ".", "4"],
            [".", ".", ".", "6"],
            [".", ".", ".", "9"],
            [".", ".", ".", "8"],
            ["1", "3", "7", "."]
        ]
        tablero_estudiante = Tablero()
        tablero_estudiante.cargar_tablero("tablero19.txt")
        
        self.assertIsNotNone(tablero_estudiante.tablero)
        self.assertListEqual(tablero_esperado, tablero_estudiante.tablero)
        

    @timeout(N_SECOND)
    def test_07_cargar_tablero(self):
        """
        Carga un tablero 6x6 todo del mismo numero
        """

        tablero_esperado = [
            ["7", "7", "7", "7", "7", "7"],
            ["7", "7", "7", "7", "7", "7"],
            ["7", "7", "7", "7", "7", "7"],
            ["7", "7", "7", "7", "7", "7"],
            ["7", "7", "7", "7", "7", "7"],
            ["7", "7", "7", "7", "7", "."]
        ]
        tablero_estudiante = Tablero()
        tablero_estudiante.cargar_tablero("tablero20.txt")
        
        self.assertIsNotNone(tablero_estudiante.tablero)
        self.assertListEqual(tablero_esperado, tablero_estudiante.tablero)
    
    
    @timeout(N_SECOND)
    def test_08_cargar_tablero(self):
        """
        Carga un tablero 4x7 con filas y columnas objetivos de 0's
        """
        
        tablero_esperado = [
            ["5", "4", "7", "10", "9", "17", "0"],
            ["22", "1", "1", "13", "20", "2", "0"],
            ["54", "6", "14", "15", "1", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "."]
        ]
        tablero_estudiante = Tablero()
        tablero_estudiante.cargar_tablero("tablero21.txt")
        
        self.assertIsNotNone(tablero_estudiante.tablero)
        self.assertListEqual(tablero_esperado, tablero_estudiante.tablero)