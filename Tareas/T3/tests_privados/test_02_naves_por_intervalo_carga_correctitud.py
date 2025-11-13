import os
import sys
import unittest
from collections.abc import Iterable
from backend.consultas import naves_por_intervalo_carga
from utilidades import Nave
from tests_privados.timeout_function import timeout
from tests_privados.utils import FLEXIBILIDAD_ADICIONAL
sys.stdout = open(os.devnull, 'w')


# Constante para timeout en tests
N_SECOND = FLEXIBILIDAD_ADICIONAL*0.08


class TestNavesPorIntervaloCarga(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica que se retorne la lista nave que hay.
        """

        lista_naves = [
            Nave(
                patente="N-101",
                material="Grafeno",
                tamano="L", capacidad_astronautas=5, capacidad_minerales=500.5, autonomia=509.54),
            ]

        generador_naves = (nave for nave in lista_naves)

        tupla = (0, 1000.912)

        resultado_estudiante = naves_por_intervalo_carga(generador_naves, tupla)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        lista_esperada = [
            Nave(
                patente="N-101",
                material="Grafeno",
                tamano="L", capacidad_astronautas=5, capacidad_minerales=500.5, autonomia=509.54),
            ]

        self.assertEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que la función pueda retornar las naves que están en el límite inferior.
        """

        lista_naves = [
            Nave(
                patente="N-987",
                material="Grafeno",
                tamano="L", capacidad_astronautas=5, capacidad_minerales=450.00, autonomia=509.54),
            Nave(
                patente="IIC-2233",
                material="Compósito",
                tamano="L", capacidad_astronautas=5, capacidad_minerales=450.00, autonomia=304.20),
            Nave(
                patente="Nave",
                material="Titanio",
                tamano="L", capacidad_astronautas=5, capacidad_minerales=450.00, autonomia=400.21)
        ]

        generador_naves = (nave for nave in lista_naves)

        tupla = (450.00, 750.00)

        resultado_estudiante = naves_por_intervalo_carga(generador_naves, tupla)

        lista_esperada = [
            Nave(
                patente="N-987",
                material="Grafeno",
                tamano="L", capacidad_astronautas=5, capacidad_minerales=450.00, autonomia=509.54),
            Nave(
                patente="IIC-2233",
                material="Compósito",
                tamano="L", capacidad_astronautas=5, capacidad_minerales=450.00, autonomia=304.20),
            Nave(
                patente="Nave",
                material="Titanio",
                tamano="L", capacidad_astronautas=5, capacidad_minerales=450.00, autonomia=400.21)
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
                tamano="L", capacidad_astronautas=5, capacidad_minerales=627.31, autonomia=509.54),
            Nave(
                patente="N-102",
                material="Compósito",
                tamano="L", capacidad_astronautas=5, capacidad_minerales=604.56, autonomia=304.20),
            Nave(
                patente="N-103",
                material="Titanio",
                tamano="L", capacidad_astronautas=5, capacidad_minerales=42.971, autonomia=400.21),
            Nave(
                patente="N-104",
                material="Acero Inoxidable",
                tamano="L", capacidad_astronautas=5, capacidad_minerales=118.92, autonomia=304.20),
            Nave(
                patente="N-105",
                material="Madera",
                tamano="L", capacidad_astronautas=5, capacidad_minerales=1997.2, autonomia=400.21)
        ]

        lista_esperada = [
            Nave(
                patente="N-101",
                material="Grafeno",
                tamano="L", capacidad_astronautas=5, capacidad_minerales=627.31, autonomia=509.54),
            Nave(
                patente="N-102",
                material="Compósito",
                tamano="L", capacidad_astronautas=5, capacidad_minerales=604.56, autonomia=304.20),
        ]

        generador_naves = (nave for nave in lista_naves)

        tupla = (450.67, 700.76)

        resultado_estudiante = naves_por_intervalo_carga(generador_naves, tupla)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que se retorne las naves, incluyendo ambos límites
        """

        lista_naves = [
            Nave(
                patente="Nave1",
                material="Titanio",
                tamano="L", capacidad_astronautas=3, capacidad_minerales=450.36, autonomia=509.54),
            Nave(
                patente="Nave2",
                material="Titanio",
                tamano="L", capacidad_astronautas=9, capacidad_minerales=500.45, autonomia=304.20),
            Nave(
                patente="Nave3",
                material="Titanio",
                tamano="M", capacidad_astronautas=4, capacidad_minerales=765.13, autonomia=734.21),
            Nave(
                patente="Nave4",
                material="Aluminio",
                tamano="M", capacidad_astronautas=2, capacidad_minerales=556.18, autonomia=87.24),
            Nave(
                patente="Nave5",
                material="Grafeno",
                tamano="XL",
                capacidad_astronautas=3, capacidad_minerales=893.41, autonomia=724.91),
            Nave(
                patente="Nave6",
                material="Titanio",
                tamano="S", capacidad_astronautas=8, capacidad_minerales=400.31, autonomia=746.45),
            Nave(
                patente="Nave7",
                material="Aluminio",
                tamano="L", capacidad_astronautas=7, capacidad_minerales=277.11, autonomia=999.56),
            Nave(
                patente="Nave8",
                material="Acero inoxidable",
                tamano="L", capacidad_astronautas=2, capacidad_minerales=342.31, autonomia=843.87),
            Nave(
                patente="Nave9",
                material="Aluminio",
                tamano="L", capacidad_astronautas=10, capacidad_minerales=645.27, autonomia=365.87)
        ]

        lista_esperada = [Nave(
                patente="Nave1",
                material="Titanio",
                tamano="L", capacidad_astronautas=3, capacidad_minerales=450.36, autonomia=509.54),
            Nave(
                patente="Nave2",
                material="Titanio",
                tamano="L", capacidad_astronautas=9, capacidad_minerales=500.45, autonomia=304.20),
            Nave(
                patente="Nave4",
                material="Aluminio",
                tamano="M", capacidad_astronautas=2, capacidad_minerales=556.18, autonomia=87.24),
            Nave(
                patente="Nave6",
                material="Titanio",
                tamano="S", capacidad_astronautas=8, capacidad_minerales=400.31, autonomia=746.45),
            Nave(
                patente="Nave8",
                material="Acero inoxidable",
                tamano="L", capacidad_astronautas=2, capacidad_minerales=342.31, autonomia=843.87),
            ]

        generador_naves = (nave for nave in lista_naves)

        tupla = (342.31, 556.18)

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
                patente="Nave1",
                material="Titanio",
                tamano="L", capacidad_astronautas=3, capacidad_minerales=450.36, autonomia=509.54),
            Nave(
                patente="Nave2",
                material="Titanio",
                tamano="L", capacidad_astronautas=9, capacidad_minerales=500.45, autonomia=304.20),
            Nave(
                patente="Nave3",
                material="Titanio",
                tamano="M", capacidad_astronautas=4, capacidad_minerales=765.13, autonomia=734.21),
            Nave(
                patente="Nave4",
                material="Aluminio",
                tamano="M", capacidad_astronautas=2, capacidad_minerales=556.18, autonomia=87.24),
            Nave(
                patente="Nave5",
                material="Grafeno",
                tamano="XL",
                capacidad_astronautas=3, capacidad_minerales=893.41, autonomia=724.91),
            Nave(
                patente="Nave6",
                material="Titanio",
                tamano="S", capacidad_astronautas=8, capacidad_minerales=981.41, autonomia=746.45),
            Nave(
                patente="Nave7",
                material="Aluminio",
                tamano="L", capacidad_astronautas=7, capacidad_minerales=277.11, autonomia=999.56),
            Nave(
                patente="Nave8",
                material="Acero inoxidable",
                tamano="L", capacidad_astronautas=2, capacidad_minerales=342.31, autonomia=843.87),
            Nave(
                patente="Nave9",
                material="Aluminio",
                tamano="L", capacidad_astronautas=10, capacidad_minerales=645.27, autonomia=365.87)
        ]

        lista_esperada = [
            Nave(
                patente="Nave3",
                material="Titanio",
                tamano="M", capacidad_astronautas=4, capacidad_minerales=765.13, autonomia=734.21),
            Nave(
                patente="Nave5",
                material="Grafeno",
                tamano="XL",
                capacidad_astronautas=3, capacidad_minerales=893.41, autonomia=724.91),
            Nave(
                patente="Nave6",
                material="Titanio",
                tamano="S", capacidad_astronautas=8, capacidad_minerales=981.41, autonomia=746.45),
            Nave(
                patente="Nave9",
                material="Aluminio",
                tamano="L", capacidad_astronautas=10, capacidad_minerales=645.27, autonomia=365.87)
        ]

        generador_naves = (nave for nave in lista_naves)

        tupla = (600.12, 981.41)

        resultado_estudiante = naves_por_intervalo_carga(generador_naves, tupla)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica que se retornen las naves entre medio.
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
                patente="N-002",
                material="Titanio",
                tamano="L", capacidad_astronautas=9, capacidad_minerales=450.36, autonomia=304.20),
            Nave(
                patente="N-006",
                material="Titanio",
                tamano="S", capacidad_astronautas=8, capacidad_minerales=400.31, autonomia=746.45),
            Nave(
                patente="N-008",
                material="Acero inoxidable",
                tamano="L", capacidad_astronautas=2, capacidad_minerales=342.31, autonomia=843.87),
            ]

        generador_naves = (nave for nave in lista_naves)

        tupla = (289.11, 459.99)

        resultado_estudiante = naves_por_intervalo_carga(generador_naves, tupla)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        self.assertCountEqual(lista_resultado, lista_esperada)
