import os
import sys
import unittest
from collections.abc import Iterable
from backend.consultas import naves_de_material, cargar_naves
from tests_privados.timeout_function import timeout
from tests_privados.utils import FLEXIBILIDAD_ADICIONAL
from tests_privados.solution.test_0 import (
    NAVES_DE_MATERIAL_S_1,
    NAVES_DE_MATERIAL_M_1,
    NAVES_DE_MATERIAL_L_1,
    NAVES_DE_MATERIAL_S_2,
    NAVES_DE_MATERIAL_M_2,
    NAVES_DE_MATERIAL_L_2
)

sys.stdout = open(os.devnull, 'w')


# Constante para timeout en tests
N_SECOND = FLEXIBILIDAD_ADICIONAL*0.08


class TestNavesDeMaterial(unittest.TestCase):

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

        resultado_estudiante = naves_de_material(generador_naves, "Grafeno")

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        lista_esperada = NAVES_DE_MATERIAL_S_1

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S.
        """

        tamano = "out_new_S"

        path = os.path.join("data_new", tamano, "Nave.csv")

        generador_naves = cargar_naves(path)

        resultado_estudiante = naves_de_material(generador_naves, "Compósito")

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        lista_esperada = NAVES_DE_MATERIAL_S_2

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """

        tamano = "out_new_M"

        path = os.path.join("data_new", tamano, "Nave.csv")

        generador_naves = cargar_naves(path)

        resultado_estudiante = naves_de_material(generador_naves, "Acero Inoxidable")

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        lista_esperada = NAVES_DE_MATERIAL_M_1

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """

        tamano = "out_new_M"

        path = os.path.join("data_new", tamano, "Nave.csv")

        generador_naves = cargar_naves(path)

        resultado_estudiante = naves_de_material(generador_naves, "Compósito")

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        lista_esperada = NAVES_DE_MATERIAL_M_2

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """

        tamano = "out_new_L"

        path = os.path.join("data_new", tamano, "Nave.csv")

        generador_naves = cargar_naves(path)

        resultado_estudiante = naves_de_material(generador_naves, "Grafeno")

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        lista_esperada = NAVES_DE_MATERIAL_L_1

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """

        tamano = "out_new_L"

        path = os.path.join("data_new", tamano, "Nave.csv")

        generador_naves = cargar_naves(path)

        resultado_estudiante = naves_de_material(generador_naves, "Titanio")

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        lista_esperada = NAVES_DE_MATERIAL_L_2

        self.assertCountEqual(lista_resultado, lista_esperada)
