import os
import sys
import unittest
from tablero import Tablero
from tests_privados.timeout_function import timeout

sys.stdout = open(os.devnull, 'w')
N_SECOND = 7


class TestInitTablero(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_00_verificar_tipo_atributos_obligatorios(self):
        """
        Verifica que los atributos obligatorios tengan el tipo correcto
        """
        tablero = Tablero()

        self.assertIsInstance(tablero.tablero, list, "self.tablero debe ser una lista")

        self.assertIsInstance(tablero.movimientos, int, "self.movimientos debe ser un int")

        self.assertIsInstance(tablero.estado, bool, "self.estado debe ser un bool")

    @timeout(N_SECOND)
    def test_01_verificar_valores_iniciales_atributos_obligatorios(self):
        """
        Verifica que los atributos obligatorios tengan los valores iniciales correctos
        """
        tablero = Tablero()

        self.assertEqual(tablero.tablero, [], "self.tablero debe inicializarse con una lista vacía")

        self.assertEqual(tablero.movimientos, 0, "self.movimientos debe inicializarse en 0")

        self.assertEqual(tablero.estado, False, "self.estado debe inicializarse en False")

    @timeout(N_SECOND)
    def test_02_verificar_estructura_lista_de_listas(self):
        """
        Verifica que self.tablero sea una lista de listas
        """
        tablero = Tablero()

        self.assertIsInstance(tablero.tablero, list, "self.tablero debe ser una lista")

        tablero.tablero.append(["1", "2", "3"])
        tablero.tablero.append([".", "2", "."])
        tablero.tablero.append([".", "4", "."])

        self.assertIsInstance(tablero.tablero[0], list, "self.tablero debe poder contener listas")

    @timeout(N_SECOND)
    def test_03_verificar_atributos_no_nulos(self):
        """
        Verifica que los atributos obligatorios no sean None
        """
        tablero = Tablero()

        self.assertIsNotNone(tablero.tablero, "self.tablero no debe ser None")

        self.assertIsNotNone(tablero.movimientos, "self.movimientos no debe ser None")

        self.assertIsNotNone(tablero.estado, "self.estado no debe ser None")

    @timeout(N_SECOND)
    def test_04_verificar_instancia_independiente(self):
        """
        Verifica que cada instancia de Tablero tenga atributos independientes
        """
        tablero1 = Tablero()
        tablero2 = Tablero()

        tablero1.tablero.append(["1", "2", "3"])
        tablero1.tablero.append([".", "2", "."])
        tablero1.tablero.append([".", "4", "."])
        tablero1.movimientos = 5
        tablero1.estado = True

        self.assertEqual(tablero2.tablero, [], "Cada instancia debe tener su propia lista tablero")
        self.assertEqual(tablero2.movimientos, 0, "Cada tablero debe tener contar sus movimientos")
        self.assertFalse(tablero2.estado, "Cada instancia debe tener su propio estado")

    @timeout(N_SECOND)
    def test_05_verificar_int_movimientos(self):
        """
        Verifica que Tablero pueda aumentar movimientos
        """
        tablero = Tablero()
        tablero.movimientos += 1

        self.assertEqual(tablero.movimientos, 1, "Se deben poder sumar movimientos")

    @timeout(N_SECOND)
    def test_06_verificar_bool_estado(self):
        """
        Verifica que Tablero pueda cambiar de estado
        """
        tablero = Tablero()
        tablero_original = tablero.estado
        tablero.estado = True
        tablero_modificado = tablero.estado

        self.assertTrue(tablero_modificado, "Se debe poder cambiar el estado")
        self.assertFalse(tablero_original, "Se debe poder cambiar el estado")

    @timeout(N_SECOND)
    def test_07_verificar_dos_tableros(self):
        """
        Verifica que genere 2 tableros bien e independientes
        """
        tablero = Tablero()
        tablero2 = Tablero()

        self.assertFalse(tablero.estado, "El estado comienza como False")
        self.assertFalse(tablero2.estado, "El estado comienza como False")

        self.assertEqual(tablero.tablero, [], "Cada instancia debe tener su propia lista tablero")
        self.assertEqual(tablero2.tablero, [], "Cada instancia debe tener su propia lista tablero")

        self.assertEqual(tablero.movimientos, 0, "Cada tablero debe tener contar sus movimientos")
        self.assertEqual(tablero2.movimientos, 0, "Cada tablero debe tener contar sus movimientos")

    @timeout(N_SECOND)
    def test_08_verificar_dos_tableros_independientes(self):
        """
        Verifica que genere 2 tableros bien y que no sean lo mismo
        """
        tablero = Tablero()
        tablero2 = Tablero()

        self.assertIsNot(tablero, tablero2)

    @timeout(N_SECOND)
    def test_09_verificar_dos_tableros(self):
        """
        Se verifica que efectivamente tiene los atributos
        """
        tablero = Tablero()

        self.assertTrue(hasattr(tablero, "estado"), "El estado debería ser un atributo")
        self.assertTrue(hasattr(tablero, "movimientos"), "Los movimientos deberían ser un atributo")
        self.assertTrue(hasattr(tablero, "tablero"), "El tablero debería ser un atributo")
