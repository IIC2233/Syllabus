import os
import sys
import unittest
from collections.abc import Iterable
from backend.consultas import naves_pueden_llevar, cargar_planeta_minerales, cargar_naves
from tests_publicos.timeout_function import timeout
from tests_publicos.solution.test_10 import (
    NAVES_PUEDEN_LLEVAR_S_1,
    NAVES_PUEDEN_LLEVAR_M_1,
    NAVES_PUEDEN_LLEVAR_L_1,
    NAVES_PUEDEN_LLEVAR_S_2,
    NAVES_PUEDEN_LLEVAR_M_2,
    NAVES_PUEDEN_LLEVAR_L_2
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

        g_pm = cargar_planeta_minerales(path)

        path = os.path.join("data", tamano, "Nave.csv")

        g_n = cargar_naves(path)

        resultado_estudiante = naves_pueden_llevar(g_n, g_pm, 53)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        resultado = list(resultado_estudiante)

        esperado = NAVES_PUEDEN_LLEVAR_S_1

        lista_resultado = [(patente, id, round(cantidad, 2)) for patente, id, cantidad in resultado]

        lista_esperada = [(patente, id, round(cantidad, 2)) for patente, id, cantidad in esperado]

        self.assertTrue(all(isinstance(item, tuple) for item in lista_resultado))

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S.
        """

        tamano = "out_S"

        path = os.path.join("data", tamano, "PlanetaMineral.csv")

        g_pm = cargar_planeta_minerales(path)

        path = os.path.join("data", tamano, "Nave.csv")

        g_n = cargar_naves(path)

        resultado_estudiante = naves_pueden_llevar(g_n, g_pm, 22)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        resultado = list(resultado_estudiante)

        esperado = NAVES_PUEDEN_LLEVAR_S_2

        lista_resultado = [(patente, id, round(cantidad, 2)) for patente, id, cantidad in resultado]

        lista_esperada = [(patente, id, round(cantidad, 2)) for patente, id, cantidad in esperado]

        self.assertTrue(all(isinstance(item, tuple) for item in lista_resultado))

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """

        tamano = "out_M"

        path = os.path.join("data", tamano, "PlanetaMineral.csv")

        g_pm = cargar_planeta_minerales(path)

        path = os.path.join("data", tamano, "Nave.csv")

        g_n = cargar_naves(path)

        resultado_estudiante = naves_pueden_llevar(g_n, g_pm, 91)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        resultado = list(resultado_estudiante)

        esperado = NAVES_PUEDEN_LLEVAR_M_1

        lista_resultado = [(patente, id, round(cantidad, 2)) for patente, id, cantidad in resultado]

        lista_esperada = [(patente, id, round(cantidad, 2)) for patente, id, cantidad in esperado]

        self.assertTrue(all(isinstance(item, tuple) for item in lista_resultado))

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M, y que retorne vacío.
        """

        tamano = "out_M"

        path = os.path.join("data", tamano, "PlanetaMineral.csv")

        g_pm = cargar_planeta_minerales(path)

        path = os.path.join("data", tamano, "Nave.csv")

        g_n = cargar_naves(path)

        resultado_estudiante = naves_pueden_llevar(g_n, g_pm, 54)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        resultado = list(resultado_estudiante)

        esperado = NAVES_PUEDEN_LLEVAR_M_2

        lista_resultado = [(patente, id, round(cantidad, 2)) for patente, id, cantidad in resultado]

        lista_esperada = [(patente, id, round(cantidad, 2)) for patente, id, cantidad in esperado]

        self.assertTrue(all(isinstance(item, tuple) for item in lista_resultado))

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """

        tamano = "out_L"

        path = os.path.join("data", tamano, "PlanetaMineral.csv")

        g_pm = cargar_planeta_minerales(path)

        path = os.path.join("data", tamano, "Nave.csv")

        g_n = cargar_naves(path)

        resultado_estudiante = naves_pueden_llevar(g_n, g_pm, 1002)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        resultado = list(resultado_estudiante)

        esperado = NAVES_PUEDEN_LLEVAR_L_1

        lista_resultado = [(patente, id, round(cantidad, 2)) for patente, id, cantidad in resultado]

        lista_esperada = [(patente, id, round(cantidad, 2)) for patente, id, cantidad in esperado]

        self.assertTrue(all(isinstance(item, tuple) for item in lista_resultado))

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """

        tamano = "out_L"

        path = os.path.join("data", tamano, "PlanetaMineral.csv")

        g_pm = cargar_planeta_minerales(path)

        path = os.path.join("data", tamano, "Nave.csv")

        g_n = cargar_naves(path)

        resultado_estudiante = naves_pueden_llevar(g_n, g_pm, 68)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        resultado = list(resultado_estudiante)

        esperado = NAVES_PUEDEN_LLEVAR_L_2

        lista_resultado = [(patente, id, round(cantidad, 2)) for patente, id, cantidad in resultado]

        lista_esperada = [(patente, id, round(cantidad, 2)) for patente, id, cantidad in esperado]

        self.assertTrue(all(isinstance(item, tuple) for item in lista_resultado))

        self.assertCountEqual(lista_resultado, lista_esperada)
