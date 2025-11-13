import os
import sys
import unittest
from collections.abc import Iterable
from backend.consultas import naves_de_material
from utilidades import Nave
from tests_privados.timeout_function import timeout
from tests_privados.utils import FLEXIBILIDAD_ADICIONAL
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
        Verifica que se retorne lista con el material (1).
        """

        lista_naves = [
            Nave(
                patente="N-101",
                material="Grafeno",
                tamano="L", capacidad_astronautas=5, capacidad_minerales=500.57, autonomia=509.54),
            Nave(
                patente="N-102",
                material="Compósito",
                tamano="L", capacidad_astronautas=5, capacidad_minerales=450.86, autonomia=304.20),
            Nave(
                patente="N-103",
                material="Titanio",
                tamano="L", capacidad_astronautas=5, capacidad_minerales=742.61, autonomia=400.21)
        ]

        generador_naves = (nave for nave in lista_naves)

        resultado_estudiante = naves_de_material(generador_naves, "Compósito")

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        lista_esperada = [
            Nave(
                patente="N-102",
                material="Compósito",
                tamano="L", capacidad_astronautas=5, capacidad_minerales=450.86, autonomia=304.20),
            ]

        self.assertEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se retorne lista con el material cuando no es alguno de los nombres anteriores.
        """

        lista_naves = [Nave(
                patente="N-00123",
                material="Titanio",
                tamano="L", capacidad_astronautas=9, capacidad_minerales=450.36, autonomia=304.20),
            Nave(
                patente="N-003",
                material="Titanio",
                tamano="M", capacidad_astronautas=4, capacidad_minerales=628.41, autonomia=734.21),
            Nave(
                patente="N-004",
                material="Oro",
                tamano="M", capacidad_astronautas=2, capacidad_minerales=893.41, autonomia=87.24),
            Nave(
                patente="N-005",
                material="Grafeno",
                tamano="XL",
                capacidad_astronautas=3, capacidad_minerales=556.18, autonomia=724.91),
            ]

        generador_vacio = (nave for nave in lista_naves)

        resultado_estudiante = naves_de_material(generador_vacio, "Oro")

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        lista_esperada = [Nave(
                patente="N-004",
                material="Oro",
                tamano="M", capacidad_astronautas=2, capacidad_minerales=893.41, autonomia=87.24),
            ]

        self.assertEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se no se retorne ninguna nave.
        """

        lista_naves = [
            Nave(
                patente="N-101",
                material="Grafeno",
                tamano="L", capacidad_astronautas=5, capacidad_minerales=500.85, autonomia=509.54),
            Nave(
                patente="N-102",
                material="Compósito",
                tamano="L", capacidad_astronautas=5, capacidad_minerales=450.66, autonomia=304.20),
            Nave(
                patente="N-103",
                material="Titanio",
                tamano="L", capacidad_astronautas=5, capacidad_minerales=742.91, autonomia=400.21)
        ]

        generador_naves = (nave for nave in lista_naves)

        resultado_estudiante = naves_de_material(generador_naves, "Plata")

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        self.assertCountEqual(lista_resultado, [])

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que se retorne todas las naves que contienen el material (5).
        """

        lista_naves = [
            Nave(
                patente="N-444",
                material="Titanio",
                tamano="L", capacidad_astronautas=9, capacidad_minerales=450.36, autonomia=304.20),
            Nave(
                patente="N-111",
                material="Titanio",
                tamano="M", capacidad_astronautas=4, capacidad_minerales=628.41, autonomia=734.21),
            Nave(
                patente="N-222",
                material="Aluminio",
                tamano="M", capacidad_astronautas=2, capacidad_minerales=893.41, autonomia=87.24),
            Nave(
                patente="N-333",
                material="Titanio",
                tamano="L", capacidad_astronautas=3, capacidad_minerales=500.45, autonomia=509.54),
            Nave(
                patente="N-888",
                material="Grafeno",
                tamano="XL",
                capacidad_astronautas=3, capacidad_minerales=556.18, autonomia=724.91),
            Nave(
                patente="N-555",
                material="Titanio",
                tamano="S", capacidad_astronautas=8, capacidad_minerales=400.31, autonomia=746.45),
            Nave(
                patente="N-007",
                material="Aluminio",
                tamano="L", capacidad_astronautas=7, capacidad_minerales=765.13, autonomia=999.56),
            Nave(
                patente="N-008",
                material="Acero inoxidable",
                tamano="L", capacidad_astronautas=2, capacidad_minerales=342.31, autonomia=843.87),
            Nave(
                patente="N-009",
                material="Aluminio",
                tamano="L", capacidad_astronautas=10, capacidad_minerales=645.27, autonomia=365.83),
            Nave(
                patente="N-112",
                material="Titanio",
                tamano="L", capacidad_astronautas=9, capacidad_minerales=814.36, autonomia=164.20)
            ]

        lista_esperada = [
            Nave(
                patente="N-444",
                material="Titanio",
                tamano="L", capacidad_astronautas=9, capacidad_minerales=450.36, autonomia=304.20),
            Nave(
                patente="N-111",
                material="Titanio",
                tamano="M", capacidad_astronautas=4, capacidad_minerales=628.41, autonomia=734.21),
            Nave(
                patente="N-333",
                material="Titanio",
                tamano="L", capacidad_astronautas=3, capacidad_minerales=500.45, autonomia=509.54),
            Nave(
                patente="N-555",
                material="Titanio",
                tamano="S", capacidad_astronautas=8, capacidad_minerales=400.31, autonomia=746.45),
            Nave(
                patente="N-112",
                material="Titanio",
                tamano="L", capacidad_astronautas=9, capacidad_minerales=814.36, autonomia=164.20)
            ]

        generador_naves = (nave for nave in lista_naves)

        resultado_estudiante = naves_de_material(generador_naves, "Titanio")

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que se retorne todas las naves del generador.
        """

        lista_naves = [
            Nave(
                patente="N-001",
                material="Titanio",
                tamano="L", capacidad_astronautas=3, capacidad_minerales=500.45, autonomia=509.54),
            Nave(
                patente="N-002",
                material="Titanio",
                tamano="L", capacidad_astronautas=9, capacidad_minerales=450.36, autonomia=304.20),
            Nave(
                patente="N-003",
                material="Titanio",
                tamano="M", capacidad_astronautas=4, capacidad_minerales=628.41, autonomia=734.21),
            Nave(
                patente="N-007",
                material="Titanio",
                tamano="L", capacidad_astronautas=7, capacidad_minerales=765.13, autonomia=999.56),
            ]

        lista_esperada = [
            Nave(
                patente="N-001",
                material="Titanio",
                tamano="L", capacidad_astronautas=3, capacidad_minerales=500.45, autonomia=509.54),
            Nave(
                patente="N-002",
                material="Titanio",
                tamano="L", capacidad_astronautas=9, capacidad_minerales=450.36, autonomia=304.20),
            Nave(
                patente="N-003",
                material="Titanio",
                tamano="M", capacidad_astronautas=4, capacidad_minerales=628.41, autonomia=734.21),
            Nave(
                patente="N-007",
                material="Titanio",
                tamano="L", capacidad_astronautas=7, capacidad_minerales=765.13, autonomia=999.56),
            ]

        generador_naves = (nave for nave in lista_naves)

        resultado_estudiante = naves_de_material(generador_naves, "Titanio")

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica que se retornen las naves del material.
        """

        lista_naves = [
            Nave(
                patente="N-891",
                material="Grafeno",
                tamano="L", capacidad_astronautas=5, capacidad_minerales=500.85, autonomia=509.54),
            Nave(
                patente="N-112",
                material="Compósito",
                tamano="L", capacidad_astronautas=5, capacidad_minerales=450.66, autonomia=304.20),
            Nave(
                patente="N-103",
                material="Titanio",
                tamano="L", capacidad_astronautas=5, capacidad_minerales=742.91, autonomia=400.21),
            Nave(
                patente="N-001",
                material="Plumavit",
                tamano="L", capacidad_astronautas=3, capacidad_minerales=500.45, autonomia=509.54),
            Nave(
                patente="N-002",
                material="Plastico",
                tamano="L", capacidad_astronautas=9, capacidad_minerales=450.36, autonomia=304.20),
            Nave(
                patente="N-235",
                material="Titanio",
                tamano="M", capacidad_astronautas=4, capacidad_minerales=628.41, autonomia=734.21),
            Nave(
                patente="N-2t46",
                material="Plumavit",
                tamano="M", capacidad_astronautas=2, capacidad_minerales=893.41, autonomia=87.24),
            Nave(
                patente="N-8w2",
                material="Titanio",
                tamano="XL",
                capacidad_astronautas=3, capacidad_minerales=556.18, autonomia=724.91)
            ]

        lista_esperada = [
            Nave(
                patente="N-001",
                material="Plumavit",
                tamano="L", capacidad_astronautas=3, capacidad_minerales=500.45, autonomia=509.54),
            Nave(
                patente="N-2t46",
                material="Plumavit",
                tamano="M", capacidad_astronautas=2, capacidad_minerales=893.41, autonomia=87.24),
            ]

        generador_naves = (nave for nave in lista_naves)

        resultado_estudiante = naves_de_material(generador_naves, "Plumavit")

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        self.assertCountEqual(lista_resultado, lista_esperada)
