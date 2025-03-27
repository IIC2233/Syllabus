import unittest

from clases import BicicletaElectrica, Vehiculo, MotorElectrico


class VerificarClaseBicicletaElectrica(unittest.TestCase):

    def test_herencia(self):
        """
        Verifica que BicicletaElectrica herede correctamente.
        """
        self.assertIn(Vehiculo, BicicletaElectrica.__mro__)
        self.assertIn(MotorElectrico, BicicletaElectrica.__mro__)


    def test_verifica_bateria_funcional(self):
        """
        Verifica los recorridos cuando la batería funciona.
        Se comprueba tanto el texto que retorna el método,
        como que disminuya la vida útil de la batería.
        """
        bici = BicicletaElectrica(
            rendimiento=10, marca="Trek", energia=22.7,
            vida_util_bateria=10
        )

        self.assertEqual(bici.recorrer(10),
                         "Anduve en bicicleta electrica 10.0Km"
                         " y eso consume 1.0W de energia electrica")
        self.assertEqual(bici.vida_util_bateria, 9)

    def test_verifica_bateria_no_funcional(self):
        """
        Verifica los recorridos cuando la batería está muerta.
        Se comprueba tanto el texto que retorna el método,
        como que se mantenga la vida útil de la batería.
        """
        bici = BicicletaElectrica(
            rendimiento=10, marca="Trek", energia=22.7,
            vida_util_bateria=0
        )

        self.assertEqual(bici.recorrer(10),
                         "La bateria de la bicicleta electrica"
                         " no funciona, tuve que pedalear 10.0Km")
        self.assertLessEqual(bici.vida_util_bateria, 0)

    def test_verifica_autonomia(self):
        """
        Verifica el texto de autonomía de la bicicleta eléctrica.
        Se comprueba tanto el texto que retorna el método,
        como que disminuya la vida útil de la batería.
        """
        bici = BicicletaElectrica(
            rendimiento=10, marca="Trek", energia=22.7,
            vida_util_bateria=10
        )

        self.assertEqual(bici.recorrer(300),
                         "Anduve en bicicleta electrica 227.0Km"
                         " y eso consume 22.7W de energia electrica"
                         ", los 73.0Km restantes los tuve que pedalear")
        self.assertEqual(bici.vida_util_bateria, 9)

    def test_recorrer_multiple(self):
        """
        Verifica el texto de recorrer y vida útil de la batería
        cuando se recorre múltiples veces.
        """
        bici = BicicletaElectrica(marca="Trek", rendimiento=5, energia=1.0,
                                  vida_util_bateria=2)
        recorrido = bici.recorrer(4)
        self.assertEqual(recorrido,
                         "Anduve en bicicleta electrica 4.0Km y "
                         "eso consume 0.8W de energia electrica")
        self.assertEqual(bici.vida_util_bateria, 1)

        recorrido = bici.recorrer(6)
        self.assertEqual(recorrido,
                         "Anduve en bicicleta electrica 1.0Km y "
                         "eso consume 0.2W de energia electrica"
                         ", los 5.0Km restantes los tuve que pedalear")
        self.assertEqual(bici.vida_util_bateria, 0)

        recorrido = bici.recorrer(2)
        self.assertEqual(recorrido,
                         "La bateria de la bicicleta electrica no funciona, "
                         "tuve que pedalear 2.0Km")
        self.assertLessEqual(bici.vida_util_bateria, 0)
