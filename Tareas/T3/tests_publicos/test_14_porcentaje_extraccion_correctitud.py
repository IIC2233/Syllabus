import os
import sys
import unittest
from backend.consultas import porcentaje_extraccion
from utilidades import MisionMineral, PlanetaMineral, Tripulacion, Mision
from tests_publicos.timeout_function import timeout
sys.stdout = open(os.devnull, 'w')


# Constante para timeout en tests
N_SECOND = 0.08


class TestPorcentajeExtraccion(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica que se retorne bien la cantidad con sólo un tripulante.
        """

        mision = Mision(
                id_mision=1,
                fecha="2024-03-02",
                hora="22:33",
                id_equipo=1,
                id_planeta=1,
                lograda=True
            )

        lista_planetas_mineral = [
            PlanetaMineral(
                id_planeta=1,
                id_mineral=2,
                cantidad_disponible=935.28,
                pureza=0.87
            )
        ]

        lista_tripulacion = [
            Tripulacion(
                id_equipo=1,
                patente_nave="N-1",
                id_astronauta=1,
                rango=5)
        ]

        lista_mision_mineral = [
            MisionMineral(
                id_mision=1,
                id_mineral=2,
                cantidad=689.23
                )
        ]

        cantidad = 689.23 * 100 / (935.28 * 0.87)

        tupla_esperada = (cantidad, cantidad)
        tupla_esperada = (round(tupla_esperada[0], 2), round(tupla_esperada[1], 2))

        g_mis = (mision_mineral for mision_mineral in lista_mision_mineral)
        g_planetas = (planeta for planeta in lista_planetas_mineral)

        g_t = (tripulacion for tripulacion in lista_tripulacion)

        resultado_estudiante = porcentaje_extraccion(g_t, g_mis, g_planetas, mision)

        tupla_estudiante = (round(resultado_estudiante[0], 2), round(resultado_estudiante[1], 2))

        self.assertIsInstance(resultado_estudiante, tuple)

        self.assertTupleEqual(tupla_estudiante, tupla_esperada)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se divida bien en los tripulantes.
        """

        mision = Mision(
                id_mision=1,
                fecha="2024-03-02",
                hora="22:33",
                id_equipo=1,
                id_planeta=1,
                lograda=True
            )

        lista_planetas_mineral = [
            PlanetaMineral(
                id_planeta=1,
                id_mineral=3,
                cantidad_disponible=823.58,
                pureza=0.54
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
        ]

        lista_mision_mineral = [
            MisionMineral(
                id_mision=1,
                id_mineral=3,
                cantidad=274.93
                )
        ]

        cantidad = 274.93 * 100 / (823.58 * 0.54)

        tupla_esperada = (cantidad, cantidad/2)
        tupla_esperada = (round(tupla_esperada[0], 2), round(tupla_esperada[1], 2))

        g_mis = (mision_mineral for mision_mineral in lista_mision_mineral)

        g_planetas = (planeta for planeta in lista_planetas_mineral)

        g_t = (tripulacion for tripulacion in lista_tripulacion)

        resultado_estudiante = porcentaje_extraccion(g_t, g_mis, g_planetas, mision)
        tupla_estudiante = (round(resultado_estudiante[0], 2), round(resultado_estudiante[1], 2))

        self.assertIsInstance(resultado_estudiante, tuple)

        self.assertTupleEqual(tupla_estudiante, tupla_esperada)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se considere bien cuando hay más de un material, con sólo una persona
        """

        mision = Mision(
                id_mision=1,
                fecha="2024-06-11",
                hora="13:31",
                id_equipo=1,
                id_planeta=3,
                lograda=True)

        lista_planetas_mineral = [
            PlanetaMineral(
                id_planeta=3,
                id_mineral=2,
                cantidad_disponible=543.21,
                pureza=0.62
            ),
            PlanetaMineral(
                id_planeta=3,
                id_mineral=1,
                cantidad_disponible=735.29,
                pureza=0.89
            )]

        lista_tripulacion = [
            Tripulacion(
                id_equipo=1,
                patente_nave="N-1",
                id_astronauta=1,
                rango=5),
        ]

        lista_mision_mineral = [
            MisionMineral(
                id_mision=1,
                id_mineral=1,
                cantidad=274.93
                ),
            MisionMineral(
                id_mision=1,
                id_mineral=2,
                cantidad=233.13
                ),
        ]

        total = 543.21 * 0.62 + 735.29 * 0.89

        cantidad = 274.93 + 233.13

        porcentaje = cantidad*100/total

        tupla_esperada = (porcentaje, porcentaje)
        tupla_esperada = (round(tupla_esperada[0], 2), round(tupla_esperada[1], 2))

        g_mis = (mision_mineral for mision_mineral in lista_mision_mineral)
        g_planetas = (planeta for planeta in lista_planetas_mineral)

        g_t = (tripulacion for tripulacion in lista_tripulacion)

        resultado_estudiante = porcentaje_extraccion(g_t, g_mis, g_planetas, mision)
        tupla_estudiante = (round(resultado_estudiante[0], 2), round(resultado_estudiante[1], 2))

        self.assertIsInstance(resultado_estudiante, tuple)

        self.assertTupleEqual(tupla_estudiante, tupla_esperada)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que se no considere tripulantes que no corresponden al equipo
        """

        mision = Mision(
                id_mision=1,
                fecha="2024-06-11",
                hora="13:31",
                id_equipo=2,
                id_planeta=1,
                lograda=True
            )

        lista_planetas_mineral = [
            PlanetaMineral(
                id_planeta=1,
                id_mineral=1,
                cantidad_disponible=18813.12,
                pureza=0.43
            )
            ]

        lista_tripulacion = [
            Tripulacion(
                id_equipo=2,
                patente_nave="N-2",
                id_astronauta=1,
                rango=5),
            Tripulacion(
                id_equipo=2,
                patente_nave="N-2",
                id_astronauta=3,
                rango=5),
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

        lista_mision_mineral = [
            MisionMineral(
                id_mision=1,
                id_mineral=1,
                cantidad=274.93
                )
        ]

        cantidad = 100 * 274.93 / (18813.12 * 0.43)

        tupla_esperada = (cantidad, cantidad/2)
        tupla_esperada = (round(tupla_esperada[0], 2), round(tupla_esperada[1], 2))

        g_mis = (mision_mineral for mision_mineral in lista_mision_mineral)
        g_planetas = (planeta for planeta in lista_planetas_mineral)

        g_t = (tripulacion for tripulacion in lista_tripulacion)

        resultado_estudiante = porcentaje_extraccion(g_t, g_mis, g_planetas, mision)

        tupla_estudiante = (round(resultado_estudiante[0], 2), round(resultado_estudiante[1], 2))

        self.assertIsInstance(resultado_estudiante, tuple)

        self.assertTupleEqual(tupla_estudiante, tupla_esperada)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que funcione si hay minerales asociados a otros planetas y minerales asociados a
        otras misiones.
        """

        mision = Mision(
                id_mision=1,
                fecha="2024-06-11",
                hora="13:31",
                id_equipo=2,
                id_planeta=5,
                lograda=True
            )

        lista_planetas_mineral = [
            PlanetaMineral(
                id_planeta=1,
                id_mineral=2,
                cantidad_disponible=935.28,
                pureza=0.87
            ),
            PlanetaMineral(
                id_planeta=4,
                id_mineral=2,
                cantidad_disponible=8129.28,
                pureza=0.23
            ),
            PlanetaMineral(
                id_planeta=5,
                id_mineral=1,
                cantidad_disponible=4415.20,
                pureza=0.51
            )
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
                rango=5),
            Tripulacion(
                id_equipo=2,
                patente_nave="N-3",
                id_astronauta=2,
                rango=5),
            Tripulacion(
                id_equipo=2,
                patente_nave="N-2",
                id_astronauta=4,
                rango=5),
        ]

        lista_mision_mineral = [
            MisionMineral(
                id_mision=1,
                id_mineral=1,
                cantidad=911.93
                ),
            MisionMineral(
                id_mision=5,
                id_mineral=81,
                cantidad=918.39
                ),
            MisionMineral(
                id_mision=2,
                id_mineral=4,
                cantidad=537.93
                )
        ]

        total = 911.93 * 100 / (4415.20 * 0.51)

        tupla_esperada = (total, total/4)
        tupla_esperada = (round(tupla_esperada[0], 2), round(tupla_esperada[1], 2))

        g_mis = (mision_mineral for mision_mineral in lista_mision_mineral)
        g_planetas = (planeta for planeta in lista_planetas_mineral)

        g_t = (tripulacion for tripulacion in lista_tripulacion)

        resultado_estudiante = porcentaje_extraccion(g_t, g_mis, g_planetas, mision)

        tupla_estudiante = (round(resultado_estudiante[0], 2), round(resultado_estudiante[1], 2))

        self.assertIsInstance(resultado_estudiante, tuple)

        self.assertTupleEqual(tupla_estudiante, tupla_esperada)

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica que sólo se considere misiones hechas
        """

        mision = Mision(
                id_mision=1,
                fecha="2023-09-03",
                hora="19:27",
                id_equipo=7,
                id_planeta=542,
                lograda=None
            )

        lista_planetas_mineral = [
            PlanetaMineral(
                id_planeta=542,
                id_mineral=2,
                cantidad_disponible=935.28,
                pureza=0.87
            ),
            PlanetaMineral(
                id_planeta=1,
                id_mineral=2,
                cantidad_disponible=935.28,
                pureza=0.87
            )
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

        lista_mision_mineral = [
            MisionMineral(
                id_mision=1,
                id_mineral=1,
                cantidad=274.93
                ),
            MisionMineral(
                id_mision=1,
                id_mineral=2,
                cantidad=233.13
                ),
        ]

        tupla_esperada = (0.0, 0.0)

        g_mis = (mision_mineral for mision_mineral in lista_mision_mineral)
        g_planetas = (planeta for planeta in lista_planetas_mineral)

        g_t = (tripulacion for tripulacion in lista_tripulacion)

        resultado_estudiante = porcentaje_extraccion(g_t, g_mis, g_planetas, mision)
        tupla_estudiante = (round(resultado_estudiante[0], 2), round(resultado_estudiante[1], 2))

        self.assertIsInstance(resultado_estudiante, tuple)

        self.assertTupleEqual(tupla_estudiante, tupla_esperada)
