import os
import sys
import unittest
from collections.abc import Iterable
from backend.consultas import (
    mineral_por_nave, cargar_materiales_mision, cargar_tripulaciones, cargar_mision)
from tests_privados.timeout_function import timeout
from tests_privados.utils import FLEXIBILIDAD_ADICIONAL
from tests_privados.solution.test_13 import (
    MINERAL_POR_NAVE_S_1,
    MINERAL_POR_NAVE_M_1,
    MINERAL_POR_NAVE_L_1,
)

sys.stdout = open(os.devnull, 'w')


# Constante para timeout en tests
N_SECOND = FLEXIBILIDAD_ADICIONAL*0.08


class TestDisponibilidadPorPlaneta(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S.
        """

        tamano = "out_new_S"

        path = os.path.join("data_new", tamano, "MisionMineral.csv")

        g_mm = cargar_materiales_mision(path)

        path = os.path.join("data_new", tamano, "Tripulacion.csv")

        g_t = cargar_tripulaciones(path)

        path = os.path.join("data_new", tamano, "Mision.csv")

        g_m = cargar_mision(path)

        resultado_estudiante = mineral_por_nave(g_t, g_m, g_mm)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        esperado = MINERAL_POR_NAVE_S_1

        resultado = list(resultado_estudiante)

        self.assertTrue(all(isinstance(item, tuple) for item in resultado))

        for (
            resultado_planeta, resultado_c1), (
                esperado_planeta, esperado_c1) in zip(
                    sorted(resultado), sorted(esperado)):
            self.assertEqual(resultado_planeta, esperado_planeta)
            self.assertAlmostEqual(resultado_c1, esperado_c1, delta=0.010001)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """

        tamano = "out_new_M"

        path = os.path.join("data_new", tamano, "MisionMineral.csv")

        g_mm = cargar_materiales_mision(path)

        path = os.path.join("data_new", tamano, "Tripulacion.csv")

        g_t = cargar_tripulaciones(path)

        path = os.path.join("data_new", tamano, "Mision.csv")

        g_m = cargar_mision(path)

        resultado_estudiante = mineral_por_nave(g_t, g_m, g_mm)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        resultado = list(resultado_estudiante)

        esperado = MINERAL_POR_NAVE_M_1

        self.assertTrue(all(isinstance(item, tuple) for item in resultado))

        for (
            resultado_planeta, resultado_c1), (
                esperado_planeta, esperado_c1) in zip(
                    sorted(resultado), sorted(esperado)):
            self.assertEqual(resultado_planeta, esperado_planeta)
            self.assertAlmostEqual(resultado_c1, esperado_c1, delta=0.010001)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """

        tamano = "out_new_L"

        path = os.path.join("data_new", tamano, "MisionMineral.csv")

        g_mm = cargar_materiales_mision(path)

        path = os.path.join("data_new", tamano, "Tripulacion.csv")

        g_t = cargar_tripulaciones(path)

        path = os.path.join("data_new", tamano, "Mision.csv")

        g_m = cargar_mision(path)

        resultado_estudiante = mineral_por_nave(g_t, g_m, g_mm)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        resultado = list(resultado_estudiante)

        esperado = MINERAL_POR_NAVE_L_1

        self.assertTrue(all(isinstance(item, tuple) for item in resultado))

        for (
            resultado_planeta, resultado_c1), (
                esperado_planeta, esperado_c1) in zip(
                    sorted(resultado), sorted(esperado)):
            self.assertEqual(resultado_planeta, esperado_planeta)
            self.assertAlmostEqual(resultado_c1, esperado_c1, delta=0.010001)
