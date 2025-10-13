import os
import sys
import unittest
from collections.abc import Iterable

from tests_publicos.timeout_function import timeout
from tests_publicos.solution.test_11 import *

sys.stdout = open(os.devnull, 'w')

# Constante para timeout en tests
N_SECOND = 0.08

from backend.consultas import ganancias_potenciales_por_planeta, cargar_minerales, cargar_planeta_minerales, cargar_planetas

def _gen(iterable):
    return (item for item in iterable)


class TestGananciasPotencialesPorPlanetaCargaDatos(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica cálculo correcto con dataset S sin precios (diccionario vacío).
        """
        size = "out_S"
        path_minerales = os.path.join("data", size, "Mineral.csv")
        path_planetas = os.path.join("data", size, "Planeta.csv")
        path_planeta_minerales = os.path.join("data", size, "PlanetaMineral.csv")
        precios = {}

        resultado = ganancias_potenciales_por_planeta(
            cargar_minerales(path_minerales),
            cargar_planeta_minerales(path_planeta_minerales),
            cargar_planetas(path_planetas),
            precios,
        )

        self.assertIsInstance(resultado, dict)
        
        # Verificar que tienen las mismas claves
        self.assertEqual(set(resultado.keys()), set(GANANCIAS_POR_PLANETA_S_0.keys()))
        
        # Verificar cada valor usando assertAlmostEqual
        for planeta_id in GANANCIAS_POR_PLANETA_S_0:
            self.assertAlmostEqual(resultado[planeta_id], GANANCIAS_POR_PLANETA_S_0[planeta_id], places=2)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica cálculo correcto con dataset S con precios.
        """
        size = "out_S"
        path_minerales = os.path.join("data", size, "Mineral.csv")
        path_planetas = os.path.join("data", size, "Planeta.csv")
        path_planeta_minerales = os.path.join("data", size, "PlanetaMineral.csv")
        precios = diccionario_precios_out_S

        resultado = ganancias_potenciales_por_planeta(
            cargar_minerales(path_minerales),
            cargar_planeta_minerales(path_planeta_minerales),
            cargar_planetas(path_planetas),
            precios,
        )

        self.assertIsInstance(resultado, dict)
        
        # Verificar que tienen las mismas claves
        self.assertEqual(set(resultado.keys()), set(GANANCIAS_POR_PLANETA_S_1.keys()))
        
        # Verificar cada valor usando assertAlmostEqual
        for planeta_id in GANANCIAS_POR_PLANETA_S_1:
            self.assertAlmostEqual(resultado[planeta_id], GANANCIAS_POR_PLANETA_S_1[planeta_id], places=2)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica cálculo correcto con dataset M con precios.
        """
        size = "out_M"
        path_minerales = os.path.join("data", size, "Mineral.csv")
        path_planetas = os.path.join("data", size, "Planeta.csv")
        path_planeta_minerales = os.path.join("data", size, "PlanetaMineral.csv")
        precios = diccionario_precios_out_M

        resultado = ganancias_potenciales_por_planeta(
            cargar_minerales(path_minerales),
            cargar_planeta_minerales(path_planeta_minerales),
            cargar_planetas(path_planetas),
            precios,
        )

        self.assertIsInstance(resultado, dict)
        
        # Verificar que tienen las mismas claves
        self.assertEqual(set(resultado.keys()), set(GANANCIAS_POR_PLANETA_M_0.keys()))
        
        # Verificar cada valor usando assertAlmostEqual
        for planeta_id in GANANCIAS_POR_PLANETA_M_0:
            self.assertAlmostEqual(resultado[planeta_id], GANANCIAS_POR_PLANETA_M_0[planeta_id], places=2)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica cálculo correcto con dataset M sin precios (diccionario vacío).
        """
        size = "out_M"
        path_minerales = os.path.join("data", size, "Mineral.csv")
        path_planetas = os.path.join("data", size, "Planeta.csv")
        path_planeta_minerales = os.path.join("data", size, "PlanetaMineral.csv")
        precios = {}

        resultado = ganancias_potenciales_por_planeta(
            cargar_minerales(path_minerales),
            cargar_planeta_minerales(path_planeta_minerales),
            cargar_planetas(path_planetas),
            precios,
        )

        self.assertIsInstance(resultado, dict)
        
        # Verificar que tienen las mismas claves
        self.assertEqual(set(resultado.keys()), set(GANANCIAS_POR_PLANETA_M_1.keys()))
        
        # Verificar cada valor usando assertAlmostEqual
        for planeta_id in GANANCIAS_POR_PLANETA_M_1:
            self.assertAlmostEqual(resultado[planeta_id], GANANCIAS_POR_PLANETA_M_1[planeta_id], places=2)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica cálculo correcto con dataset L con precios.
        """
        size = "out_L"
        path_minerales = os.path.join("data", size, "Mineral.csv")
        path_planetas = os.path.join("data", size, "Planeta.csv")
        path_planeta_minerales = os.path.join("data", size, "PlanetaMineral.csv")
        precios = diccionario_precios_out_L

        resultado = ganancias_potenciales_por_planeta(
            cargar_minerales(path_minerales),
            cargar_planeta_minerales(path_planeta_minerales),
            cargar_planetas(path_planetas),
            precios,
        )

        self.assertIsInstance(resultado, dict)
        
        # Verificar que tienen las mismas claves
        self.assertEqual(set(resultado.keys()), set(GANANCIAS_POR_PLANETA_L_0.keys()))
        
        # Verificar cada valor usando assertAlmostEqual
        for planeta_id in GANANCIAS_POR_PLANETA_L_0:
            self.assertAlmostEqual(resultado[planeta_id], GANANCIAS_POR_PLANETA_L_0[planeta_id], places=2)

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica cálculo correcto con dataset L sin precios (diccionario vacío).
        """
        size = "out_L"
        path_minerales = os.path.join("data", size, "Mineral.csv")
        path_planetas = os.path.join("data", size, "Planeta.csv")
        path_planeta_minerales = os.path.join("data", size, "PlanetaMineral.csv")
        precios = {}

        resultado = ganancias_potenciales_por_planeta(
            cargar_minerales(path_minerales),
            cargar_planeta_minerales(path_planeta_minerales),
            cargar_planetas(path_planetas),
            precios,
        )

        self.assertIsInstance(resultado, dict)
        
        # Verificar que tienen las mismas claves
        self.assertEqual(set(resultado.keys()), set(GANANCIAS_POR_PLANETA_L_1.keys()))
        
        # Verificar cada valor usando assertAlmostEqual
        for planeta_id in GANANCIAS_POR_PLANETA_L_1:
            self.assertAlmostEqual(resultado[planeta_id], GANANCIAS_POR_PLANETA_L_1[planeta_id], places=2)
