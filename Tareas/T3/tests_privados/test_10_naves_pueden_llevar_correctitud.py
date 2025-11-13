import os
import sys
import unittest
from collections.abc import Iterable
from backend.consultas import naves_pueden_llevar
from utilidades import Nave, PlanetaMineral
from tests_privados.timeout_function import timeout
from tests_privados.utils import FLEXIBILIDAD_ADICIONAL
sys.stdout = open(os.devnull, 'w')

# Constante para timeout en tests
N_SECOND = FLEXIBILIDAD_ADICIONAL*0.08


class TestNavesPuedenLlevar(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica que se retorne una nave con un unico material.
        """

        lista_naves = [
            Nave(
                patente="N-101",
                material="Grafeno",
                tamano="L", capacidad_astronautas=5, capacidad_minerales=341.98, autonomia=509.54),
            Nave(
                patente="N-102",
                material="Grafeno",
                tamano="L", capacidad_astronautas=5, capacidad_minerales=773.1, autonomia=509.54),
        ]

        lista_minerales = [
            PlanetaMineral(
                id_planeta=1,
                id_mineral=2,
                cantidad_disponible=6322.76,
                pureza=0.87
            )
        ]

        id_planeta = 1

        esperado = [("N-101", 2, 341.98*100/6322.76), ("N-102", 2, 773.1*100/6322.76)]

        generador_minerales = (mineral for mineral in lista_minerales)

        generador_naves = (nave for nave in lista_naves)

        resultado_estudiante = naves_pueden_llevar(generador_naves, generador_minerales, id_planeta)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        resultado = list(resultado_estudiante)

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
        Verifica que la función discrimine el planeta.
        """

        lista_naves = [
            Nave(
                patente="N-101",
                material="Grafeno",
                tamano="L", capacidad_astronautas=5, capacidad_minerales=73.64, autonomia=509.54),
        ]

        lista_minerales = [
            PlanetaMineral(
                id_planeta=1,
                id_mineral=2,
                cantidad_disponible=6322.76,
                pureza=0.87
            ),
            PlanetaMineral(
                id_planeta=2,
                id_mineral=2,
                cantidad_disponible=324.71,
                pureza=0.78
            )
        ]

        id_planeta = 2

        esperado = [("N-101", 2, 73.64*100/324.71)]

        generador_minerales = (mineral for mineral in lista_minerales)

        generador_naves = (nave for nave in lista_naves)

        resultado_estudiante = naves_pueden_llevar(generador_naves, generador_minerales, id_planeta)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        resultado = list(resultado_estudiante)

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
        Verifica que la misma nave pueda llevar la totalidad de un material pero parte de otro.
        """

        lista_naves = [
            Nave(
                patente="N-101",
                material="Grafeno",
                tamano="L", capacidad_astronautas=5, capacidad_minerales=450.68, autonomia=509.54),
            ]

        lista_minerales = [
            PlanetaMineral(
                id_planeta=1,
                id_mineral=4,
                cantidad_disponible=399.67,
                pureza=0.43
            ),
            PlanetaMineral(
                id_planeta=1,
                id_mineral=5,
                cantidad_disponible=808.41,
                pureza=0.87
            )
        ]

        id_planeta = 1

        esperado = [
            ("N-101", 4, 100),
            ("N-101", 5, 450.68*100/808.41)]

        generador_minerales = (mineral for mineral in lista_minerales)

        generador_naves = (nave for nave in lista_naves)

        resultado_estudiante = naves_pueden_llevar(generador_naves, generador_minerales, id_planeta)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        resultado = list(resultado_estudiante)

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
        Verifica que solo se retornen los materiales del planeta, cuando no hay ninguno.
        """

        lista_naves = [
            Nave(
                patente="N-008",
                material="Acero inoxidable",
                tamano="L", capacidad_astronautas=2, capacidad_minerales=342.31, autonomia=843.87),
            ]

        lista_minerales = [
            PlanetaMineral(
                id_planeta=1,
                id_mineral=2,
                cantidad_disponible=823.21,
                pureza=0.34
            ),
            PlanetaMineral(
                id_planeta=2,
                id_mineral=3,
                cantidad_disponible=528.17,
                pureza=0.09
            ),
            PlanetaMineral(
                id_planeta=1,
                id_mineral=4,
                cantidad_disponible=375.28,
                pureza=0.73
            ),
            PlanetaMineral(
                id_planeta=3,
                id_mineral=6,
                cantidad_disponible=833.28,
                pureza=0.19
            )
        ]

        id_planeta = 5

        esperado = [("N-008", 2, 0.0)]

        generador_minerales = (mineral for mineral in lista_minerales)

        generador_naves = (nave for nave in lista_naves)

        resultado_estudiante = naves_pueden_llevar(generador_naves, generador_minerales, id_planeta)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        resultado = list(resultado_estudiante)

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
        Combinaciones de lo anterior con dos naves
        """

        lista_naves = [
            Nave(
                patente="N-007",
                material="Titanio",
                tamano="L", capacidad_astronautas=7, capacidad_minerales=122.12, autonomia=999.56),
            Nave(
                patente="N-008",
                material="Compósito",
                tamano="L", capacidad_astronautas=7, capacidad_minerales=713.54, autonomia=134.56)
            ]

        lista_minerales = [
            PlanetaMineral(
                id_planeta=1,
                id_mineral=2,
                cantidad_disponible=431.12,
                pureza=0.84
            ),
            PlanetaMineral(
                id_planeta=1,
                id_mineral=3,
                cantidad_disponible=98.28,
                pureza=0.71
            ),
            PlanetaMineral(
                id_planeta=1,
                id_mineral=11,
                cantidad_disponible=2233.28,
                pureza=0.65
            ),
            PlanetaMineral(
                id_planeta=2,
                id_mineral=5,
                cantidad_disponible=235.98,
                pureza=0.15
            )
        ]

        id_planeta = 1

        esperado = [
            ("N-007", 2, 122.12*100/431.12),
            ("N-007", 3, 100),
            ("N-007", 11, 122.12*100/2233.28),
            ("N-008", 2, 100),
            ("N-008", 3, 100),
            ("N-008", 11, 713.54*100/2233.28)]

        generador_minerales = (mineral for mineral in lista_minerales)

        generador_naves = (nave for nave in lista_naves)

        resultado_estudiante = naves_pueden_llevar(generador_naves, generador_minerales, id_planeta)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        resultado = list(resultado_estudiante)

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
        Verifica que se cumplan mezclas de los tests anteriores.
        """

        lista_naves = [
            Nave(
                patente="N-002",
                material="Titanio",
                tamano="L", capacidad_astronautas=9, capacidad_minerales=450.36, autonomia=304.20),
            Nave(
                patente="N-003",
                material="Titanio",
                tamano="M", capacidad_astronautas=4, capacidad_minerales=111, autonomia=734.21),
            Nave(
                patente="N-007",
                material="Titanio",
                tamano="L", capacidad_astronautas=7, capacidad_minerales=765.13, autonomia=999.56),
        ]

        lista_minerales = [
            PlanetaMineral(
                id_planeta=3,
                id_mineral=3,
                cantidad_disponible=120.412,
                pureza=0.71
            ),
            PlanetaMineral(
                id_planeta=3,
                id_mineral=4,
                cantidad_disponible=651.12,
                pureza=0.14
            ),
            PlanetaMineral(
                id_planeta=23,
                id_mineral=11,
                cantidad_disponible=470.23,
                pureza=0.65
            )
        ]

        id_planeta = 3

        esperado = [
            ("N-002", 3, 100),
            ("N-003", 3, 111*100/120.412),
            ("N-007", 3, 100),
            ("N-002", 4, 100*450.36/651.12),
            ("N-003", 4, 111*100/651.12),
            ("N-007", 4, 100)
            ]

        generador_minerales = (mineral for mineral in lista_minerales)

        generador_naves = (nave for nave in lista_naves)

        resultado_estudiante = naves_pueden_llevar(generador_naves, generador_minerales, id_planeta)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        resultado = list(resultado_estudiante)

        for (
            patente_resultado, id_resultado, resultado_c1), (
                patente_esperado, id_esperado, esperado_c1) in zip(
                    sorted(resultado), sorted(esperado)):
            self.assertEqual(patente_resultado, patente_esperado)
            self.assertEqual(id_resultado, id_esperado)
            self.assertAlmostEqual(resultado_c1, esperado_c1, delta=0.010001)

        self.assertTrue(all(isinstance(item, tuple) for item in resultado))
