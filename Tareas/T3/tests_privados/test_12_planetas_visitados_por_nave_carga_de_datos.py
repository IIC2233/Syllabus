import os
import sys
import unittest
from collections.abc import Iterable
from backend.consultas import (
    planetas_visitados_por_nave, cargar_planetas, cargar_tripulaciones, cargar_mision)
from tests_privados.timeout_function import timeout
from tests_privados.utils import FLEXIBILIDAD_ADICIONAL
from tests_privados.solution.test_12 import (
    PLANETAS_VISITADOS_POR_NAVE_S_1,
    PLANETAS_VISITADOS_POR_NAVE_M_1,
    PLANETAS_VISITADOS_POR_NAVE_L_1,
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

        path = os.path.join("data_new", tamano, "Planeta.csv")

        g_p = cargar_planetas(path)

        path = os.path.join("data_new", tamano, "Tripulacion.csv")

        g_t = cargar_tripulaciones(path)

        path = os.path.join("data_new", tamano, "Mision.csv")

        g_m = cargar_mision(path)

        resultado_estudiante = planetas_visitados_por_nave(g_p, g_m, g_t)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_esperada = PLANETAS_VISITADOS_POR_NAVE_S_1

        lista_resultado = list(resultado_estudiante)

        self.assertTrue(all(isinstance(item, tuple) for item in lista_resultado))

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """

        tamano = "out_new_M"

        path = os.path.join("data_new", tamano, "Planeta.csv")

        g_p = cargar_planetas(path)

        path = os.path.join("data_new", tamano, "Tripulacion.csv")

        g_t = cargar_tripulaciones(path)

        path = os.path.join("data_new", tamano, "Mision.csv")

        g_m = cargar_mision(path)

        resultado_estudiante = planetas_visitados_por_nave(g_p, g_m, g_t)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        lista_esperada = PLANETAS_VISITADOS_POR_NAVE_M_1

        self.assertTrue(all(isinstance(item, tuple) for item in lista_resultado))

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND*8)
    def test_2(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """

        tamano = "out_new_L"

        path = os.path.join("data_new", tamano, "Planeta.csv")

        g_p = cargar_planetas(path)

        path = os.path.join("data_new", tamano, "Tripulacion.csv")

        g_t = cargar_tripulaciones(path)

        path = os.path.join("data_new", tamano, "Mision.csv")

        g_m = cargar_mision(path)

        resultado_estudiante = planetas_visitados_por_nave(g_p, g_m, g_t)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        lista_esperada = PLANETAS_VISITADOS_POR_NAVE_L_1

        self.assertTrue(all(isinstance(item, tuple) for item in lista_resultado))

        self.assertCountEqual(lista_resultado, lista_esperada)
