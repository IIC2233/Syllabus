import os
import sys
import unittest
from collections.abc import Iterable
from backend.consultas import naves_por_intervalo_carga, cargar_naves
from tests_publicos.timeout_function import timeout
from tests_publicos.solution.test_2 import (
    NAVES_POR_INTERVALO_CARGA_S_1,
    NAVES_POR_INTERVALO_CARGA_M_1,
    NAVES_POR_INTERVALO_CARGA_L_1,
    NAVES_POR_INTERVALO_CARGA_S_2,
    NAVES_POR_INTERVALO_CARGA_M_2,
    NAVES_POR_INTERVALO_CARGA_L_2
)

sys.stdout = open(os.devnull, 'w')


# Constante para timeout en tests
N_SECOND = 0.08


class TestNavesPorIntervaloDeCarga(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S.
        """

        tamano = "out_S"

        path = os.path.join("data", tamano, "Nave.csv")

        generador_naves = cargar_naves(path)

        tupla = (1217.19, 1861.46)

        resultado_estudiante = naves_por_intervalo_carga(generador_naves, tupla)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        lista_esperada = NAVES_POR_INTERVALO_CARGA_S_1

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S.
        """

        tamano = "out_S"

        path = os.path.join("data", tamano, "Nave.csv")

        generador_naves = cargar_naves(path)

        tupla = (1280.17, 1635.65)

        resultado_estudiante = naves_por_intervalo_carga(generador_naves, tupla)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        lista_esperada = NAVES_POR_INTERVALO_CARGA_S_2

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """

        tamano = "out_M"

        path = os.path.join("data", tamano, "Nave.csv")

        generador_naves = cargar_naves(path)

        tupla = (748.73, 1219.52)

        resultado_estudiante = naves_por_intervalo_carga(generador_naves, tupla)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        lista_esperada = NAVES_POR_INTERVALO_CARGA_M_1

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M, y que retorne vacío.
        """

        tamano = "out_M"

        path = os.path.join("data", tamano, "Nave.csv")

        generador_naves = cargar_naves(path)

        tupla = (1498.98, 1984.95)

        resultado_estudiante = naves_por_intervalo_carga(generador_naves, tupla)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        lista_esperada = NAVES_POR_INTERVALO_CARGA_M_2

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """

        tamano = "out_L"

        path = os.path.join("data", tamano, "Nave.csv")

        generador_naves = cargar_naves(path)

        tupla = (1208.08, 1929.21)

        resultado_estudiante = naves_por_intervalo_carga(generador_naves, tupla)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        lista_esperada = NAVES_POR_INTERVALO_CARGA_L_1

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """

        tamano = "out_L"

        path = os.path.join("data", tamano, "Nave.csv")

        generador_naves = cargar_naves(path)

        tupla = (751.3, 1989.99)

        resultado_estudiante = naves_por_intervalo_carga(generador_naves, tupla)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        lista_esperada = NAVES_POR_INTERVALO_CARGA_L_2

        self.assertCountEqual(lista_resultado, lista_esperada)
