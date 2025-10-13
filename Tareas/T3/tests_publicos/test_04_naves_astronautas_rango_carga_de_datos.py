import os
import sys
import unittest
from collections.abc import Generator
from backend.consultas import naves_astronautas_rango, cargar_tripulaciones
from tests_publicos.timeout_function import timeout
from tests_publicos.solution.test_4 import (
    NAVES_ASTRONAUTAS_RANGO_S_1,
    NAVES_ASTRONAUTAS_RANGO_M_1,
    NAVES_ASTRONAUTAS_RANGO_L_1,
    NAVES_ASTRONAUTAS_RANGO_S_2,
    NAVES_ASTRONAUTAS_RANGO_M_2,
    NAVES_ASTRONAUTAS_RANGO_L_2
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

        path = os.path.join("data", tamano, "Tripulacion.csv")

        g_t = cargar_tripulaciones(path)

        resultado_estudiante = naves_astronautas_rango(g_t, 3, 3)

        self.assertIsInstance(resultado_estudiante, (Generator))

        lista_resultado = list(resultado_estudiante)
        self.assertTrue(all(isinstance(item, tuple) for item in lista_resultado), 'Revisa que el primer generador sea de tuples')
        self.assertTrue(all(isinstance(item, Generator) for _, item in lista_resultado), 'Revisa que las ids astronauta se entregen como generador')

        lista_resultado = [(k, tuple(v)) for k, v in lista_resultado]
        lista_esperada = NAVES_ASTRONAUTAS_RANGO_S_1

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S.
        """

        tamano = "out_S"

        path = os.path.join("data", tamano, "Tripulacion.csv")

        g_t = cargar_tripulaciones(path)

        resultado_estudiante = naves_astronautas_rango(g_t, 4, 3)

        self.assertIsInstance(resultado_estudiante, (Generator))

        lista_resultado = list(resultado_estudiante)
        self.assertTrue(all(isinstance(item, tuple) for item in lista_resultado), 'Revisa que el primer generador sea de tuples')
        self.assertTrue(all(isinstance(item, Generator) for _, item in lista_resultado), 'Revisa que las ids astronauta se entregen como generador')

        lista_resultado = [(k, tuple(v)) for k, v in lista_resultado]
        lista_esperada = NAVES_ASTRONAUTAS_RANGO_S_2

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """

        tamano = "out_M"

        path = os.path.join("data", tamano, "Tripulacion.csv")

        g_t = cargar_tripulaciones(path)

        resultado_estudiante = naves_astronautas_rango(g_t, 1, 4)

        self.assertIsInstance(resultado_estudiante, (Generator))

        lista_resultado = list(resultado_estudiante)
        self.assertTrue(all(isinstance(item, tuple) for item in lista_resultado), 'Revisa que el primer generador sea de tuples')
        self.assertTrue(all(isinstance(item, Generator) for _, item in lista_resultado), 'Revisa que las ids astronauta se entregen como generador')

        lista_resultado = [(k, tuple(v)) for k, v in lista_resultado]
        lista_esperada = NAVES_ASTRONAUTAS_RANGO_M_1

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M, y que retorne vacío.
        """

        tamano = "out_M"

        path = os.path.join("data", tamano, "Tripulacion.csv")

        g_t = cargar_tripulaciones(path)

        resultado_estudiante = naves_astronautas_rango(g_t, 3, 6)

        self.assertIsInstance(resultado_estudiante, (Generator))

        lista_resultado = list(resultado_estudiante)
        self.assertTrue(all(isinstance(item, tuple) for item in lista_resultado), 'Revisa que el primer generador sea de tuples')
        self.assertTrue(all(isinstance(item, Generator) for _, item in lista_resultado), 'Revisa que las ids astronauta se entregen como generador')

        lista_resultado = [(k, tuple(v)) for k, v in lista_resultado]
        lista_esperada = NAVES_ASTRONAUTAS_RANGO_M_2

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """

        tamano = "out_L"

        path = os.path.join("data", tamano, "Tripulacion.csv")

        g_t = cargar_tripulaciones(path)

        resultado_estudiante = naves_astronautas_rango(g_t, 2, 3)

        self.assertIsInstance(resultado_estudiante, (Generator))

        lista_resultado = list(resultado_estudiante)
        self.assertTrue(all(isinstance(item, tuple) for item in lista_resultado), 'Revisa que el primer generador sea de tuples')
        self.assertTrue(all(isinstance(item, Generator) for _, item in lista_resultado), 'Revisa que las ids astronauta se entregen como generador')

        lista_resultado = [(k, tuple(v)) for k, v in lista_resultado]
        lista_esperada = NAVES_ASTRONAUTAS_RANGO_L_1

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """

        tamano = "out_L"

        path = os.path.join("data", tamano, "Tripulacion.csv")

        g_t = cargar_tripulaciones(path)

        resultado_estudiante = naves_astronautas_rango(g_t, 4, 6)

        self.assertIsInstance(resultado_estudiante, (Generator))

        lista_resultado = list(resultado_estudiante)
        self.assertTrue(all(isinstance(item, tuple) for item in lista_resultado), 'Revisa que el primer generador sea de tuples')
        self.assertTrue(all(isinstance(item, Generator) for _, item in lista_resultado), 'Revisa que las ids astronauta se entregen como generador')

        lista_resultado = [(k, tuple(v)) for k, v in lista_resultado]
        lista_esperada = NAVES_ASTRONAUTAS_RANGO_L_2

        self.assertCountEqual(lista_resultado, lista_esperada)
