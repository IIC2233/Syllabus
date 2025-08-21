import os
import sys
import unittest
from dccasillas import DCCasillas
from tests_publicos.timeout_function import timeout

sys.stdout = open(os.devnull, 'w')

N_SECOND = 10


class TestRecuperaEstado(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_00_tablero_simple(self):
        """
        Un archivo con tablero simple
        """
        juego = DCCasillas("usuario_1", "configuracion1.txt")
        recupera = juego.recuperar_estado()
        usuario = juego.usuario
        tableros = juego.tableros

        tablero_esperado = [
            ["X2", ".", "1", ".", "4", "."],
            ["3", ".", "2", ".", "1", "."],
            ["4", "2", "3", "2", "2", "10"],
            ["7", ".", "3", ".", "3", "."]
        ]

        elementos_esperados = [tablero_esperado, 3, False]
        elementos_estudiante = [tableros[0].tablero, tableros[0].movimientos, tableros[0].estado]

        self.assertEqual(recupera, True)
        self.assertEqual(usuario, "usuario_1")
        self.assertListEqual(elementos_esperados, elementos_estudiante)

    @timeout(N_SECOND)
    def test_01_dos_tableros_combinado(self):
        """
        Archivo con dos tableros, uno resuelto
        """

        juego = DCCasillas("usuario_2", "configuracion2.txt")
        recupera = juego.recuperar_estado()
        usuario = juego.usuario
        tableros = juego.tableros

        tablero_1 = [
            ["X2", ".", "1", ".", "X4", "."],
            ["3", ".", "2", ".", "1", "."],
            ["4", "2", "X3", "2", "2", "10"],
            ["7", ".", "3", ".", "3", "."]
        ]

        tablero_2 = [
            ["13", ".", "14", "7", ".", "X4", "8"],
            ["1", "11", "11", ".", "15", ".", "6"],
            ["X9", "6", "13", ".", "6", "1", "15"],
            ["5", "4", "11", "X5", ".", ".", "."],
            ["6", ".", "2", "15", "11", "X10", "7"],
            [".", ".", ".", "14", ".", "16", "."]
        ]

        elementos_esperados = [
            [tablero_1, 4, True],
            [tablero_2, 6, False]
        ]

        elementos_estudiante = [
            [tableros[0].tablero, tableros[0].movimientos, tableros[0].estado],
            [tableros[1].tablero, tableros[1].movimientos, tableros[1].estado]
        ]

        self.assertEqual(recupera, True)
        self.assertEqual(usuario, "usuario_2")
        self.assertListEqual(elementos_esperados, elementos_estudiante)

    @timeout(N_SECOND)
    def test_02_tableros_resueltos(self):
        """
        Archivo con dos tableros, ambos resueltos
        """

        juego = DCCasillas("usuario_3", "configuracion3.txt")
        recupera = juego.recuperar_estado()
        usuario = juego.usuario
        tableros = juego.tableros

        tablero_1 = [
            ["X2", ".", "1", ".", "X4", "."],
            ["3", ".", "2", ".", "1", "."],
            ["4", "2", "X3", "2", "2", "10"],
            ["7", ".", "3", ".", "3", "."]
        ]

        tablero_2 = [
            ["6", ".", "4", "1", "10", "."],
            ["6", "3", ".", "5", "9", "."],
            ["10", "X3", "13", "7", "10", "."],
            ["X4", ".", "3", "7", "X16", "10"],
            ["5", "3", ".", "X7", "X5", "8"],
            [".", "6", ".", ".", ".", "."]
        ]

        elementos_esperados = [
            [tablero_1, 8, True],
            [tablero_2, 5, True]
        ]

        elementos_estudiante = [
            [tableros[0].tablero, tableros[0].movimientos, tableros[0].estado],
            [tableros[1].tablero, tableros[1].movimientos, tableros[1].estado]
        ]

        self.assertEqual(recupera, True)
        self.assertEqual(usuario, "usuario_3")
        self.assertListEqual(elementos_esperados, elementos_estudiante)

    @timeout(N_SECOND)
    def test_03_tablero_usuario_exotico(self):
        """
        Archivo con nombre repetido pero con tildes
        """

        juego = DCCasillas("usuarioo", "configuracion4.txt")
        recupera = juego.recuperar_estado()
        usuario = juego.usuario
        tableros = juego.tableros

        tablero_1 = [
            ["5", ".", "12", ".", "8", "X7", ".", ".", ".", "13"],
            ["4", "8", "X16", "11", "X17", "14", ".", "5", ".", "11"],
            [".", "12", "13", ".", "X4", "12", "X9", "X2", "X14", "6"],
            ["X2", ".", ".", "13", "7", "4", ".", ".", "13", "."],
            ["X16", ".", "9", "8", "3", ".", "9", "7", "7", "12"],
            [".", "1", "1", ".", "11", "X6", "X16", "10", ".", "17"],
            ["9", "20", ".", ".", ".", "6", ".", ".", "18", "."]
        ]

        elementos_esperados = [
            [tablero_1, 23, False]
        ]

        elementos_estudiante = [
            [tableros[0].tablero, tableros[0].movimientos, tableros[0].estado]
        ]

        self.assertEqual(recupera, True)
        self.assertEqual(usuario, "usuarioo")
        self.assertListEqual(elementos_esperados, elementos_estudiante)

    @timeout(N_SECOND)
    def test_04_tablero_tres(self):
        """
        Archivo con tres tableros
        """

        juego = DCCasillas("usuario_4", "configuracion5.txt")
        recupera = juego.recuperar_estado()
        usuario = juego.usuario
        tableros = juego.tableros

        tablero_1 = [
            ["X2", ".", "1", ".", "X4", "."],
            ["3", ".", "2", ".", "1", "."],
            ["4", "2", "X3", "2", "2", "10"],
            ["7", ".", "3", ".", "3", "."]
        ]

        tablero_6 = [
            ["6", ".", "4", "1", "10", "."],
            ["6", "3", ".", "5", "9", "."],
            ["10", "X3", "13", "7", "10", "."],
            ["X4", ".", "3", "7", "X16", "10"],
            ["5", "3", ".", "X7", "X5", "8"],
            [".", "6", ".", ".", ".", "."]
        ]

        tablero_3 = [
            ["10", "1", "2", "X3", "17", ".", ".", "X6", ".", ".", "3"],
            ["12", "15", "2", ".", "5", "X15", "12", "1", "7", "5", "9"],
            ["X7", "9", "17", "X3", ".", "X3", ".", "2", "3", "4", "4"],
            [".", "17", "4", "7", "15", "15", ".", ".", ".", "3", "."],
            [".", ".", ".", "16", ".", "13", "15", "11", "2", ".", "14"],
            [".", "10", ".", "1", ".", "2", "4", ".", ".", "X9", "."],
            ["X1", "6", ".", "12", "3", ".", "7", "17", ".", ".", "3"],
            [".", "6", "X11", "3", "3", "12", "11", "16", ".", "16", "8"],
            [".", ".", "8", "1", "X11", "X17", "15", "X16", "13", ".", "."],
            ["X11", "16", "16", ".", "17", ".", "7", "14", "13", "11", "."],
            ["4", ".", "12", "9", "5", ".", ".", ".", "11", ".", "."]
        ]

        elementos_esperados = [
            [tablero_3, 27, False],
            [tablero_1, 4, True],
            [tablero_6, 6, True]
        ]

        elementos_estudiante = [
            [tableros[0].tablero, tableros[0].movimientos, tableros[0].estado],
            [tableros[1].tablero, tableros[1].movimientos, tableros[1].estado],
            [tableros[2].tablero, tableros[2].movimientos, tableros[2].estado]
        ]

        self.assertEqual(recupera, True)
        self.assertEqual(usuario, "usuario_4")
        self.assertListEqual(elementos_esperados, elementos_estudiante)

    @timeout(N_SECOND)
    def test_05_tablero_dos_resueltos(self):
        """
        Archivo con dos tableros resueltos
        """

        juego = DCCasillas("usuario", "configuracion6.txt")
        recupera = juego.recuperar_estado()
        usuario = juego.usuario
        tableros = juego.tableros

        tablero_1 = [
            ["X2", ".", "1", ".", "X4", "."],
            ["3", ".", "2", ".", "1", "."],
            ["4", "2", "X3", "2", "2", "10"],
            ["7", ".", "3", ".", "3", "."]
        ]

        tablero_2 = [
            ["13", ".", "14", "7", ".", "X4", "8"],
            ["1", "11", "11", ".", "15", ".", "6"],
            ["X9", "6", "13", ".", "6", "1", "15"],
            ["5", "4", "11", "X5", ".", ".", "."],
            ["6", ".", "2", "15", "11", "X10", "7"],
            [".", ".", ".", "14", ".", "16", "."]
        ]

        tablero_4 = [
            [".", ".",  "13",  "1",     "X8", ".",    "X16", "14"],
            ["X8", "4", "X11",  "X12",   "3",   "12", "7", "."],
            ["7", "3",  "X2",  ".",    ".",    "X14", "9", "19"],
            ["3", "2",  "X7",   "1",   "X17",   "X9", ".", "6"],
            [".", "4",  "2",  ".",     "X15",   "X5", "2", "8"],
            ["3", "X2",  ".",  ".",    "7",     ".", "X6", "10"],
            ["1", "X15", ".",  "6",   "X13",    "X17", ".", "7"],
            [".", "13", ".",    ".",   ".",       ".", "18", "."]
        ]

        elementos_esperados = [
                    [tablero_4, 19, True],
                    [tablero_1, 7, True],
                    [tablero_2, 4, False]
                ]

        elementos_estudiante = [
            [tableros[0].tablero, tableros[0].movimientos, tableros[0].estado],
            [tableros[1].tablero, tableros[1].movimientos, tableros[1].estado],
            [tableros[2].tablero, tableros[2].movimientos, tableros[2].estado]
        ]

        self.assertEqual(recupera, True)
        self.assertEqual(usuario, "usuario")
        self.assertListEqual(elementos_esperados, elementos_estudiante)

    @timeout(N_SECOND)
    def test_06_tablero_no_guardado(self):
        """
        Archivo que no existe
        """

        juego = DCCasillas("usuario_2233", "configuracion1.txt")
        recupera = juego.recuperar_estado()

        self.assertEqual(recupera, False)

    @timeout(N_SECOND)
    def test_07_tablero_incompleto(self):
        """
        Archivo incompleto
        """

        juego = DCCasillas("usuario_5", "configuracion1.txt")
        recupera = juego.recuperar_estado()

        self.assertEqual(recupera, False)

    @timeout(N_SECOND)
    def test_08_coordenadas_negativas(self):
        """
        Archivo que tiene números negativos y no corresponde
        """

        juego = DCCasillas("usuario_6", "configuracion1.txt")
        recupera = juego.recuperar_estado()

        self.assertEqual(recupera, False)
