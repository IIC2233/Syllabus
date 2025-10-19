import os
import sys
import unittest
from collections.abc import Iterable
from backend.consultas import disponibilidad_por_planeta
from utilidades import Planeta, PlanetaMineral
from tests_publicos.timeout_function import timeout
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
        Verifica que se retorne el planeta y el mineral cuando es el único planeta pero tiene otros.
        """

        lista_planetas = [Planeta(
            id_planeta=1,
            nombre="Marte",
            coordenada_x=2341.12,
            coordenada_y=-3284193.12,
            tamano="S",
            tipo="Rojo"
        )]

        lista_minerales = [
            PlanetaMineral(
                id_planeta=1,
                id_mineral=100,
                cantidad_disponible=88325.98,
                pureza=0.98
            ),
            PlanetaMineral(
                id_planeta=1,
                id_mineral=101,
                cantidad_disponible=3211.98,
                pureza=0.12
            ),
            PlanetaMineral(
                id_planeta=1,
                id_mineral=102,
                cantidad_disponible=581394.98,
                pureza=0.65
            )
        ]

        lista_esperada = [("Marte", 1, 3211.98)]

        generador_planetas = (planeta for planeta in lista_planetas)

        generador_minerales = (mineral for mineral in lista_minerales)

        resultado_estudiante = disponibilidad_por_planeta(
            generador_minerales, generador_planetas, 101)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        self.assertTrue(all(isinstance(item, tuple) for item in lista_resultado))

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se retornen todos los planetas con el material.
        """

        lista_planetas = [
            Planeta(
                id_planeta=1,
                nombre="Marte",
                coordenada_x=2341.12,
                coordenada_y=-3284193.12,
                tamano="S",
                tipo="Rojo"),
            Planeta(
                id_planeta=2,
                nombre="Tierra",
                coordenada_x=0.12,
                coordenada_y=12.12,
                tamano="M",
                tipo="Sólido")]

        lista_minerales = [
            PlanetaMineral(
                id_planeta=1,
                id_mineral=100,
                cantidad_disponible=88325.98,
                pureza=0.98
            ),
            PlanetaMineral(
                id_planeta=1,
                id_mineral=101,
                cantidad_disponible=211.98,
                pureza=0.12
            ),
            PlanetaMineral(
                id_planeta=1,
                id_mineral=102,
                cantidad_disponible=581394.98,
                pureza=0.65
            ),
            PlanetaMineral(
                id_planeta=2,
                id_mineral=101,
                cantidad_disponible=100.98,
                pureza=0.54
            ),
        ]

        lista_esperada = [("Marte", 1, 211.98), ("Tierra", 2, 100.98)]

        generador_planetas = (planeta for planeta in lista_planetas)

        generador_minerales = (mineral for mineral in lista_minerales)

        resultado_estudiante = disponibilidad_por_planeta(
            generador_minerales, generador_planetas, 101)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        self.assertTrue(all(isinstance(item, tuple) for item in lista_resultado))

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se retorne el planeta sin producción del mineral.
        """

        lista_planetas = [
            Planeta(
                id_planeta=1,
                nombre="Marte",
                coordenada_x=2341.12,
                coordenada_y=-3284193.12,
                tamano="S",
                tipo="Rojo"),
            Planeta(
                id_planeta=2,
                nombre="Tierra",
                coordenada_x=0.12,
                coordenada_y=12.12,
                tamano="M",
                tipo="Sólido")]

        lista_minerales = [
            PlanetaMineral(
                id_planeta=1,
                id_mineral=100,
                cantidad_disponible=88325.98,
                pureza=0.98
            ),
            PlanetaMineral(
                id_planeta=1,
                id_mineral=101,
                cantidad_disponible=3211.98,
                pureza=0.12
            ),
            PlanetaMineral(
                id_planeta=1,
                id_mineral=102,
                cantidad_disponible=581394.98,
                pureza=0.65
            ),
            PlanetaMineral(
                id_planeta=2,
                id_mineral=101,
                cantidad_disponible=100.98,
                pureza=0.54
            ),
        ]

        lista_esperada = [("Marte", 1, 88325.98), ("Tierra", 2, 0.0)]

        generador_planetas = (planeta for planeta in lista_planetas)

        generador_minerales = (mineral for mineral in lista_minerales)

        resultado_estudiante = disponibilidad_por_planeta(
            generador_minerales, generador_planetas, 100)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        self.assertTrue(all(isinstance(item, tuple) for item in lista_resultado))

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que se considere el mismo material con otra pureza
        """

        lista_planetas = [
            Planeta(
                id_planeta=1,
                nombre="Marte",
                coordenada_x=2341.12,
                coordenada_y=-3284193.12,
                tamano="S",
                tipo="Rojo"),
            Planeta(
                id_planeta=2,
                nombre="Tierra",
                coordenada_x=0.12,
                coordenada_y=12.12,
                tamano="M",
                tipo="Sólido")]

        lista_minerales = [
            PlanetaMineral(
                id_planeta=1,
                id_mineral=101,
                cantidad_disponible=581394.98,
                pureza=0.65
            ),
            PlanetaMineral(
                id_planeta=2,
                id_mineral=101,
                cantidad_disponible=100.98,
                pureza=0.54
            ),
        ]

        lista_esperada = [("Marte", 1, 581394.98), ("Tierra", 2, 100.98)]

        generador_planetas = (planeta for planeta in lista_planetas)

        generador_minerales = (mineral for mineral in lista_minerales)

        resultado_estudiante = disponibilidad_por_planeta(
            generador_minerales, generador_planetas, 101)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        self.assertTrue(all(isinstance(item, tuple) for item in lista_resultado))

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que funcione si algun planeta no tienen ningun material
        """

        lista_planetas = [
            Planeta(
                id_planeta=1,
                nombre="Marte",
                coordenada_x=2341.12,
                coordenada_y=-3284193.12,
                tamano="S",
                tipo="Rojo"),
            Planeta(
                id_planeta=2,
                nombre="Tierra",
                coordenada_x=0.12,
                coordenada_y=12.12,
                tamano="M",
                tipo="Sólido"),
            Planeta(
                id_planeta=3,
                nombre="Mercurio",
                coordenada_x=2355.52,
                coordenada_y=834782.32,
                tamano="L",
                tipo="Gaseoso")]

        lista_minerales = [
            PlanetaMineral(
                id_planeta=1,
                id_mineral=100,
                cantidad_disponible=88325.98,
                pureza=0.98
            ),
            PlanetaMineral(
                id_planeta=1,
                id_mineral=103,
                cantidad_disponible=3211.98,
                pureza=0.12
            ),
            PlanetaMineral(
                id_planeta=1,
                id_mineral=101,
                cantidad_disponible=581394.98,
                pureza=0.65
            ),
            PlanetaMineral(
                id_planeta=2,
                id_mineral=103,
                cantidad_disponible=100.98,
                pureza=0.54
            ),
        ]

        lista_esperada = [("Marte", 1, 3211.98), ("Tierra", 2, 100.98), ("Mercurio", 3, 0.0)]

        generador_planetas = (planeta for planeta in lista_planetas)

        generador_minerales = (mineral for mineral in lista_minerales)

        resultado_estudiante = disponibilidad_por_planeta(
            generador_minerales, generador_planetas, 103)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        self.assertTrue(all(isinstance(item, tuple) for item in lista_resultado))

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica que funcione si algun planeta no tienen ningun material y otros lo tienen
        """

        lista_planetas = [
            Planeta(
                id_planeta=1,
                nombre="Marte",
                coordenada_x=2341.12,
                coordenada_y=-3284193.12,
                tamano="S",
                tipo="Rojo"),
            Planeta(
                id_planeta=2,
                nombre="Tierra",
                coordenada_x=0.12,
                coordenada_y=12.12,
                tamano="M",
                tipo="Sólido"),
            Planeta(
                id_planeta=3,
                nombre="Mercurio",
                coordenada_x=46247.52,
                coordenada_y=765.32,
                tamano="L",
                tipo="Gaseoso"),
            Planeta(
                id_planeta=4,
                nombre="Venus",
                coordenada_x=1923.11,
                coordenada_y=9387.32,
                tamano="L",
                tipo="Gaseoso"),
            Planeta(
                id_planeta=5,
                nombre="Saturno",
                coordenada_x=193.74,
                coordenada_y=86834.12,
                tamano="L",
                tipo="Anilloso")]

        lista_minerales = [
            PlanetaMineral(
                id_planeta=1,
                id_mineral=103,
                cantidad_disponible=1234.56,
                pureza=0.98
            ),
            PlanetaMineral(
                id_planeta=3,
                id_mineral=104,
                cantidad_disponible=3211.98,
                pureza=0.12
            ),
            PlanetaMineral(
                id_planeta=4,
                id_mineral=101,
                cantidad_disponible=581394.98,
                pureza=0.65
            ),
            PlanetaMineral(
                id_planeta=2,
                id_mineral=104,
                cantidad_disponible=100.98,
                pureza=0.54
            ),
            PlanetaMineral(
                id_planeta=3,
                id_mineral=103,
                cantidad_disponible=22.33,
                pureza=0.54
            ),
            PlanetaMineral(
                id_planeta=5,
                id_mineral=103,
                cantidad_disponible=2025.02,
                pureza=0.65
            )
        ]

        lista_esperada = [
            ("Marte", 1, 1234.56), ("Tierra", 2, 0.0), ("Mercurio", 3, 22.33),
            ("Venus", 4, 0.0), ("Saturno", 5, 2025.02)]

        generador_planetas = (planeta for planeta in lista_planetas)

        generador_minerales = (mineral for mineral in lista_minerales)

        resultado_estudiante = disponibilidad_por_planeta(
            generador_minerales, generador_planetas, 103)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        self.assertTrue(all(isinstance(item, tuple) for item in lista_resultado))

        self.assertCountEqual(lista_resultado, lista_esperada)
