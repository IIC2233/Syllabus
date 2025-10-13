import os
import sys
import unittest
from collections.abc import Iterable
from backend.consultas import disponibilidad_por_planeta, cargar_planeta_minerales, cargar_planetas
from tests_publicos.timeout_function import timeout
from tests_publicos.solution.test_7 import (
    DISPONIBILIDAD_POR_PLANETA_S_1,
    DISPONIBILIDAD_POR_PLANETA_M_1,
    DISPONIBILIDAD_POR_PLANETA_L_1,
    DISPONIBILIDAD_POR_PLANETA_S_2,
    DISPONIBILIDAD_POR_PLANETA_M_2,
    DISPONIBILIDAD_POR_PLANETA_L_2
)

sys.stdout = open(os.devnull, 'w')


# Constante para timeout en tests
N_SECOND = 0.08


class TestDisponibilidadPorPlaneta(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S.
        """

        tamano = "out_S"

        path = os.path.join("data", tamano, "PlanetaMineral.csv")

        g_pc = cargar_planeta_minerales(path)

        path = os.path.join("data", tamano, "Planeta.csv")

        g_p = cargar_planetas(path)

        resultado_estudiante = disponibilidad_por_planeta(g_pc, g_p, 37)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        self.assertTrue(all(isinstance(item, tuple) for item in lista_resultado))

        lista_esperada = DISPONIBILIDAD_POR_PLANETA_S_1

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S.
        """

        tamano = "out_S"

        path = os.path.join("data", tamano, "PlanetaMineral.csv")

        g_pc = cargar_planeta_minerales(path)

        path = os.path.join("data", tamano, "Planeta.csv")

        g_p = cargar_planetas(path)

        resultado_estudiante = disponibilidad_por_planeta(g_pc, g_p, 79)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        self.assertTrue(all(isinstance(item, tuple) for item in lista_resultado))

        lista_esperada = DISPONIBILIDAD_POR_PLANETA_S_2

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """

        tamano = "out_M"

        path = os.path.join("data", tamano, "PlanetaMineral.csv")

        g_pc = cargar_planeta_minerales(path)

        path = os.path.join("data", tamano, "Planeta.csv")

        g_p = cargar_planetas(path)

        resultado_estudiante = disponibilidad_por_planeta(g_pc, g_p, 145)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        self.assertTrue(all(isinstance(item, tuple) for item in lista_resultado))

        lista_esperada = DISPONIBILIDAD_POR_PLANETA_M_1

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M, y que retorne vacío.
        """

        tamano = "out_M"

        path = os.path.join("data", tamano, "PlanetaMineral.csv")

        g_pc = cargar_planeta_minerales(path)

        path = os.path.join("data", tamano, "Planeta.csv")

        g_p = cargar_planetas(path)

        resultado_estudiante = disponibilidad_por_planeta(g_pc, g_p, 115)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        self.assertTrue(all(isinstance(item, tuple) for item in lista_resultado))

        lista_esperada = DISPONIBILIDAD_POR_PLANETA_M_2

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """

        tamano = "out_L"

        path = os.path.join("data", tamano, "PlanetaMineral.csv")

        g_pc = cargar_planeta_minerales(path)

        path = os.path.join("data", tamano, "Planeta.csv")

        g_p = cargar_planetas(path)

        resultado_estudiante = disponibilidad_por_planeta(g_pc, g_p, 434)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        self.assertTrue(all(isinstance(item, tuple) for item in lista_resultado))

        lista_esperada = DISPONIBILIDAD_POR_PLANETA_L_1

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """

        tamano = "out_L"

        path = os.path.join("data", tamano, "PlanetaMineral.csv")

        g_pc = cargar_planeta_minerales(path)

        path = os.path.join("data", tamano, "Planeta.csv")

        g_p = cargar_planetas(path)

        resultado_estudiante = disponibilidad_por_planeta(g_pc, g_p, 353)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        self.assertTrue(all(isinstance(item, tuple) for item in lista_resultado))

        lista_esperada = DISPONIBILIDAD_POR_PLANETA_L_2

        self.assertCountEqual(lista_resultado, lista_esperada)
