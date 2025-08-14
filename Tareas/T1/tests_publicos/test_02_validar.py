import unittest

from tablero import Tablero 

from tests_publicos.timeout_function import timeout

N_SECOND = 5

class TestValidar(unittest.TestCase):
    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None
    

    @timeout(N_SECOND)
    def test_00_validar_False_1(self):
        """
        Valida que un tablero 2x4 retorna False
        """
        tablero = [["1", "2", "3", "4"],
                   [".", ".", ".", "."]]

        tablero_estudiante = Tablero()
        tablero_estudiante.tablero = tablero

        resultado_estudiante = tablero_estudiante.validar()

        self.assertIsNotNone(resultado_estudiante)
        self.assertFalse(resultado_estudiante, "Se espera que sea False")

    
    @timeout(N_SECOND)
    def test_01_validar_False_2(self):
        """
        Valida que un tablero 4x5 retorna False
        """
        tablero = [["5", "3", "4", "8", "20"],
                   [".", ".", ".", ".", "5"],
                   ["1", ".", ".", "4", "5"],
                   ["6", "3", "4", "12", "."]]
        
        tablero_estudiante = Tablero()
        tablero_estudiante.tablero = tablero

        resultado_estudiante = tablero_estudiante.validar()

        self.assertIsNotNone(resultado_estudiante)
        self.assertFalse(resultado_estudiante, "Se espera que sea False")

    
    @timeout(N_SECOND)
    def test_02_validar_False_3(self):
        """
        Valida que un tablero 4x4 retorna False
        """
        tablero = [["1", "2", ".", "5"],
                   ["4", ".", "3", "8"],
                   [".", "3", "2", "5"],
                   ["6", "5", "6", "."]]

        tablero_estudiante = Tablero()
        tablero_estudiante.tablero = tablero

        resultado_estudiante = tablero_estudiante.validar()

        self.assertIsNotNone(resultado_estudiante)
        self.assertFalse(resultado_estudiante, "Se espera que sea False")

    
    @timeout(N_SECOND)
    def test_03_validar_False_4(self):
        """
        Valida que un tablero 5x8 retorna False
        """
        tablero = [["5", "3", ".", "4", "2", "1", "2", "20"],
                   ["2", ".", "3", ".", "4", "2", "3", "15"],
                   [".", "4", "2", "3", ".", "5", "2", "14"],
                   ["1", "1", "1", "1", "1", "1", "1", "7"],
                   ["15", "12", "9", "15", "9", "13", "5", "."]]

        tablero_estudiante = Tablero()
        tablero_estudiante.tablero = tablero

        resultado_estudiante = tablero_estudiante.validar()

        self.assertIsNotNone(resultado_estudiante)
        self.assertFalse(resultado_estudiante, "Se espera que sea False")

    
    @timeout(N_SECOND)
    def test_04_validar_False_5(self):
        """
        Valida que un tablero 7x7 retorna False
        """
        tablero = [["10", "5", "3", "2", "1", "8","30"],
                   ["9", "4", "2", "1", "7", "6","29"],
                   ["8", "3", "1", "6", "5", "4","."],
                   ["7", "2", "5", "4", "3", "1","22"],
                   ["6", "1", "4", "3", "2", "9","."],
                   ["5", "9", "8", "7", "6", "10","45"],
                   [".", "24", ".", ".", "24", ".", "."]]

        tablero_estudiante = Tablero()
        tablero_estudiante.tablero = tablero

        resultado_estudiante = tablero_estudiante.validar()

        self.assertIsNotNone(resultado_estudiante)
        self.assertFalse(resultado_estudiante, "Se espera que sea False")


    @timeout(N_SECOND)
    def test_05_validar_False_6(self):
        """
        Valida que un tablero 4x5 (vacio) retorna False
        """
        tablero = [[".",".",".",".","3"],
                   [".",".",".",".","4"],
                   [".",".",".",".","9"],
                   ["5",".","1",".","."]]
    
        tablero_estudiante = Tablero()
        tablero_estudiante.tablero = tablero

        resultado_estudiante = tablero_estudiante.validar()

        self.assertIsNotNone(resultado_estudiante)
        self.assertFalse(resultado_estudiante, "Se espera que sea False")
    

    @timeout(N_SECOND)
    def test_06_validar_True_1(self):
        """
        Valida que un tablero 6x2 retorna True
        """
        tablero = [["1", "1"],
                   ["2", "2"],
                   ["3", "3"],
                   ["4", "."],
                   ["0", "."], 
                   ["10", "."]]

        tablero_estudiante = Tablero()
        tablero_estudiante.tablero = tablero

        resultado_estudiante = tablero_estudiante.validar()

        self.assertIsNotNone(resultado_estudiante)
        self.assertTrue(resultado_estudiante, "Se espera que sea True")

    
    @timeout(N_SECOND)
    def test_07_validar_True_2(self):
        """
        Valida que un tablero 5x3 (con el mismo numero) retorna True
        """
        tablero = [["0", "0", "0"],
                   ["0", "0", "0"],
                   ["0", "0", "0"],
                   ["0", "0", "0"],
                   ["0", "0", "."]]

        tablero_estudiante = Tablero()
        tablero_estudiante.tablero = tablero

        resultado_estudiante = tablero_estudiante.validar()

        self.assertIsNotNone(resultado_estudiante)
        self.assertTrue(resultado_estudiante, "Se espera que sea True")


    @timeout(N_SECOND)
    def test_08_validar_True_3(self):
        """
        Valida tablero 8x5 retorna True
        """
        tablero = [[".", ".", ".", "." ,"."],
                   [".", ".", ".", "." ,"."],
                   ["5", ".", ".", "." ,"5"],
                   [".", "2", "1", "1" ,"4"],
                   ["8", ".", "1", ".", "9"],
                   ["2", ".", ".", "." ,"."],
                   [".", "5", ".", "." ,"."],
                   ["15", "7", "2", "1", "."]]


        tablero_estudiante = Tablero()
        tablero_estudiante.tablero = tablero

        resultado_estudiante = tablero_estudiante.validar()

        self.assertIsNotNone(resultado_estudiante)
        self.assertTrue(resultado_estudiante, "Se espera que sea True")

    
    @timeout(N_SECOND)
    def test_09_validar_True_4(self):
        """
        Valida tablero 5x5 retorna True
        """
        tablero = [[".", "23", "1", "27", "51"],
                   ["2", "2", ".", "8", "12"],
                   ["3", "12", ".", "9", "24"],
                   [".", ".", ".", "3", "3"],
                   ["5", "37", "1", "47", "."]]

        tablero_estudiante = Tablero()
        tablero_estudiante.tablero = tablero

        resultado_estudiante = tablero_estudiante.validar()

        self.assertIsNotNone(resultado_estudiante)
        self.assertTrue(resultado_estudiante, "Se espera que sea True")