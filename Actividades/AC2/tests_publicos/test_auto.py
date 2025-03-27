import unittest

from clases import Auto, Vehiculo


class VerificarClaseAuto(unittest.TestCase):

    def test_herencia(self):
        """
        Verifica que la herencia se hace correctamente en Auto.
        """
        self.assertIn(Vehiculo, Auto.__mro__)

    def test_recorrer(self):
        """
        Verifica el texto de recorrer.
        """
        auto = Auto(marca="BMW", rendimiento=5, energia=127.0)
        self.assertEqual(
            auto.recorrer(10),
            "Anduve en auto 10.0Km y eso consume 2.0L de bencina"
        )

    def test_energia(self):
        """
        Verifica que se consuma energia/gasolina luego de recorrer.
        """

        auto = Auto(marca="BMW", rendimiento=5, energia=127.0)
        auto.recorrer(10)

        self.assertEqual(auto.energia, 125.0)

    def test_kilometraje_valor_por_defecto(self):
        """
        Verifica que el kilometraje parta en 0.
        """
        auto = Auto(marca="BMW", rendimiento=5, energia=127.0)
        self.assertEqual(auto.kilometraje, 0.0)

    def test_aumento_kilometraje(self):
        """
        Verifica que el kilometraje avance luego de haber recorrido.
        """

        auto = Auto(marca="BMW", rendimiento=5, energia=127.0)
        auto.recorrer(30)

        self.assertEqual(auto.kilometraje, 30.0)

    def test_recorrer_multiple(self):
        """
        Verifica el texto de recorrer y kilometraje del auto
        cuando es llamado múltiples veces el método recorrer.
        """
        auto = Auto(marca="BMW", rendimiento=5, energia=2.0)
        recorrido = auto.recorrer(8)
        self.assertEqual(recorrido,
                         "Anduve en auto 8.0Km y "
                         "eso consume 1.6L de bencina")
        self.assertEqual(auto.kilometraje, 8)

        recorrido = auto.recorrer(12)
        self.assertEqual(recorrido,
                         "Anduve en auto 2.0Km y "
                         "eso consume 0.4L de bencina")
        self.assertEqual(auto.kilometraje, 10)
