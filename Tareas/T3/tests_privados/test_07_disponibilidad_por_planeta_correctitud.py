import os
import sys
import unittest
from collections.abc import Iterable
from backend.consultas import disponibilidad_por_planeta
from utilidades import Planeta, PlanetaMineral
from tests_privados.timeout_function import timeout
from tests_privados.utils import FLEXIBILIDAD_ADICIONAL
sys.stdout = open(os.devnull, 'w')


# Constante para timeout en tests
N_SECOND = FLEXIBILIDAD_ADICIONAL*0.08


class TestDisponibilidadPorPlaneta(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica que se retornen los dos planetas cuando ambos tienen otros materiales.
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
                nombre="Jupiter",
                coordenada_x=1566.12,
                coordenada_y=-26242.432,
                tamano="M",
                tipo="Gas"
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
            ),
            PlanetaMineral(
                id_planeta=2,
                id_mineral=102,
                cantidad_disponible=4.98,
                pureza=0.65
            )
        ]

        lista_esperada = [("Marte", 1, 581394.98), ("Jupiter", 2, 4.98)]

        generador_planetas = (planeta for planeta in lista_planetas)

        generador_minerales = (mineral for mineral in lista_minerales)

        resultado_estudiante = disponibilidad_por_planeta(
            generador_minerales, generador_planetas, 102)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        self.assertTrue(all(isinstance(item, tuple) for item in lista_resultado))

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se retorne 0 a todos los planetas que no tienen el material.
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

        lista_esperada = [("Marte", 1, 0.0), ("Tierra", 2, 0.0)]

        generador_planetas = (planeta for planeta in lista_planetas)

        generador_minerales = (mineral for mineral in lista_minerales)

        resultado_estudiante = disponibilidad_por_planeta(
            generador_minerales, generador_planetas, 2233)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        self.assertTrue(all(isinstance(item, tuple) for item in lista_resultado))

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se retorne bien para tres planetas.
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
                nombre="Jupiter",
                coordenada_x=26023.12,
                coordenada_y=124522.12,
                tamano="M",
                tipo="Rocoso")]

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
                cantidad_disponible=8222.98,
                pureza=0.65
            ),
            PlanetaMineral(
                id_planeta=2,
                id_mineral=101,
                cantidad_disponible=914.1424,
                pureza=0.54
            ),
            PlanetaMineral(
                id_planeta=2,
                id_mineral=103,
                cantidad_disponible=1352.98,
                pureza=0.12
            ),
            PlanetaMineral(
                id_planeta=3,
                id_mineral=101,
                cantidad_disponible=1556.98,
                pureza=0.12
            ),
            PlanetaMineral(
                id_planeta=3,
                id_mineral=102,
                cantidad_disponible=8653.98,
                pureza=0.12
            )
        ]

        lista_esperada = [("Marte", 1, 3211.98), ("Tierra", 2, 914.1424), ("Jupiter", 3, 1556.98)]

        generador_planetas = (planeta for planeta in lista_planetas)

        generador_minerales = (mineral for mineral in lista_minerales)

        resultado_estudiante = disponibilidad_por_planeta(
            generador_minerales, generador_planetas, 101)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        self.assertTrue(all(isinstance(item, tuple) for item in lista_resultado))

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que pueda recibir un generador vacío de minerales
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

        lista_minerales = []

        lista_esperada = [("Marte", 1, 0.0), ("Tierra", 2, 0.0)]

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
        Verifica que funcione si algun planeta no tienen ningun material y hay materiales con
        purezas distintas
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
                id_mineral=101,
                cantidad_disponible=987654.98,
                pureza=0.922
            ),
            PlanetaMineral(
                id_planeta=1,
                id_mineral=102,
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
            PlanetaMineral(
                id_planeta=3,
                id_mineral=103,
                cantidad_disponible=87654345.98,
                pureza=0.54
            )
        ]

        lista_esperada = [("Marte", 1, 0.0), ("Tierra", 2, 100.98), ("Mercurio", 3, 87654345.98)]

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
        Verifica que funcione para 5 planetas
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
                id_planeta=1,
                id_mineral=104,
                cantidad_disponible=8826.43,
                pureza=0.765
            ),
            PlanetaMineral(
                id_planeta=2,
                id_mineral=104,
                cantidad_disponible=9119.272,
                pureza=0.535
            ),
            PlanetaMineral(
                id_planeta=3,
                id_mineral=104,
                cantidad_disponible=9531.222,
                pureza=0.76
            ),
            PlanetaMineral(
                id_planeta=4,
                id_mineral=101,
                cantidad_disponible=581394.98,
                pureza=0.65
            ),
            PlanetaMineral(
                id_planeta=3,
                id_mineral=103,
                cantidad_disponible=22.33,
                pureza=0.54
            ),
            PlanetaMineral(
                id_planeta=4,
                id_mineral=104,
                cantidad_disponible=1106.003,
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
            ("Marte", 1, 8826.43), ("Tierra", 2, 9119.272), ("Mercurio", 3, 9531.222),
            ("Venus", 4, 1106.003), ("Saturno", 5, 0.0)]

        generador_planetas = (planeta for planeta in lista_planetas)

        generador_minerales = (mineral for mineral in lista_minerales)

        resultado_estudiante = disponibilidad_por_planeta(
            generador_minerales, generador_planetas, 104)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        self.assertTrue(all(isinstance(item, tuple) for item in lista_resultado))

        self.assertCountEqual(lista_resultado, lista_esperada)
