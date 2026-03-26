import unittest

from bases import ParDeGenes
from dominancia import Dominante, Codominante, Recesivo


class VerificarAdd(unittest.TestCase):
    """Verifica el método __add__."""

    def test_dominante_dominante(self):
        """Verifica el caso cuando dos genes son dominantes"""
        rasgo = "Ojos"
        valor = "Rojos"

        gen_1 = Dominante(rasgo=rasgo, valor=valor)
        gen_2 = Dominante(rasgo=rasgo, valor=valor)

        par = gen_1 + gen_2

        self.assertIsInstance(par, ParDeGenes)
        self.assertEqual(par.fenotipo, valor)

    def test_dominante_recesivo(self):
        """Verifica el caso cuando hay dominante + recesivo"""
        rasgo = "Ojos"
        valor1 = "Rojos"
        valor2 = "Verdes"

        gen_1 = Dominante(rasgo=rasgo, valor=valor1)
        gen_2 = Recesivo(rasgo=rasgo, valor=valor2)

        par = gen_1 + gen_2

        self.assertIsInstance(par, ParDeGenes)
        self.assertEqual(par.fenotipo, valor1)

        par = gen_2 + gen_1

        self.assertIsInstance(par, ParDeGenes)
        self.assertEqual(par.fenotipo, valor1)

    def test_dominantes_codominante(self):
        """Test de caso dominante + codominante"""
        rasgo = "Ojos"
        valor1 = "Rojos"
        valor2 = "Verdes"

        gen_1 = Dominante(rasgo=rasgo, valor=valor1)
        gen_2 = Codominante(rasgo=rasgo, valor=valor2)

        par = gen_1 + gen_2

        self.assertIsInstance(par, ParDeGenes)
        self.assertEqual(par.fenotipo, valor1)

        par = gen_2 + gen_1

        self.assertIsInstance(par, ParDeGenes)
        self.assertEqual(par.fenotipo, valor1)

    def test_recesivo_recesivo(self):
        """Verifica el caso cuando hay recesivo + recesivo"""
        rasgo = "Ojos"
        valor = "Rojos"

        gen_1 = Recesivo(rasgo=rasgo, valor=valor)
        gen_2 = Recesivo(rasgo=rasgo, valor=valor)

        par = gen_1 + gen_2

        self.assertIsInstance(par, ParDeGenes)
        self.assertEqual(par.fenotipo, valor)


    def test_codominante_codominante_igual(self):
        """Verifica el caso en que ambos son codominantes iguales"""
        rasgo = "Cola"
        valor = "recta"

        gen_1 = Codominante(rasgo=rasgo, valor=valor)
        gen_2 = Codominante(rasgo=rasgo, valor=valor)

        par = gen_1 + gen_2

        self.assertIsInstance(par, ParDeGenes)
        self.assertEqual(par.fenotipo, valor)

    def test_codominante_codominante_distinto(self):
        """Verifica el caso en que ambos son codominantes distintos"""
        rasgo = "Cola"
        valor1 = "recta"
        valor2 = "enroscada"

        gen_1 = Codominante(rasgo=rasgo, valor=valor1)
        gen_2 = Codominante(rasgo=rasgo, valor=valor2)

        par = gen_1 + gen_2

        self.assertIsInstance(par, ParDeGenes)
        self.assertIn(
            par.fenotipo,
            [
                f"Mezcla entre {valor1} y {valor2}",
                f"Mezcla entre {valor2} y {valor1}",
            ]
        )

        par = gen_2 + gen_1

        self.assertIsInstance(par, ParDeGenes)
        self.assertIn(
            par.fenotipo,
            [
                f"Mezcla entre {valor1} y {valor2}",
                f"Mezcla entre {valor2} y {valor1}",
            ]
        )
