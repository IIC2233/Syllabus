import os
import sys
import unittest
from collections.abc import Iterable

from tests_publicos.timeout_function import timeout
from tests_publicos.solution.test_20 import *
from utilidades import N_SECOND

from consultas import cargar_contenido_pedidos, cargar_pedidos, cargar_locales, \
    pizzas_vendidas_mes_pais



class TestPizzasVendidasMesPaisCargaDatos(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S.
        """
        carpeta = "s"

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        path = os.path.join("data", carpeta, "pedidos.csv")
        generador_pedidos = cargar_pedidos(path)

        path = os.path.join("data", carpeta, "locales.csv")
        generador_locales = cargar_locales(path)

        resultado_estudiante = pizzas_vendidas_mes_pais(
            generador_contenido_pedidos,
            generador_pedidos,
            generador_locales,
            "Ghana",
            3,
            2024,
        )

        resultado_esperado = PIZZAS_VENDIDAS_MES_PAIS_S_1

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual((resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S.
        """
        carpeta = "s"

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        path = os.path.join("data", carpeta, "pedidos.csv")
        generador_pedidos = cargar_pedidos(path)

        path = os.path.join("data", carpeta, "locales.csv")
        generador_locales = cargar_locales(path)

        resultado_estudiante = pizzas_vendidas_mes_pais(
            generador_contenido_pedidos,
            generador_pedidos,
            generador_locales,
            "Japan",
            3,
            2024,
        )

        resultado_esperado = PIZZAS_VENDIDAS_MES_PAIS_S_2

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual((resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        path = os.path.join("data", carpeta, "pedidos.csv")
        generador_pedidos = cargar_pedidos(path)

        path = os.path.join("data", carpeta, "locales.csv")
        generador_locales = cargar_locales(path)

        resultado_estudiante = pizzas_vendidas_mes_pais(
            generador_contenido_pedidos,
            generador_pedidos,
            generador_locales,
            "Greece",
            8,
            2024,
        )

        resultado_esperado = PIZZAS_VENDIDAS_MES_PAIS_M_1

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual((resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        path = os.path.join("data", carpeta, "pedidos.csv")
        generador_pedidos = cargar_pedidos(path)

        path = os.path.join("data", carpeta, "locales.csv")
        generador_locales = cargar_locales(path)

        resultado_estudiante = pizzas_vendidas_mes_pais(
            generador_contenido_pedidos,
            generador_pedidos,
            generador_locales,
            "Spain",
            7,
            2024,
        )

        resultado_esperado = PIZZAS_VENDIDAS_MES_PAIS_M_2

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual((resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        path = os.path.join("data", carpeta, "pedidos.csv")
        generador_pedidos = cargar_pedidos(path)

        path = os.path.join("data", carpeta, "locales.csv")
        generador_locales = cargar_locales(path)

        resultado_estudiante = pizzas_vendidas_mes_pais(
            generador_contenido_pedidos,
            generador_pedidos,
            generador_locales,
            "France",
            6,
            2024,
        )

        resultado_esperado = PIZZAS_VENDIDAS_MES_PAIS_M_3

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual((resultado_estudiante), resultado_esperado)
