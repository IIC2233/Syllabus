import os
import sys
import unittest
from collections.abc import Iterable
from backend.consultas import planetas_visitados_por_nave
from utilidades import Mision, Planeta, Tripulacion
from tests_publicos.timeout_function import timeout
sys.stdout = open(os.devnull, 'w')


# Constante para timeout en tests
N_SECOND = 0.08


class TestPlanetasVisitadosPorNave(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica que se retorne el unico planeta que se visitó.
        """

        lista_misiones = [
            Mision(
                id_mision=1,
                fecha="2024-03-02",
                hora="22:33",
                id_equipo=1,
                id_planeta=1,
                lograda=True
            )
        ]

        lista_planetas = [
            Planeta(
                id_planeta=1,
                nombre="Marte",
                coordenada_x=2341.12,
                coordenada_y=-3284193.12,
                tamano="S",
                tipo="Rojo")
        ]

        lista_tripulacion = [
            Tripulacion(
                id_equipo=1,
                patente_nave="N-1",
                id_astronauta=1,
                rango=5),
            Tripulacion(
                id_equipo=1,
                patente_nave="N-1",
                id_astronauta=2,
                rango=5),
            Tripulacion(
                id_equipo=1,
                patente_nave="N-1",
                id_astronauta=3,
                rango=5)
        ]

        lista_esperada = [("N-1", "Marte", 1)]

        g_mis = (mision for mision in lista_misiones)

        g_planetas = (planeta for planeta in lista_planetas)

        g_t = (tripulacion for tripulacion in lista_tripulacion)

        resultado_estudiante = planetas_visitados_por_nave(g_planetas, g_mis, g_t)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        self.assertTrue(all(isinstance(item, tuple) for item in lista_resultado))

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se manejen cuando hay más de un planeta visitado.
        """

        lista_misiones = [
            Mision(
                id_mision=1,
                fecha="2024-03-02",
                hora="22:33",
                id_equipo=1,
                id_planeta=1,
                lograda=True
            ),
            Mision(
                id_mision=2,
                fecha="2022-05-10",
                hora="10:17",
                id_equipo=1,
                id_planeta=2,
                lograda=True
            )
        ]

        lista_planetas = lista_planetas = [
            Planeta(
                id_planeta=1,
                nombre="Miércole",
                coordenada_x=2341.12,
                coordenada_y=-3284193.12,
                tamano="S",
                tipo="Rojo"),
            Planeta(
                id_planeta=2,
                nombre="Agua",
                coordenada_x=0.12,
                coordenada_y=12.12,
                tamano="M",
                tipo="Sólido"),
            ]

        lista_tripulacion = [
            Tripulacion(
                id_equipo=1,
                patente_nave="N-1",
                id_astronauta=1,
                rango=5),
            Tripulacion(
                id_equipo=1,
                patente_nave="N-1",
                id_astronauta=2,
                rango=5),
            Tripulacion(
                id_equipo=1,
                patente_nave="N-1",
                id_astronauta=3,
                rango=5)
        ]

        lista_esperada = [("N-1", "Miércole", 1), ("N-1", "Agua", 2)]

        g_mis = (mision for mision in lista_misiones)

        g_planetas = (planeta for planeta in lista_planetas)

        g_t = (tripulacion for tripulacion in lista_tripulacion)

        resultado_estudiante = planetas_visitados_por_nave(g_planetas, g_mis, g_t)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        self.assertTrue(all(isinstance(item, tuple) for item in lista_resultado))

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se retornen bien cuando hay visitas de equipos diferentes, y hay planetas no
        visitados
        """

        lista_misiones = [
            Mision(
                id_mision=1,
                fecha="2024-06-11",
                hora="13:31",
                id_equipo=1,
                id_planeta=3,
                lograda=True
            ),
            Mision(
                id_mision=2,
                fecha="2026-09-06",
                hora="03:21",
                id_equipo=2,
                id_planeta=4,
                lograda=False
            )
        ]

        lista_planetas = [
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

        lista_tripulacion = [
            Tripulacion(
                id_equipo=1,
                patente_nave="N-1",
                id_astronauta=1,
                rango=5),
            Tripulacion(
                id_equipo=1,
                patente_nave="N-1",
                id_astronauta=3,
                rango=5),
            Tripulacion(
                id_equipo=1,
                patente_nave="N-1",
                id_astronauta=9,
                rango=5),
            Tripulacion(
                id_equipo=2,
                patente_nave="N-2",
                id_astronauta=2,
                rango=5),
            Tripulacion(
                id_equipo=2,
                patente_nave="N-2",
                id_astronauta=7,
                rango=5)
        ]

        lista_esperada = [("N-1", "Mercurio", 3), ("N-2", "Venus", 4)]

        g_mis = (mision for mision in lista_misiones)

        g_planetas = (planeta for planeta in lista_planetas)

        g_t = (tripulacion for tripulacion in lista_tripulacion)

        resultado_estudiante = planetas_visitados_por_nave(g_planetas, g_mis, g_t)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        self.assertTrue(all(isinstance(item, tuple) for item in lista_resultado))

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que se considere cuando una mision no se ha realizado
        """

        lista_misiones = [
            Mision(
                id_mision=1,
                fecha="2024-06-11",
                hora="13:31",
                id_equipo=2,
                id_planeta=4,
                lograda=None
            )
        ]

        lista_planetas = [
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
            ]

        lista_tripulacion = [
            Tripulacion(
                id_equipo=2,
                patente_nave="N-1",
                id_astronauta=1,
                rango=5),
            Tripulacion(
                id_equipo=2,
                patente_nave="N-1",
                id_astronauta=3,
                rango=5)
        ]

        lista_esperada = [("N-1", None, None)]

        g_mis = (mision for mision in lista_misiones)

        g_planetas = (planeta for planeta in lista_planetas)

        g_t = (tripulacion for tripulacion in lista_tripulacion)

        resultado_estudiante = planetas_visitados_por_nave(g_planetas, g_mis, g_t)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        self.assertTrue(all(isinstance(item, tuple) for item in lista_resultado))

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que funcione si distintos equipos han ido al mismo planeta.
        """

        lista_misiones = [
            Mision(
                id_mision=1,
                fecha="2024-06-11",
                hora="13:31",
                id_equipo=1,
                id_planeta=5,
                lograda=True
            ),
            Mision(
                id_mision=2,
                fecha="2021-05-08",
                hora="11:24",
                id_equipo=2,
                id_planeta=5,
                lograda=True
            )
        ]

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

        lista_tripulacion = [
            Tripulacion(
                id_equipo=1,
                patente_nave="N-1",
                id_astronauta=1,
                rango=5),
            Tripulacion(
                id_equipo=1,
                patente_nave="N-1",
                id_astronauta=3,
                rango=5),
            Tripulacion(
                id_equipo=3,
                patente_nave="N-3",
                id_astronauta=1,
                rango=5),
            Tripulacion(
                id_equipo=2,
                patente_nave="N-2",
                id_astronauta=1,
                rango=5),
        ]

        lista_esperada = [("N-1", "Saturno", 5), ("N-2", "Saturno", 5), ("N-3", None, None)]

        g_mis = (mision for mision in lista_misiones)

        g_planetas = (planeta for planeta in lista_planetas)

        g_t = (tripulacion for tripulacion in lista_tripulacion)

        resultado_estudiante = planetas_visitados_por_nave(g_planetas, g_mis, g_t)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        self.assertTrue(all(isinstance(item, tuple) for item in lista_resultado))

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica que solo se declare solo una vez cuando hay dos misiones en el mismo planeta
        """

        lista_misiones = [
            Mision(
                id_mision=1,
                fecha="2023-09-03",
                hora="19:27",
                id_equipo=7,
                id_planeta=542,
                lograda=False
            ),
            Mision(
                id_mision=2,
                fecha="2026-11-04'",
                hora="19:27",
                id_equipo=7,
                id_planeta=542,
                lograda=False
            )
        ]

        lista_planetas = [
            Planeta(
                id_planeta=542,
                nombre="Tierra-0",
                coordenada_x=2341.12,
                coordenada_y=-3284193.12,
                tamano="S",
                tipo="Sólido"),
            ]

        lista_tripulacion = [
            Tripulacion(
                id_equipo=7,
                patente_nave="H0L4",
                id_astronauta=1,
                rango=5),
            Tripulacion(
                id_equipo=7,
                patente_nave="H0L4",
                id_astronauta=2,
                rango=5),
            Tripulacion(
                id_equipo=7,
                patente_nave="H0L4",
                id_astronauta=3,
                rango=5)
        ]

        lista_esperada = [("H0L4", "Tierra-0", 542)]

        g_mis = (mision for mision in lista_misiones)

        g_planetas = (planeta for planeta in lista_planetas)

        g_t = (tripulacion for tripulacion in lista_tripulacion)

        resultado_estudiante = planetas_visitados_por_nave(g_planetas, g_mis, g_t)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        self.assertTrue(all(isinstance(item, tuple) for item in lista_resultado))

        self.assertCountEqual(lista_resultado, lista_esperada)
