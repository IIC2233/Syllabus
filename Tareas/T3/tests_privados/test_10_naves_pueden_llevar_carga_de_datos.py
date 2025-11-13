import os
import sys
import unittest
from collections.abc import Iterable
from backend.consultas import naves_pueden_llevar, cargar_planeta_minerales, cargar_naves
from tests_privados.timeout_function import timeout
from tests_privados.utils import FLEXIBILIDAD_ADICIONAL
from tests_privados.solution.test_10 import (
    NAVES_PUEDEN_LLEVAR_S_1,
    NAVES_PUEDEN_LLEVAR_M_1,
    NAVES_PUEDEN_LLEVAR_L_1,
    NAVES_PUEDEN_LLEVAR_S_2,
    NAVES_PUEDEN_LLEVAR_M_2,
    NAVES_PUEDEN_LLEVAR_L_2
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

        path = os.path.join("data_new", tamano, "PlanetaMineral.csv")

        g_pm = cargar_planeta_minerales(path)

        path = os.path.join("data_new", tamano, "Nave.csv")

        g_n = cargar_naves(path)

        resultado_estudiante = naves_pueden_llevar(g_n, g_pm, 37)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        esperado = NAVES_PUEDEN_LLEVAR_S_1

        resultado = list(resultado_estudiante)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        for (
            patente_resultado, id_resultado, resultado_c1), (
                patente_esperado, id_esperado, esperado_c1) in zip(
                    sorted(resultado), sorted(esperado)):
            self.assertEqual(patente_resultado, patente_esperado)
            self.assertEqual(id_resultado, id_esperado)
            self.assertAlmostEqual(resultado_c1, esperado_c1, delta=0.010001)

        self.assertTrue(all(isinstance(item, tuple) for item in resultado))

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S.
        """

        tamano = "out_new_S"

        path = os.path.join("data_new", tamano, "PlanetaMineral.csv")

        g_pm = cargar_planeta_minerales(path)

        path = os.path.join("data_new", tamano, "Nave.csv")

        g_n = cargar_naves(path)

        resultado_estudiante = naves_pueden_llevar(g_n, g_pm, 10)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        resultado = list(resultado_estudiante)

        esperado = NAVES_PUEDEN_LLEVAR_S_2

        self.assertIsInstance(resultado_estudiante, (Iterable))

        for (
            patente_resultado, id_resultado, resultado_c1), (
                patente_esperado, id_esperado, esperado_c1) in zip(
                    sorted(resultado), sorted(esperado)):
            self.assertEqual(patente_resultado, patente_esperado)
            self.assertEqual(id_resultado, id_esperado)
            self.assertAlmostEqual(resultado_c1, esperado_c1, delta=0.010001)

        self.assertTrue(all(isinstance(item, tuple) for item in resultado))

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """

        tamano = "out_new_M"

        path = os.path.join("data_new", tamano, "PlanetaMineral.csv")

        g_pm = cargar_planeta_minerales(path)

        path = os.path.join("data_new", tamano, "Nave.csv")

        g_n = cargar_naves(path)

        resultado_estudiante = naves_pueden_llevar(g_n, g_pm, 199)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        resultado = list(resultado_estudiante)

        esperado = NAVES_PUEDEN_LLEVAR_M_1

        self.assertIsInstance(resultado_estudiante, (Iterable))

        for (
            patente_resultado, id_resultado, resultado_c1), (
                patente_esperado, id_esperado, esperado_c1) in zip(
                    sorted(resultado), sorted(esperado)):
            self.assertEqual(patente_resultado, patente_esperado)
            self.assertEqual(id_resultado, id_esperado)
            self.assertAlmostEqual(resultado_c1, esperado_c1, delta=0.010001)

        self.assertTrue(all(isinstance(item, tuple) for item in resultado))

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M, y que retorne vacío.
        """

        tamano = "out_new_M"

        path = os.path.join("data_new", tamano, "PlanetaMineral.csv")

        g_pm = cargar_planeta_minerales(path)

        path = os.path.join("data_new", tamano, "Nave.csv")

        g_n = cargar_naves(path)

        resultado_estudiante = naves_pueden_llevar(g_n, g_pm, 122)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        resultado = list(resultado_estudiante)

        esperado = NAVES_PUEDEN_LLEVAR_M_2

        self.assertIsInstance(resultado_estudiante, (Iterable))

        for (
            patente_resultado, id_resultado, resultado_c1), (
                patente_esperado, id_esperado, esperado_c1) in zip(
                    sorted(resultado), sorted(esperado)):
            self.assertEqual(patente_resultado, patente_esperado)
            self.assertEqual(id_resultado, id_esperado)
            self.assertAlmostEqual(resultado_c1, esperado_c1, delta=0.010001)

        self.assertTrue(all(isinstance(item, tuple) for item in resultado))

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """

        tamano = "out_new_L"

        path = os.path.join("data_new", tamano, "PlanetaMineral.csv")

        g_pm = cargar_planeta_minerales(path)

        path = os.path.join("data_new", tamano, "Nave.csv")

        g_n = cargar_naves(path)

        resultado_estudiante = naves_pueden_llevar(g_n, g_pm, 488)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        resultado = list(resultado_estudiante)

        esperado = NAVES_PUEDEN_LLEVAR_L_1

        self.assertIsInstance(resultado_estudiante, (Iterable))

        for (
            patente_resultado, id_resultado, resultado_c1), (
                patente_esperado, id_esperado, esperado_c1) in zip(
                    sorted(resultado), sorted(esperado)):
            self.assertEqual(patente_resultado, patente_esperado)
            self.assertEqual(id_resultado, id_esperado)
            self.assertAlmostEqual(resultado_c1, esperado_c1, delta=0.010001)

        self.assertTrue(all(isinstance(item, tuple) for item in resultado))

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """

        tamano = "out_new_L"

        path = os.path.join("data_new", tamano, "PlanetaMineral.csv")

        g_pm = cargar_planeta_minerales(path)

        path = os.path.join("data_new", tamano, "Nave.csv")

        g_n = cargar_naves(path)

        resultado_estudiante = naves_pueden_llevar(g_n, g_pm, 1181)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        resultado = list(resultado_estudiante)

        esperado = NAVES_PUEDEN_LLEVAR_L_2

        self.assertIsInstance(resultado_estudiante, (Iterable))

        for (
            patente_resultado, id_resultado, resultado_c1), (
                patente_esperado, id_esperado, esperado_c1) in zip(
                    sorted(resultado), sorted(esperado)):
            self.assertEqual(patente_resultado, patente_esperado)
            self.assertEqual(id_resultado, id_esperado)
            self.assertAlmostEqual(resultado_c1, esperado_c1, delta=0.010001)

        self.assertTrue(all(isinstance(item, tuple) for item in resultado))
