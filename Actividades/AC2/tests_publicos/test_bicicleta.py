import unittest

from clases import Bicicleta, Vehiculo


class VerificarClaseBicicleta(unittest.TestCase):

    def test_herencia(self):
        """
        Verifica que Bicicleta herede correctamente.
        """
        self.assertIn(Vehiculo, Bicicleta.__mro__)

    def test_recorrer(self):
        """
        Verifica el texto de recorrer.
        """
        bici = Bicicleta(marca="Trek", rendimiento=5, energia=0.0)
        recorrido = bici.recorrer(10)
        self.assertEqual(recorrido,
                         "Anduve en bicicleta 10.0Km y "
                         "eso no consume bencina ni energia electrica")

    def test_recorrer_multiple(self):
        """
        Verifica el texto de recorrer cuando es llamado múltiples veces.
        """
        bici = Bicicleta(marca="Trek", rendimiento=5, energia=7.0)
        recorrido = bici.recorrer(8)
        self.assertEqual(recorrido,
                         "Anduve en bicicleta 8.0Km y "
                         "eso no consume bencina ni energia electrica")

        recorrido = bici.recorrer(12)
        self.assertEqual(recorrido,
                         "Anduve en bicicleta 12.0Km y "
                         "eso no consume bencina ni energia electrica")
