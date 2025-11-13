import os
import sys
import unittest
from collections.abc import Iterable

from tests_privados.timeout_function import timeout
from tests_privados.utils import FLEXIBILIDAD_ADICIONAL
sys.stdout = open(os.devnull, 'w')

# Constante para timeout en tests
N_SECOND = FLEXIBILIDAD_ADICIONAL*0.08

from backend.consultas import ganancias_potenciales_por_planeta
from utilidades import Mineral, PlanetaMineral, Planeta


def _gen(iterable):
    return (item for item in iterable)


class TestGananciasPotencialesPorPlanetaCorrectitud(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica cálculo correcto con datos básicos usando la fórmula.
        """
        minerales = [
            Mineral(1, "Min-A", "A", 1, 1.0),
        ]

        planeta_minerales = [
            PlanetaMineral(1, 1, 100.0, 0.5),
        ]

        planetas = [
            Planeta(1, "P1", 0.0, 0.0, "S", "X"),
        ]

        precios = {"Min-A": 5.0}
        
        resultado = ganancias_potenciales_por_planeta(
            _gen(minerales), _gen(planeta_minerales), _gen(planetas), precios
        )

        self.assertIsInstance(resultado, dict)
        # Fórmula: precio * cantidad * pureza = 5.0 * 100.0 * 0.5 = 250.0
        esperado = {1: 250.0}
        self.assertEqual(resultado, esperado)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se retorne diccionario vacío cuando no hay planetas.
        """
        minerales = [
            Mineral(1, "Min-A", "A", 1, 1.0),
        ]

        planeta_minerales = [
            PlanetaMineral(1, 1, 100.0, 0.5),
        ]

        planetas = []  # Sin planetas

        precios = {"Min-A": 5.0}
        
        resultado = ganancias_potenciales_por_planeta(
            _gen(minerales), _gen(planeta_minerales), _gen(planetas), precios
        )

        self.assertIsInstance(resultado, dict)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se manejen correctamente planetas sin minerales.
        """
        minerales = [
            Mineral(1, "Min-A", "A", 1, 1.0),
        ]

        planeta_minerales = []  # Sin minerales en planetas

        planetas = [
            Planeta(1, "P1", 0.0, 0.0, "S", "X"),
            Planeta(2, "P2", 0.0, 0.0, "S", "X"),
        ]

        precios = {"Min-A": 5.0}
        
        resultado = ganancias_potenciales_por_planeta(
            _gen(minerales), _gen(planeta_minerales), _gen(planetas), precios
        )

        self.assertIsInstance(resultado, dict)
        # Sin minerales, todos los planetas deben tener valor 0
        esperado = {1: 0.0, 2: 0.0}
        self.assertEqual(resultado, esperado)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que se manejen correctamente diferentes purezas de minerales.
        """
        minerales = [
            Mineral(1, "Min-A", "A", 1, 1.0),
            Mineral(2, "Min-B", "B", 2, 2.0),
        ]

        planeta_minerales = [
            PlanetaMineral(1, 1, 100.0, 0.1),   # Baja pureza
            PlanetaMineral(2, 2, 100.0, 0.9),   # Alta pureza
        ]

        planetas = [
            Planeta(1, "P1", 0.0, 0.0, "S", "X"),
            Planeta(2, "P2", 0.0, 0.0, "S", "X"),
        ]

        precios = {"Min-A": 10.0, "Min-B": 10.0}
        
        resultado = ganancias_potenciales_por_planeta(
            _gen(minerales), _gen(planeta_minerales), _gen(planetas), precios
        )

        self.assertIsInstance(resultado, dict)
        # Planeta 1: 10.0 * 100.0 * 0.1 = 100.0
        # Planeta 2: 10.0 * 100.0 * 0.9 = 900.0
        esperado = {1: 100.0, 2: 900.0}
        self.assertEqual(resultado, esperado)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que se manejen correctamente múltiples minerales en un planeta.
        """
        minerales = [
            Mineral(1, "Min-A", "A", 1, 1.0),
            Mineral(2, "Min-B", "B", 2, 2.0),
            Mineral(3, "Min-C", "C", 3, 3.0),
        ]

        planeta_minerales = [
            PlanetaMineral(1, 1, 50.0, 0.5),    # Min-A en planeta 1
            PlanetaMineral(1, 2, 30.0, 0.8),    # Min-B en planeta 1
            PlanetaMineral(1, 3, 20.0, 1.0),    # Min-C en planeta 1
            PlanetaMineral(2, 1, 100.0, 0.3),   # Min-A en planeta 2
        ]

        planetas = [
            Planeta(1, "P1", 0.0, 0.0, "S", "X"),
            Planeta(2, "P2", 0.0, 0.0, "S", "X"),
        ]

        precios = {"Min-A": 2.0, "Min-B": 3.0, "Min-C": 5.0}
        
        resultado = ganancias_potenciales_por_planeta(
            _gen(minerales), _gen(planeta_minerales), _gen(planetas), precios
        )

        self.assertIsInstance(resultado, dict)
        # Planeta 1: (2.0 * 50.0 * 0.5) + (3.0 * 30.0 * 0.8) + (5.0 * 20.0 * 1.0) = 50.0 + 72.0 + 100.0 = 222.0
        # Planeta 2: 2.0 * 100.0 * 0.3 = 60.0
        esperado = {1: 222.0, 2: 60.0}
        self.assertEqual(resultado, esperado)

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica que se manejen correctamente minerales con precios altos y bajos.
        """
        minerales = [
            Mineral(1, "Min-A", "A", 1, 1.0),
            Mineral(2, "Min-B", "B", 2, 2.0),
        ]

        planeta_minerales = [
            PlanetaMineral(1, 1, 10.0, 1.0),    # Cantidad pequeña
            PlanetaMineral(2, 2, 1000.0, 0.1),  # Cantidad grande, baja pureza
        ]

        planetas = [
            Planeta(1, "P1", 0.0, 0.0, "S", "X"),
            Planeta(2, "P2", 0.0, 0.0, "S", "X"),
        ]

        precios = {"Min-A": 1000.0, "Min-B": 0.1}  # Precio alto vs precio bajo
        
        resultado = ganancias_potenciales_por_planeta(
            _gen(minerales), _gen(planeta_minerales), _gen(planetas), precios
        )

        self.assertIsInstance(resultado, dict)
        # Planeta 1: 1000.0 * 10.0 * 1.0 = 10000.0
        # Planeta 2: 0.1 * 1000.0 * 0.1 = 10.0
        esperado = {1: 10000.0, 2: 10.0}
        self.assertEqual(resultado, esperado)

