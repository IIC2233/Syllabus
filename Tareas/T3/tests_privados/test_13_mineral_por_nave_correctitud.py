import os
import sys
import unittest
from collections.abc import Iterable
from backend.consultas import mineral_por_nave
from utilidades import Mision, MisionMineral, Tripulacion
from tests_privados.timeout_function import timeout
from tests_privados.utils import FLEXIBILIDAD_ADICIONAL
sys.stdout = open(os.devnull, 'w')


# Constante para timeout en tests
N_SECOND = FLEXIBILIDAD_ADICIONAL*0.08


class TestMineralPorNave(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica que pueda recibir un generador vacío.
        """

        lista_misiones = []

        lista_minerales = []

        lista_tripulacion = [
            Tripulacion(
                id_equipo=5,
                patente_nave="N-1",
                id_astronauta=1,
                rango=5),
            Tripulacion(
                id_equipo=5,
                patente_nave="N-1",
                id_astronauta=2,
                rango=5),
            Tripulacion(
                id_equipo=5,
                patente_nave="N-1",
                id_astronauta=3,
                rango=5)
        ]

        lista_esperada = [("N-1", 0.0)]
        g_mis = (mision for mision in lista_misiones)

        g_min = (mineral for mineral in lista_minerales)

        g_t = (tripulacion for tripulacion in lista_tripulacion)

        resultado_estudiante = mineral_por_nave(g_t, g_mis, g_min)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se manejen bien cuando hay más de una misión de distintos equipos.
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
                id_planeta=1,
                lograda=True
            ),
            Mision(
                id_mision=3,
                fecha="2023-11-09",
                hora="22:33",
                id_equipo=2,
                id_planeta=1,
                lograda=True
            ),
            Mision(
                id_mision=4,
                fecha="2021-10-05",
                hora="10:17",
                id_equipo=2,
                id_planeta=1,
                lograda=True
            )
        ]

        lista_minerales = [
            MisionMineral(
                id_mision=1,
                id_mineral=1,
                cantidad=17.33
                ),
            MisionMineral(
                id_mision=2,
                id_mineral=4,
                cantidad=100.54
                ),
            MisionMineral(
                id_mision=3,
                id_mineral=1,
                cantidad=988.13
                ),
            MisionMineral(
                id_mision=4,
                id_mineral=4,
                cantidad=91734.124
                )
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
                id_equipo=2,
                patente_nave="N-12",
                id_astronauta=3,
                rango=5)
        ]

        lista_esperada = [("N-1", 17.33 + 100.54), ("N-12", 988.13 + 91734.124)]

        g_mis = (mision for mision in lista_misiones)

        g_min = (mineral for mineral in lista_minerales)

        g_t = (tripulacion for tripulacion in lista_tripulacion)

        resultado_estudiante = mineral_por_nave(g_t, g_mis, g_min)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se retornen bien cuando hay misiones de equipos diferentes y algunas no se
        hicieron
        """

        lista_misiones = [
            Mision(
                id_mision=1,
                fecha="2024-06-11",
                hora="13:31",
                id_equipo=1,
                id_planeta=1,
                lograda=True
            ),
            Mision(
                id_mision=2,
                fecha="2024-06-11",
                hora="13:31",
                id_equipo=1,
                id_planeta=1,
                lograda=True
            ),
            Mision(
                id_mision=3,
                fecha="2026-09-06",
                hora="03:21",
                id_equipo=2,
                id_planeta=626,
                lograda=False
            )
        ]

        lista_minerales = [
            MisionMineral(
                id_mision=1,
                id_mineral=12,
                cantidad=1236.123
                ),
            MisionMineral(
                id_mision=2,
                id_mineral=2,
                cantidad=4124.22
                )
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
                id_astronauta=3,
                rango=5),
            Tripulacion(
                id_equipo=2,
                patente_nave="N-2",
                id_astronauta=2,
                rango=5)
        ]

        lista_esperada = [("N-1", 1236.123 + 4124.22), ("N-2", 0.0)]

        g_mis = (mision for mision in lista_misiones)

        g_min = (mineral for mineral in lista_minerales)

        g_t = (tripulacion for tripulacion in lista_tripulacion)

        resultado_estudiante = mineral_por_nave(g_t, g_mis, g_min)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que se considere cuando varias misiones piden más de un material
        """

        lista_misiones = [
            Mision(
                id_mision=1,
                fecha="2024-06-11",
                hora="13:31",
                id_equipo=1,
                id_planeta=1,
                lograda=True
            ),
            Mision(
                id_mision=2,
                fecha="2020-12-12",
                hora="13:31",
                id_equipo=1,
                id_planeta=3,
                lograda=True
            )
        ]
        lista_minerales = [
            MisionMineral(
                id_mision=1,
                id_mineral=1,
                cantidad=1312.12
                ),
            MisionMineral(
                id_mision=1,
                id_mineral=4,
                cantidad=9876.12
                ),
            MisionMineral(
                id_mision=1,
                id_mineral=1,
                cantidad=8162.1
                ),
            MisionMineral(
                id_mision=1,
                id_mineral=4,
                cantidad=3.1415
                )
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
                id_astronauta=3,
                rango=5)
        ]

        lista_esperada = [("N-1", 1312.12 + 9876.12 + 8162.1 + 3.1415)]

        g_mis = (mision for mision in lista_misiones)

        g_min = (mineral for mineral in lista_minerales)

        g_t = (tripulacion for tripulacion in lista_tripulacion)

        resultado_estudiante = mineral_por_nave(g_t, g_mis, g_min)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que funcione si ninguna misión se cumplió / no se hizo
        """

        lista_misiones = [
            Mision(
                id_mision=1,
                fecha="2023-09-03",
                hora="19:27",
                id_equipo=1,
                id_planeta=1,
                lograda=False
            ),
            Mision(
                id_mision=2,
                fecha="2025-01-07",
                hora="23:57",
                id_equipo=2,
                id_planeta=1,
                lograda=None
            ),
            Mision(
                id_mision=3,
                fecha="2024-06-11",
                hora="13:31",
                id_equipo=2,
                id_planeta=1,
                lograda=False
            )
        ]

        lista_minerales = [
            MisionMineral(
                id_mision=1,
                id_mineral=1,
                cantidad=664351.33
                ),
            MisionMineral(
                id_mision=1,
                id_mineral=2,
                cantidad=8725.51
                ),
            MisionMineral(
                id_mision=1,
                id_mineral=3,
                cantidad=84753.61
                ),
            MisionMineral(
                id_mision=2,
                id_mineral=3,
                cantidad=138.12
                ),
            MisionMineral(
                id_mision=3,
                id_mineral=3,
                cantidad=442.123
                )
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
                id_astronauta=3,
                rango=5),
            Tripulacion(
                id_equipo=2,
                patente_nave="N-2",
                id_astronauta=1,
                rango=5),
            Tripulacion(
                id_equipo=3,
                patente_nave="N-3",
                id_astronauta=1,
                rango=5)
        ]

        lista_esperada = [("N-1", 0.0), ("N-2", 0.0), ("N-3", 0.0)]

        g_mis = (mision for mision in lista_misiones)

        g_min = (mineral for mineral in lista_minerales)

        g_t = (tripulacion for tripulacion in lista_tripulacion)

        resultado_estudiante = mineral_por_nave(g_t, g_mis, g_min)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica que funcione con para 4 naves si una no tiene misiones
        """

        lista_misiones = [
            Mision(
                id_mision=1,
                fecha="2023-09-03",
                hora="19:27",
                id_equipo=1,
                id_planeta=542,
                lograda=True
            ),
            Mision(
                id_mision=2,
                fecha="2025-01-07",
                hora="23:57",
                id_equipo=2,
                id_planeta=542,
                lograda=True
            ),
            Mision(
                id_mision=3,
                fecha="2021-05-10",
                hora="23:57",
                id_equipo=4,
                id_planeta=542,
                lograda=True
            ),
            Mision(
                id_mision=4,
                fecha="2026-07-01",
                hora="23:57",
                id_equipo=4,
                id_planeta=542,
                lograda=True
            )
        ]

        lista_minerales = [
            MisionMineral(
                id_mision=1,
                id_mineral=2,
                cantidad=27.1124
                ),
            MisionMineral(
                id_mision=2,
                id_mineral=4,
                cantidad=3.1415
                ),
            MisionMineral(
                id_mision=3,
                id_mineral=4,
                cantidad=2714.15
                ),
            MisionMineral(
                id_mision=4,
                id_mineral=4,
                cantidad=1566.415
                )
        ]

        lista_tripulacion = [
            Tripulacion(
                id_equipo=1,
                patente_nave="N-001",
                id_astronauta=1,
                rango=5),
            Tripulacion(
                id_equipo=1,
                patente_nave="N-001",
                id_astronauta=2,
                rango=5),
            Tripulacion(
                id_equipo=1,
                patente_nave="N-001",
                id_astronauta=3,
                rango=5),
            Tripulacion(
                id_equipo=2,
                patente_nave="N-002",
                id_astronauta=4,
                rango=5),
            Tripulacion(
                id_equipo=2,
                patente_nave="N-002",
                id_astronauta=5,
                rango=5),
            Tripulacion(
                id_equipo=3,
                patente_nave="N-003",
                id_astronauta=6,
                rango=5),
            Tripulacion(
                id_equipo=3,
                patente_nave="N-003",
                id_astronauta=7,
                rango=5),
            Tripulacion(
                id_equipo=4,
                patente_nave="N-004",
                id_astronauta=8,
                rango=5)
        ]

        total4 = 2714.15 + 1566.415

        lista_esperada = [("N-001", 27.1124), ("N-002", 3.1415), ("N-003", 0.0), ("N-004", total4)]

        g_mis = (mision for mision in lista_misiones)

        g_min = (mineral for mineral in lista_minerales)

        g_t = (tripulacion for tripulacion in lista_tripulacion)

        resultado_estudiante = mineral_por_nave(g_t, g_mis, g_min)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        self.assertCountEqual(lista_resultado, lista_esperada)
