import unittest

from tablero import Tablero

from tests_publicos.timeout_function import timeout

N_SECOND = 10

class TestCargarTablero(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None
    

    @timeout(N_SECOND)
    def test_00_cargar_tablero(self):
        """
        Carga un tablero 2x5
        """
        tablero_esperado = [["1", "2", "3", "4"],
                            [".", ".", ".", "."]]
        
        resultado_estudiante = Tablero()
        resultado_estudiante.cargar_tablero("tablero01.txt")

        self.assertIsNotNone(resultado_estudiante)
        self.assertListEqual(resultado_estudiante.tablero, tablero_esperado)


    @timeout(N_SECOND)
    def test_01_cargar_tablero(self):
        """
        Carga un tablero 4x6
        """
        tablero_esperado = [["2", ".", "1", ".", "4", "."],
                            ["3", ".", "2", ".", "1", "."],
                            ["4", "2", "3", "2", "2", "10"],
                            ["7", ".", "3", ".", "3", "."]]

        resultado_estudiante = Tablero()
        resultado_estudiante.cargar_tablero("tablero02.txt")

        self.assertIsNotNone(resultado_estudiante)
        self.assertListEqual(resultado_estudiante.tablero, tablero_esperado)


    @timeout(N_SECOND)
    def test_02_cargar_tablero(self):
        """
        Carga un tablero 3x6
        """
        tablero_esperado = [["1", "3", "4", "3", "1", "9"],
                            ["1", "3", "5", "2", "1", "10"],
                            [".", "3", ".", ".", "1", "."]]

        resultado_estudiante = Tablero()
        resultado_estudiante.cargar_tablero("tablero03.txt")

        self.assertIsNotNone(resultado_estudiante)
        self.assertListEqual(resultado_estudiante.tablero, tablero_esperado)


    @timeout(N_SECOND)
    def test_03_cargar_tablero(self):
        """
        Carga un tablero 6x4
        """
        tablero_esperado = [["1", "1", "1", "2"],
                            ["1", ".", "2", "."],
                            ["2", "2", "2", "4"],
                            ["4", ".", "3", "."],
                            ["3", "3", "3", "6"],
                            ["10", "3", "9", "."]]

        resultado_estudiante = Tablero()
        resultado_estudiante.cargar_tablero("tablero04.txt")

        self.assertIsNotNone(resultado_estudiante)
        self.assertListEqual(resultado_estudiante.tablero, tablero_esperado)


    @timeout(N_SECOND)
    def test_04_cargar_tablero(self):
        """
        Carga un tablero 6x6
        """
        tablero_esperado = [[".", "3", ".", "3", ".", "."],
                            ["5", "5", "2", "5", "5", "12"],
                            [".", "1", "1", "1", ".", "2"],
                            ["4", "2", "1", "2", "2", "9"],
                            [".", "2", ".", "1", ".", "."],
                            [".", "10", "3", "10", ".", "."]]

        resultado_estudiante = Tablero()
        resultado_estudiante.cargar_tablero("tablero05.txt")

        self.assertIsNotNone(resultado_estudiante)
        self.assertListEqual(resultado_estudiante.tablero, tablero_esperado)


    @timeout(N_SECOND)
    def test_05_cargar_tablero(self):
        """
        Carga un tablero 6x5 vacio
        """
        tablero_esperado = [[".", ".", ".", ".", "0"],
                            [".", ".", ".", ".", "10"],
                            [".", ".", ".", ".", "24"],
                            [".", ".", ".", ".", "7"],
                            [".", ".", ".", ".", "1"],
                            ["1", "5", "8", "8", "."]]

        resultado_estudiante = Tablero()
        resultado_estudiante.cargar_tablero("tablero06.txt")

        self.assertIsNotNone(resultado_estudiante)
        self.assertListEqual(resultado_estudiante.tablero, tablero_esperado)


    @timeout(N_SECOND)
    def test_06_cargar_tablero(self):
        """
        Carga un tablero 7x5 lleno
        """
        tablero_esperado = [["13", "73", "11", "15", "24"],
                            ["5", "19", "99", "11", "25"],
                            ["8", "5", "1", "2", "3"],
                            ["47", "78", "88", "65", "6"],
                            ["7", "15", "23", "42", "56"],
                            ["9", "12", "34", "21", "18"],
                            ["4", "8", "16", "32", "."]]


        resultado_estudiante = Tablero()
        resultado_estudiante.cargar_tablero("tablero07.txt")

        self.assertIsNotNone(resultado_estudiante)
        self.assertListEqual(resultado_estudiante.tablero, tablero_esperado)

    @timeout(N_SECOND)
    def test_07_cargar_tablero(self):
        """
        Carga un tablero 17x10 masivo        
        """
        tablero_esperado = [
            ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
            ["11", "12", "13", "14", "15", "16", "17", "18", "19", "20"],
            ["21", "22", "23", "24", "25", "26", "27", "28", "29", "30"],
            ["31", "32", "33", "34", "35", "36", "37", "38", "39", "40"],
            ["41", "42", "43", "44", "45", "46", "47", "48", "49", "50"],
            ["51", "52", "53", "54", "55", "56", "57", "58", "59", "60"],
            ["61", "62", "63", "64", "65", "66", "67", "68", "69", "70"],
            ["71", "72", "73", "74", "75", "76", "77", "78", "79", "80"],
            ["81", "82", "83", "84", "85", "86", "87", "88", "89", "90"],
            ["91", "92", "93", "94", "95", "96", "97", "98", "99", "100"],
            ["101", "102", "103", "104", "105", "106", "107", "108", "109", "110"],
            ["111", "112", "113", "114", "115", "116", "117", "118", "119", "120"],
            ["121", "122", "123", "124", "125", "126", "127", "128", "129", "130"],
            ["131", "132", "133", "134", "135", "136", "137", "138", "139", "140"],
            ["141", "142", "143", "144", "145", "146", "147", "148", "149", "150"],
            ["151", "152", "153", "154", "155", "156", "157", "158", "159", "160"],
            ["161", "162", "163", "164", "165", "166", "167", "168", "169", "."]
        ]

        resultado_estudiante = Tablero()
        resultado_estudiante.cargar_tablero("tablero08.txt")

        self.assertIsNotNone(resultado_estudiante)
        self.assertListEqual(resultado_estudiante.tablero, tablero_esperado)


    @timeout(N_SECOND)
    def test_08_cargar_tablero(self):
        """
        Carga un tablero 10x3 masivo
        """

        tablero_esperado = [
            ["12", "45", "78"],
            ["34", "56", "90"],
            ["23", "67", "89"],
            ["11", "22", "33"],
            ["44", "55", "66"],
            ["77", "88", "99"],
            ["10", "20", "30"],
            ["40", "50", "60"],
            ["70", "80", "90"],
            ["13", "26", "."]
        ]

        resultado_estudiante = Tablero()
        resultado_estudiante.cargar_tablero("tablero10.txt")

        self.assertIsNotNone(resultado_estudiante)
        self.assertListEqual(resultado_estudiante.tablero, tablero_esperado)

    @timeout(N_SECOND)
    def test_09_cargar_tablero(self):
        """
        Carga un tablero 4x5 con el mismo numero
        """
        tablero_esperado = [["7", "7", "7", "7", "7"],
                            ["7", "7", "7", "7", "7"],
                            ["7", "7", "7", "7", "7"],
                            ["7", "7", "7", "7", "."]]

        resultado_estudiante = Tablero()
        resultado_estudiante.cargar_tablero("tablero09.txt")

        self.assertIsNotNone(resultado_estudiante)
        self.assertListEqual(resultado_estudiante.tablero, tablero_esperado)