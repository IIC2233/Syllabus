import os
import sys
import unittest
from collections.abc import Iterable
from backend.consultas import naves_pueden_llevar
from utilidades import Nave, PlanetaMineral
from tests_publicos.timeout_function import timeout
sys.stdout = open(os.devnull, 'w')

# ver tema float


# Constante para timeout en tests
N_SECOND = 0.08


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
                tamano="L", capacidad_astronautas=5, capacidad_minerales=500.5, autonomia=509.54),
        ]

        lista_minerales = [
            PlanetaMineral(
                id_planeta=1,
                id_mineral=2,
                cantidad_disponible=935.28,
                pureza=0.87
            )
        ]

        id_planeta = 1

        esperado = [("N-101", 2, 500.5*100/935.28)]

        generador_minerales = (mineral for mineral in lista_minerales)

        generador_naves = (nave for nave in lista_naves)

        resultado_estudiante = naves_pueden_llevar(generador_naves, generador_minerales, id_planeta)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        resultado = list(resultado_estudiante)

        lista_resultado = [(patente, id, round(cantidad, 2)) for patente, id, cantidad in resultado]

        lista_esperada = [(patente, id, round(cantidad, 2)) for patente, id, cantidad in esperado]

        self.assertTrue(all(isinstance(item, tuple) for item in lista_resultado))

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que la función pueda retornar más de un material para la misma nave.
        """

        lista_naves = [
            Nave(
                patente="N-101",
                material="Grafeno",
                tamano="L", capacidad_astronautas=5, capacidad_minerales=320.45, autonomia=509.54),
        ]

        lista_minerales = [
            PlanetaMineral(
                id_planeta=1,
                id_mineral=2,
                cantidad_disponible=935.28,
                pureza=0.87
            ),
            PlanetaMineral(
                id_planeta=1,
                id_mineral=5,
                cantidad_disponible=324.71,
                pureza=0.87
            )
        ]

        id_planeta = 1

        esperado = [("N-101", 2, 320.45*100/935.28), ("N-101", 5, 320.45*100/324.71)]

        generador_minerales = (mineral for mineral in lista_minerales)

        generador_naves = (nave for nave in lista_naves)

        resultado_estudiante = naves_pueden_llevar(generador_naves, generador_minerales, id_planeta)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        resultado = list(resultado_estudiante)

        lista_resultado = [(patente, id, round(cantidad, 2)) for patente, id, cantidad in resultado]

        lista_esperada = [(patente, id, round(cantidad, 2)) for patente, id, cantidad in esperado]

        self.assertTrue(all(isinstance(item, tuple) for item in lista_resultado))

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que funcione para varias naves.
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

        lista_minerales = [
            PlanetaMineral(
                id_planeta=1,
                id_mineral=4,
                cantidad_disponible=935.28,
                pureza=0.87
            )
        ]

        id_planeta = 1

        esperado = [
            ("N-101", 4, 450.68*100/935.28),
            ("N-102", 4, 450.66*100/935.28),
            ("N-103", 4, 742.91*100/935.28)]

        generador_minerales = (mineral for mineral in lista_minerales)

        generador_naves = (nave for nave in lista_naves)

        resultado_estudiante = naves_pueden_llevar(generador_naves, generador_minerales, id_planeta)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        resultado = list(resultado_estudiante)

        lista_resultado = [(patente, id, round(cantidad, 2)) for patente, id, cantidad in resultado]

        lista_esperada = [(patente, id, round(cantidad, 2)) for patente, id, cantidad in esperado]

        self.assertTrue(all(isinstance(item, tuple) for item in lista_resultado))

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que solo se retornen los materiales del planeta.
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

        id_planeta = 1

        esperado = [("N-008", 2, 342.31*100/823.21), ("N-008", 4, 342.31*100/375.28)]

        generador_minerales = (mineral for mineral in lista_minerales)

        generador_naves = (nave for nave in lista_naves)

        resultado_estudiante = naves_pueden_llevar(generador_naves, generador_minerales, id_planeta)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        resultado = list(resultado_estudiante)

        lista_resultado = [(patente, id, round(cantidad, 2)) for patente, id, cantidad in resultado]

        lista_esperada = [(patente, id, round(cantidad, 2)) for patente, id, cantidad in esperado]

        self.assertTrue(all(isinstance(item, tuple) for item in lista_resultado))

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que no se lleven más de la totalidad del mineral.
        """

        lista_naves = [
            Nave(
                patente="N-007",
                material="Titanio",
                tamano="L", capacidad_astronautas=7, capacidad_minerales=765.13, autonomia=999.56),
            ]

        lista_minerales = [
            PlanetaMineral(
                id_planeta=1,
                id_mineral=2,
                cantidad_disponible=769.28,
                pureza=0.84
            ),
            PlanetaMineral(
                id_planeta=1,
                id_mineral=5,
                cantidad_disponible=235.98,
                pureza=0.15
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
            )
        ]

        id_planeta = 1

        esperado = [
            ("N-007", 2, 765.13*100/769.28),
            ("N-007", 5, 100),
            ("N-007", 3, 100),
            ("N-007", 11, 765.13*100/2233.28)]

        generador_minerales = (mineral for mineral in lista_minerales)

        generador_naves = (nave for nave in lista_naves)

        resultado_estudiante = naves_pueden_llevar(generador_naves, generador_minerales, id_planeta)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        resultado = list(resultado_estudiante)

        lista_resultado = [(patente, id, round(cantidad, 2)) for patente, id, cantidad in resultado]

        lista_esperada = [(patente, id, round(cantidad, 2)) for patente, id, cantidad in esperado]

        self.assertTrue(all(isinstance(item, tuple) for item in lista_resultado))

        self.assertCountEqual(lista_resultado, lista_esperada)

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
                tamano="M", capacidad_astronautas=4, capacidad_minerales=0.00, autonomia=734.21),
            Nave(
                patente="N-007",
                material="Titanio",
                tamano="L", capacidad_astronautas=7, capacidad_minerales=765.13, autonomia=999.56),
        ]

        lista_minerales = [
            PlanetaMineral(
                id_planeta=3,
                id_mineral=3,
                cantidad_disponible=98.28,
                pureza=0.71
            ),
            PlanetaMineral(
                id_planeta=23,
                id_mineral=11,
                cantidad_disponible=470.23,
                pureza=0.65
            )
        ]

        id_planeta = 23

        esperado = [
            ("N-002", 11, 100*450.36/470.23),
            ("N-003", 11, 0.00),
            ("N-007", 11, 100),
            ]

        generador_minerales = (mineral for mineral in lista_minerales)

        generador_naves = (nave for nave in lista_naves)

        resultado_estudiante = naves_pueden_llevar(generador_naves, generador_minerales, id_planeta)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        resultado = list(resultado_estudiante)

        lista_resultado = [(patente, id, round(cantidad, 2)) for patente, id, cantidad in resultado]

        lista_esperada = [(patente, id, round(cantidad, 2)) for patente, id, cantidad in esperado]

        self.assertTrue(all(isinstance(item, tuple) for item in lista_resultado))

        self.assertCountEqual(lista_resultado, lista_esperada)
