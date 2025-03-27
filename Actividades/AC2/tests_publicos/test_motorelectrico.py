import unittest
from abc import ABC

from clases import MotorElectrico


class VerificarClaseMotorElectrico(unittest.TestCase):

    def test_usar_bateria(self):
        """
        Verifica que la batería se gaste al ser usada.
        """
        motor = MotorElectrico(3)

        motor.usar_bateria()
        self.assertEqual(motor.vida_util_bateria, 2)
        self.assertEqual(motor.usar_bateria(), True)
        self.assertEqual(motor.vida_util_bateria, 1)

        motor.usar_bateria() # Este fue el último uso.
        self.assertEqual(motor.usar_bateria(), False)

    def test_clase_abstracta(self):
        """
        Verifica que MotorElectrico sea clase abstracta.
        """
        self.assertIn(ABC, MotorElectrico.__mro__)
