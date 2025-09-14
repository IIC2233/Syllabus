import os
import sys
import unittest
from dccasillas import DCCasillas
from tests_privados.timeout_function import timeout

sys.stdout = open(os.devnull, 'w')

N_SECOND = 5


class TestAbrirTablero(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_00_tablero(self):
        """
        Varios tableros, se pide del medio
        """

        juego = DCCasillas("angelita", "config.txt")
        abrir = juego.abrir_tablero(2)
        tablero_actual = juego.tablero_actual

        self.assertIsNone(abrir)
        self.assertEqual(tablero_actual, 2)

    @timeout(N_SECOND)
    def test_01_tablero_al_medio(self):
        """
        Varios tableros, se pide al medio
        """

        juego = DCCasillas("tanico", "config01.txt")
        abrir = juego.abrir_tablero(4)
        tablero_actual = juego.tablero_actual

        self.assertIsNone(abrir)
        self.assertEqual(tablero_actual, 4)

    @timeout(N_SECOND)
    def test_02_tablero_al_medio(self):
        """
        Tres tableros, se pide el del medio
        """

        juego = DCCasillas("conna", "config02.txt")
        abrir = juego.abrir_tablero(1)
        tablero_actual = juego.tablero_actual

        self.assertIsNone(abrir)
        self.assertEqual(tablero_actual, 1)

    @timeout(N_SECOND)
    def test_03_distintos_tableros(self):
        """
        Se cambian a ambos tableros
        """

        juego = DCCasillas("leilalinda1", "config03.txt")
        abrir = juego.abrir_tablero(0)
        tablero_actual = juego.tablero_actual

        abrir2 = juego.abrir_tablero(1)
        tablero_actual2 = juego.tablero_actual

        self.assertIsNone(abrir)
        self.assertEqual(tablero_actual, 0)
        self.assertIsNone(abrir2)
        self.assertEqual(tablero_actual2, 1)

    @timeout(N_SECOND)
    def test_04_tablero_ultimo(self):
        """
        Se pide el ultimo tablero
        """

        juego = DCCasillas("clubpenguin", "configuracion8.txt")
        abrir = juego.abrir_tablero(5)
        tablero_actual = juego.tablero_actual

        self.assertIsNone(abrir)
        self.assertEqual(tablero_actual, 5)

    @timeout(N_SECOND)
    def test_05_mismo_tablero(self):
        """
        Se vuelve al mismo tablero anterior
        """

        juego = DCCasillas("malalena", "configuracion8.txt")
        abrir = juego.abrir_tablero(4)
        abrir2 = juego.abrir_tablero(2)
        abrir3 = juego.abrir_tablero(4)
        tablero_actual = juego.tablero_actual
        self.assertIsNone(abrir)
        self.assertIsNone(abrir2)
        self.assertIsNone(abrir3)
        self.assertEqual(tablero_actual, 4)

    @timeout(N_SECOND)
    def test_06_tres_cambios(self):
        """
        Tres cambios de tableros
        """

        juego = DCCasillas("Cata_Wis", "configuracion6.txt")
        abrir = juego.abrir_tablero(0)
        tablero_actual = juego.tablero_actual
        abrir2 = juego.abrir_tablero(1)
        tablero_actual2 = juego.tablero_actual
        abrir_3 = juego.abrir_tablero(2)
        tablero_actual3 = juego.tablero_actual

        self.assertIsNone(abrir)
        self.assertIsNone(abrir2)
        self.assertIsNone(abrir_3)
        self.assertEqual(tablero_actual, 0)
        self.assertEqual(tablero_actual2, 1)
        self.assertEqual(tablero_actual3, 2)

    @timeout(N_SECOND)
    def test_07_mismo_tablero(self):
        """
        Abrir el mismo tablero
        """

        juego = DCCasillas("idem", "configuracion3.txt")
        abrir = juego.abrir_tablero(1)
        tablero_actual = juego.tablero_actual
        abrir2 = juego.abrir_tablero(1)
        tablero_actual2 = juego.tablero_actual

        self.assertIsNone(abrir)
        self.assertIsNone(abrir2)
        self.assertEqual(tablero_actual, 1)
        self.assertEqual(tablero_actual2, 1)

    @timeout(N_SECOND)
    def test_08_todos_tableros(self):
        """
        Cambio de todos los tableros
        """

        juego = DCCasillas("himym", "config04.txt")
        abrir = juego.abrir_tablero(0)
        tablero_actual = juego.tablero_actual

        abrir2 = juego.abrir_tablero(1)
        tablero_actual2 = juego.tablero_actual

        abrir3 = juego.abrir_tablero(2)
        tablero_actual3 = juego.tablero_actual

        abrir4 = juego.abrir_tablero(3)
        tablero_actual4 = juego.tablero_actual

        abrir5 = juego.abrir_tablero(4)
        tablero_actual5 = juego.tablero_actual

        abrir6 = juego.abrir_tablero(5)
        tablero_actual6 = juego.tablero_actual

        self.assertIsNone(abrir)
        self.assertIsNone(abrir2)
        self.assertIsNone(abrir3)
        self.assertIsNone(abrir4)
        self.assertIsNone(abrir5)
        self.assertIsNone(abrir6)

        self.assertEqual(tablero_actual, 0)
        self.assertEqual(tablero_actual2, 1)
        self.assertEqual(tablero_actual3, 2)
        self.assertEqual(tablero_actual4, 3)
        self.assertEqual(tablero_actual5, 4)
        self.assertEqual(tablero_actual6, 5)

    @timeout(N_SECOND)
    def test_09_tablero_cualquiera(self):
        """
        Cualquier tablero
        """

        juego = DCCasillas("config04", "config04.txt")
        abrir = juego.abrir_tablero(3)
        tablero_actual = juego.tablero_actual

        self.assertIsNone(abrir)
        self.assertEqual(tablero_actual, 3)
