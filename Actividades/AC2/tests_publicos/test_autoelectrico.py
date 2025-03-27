import unittest

from clases import AutoElectrico, Auto, MotorElectrico


class VerificaClaseAutoElectrico(unittest.TestCase):

    def test_herencia(self):
        """
        Verifica que herede de MotorElectrico y Auto.
        """

        self.assertIn(Auto, AutoElectrico.__mro__)
        self.assertIn(MotorElectrico, AutoElectrico.__mro__)

    def test_recorrer_funcional(self):
        """
        Verifica el texto de recorrer cuando la batería está buena
        """
        auto = AutoElectrico(marca="Fiat", rendimiento=10, energia=89.1,
                             vida_util_bateria=10)
        self.assertEqual(auto.recorrer(30),
                         "Anduve en auto electrico 30.0Km"
                         " y eso consume 3.0W de energia electrica")

    def test_recorrer_no_funcional(self):
        """
        Verifica el texto de recorrer cuando la batería está muerta.
        """
        auto = AutoElectrico(marca="Fiat", rendimiento=10, energia=89.1,
                             vida_util_bateria=-1)

        self.assertEqual(auto.recorrer(1),
                         "La bateria del auto electrico no funciona")

    def test_energia(self):
        """
        Verifica que se consuma energia/gasolina luego de recorrer.
        """
        auto = AutoElectrico(marca="Tesla robado", rendimiento=1,
                             energia=10.0, vida_util_bateria=10)
        auto.recorrer(5)

        self.assertEqual(auto.energia, 5.0)

    def test_kilometraje_valor_por_defecto(self):
        """
        Verifica que el kilometraje parta en 0.
        """
        auto = AutoElectrico(marca="Tesla", rendimiento=1,
                             energia=10.0, vida_util_bateria=10)

        self.assertEqual(auto.kilometraje, 0.0)

    def test_kilometraje(self):
        """
        Verifica que el kilometraje avance luego de haber recorrido.
        """

        auto = AutoElectrico(marca="Autito", rendimiento=5,
                             energia=12.9, vida_util_bateria=10)
        auto.recorrer(12)

        self.assertEqual(auto.kilometraje, 12.0)

    def test_recorrer_multiple(self):
        """
        Verifica el texto de recorrer, kilometraje del auto y 
        vida útil de la batería del motor
        cuando es llamado múltiples veces el método recorrer.
        """
        auto = AutoElectrico(marca="Tesla", rendimiento=5,
                             energia=2.0, vida_util_bateria=2)
        recorrido = auto.recorrer(8)
        self.assertEqual(recorrido,
                         "Anduve en auto electrico 8.0Km y "
                         "eso consume 1.6W de energia electrica")
        self.assertEqual(auto.kilometraje, 8)
        self.assertEqual(auto.vida_util_bateria, 1)

        recorrido = auto.recorrer(12)
        self.assertEqual(recorrido,
                         "Anduve en auto electrico 2.0Km y "
                         "eso consume 0.4W de energia electrica")
        self.assertEqual(auto.kilometraje, 10)
        self.assertEqual(auto.vida_util_bateria, 0)

        recorrido = auto.recorrer(1)
        self.assertEqual(recorrido,
                         "La bateria del auto electrico no funciona")
        self.assertEqual(auto.kilometraje, 10)
        self.assertLessEqual(auto.vida_util_bateria, 1)
