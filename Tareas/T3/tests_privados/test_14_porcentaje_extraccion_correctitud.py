import os
import sys
import unittest
from backend.consultas import porcentaje_extraccion
from utilidades import MisionMineral, PlanetaMineral, Tripulacion, Mision
from tests_privados.timeout_function import timeout
from tests_privados.utils import FLEXIBILIDAD_ADICIONAL
sys.stdout = open(os.devnull, 'w')


# Constante para timeout en tests
N_SECOND = FLEXIBILIDAD_ADICIONAL*0.08


class TestPorcentajeExtraccion(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica que se retorne bien la cantidad con varios minerales y varios tripulantes.
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
                pureza=0.51
            ),
            PlanetaMineral(
                id_planeta=1,
                id_mineral=4,
                cantidad_disponible=15335,
                pureza=0.135
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
                rango=1),
            Tripulacion(
                id_equipo=1,
                patente_nave="N-1",
                id_astronauta=3,
                rango=4)
        ]

        lista_mision_mineral = [
            MisionMineral(
                id_mision=1,
                id_mineral=2,
                cantidad=334.13
                ),
            MisionMineral(
                id_mision=1,
                id_mineral=4,
                cantidad=312.213
                )
        ]

        total = 0.51 * 935.28 + 15335 * 0.135

        cantidad = (334.13 + 312.213) * 100 / total

        esperado = (cantidad, cantidad/3)

        g_mis = (mision_mineral for mision_mineral in lista_mision_mineral)
        g_planetas = (planeta for planeta in lista_planetas_mineral)

        g_t = (tripulacion for tripulacion in lista_tripulacion)

        resultado = porcentaje_extraccion(g_t, g_mis, g_planetas, mision)

        self.assertIsInstance(resultado, tuple)

        self.assertAlmostEqual(esperado[0], resultado[0])

        self.assertAlmostEqual(esperado[1], resultado[1])

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se sólo considere los minerales de la mision.
        """

        mision = Mision(
                id_mision=2,
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
                cantidad_disponible=1381.12,
                pureza=0.45
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
                ),
            MisionMineral(
                id_mision=2,
                id_mineral=3,
                cantidad=321.12
                ),
            MisionMineral(
                id_mision=3,
                id_mineral=3,
                cantidad=274.93
                )
        ]

        cantidad = 321.12 * 100 / (1381.12 * 0.45)

        esperado = (cantidad, cantidad/2)

        g_mis = (mision_mineral for mision_mineral in lista_mision_mineral)
        g_planetas = (planeta for planeta in lista_planetas_mineral)

        g_t = (tripulacion for tripulacion in lista_tripulacion)

        resultado = porcentaje_extraccion(g_t, g_mis, g_planetas, mision)

        self.assertIsInstance(resultado, tuple)

        self.assertAlmostEqual(esperado[0], resultado[0])

        self.assertAlmostEqual(esperado[1], resultado[1])

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

        esperado = (porcentaje, porcentaje)

        g_mis = (mision_mineral for mision_mineral in lista_mision_mineral)
        g_planetas = (planeta for planeta in lista_planetas_mineral)

        g_t = (tripulacion for tripulacion in lista_tripulacion)

        resultado = porcentaje_extraccion(g_t, g_mis, g_planetas, mision)

        self.assertIsInstance(resultado, tuple)

        self.assertAlmostEqual(esperado[0], resultado[0])

        self.assertAlmostEqual(esperado[1], resultado[1])

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que se no considere tripulantes que no corresponden al equipo, ni minerales que no
        se piden en la mision
        """

        mision = Mision(
                id_mision=1,
                fecha="2024-06-11",
                hora="13:31",
                id_equipo=1,
                id_planeta=1,
                lograda=True
            )

        lista_planetas_mineral = [
            PlanetaMineral(
                id_planeta=1,
                id_mineral=1,
                cantidad_disponible=12412515.12,
                pureza=0.43
            ),
            PlanetaMineral(
                id_planeta=1,
                id_mineral=2,
                cantidad_disponible=773236.2131,
                pureza=0.143
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
                patente_nave="N-2",
                id_astronauta=4,
                rango=5)
        ]

        lista_mision_mineral = [
            MisionMineral(
                id_mision=1,
                id_mineral=1,
                cantidad=14814.124
                ),
            MisionMineral(
                id_mision=1,
                id_mineral=2,
                cantidad=93.274
                ),
            MisionMineral(
                id_mision=2,
                id_mineral=1,
                cantidad=274.93
                )
        ]

        total = 12412515.12 * 0.43 + 773236.2131 * 0.143

        cantidad = 100 * (93.274 + 14814.124) / total

        esperado = (cantidad, cantidad/3)
        g_mis = (mision_mineral for mision_mineral in lista_mision_mineral)
        g_planetas = (planeta for planeta in lista_planetas_mineral)

        g_t = (tripulacion for tripulacion in lista_tripulacion)

        resultado = porcentaje_extraccion(g_t, g_mis, g_planetas, mision)

        self.assertIsInstance(resultado, tuple)

        self.assertAlmostEqual(esperado[0], resultado[0])

        self.assertAlmostEqual(esperado[1], resultado[1])

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que funcione si hay minerales asociados a otros planetas, minerales asociados a
        otras misiones y otros tripulantes
        """

        mision = Mision(
                id_mision=7,
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
            ),
            PlanetaMineral(
                id_planeta=5,
                id_mineral=3,
                cantidad_disponible=87431.151,
                pureza=0.94
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
                id_astronauta=4,
                rango=5),
            Tripulacion(
                id_equipo=2,
                patente_nave="N-2",
                id_astronauta=3,
                rango=1),
            Tripulacion(
                id_equipo=3,
                patente_nave="N-3",
                id_astronauta=2,
                rango=5)
        ]

        lista_mision_mineral = [
            MisionMineral(
                id_mision=1,
                id_mineral=1,
                cantidad=911.93
                ),
            MisionMineral(
                id_mision=7,
                id_mineral=1,
                cantidad=835.22
                ),
            MisionMineral(
                id_mision=7,
                id_mineral=3,
                cantidad=314.15
                ),
            MisionMineral(
                id_mision=5,
                id_mineral=81,
                cantidad=918.39
                )
        ]

        total = 4415.20 * 0.51 + 87431.151 * 0.94

        cantidad = (835.22 + 314.15) * 100 / total

        esperado = (cantidad, cantidad/2)
        g_mis = (mision_mineral for mision_mineral in lista_mision_mineral)
        g_planetas = (planeta for planeta in lista_planetas_mineral)

        g_t = (tripulacion for tripulacion in lista_tripulacion)

        resultado = porcentaje_extraccion(g_t, g_mis, g_planetas, mision)

        self.assertIsInstance(resultado, tuple)

        self.assertAlmostEqual(esperado[0], resultado[0])

        self.assertAlmostEqual(esperado[1], resultado[1])

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica que sólo se considere misiones logradas
        """

        mision = Mision(
                id_mision=1,
                fecha="2023-09-03",
                hora="19:27",
                id_equipo=7,
                id_planeta=542,
                lograda=False
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

        esperado = (0.0, 0.0)

        g_mis = (mision_mineral for mision_mineral in lista_mision_mineral)
        g_planetas = (planeta for planeta in lista_planetas_mineral)

        g_t = (tripulacion for tripulacion in lista_tripulacion)

        resultado = porcentaje_extraccion(g_t, g_mis, g_planetas, mision)

        self.assertIsInstance(resultado, tuple)

        self.assertAlmostEqual(esperado[0], resultado[0])

        self.assertAlmostEqual(esperado[1], resultado[1])
