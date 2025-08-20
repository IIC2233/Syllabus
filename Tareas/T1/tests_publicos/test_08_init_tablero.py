import os
import sys
import unittest
from tablero import Tablero
from tests_publicos.timeout_function import timeout

sys.stdout = open(os.devnull, 'w')
N_SECOND = 10

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
        
        self.assertEqual(tablero.tablero, [], "self.tablero debe inicializarse como una lista vacía")
        
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
        self.assertEqual(tablero2.movimientos, 0, "Cada instancia debe tener su propio contador de movimientos")
        self.assertEqual(tablero2.estado, False, "Cada instancia debe tener su propio estado")


if __name__ == '__main__':
    unittest.main()
