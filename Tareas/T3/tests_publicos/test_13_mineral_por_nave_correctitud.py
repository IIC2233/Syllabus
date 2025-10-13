import os
import sys
import unittest
from collections.abc import Iterable
from backend.consultas import mineral_por_nave
from utilidades import Mision, MisionMineral, Tripulacion
from tests_publicos.timeout_function import timeout
sys.stdout = open(os.devnull, 'w')


# Constante para timeout en tests
N_SECOND = 0.08


class TestMineralPorNave(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica que se retorne el unico equipo con una mision.
        """

        lista_misiones = [
            Mision(
                id_mision=1,
                fecha="2024-03-02",
                hora="22:33",
                id_equipo=5,
                id_planeta=1,
                lograda=True
            )
        ]

        lista_minerales = [
            MisionMineral(
                id_mision=1,
                id_mineral=1,
                cantidad=22.33
                )
        ]

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

        lista_esperada = [("N-1", 22.33)]
        g_mis = [mision for mision in lista_misiones]

        g_min = [mineral for mineral in lista_minerales]

        g_t = [tripulacion for tripulacion in lista_tripulacion]

        resultado_estudiante = mineral_por_nave(g_t, g_mis, g_min)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se manejen bien cuando hay más de una misión.
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
            )
        ]

        lista_minerales = [
            MisionMineral(
                id_mision=1,
                id_mineral=1,
                cantidad=22.33
                ),
            MisionMineral(
                id_mision=1,
                id_mineral=4,
                cantidad=2356.54
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
                id_equipo=1,
                patente_nave="N-1",
                id_astronauta=3,
                rango=5)
        ]

        lista_esperada = [("N-1", 22.33 + 2356.54)]

        g_mis = [mision for mision in lista_misiones]

        g_min = [mineral for mineral in lista_minerales]

        g_t = [tripulacion for tripulacion in lista_tripulacion]

        resultado_estudiante = mineral_por_nave(g_t, g_mis, g_min)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se retornen bien cuando hay misiones de equipos diferentes
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
                fecha="2026-09-06",
                hora="03:21",
                id_equipo=2,
                id_planeta=626,
                lograda=True
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
                id_equipo=2,
                patente_nave="N-2",
                id_astronauta=2,
                rango=5),
            Tripulacion(
                id_equipo=1,
                patente_nave="N-1",
                id_astronauta=3,
                rango=5)
        ]

        lista_esperada = [("N-1", 1236.123), ("N-2", 4124.22)]

        g_mis = [mision for mision in lista_misiones]

        g_min = [mineral for mineral in lista_minerales]

        g_t = [tripulacion for tripulacion in lista_tripulacion]

        resultado_estudiante = mineral_por_nave(g_t, g_mis, g_min)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que se considere cuando una mision pide más de un material
        """

        lista_misiones = [
            Mision(
                id_mision=1,
                fecha="2024-06-11",
                hora="13:31",
                id_equipo=1,
                id_planeta=1,
                lograda=True
            )
        ]
        lista_minerales = [
            MisionMineral(
                id_mision=1,
                id_mineral=1,
                cantidad=5253.2
                ),
            MisionMineral(
                id_mision=1,
                id_mineral=4,
                cantidad=2356.54
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

        lista_esperada = [("N-1", 2356.54 + 5253.2)]

        g_mis = [mision for mision in lista_misiones]

        g_min = [mineral for mineral in lista_minerales]

        g_t = [tripulacion for tripulacion in lista_tripulacion]

        resultado_estudiante = mineral_por_nave(g_t, g_mis, g_min)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que funcione si alguna tripulacion no tiene ninguna mision
        """

        lista_misiones = [
            Mision(
                id_mision=1,
                fecha="2024-06-11",
                hora="13:31",
                id_equipo=2,
                id_planeta=1,
                lograda=True
            )
        ]
        lista_minerales = [
            MisionMineral(
                id_mision=1,
                id_mineral=1,
                cantidad=134138.12
                ),
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

        lista_esperada = [("N-1", 0.0), ("N-2", 134138.12), ("N-3", 0.0)]

        g_mis = [mision for mision in lista_misiones]

        g_min = [mineral for mineral in lista_minerales]

        g_t = [tripulacion for tripulacion in lista_tripulacion]

        resultado_estudiante = mineral_por_nave(g_t, g_mis, g_min)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica que solo sume las misiones que fueron logradas
        """

        lista_misiones = [
            Mision(
                id_mision=1,
                fecha="2023-09-03",
                hora="19:27",
                id_equipo=1,
                id_planeta=542,
                lograda=False
            ),
            Mision(
                id_mision=2,
                fecha="2025-01-07",
                hora="23:57",
                id_equipo=2,
                id_planeta=542,
                lograda=None
            )
        ]

        lista_minerales = [
            MisionMineral(
                id_mision=1,
                id_mineral=2,
                cantidad=35246.98
                ),
            MisionMineral(
                id_mision=2,
                id_mineral=4,
                cantidad=112.98
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
                id_equipo=1,
                patente_nave="N-1",
                id_astronauta=3,
                rango=5),
            Tripulacion(
                id_equipo=2,
                patente_nave="N-314",
                id_astronauta=3,
                rango=5)
        ]

        lista_esperada = [("N-1", 0.0), ("N-314", 0.0)]

        g_mis = [mision for mision in lista_misiones]

        g_min = [mineral for mineral in lista_minerales]

        g_t = [tripulacion for tripulacion in lista_tripulacion]

        resultado_estudiante = mineral_por_nave(g_t, g_mis, g_min)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_resultado = list(resultado_estudiante)

        self.assertCountEqual(lista_resultado, lista_esperada)
