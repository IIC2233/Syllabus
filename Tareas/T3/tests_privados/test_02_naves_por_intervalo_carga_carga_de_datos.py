import os
import sys
import unittest
from collections.abc import Iterable
from backend.consultas import naves_por_intervalo_carga, cargar_naves
from tests_privados.timeout_function import timeout
from tests_privados.utils import FLEXIBILIDAD_ADICIONAL
from tests_privados.solution.test_2 import (
    NAVES_POR_INTERVALO_CARGA_S_1,
    NAVES_POR_INTERVALO_CARGA_M_1,
    NAVES_POR_INTERVALO_CARGA_L_1,
    NAVES_POR_INTERVALO_CARGA_S_2,
    NAVES_POR_INTERVALO_CARGA_M_2,
    NAVES_POR_INTERVALO_CARGA_L_2
)

sys.stdout = open(os.devnull, 'w')


# Constante para timeout en tests
N_SECOND = FLEXIBILIDAD_ADICIONAL*0.08


class TestNavesPorIntervaloDeCarga(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S.
        """

        tamano = "out_new_S"

        path = os.path.join("data_new", tamano, "Nave.csv")

        generador_naves = cargar_naves(path)

        tupla = (502.55, 611.14)

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

        tamano = "out_new_S"

        path = os.path.join("data_new", tamano, "Nave.csv")

        generador_naves = cargar_naves(path)

        tupla = (339.93, 552.45)

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

        tamano = "out_new_M"

        path = os.path.join("data_new", tamano, "Nave.csv")

        generador_naves = cargar_naves(path)

        tupla = (790.57, 929.68)

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

        tamano = "out_new_M"

        path = os.path.join("data_new", tamano, "Nave.csv")

        generador_naves = cargar_naves(path)

        tupla = (281.57, 1792.62)

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

        tamano = "out_new_L"

        path = os.path.join("data_new", tamano, "Nave.csv")

        generador_naves = cargar_naves(path)

        tupla = (721.72, 880.34)

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

        tamano = "out_new_L"

        path = os.path.join("data_new", tamano, "Nave.csv")

        generador_naves = cargar_naves(path)

        tupla = (1045.47, 1593.24)

        resultado_estudiante = naves_por_intervalo_carga(generador_naves, tupla)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        lista_esperada = NAVES_POR_INTERVALO_CARGA_L_2

        self.assertCountEqual(lista_resultado, lista_esperada)
