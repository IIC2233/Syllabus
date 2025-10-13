import os
import sys
import unittest
from collections.abc import Iterable
from backend.consultas import naves_por_intervalo_carga
from utilidades import Nave
from tests_publicos.timeout_function import timeout
sys.stdout = open(os.devnull, 'w')


# Constante para timeout en tests
N_SECOND = 0.08


class TestNavesPorIntervaloCarga(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica que se retorne lista vacía cuando no hay naves en el intervalo.
        """

        lista_naves = [
            Nave(
                patente="N-101",
                material="Grafeno",
                tamano="L", capacidad_astronautas=5, capacidad_minerales=500.5, autonomia=509.54),
            Nave(
                patente="N-102",
                material="Compósito",
                tamano="L", capacidad_astronautas=5, capacidad_minerales=450.6, autonomia=304.20),
            Nave(
                patente="N-103",
                material="Titanio",
                tamano="L", capacidad_astronautas=5, capacidad_minerales=742.1, autonomia=400.21)
        ]

        generador_naves = (nave for nave in lista_naves)

        tupla = (200.12, 430.16)

        resultado_estudiante = naves_por_intervalo_carga(generador_naves, tupla)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        self.assertEqual(lista_resultado, [])

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que la función pueda retornar todas las naves.
        """

        lista_naves = [
            Nave(
                patente="N-101",
                material="Grafeno",
                tamano="L", capacidad_astronautas=5, capacidad_minerales=500.5, autonomia=509.54),
            Nave(
                patente="N-102",
                material="Compósito",
                tamano="L", capacidad_astronautas=5, capacidad_minerales=450.6, autonomia=304.20),
            Nave(
                patente="N-103",
                material="Titanio",
                tamano="L", capacidad_astronautas=5, capacidad_minerales=742.1, autonomia=400.21)
        ]

        generador_naves = (nave for nave in lista_naves)

        tupla = (450.00, 750.00)

        resultado_estudiante = naves_por_intervalo_carga(generador_naves, tupla)

        lista_esperada = [
            Nave(
                patente="N-101",
                material="Grafeno",
                tamano="L", capacidad_astronautas=5, capacidad_minerales=500.5, autonomia=509.54),
            Nave(
                patente="N-102",
                material="Compósito",
                tamano="L", capacidad_astronautas=5, capacidad_minerales=450.6, autonomia=304.20),
            Nave(
                patente="N-103",
                material="Titanio",
                tamano="L", capacidad_astronautas=5, capacidad_minerales=742.1, autonomia=400.21)
        ]

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se retorne las naves entre medio.
        """

        lista_naves = [
            Nave(
                patente="N-101",
                material="Grafeno",
                tamano="L", capacidad_astronautas=5, capacidad_minerales=450.68, autonomia=509.54),
            Nave(
                patente="N-102",
                material="Compósito",
                tamano="L", capacidad_astronautas=5, capacidad_minerales=450.66, autonomia=304.20),
            Nave(
                patente="N-103",
                material="Titanio",
                tamano="L", capacidad_astronautas=5, capacidad_minerales=742.91, autonomia=400.21)
        ]

        lista_esperada = [Nave(
                patente="N-101",
                material="Grafeno",
                tamano="L", capacidad_astronautas=5, capacidad_minerales=450.68, autonomia=509.54)]

        generador_naves = (nave for nave in lista_naves)

        tupla = (450.67, 700.76)

        resultado_estudiante = naves_por_intervalo_carga(generador_naves, tupla)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que se retorne las naves, con una en el límite inferior.
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
                patente="N-004",
                material="Aluminio",
                tamano="M", capacidad_astronautas=2, capacidad_minerales=893.41, autonomia=87.24),
            Nave(
                patente="N-005",
                material="Grafeno",
                tamano="XL",
                capacidad_astronautas=3, capacidad_minerales=556.18, autonomia=724.91),
            Nave(
                patente="N-006",
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
                tamano="L", capacidad_astronautas=10, capacidad_minerales=645.27, autonomia=365.87)
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
                patente="N-005",
                material="Grafeno",
                tamano="XL",
                capacidad_astronautas=3, capacidad_minerales=556.18, autonomia=724.91),
            Nave(
                patente="N-009",
                material="Aluminio",
                tamano="L", capacidad_astronautas=10, capacidad_minerales=645.27, autonomia=365.87)]

        generador_naves = (nave for nave in lista_naves)

        tupla = (450.36, 646.53)

        resultado_estudiante = naves_por_intervalo_carga(generador_naves, tupla)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que se retornen las naves, con una en el límite superior.
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
                patente="N-004",
                material="Aluminio",
                tamano="M", capacidad_astronautas=2, capacidad_minerales=893.41, autonomia=87.24),
            Nave(
                patente="N-005",
                material="Grafeno",
                tamano="XL",
                capacidad_astronautas=3, capacidad_minerales=556.18, autonomia=724.91),
            Nave(
                patente="N-006",
                material="Titanio",
                tamano="S", capacidad_astronautas=8, capacidad_minerales=400.31, autonomia=746.45),
            Nave(
                patente="N-007",
                material="Titanio",
                tamano="L", capacidad_astronautas=7, capacidad_minerales=765.13, autonomia=999.56),
            Nave(
                patente="N-008",
                material="Acero inoxidable",
                tamano="L", capacidad_astronautas=2, capacidad_minerales=342.31, autonomia=843.87),
            Nave(
                patente="N-009",
                material="Grafeno",
                tamano="L", capacidad_astronautas=10, capacidad_minerales=645.27, autonomia=365.87)
        ]

        lista_esperada = [
            Nave(
                patente="N-004",
                material="Aluminio",
                tamano="M", capacidad_astronautas=2, capacidad_minerales=893.41, autonomia=87.24),
            Nave(
                patente="N-007",
                material="Titanio",
                tamano="L", capacidad_astronautas=7, capacidad_minerales=765.13, autonomia=999.56),
            ]

        generador_naves = (nave for nave in lista_naves)

        tupla = (715.42, 893.41)

        resultado_estudiante = naves_por_intervalo_carga(generador_naves, tupla)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica que se retornen las naves incluyendo ambos límites.
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
                patente="N-004",
                material="Aluminio",
                tamano="M", capacidad_astronautas=2, capacidad_minerales=893.41, autonomia=87.24),
            Nave(
                patente="N-005",
                material="Grafeno",
                tamano="XL",
                capacidad_astronautas=3, capacidad_minerales=556.18, autonomia=724.91),
            Nave(
                patente="N-006",
                material="Titanio",
                tamano="S", capacidad_astronautas=8, capacidad_minerales=400.31, autonomia=746.45),
            Nave(
                patente="N-007",
                material="Titanio",
                tamano="L", capacidad_astronautas=7, capacidad_minerales=765.13, autonomia=999.56),
            Nave(
                patente="N-008",
                material="Acero inoxidable",
                tamano="L", capacidad_astronautas=2, capacidad_minerales=342.31, autonomia=843.87),
            Nave(
                patente="N-009",
                material="Grafeno",
                tamano="L", capacidad_astronautas=10, capacidad_minerales=645.27, autonomia=365.87)
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
                patente="N-005",
                material="Grafeno",
                tamano="XL",
                capacidad_astronautas=3, capacidad_minerales=556.18, autonomia=724.91),
            Nave(
                patente="N-006",
                material="Titanio",
                tamano="S", capacidad_astronautas=8, capacidad_minerales=400.31, autonomia=746.45),
            Nave(
                patente="N-008",
                material="Acero inoxidable",
                tamano="L", capacidad_astronautas=2, capacidad_minerales=342.31, autonomia=843.87)
        ]

        generador_naves = (nave for nave in lista_naves)

        tupla = (342.31, 628.41)

        resultado_estudiante = naves_por_intervalo_carga(generador_naves, tupla)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        self.assertCountEqual(lista_resultado, lista_esperada)
