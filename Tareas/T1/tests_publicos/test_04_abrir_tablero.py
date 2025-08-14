import os
import sys
import unittest
from dccasillas import DCCasillas
from tests_publicos.timeout_function import timeout

sys.stdout = open(os.devnull, 'w')

N_SECOND = 10


class TestAbrirTablero(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_00_tablero_chico(self):
        """
        Tablero de chico unico
        """

        juego = DCCasillas("usuario_1", "configuracion1.txt")
        abrir = juego.abrir_tablero(0)
        tablero_actual = juego.tablero_actual

        self.assertIsNone(abrir)
        self.assertEqual(tablero_actual, 0)

    @timeout(N_SECOND)
    def test_01_tablero_mediano(self):
        """
        Tablero mediano, segundo
        """

        juego = DCCasillas("usuario_1", "configuracion4.txt")
        abrir = juego.abrir_tablero(0)
        tablero_actual = juego.tablero_actual

        self.assertIsNone(abrir)
        self.assertEqual(tablero_actual, 0)

    @timeout(N_SECOND)
    def test_02_tablero_grande(self):
        """
        Tablero de grande, primero
        """

        juego = DCCasillas("usuario_1", "configuracion7.txt")
        abrir = juego.abrir_tablero(0)
        tablero_actual = juego.tablero_actual

        self.assertIsNone(abrir)
        self.assertEqual(tablero_actual, 0)

    @timeout(N_SECOND)
    def test_03_tablero_grande2(self):
        """
        Tablero grande
        """

        juego = DCCasillas("usuario_1", "configuracion5.txt")
        abrir = juego.abrir_tablero(0)
        tablero_actual = juego.tablero_actual

        self.assertIsNone(abrir)
        self.assertEqual(tablero_actual, 0)

    @timeout(N_SECOND)
    def test_04_tablero_del_medio(self):
        """
        Tablero del medio
        """

        juego = DCCasillas("usuario_1", "configuracion8.txt")
        abrir = juego.abrir_tablero(3)
        tablero_actual = juego.tablero_actual

        self.assertIsNone(abrir)
        self.assertEqual(tablero_actual, 3)

    @timeout(N_SECOND)
    def test_05_dos_cambios(self):
        """
        Dos cambios de tableros
        """

        juego = DCCasillas("usuario_1", "configuracion8.txt")
        abrir = juego.abrir_tablero(4)
        abrir2 = juego.abrir_tablero(2)
        tablero_actual = juego.tablero_actual
        self.assertIsNone(abrir)
        self.assertIsNone(abrir2)
        self.assertEqual(tablero_actual, 2)

    @timeout(N_SECOND)
    def test_06_tres_cambios(self):
        """
        Tres cambios de tableros
        """

        juego = DCCasillas("usuario_1", "configuracion8.txt")
        abrir = juego.abrir_tablero(2)
        abrir2 = juego.abrir_tablero(3)
        abrir_3 = juego.abrir_tablero(0)
        tablero_actual = juego.tablero_actual

        self.assertIsNone(abrir)
        self.assertIsNone(abrir2)
        self.assertIsNone(abrir_3)
        self.assertEqual(tablero_actual, 0)

    @timeout(N_SECOND)
    def test_07_ultimo_tablero(self):
        """
        Ultimo tablero
        """

        juego = DCCasillas("usuario_1", "configuracion8.txt")
        abrir = juego.abrir_tablero(5)
        tablero_actual = juego.tablero_actual

        self.assertIsNone(abrir)
        self.assertEqual(tablero_actual, 5)

    @timeout(N_SECOND)
    def test_08_ultimo_tablero(self):
        """
        Ultimo tablero
        """

        juego = DCCasillas("usuario_1", "configuracion8.txt")
        abrir = juego.abrir_tablero(1)
        abrir2 = juego.abrir_tablero(1)
        tablero_actual = juego.tablero_actual

        self.assertIsNone(abrir)
        self.assertIsNone(abrir2)
        self.assertEqual(tablero_actual, 1)

    @timeout(N_SECOND)
    def test_09_tablero_medio(self):
        """
        Cualquier tablero
        """

        juego = DCCasillas("usuario_1", "configuracion9.txt")
        abrir = juego.abrir_tablero(5)
        tablero_actual = juego.tablero_actual

        self.assertIsNone(abrir)
        self.assertEqual(tablero_actual, 5)
