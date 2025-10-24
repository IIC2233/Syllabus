import os
import sys
import unittest
from backend.consultas import (
    porcentaje_extraccion, cargar_planeta_minerales, cargar_tripulaciones, cargar_materiales_mision)
from utilidades import Mision
from tests_publicos.timeout_function import timeout
from tests_publicos.solution.test_14 import (
    PORCENTAJE_EXTRACCION_S_1_A,
    PORCENTAJE_EXTRACCION_M_1_A,
    PORCENTAJE_EXTRACCION_L_1_A,
    PORCENTAJE_EXTRACCION_S_2_A,
    PORCENTAJE_EXTRACCION_M_2_A,
    PORCENTAJE_EXTRACCION_L_2_A,
    PORCENTAJE_EXTRACCION_S_1_B,
    PORCENTAJE_EXTRACCION_M_1_B,
    PORCENTAJE_EXTRACCION_L_1_B,
    PORCENTAJE_EXTRACCION_S_2_B,
    PORCENTAJE_EXTRACCION_M_2_B,
    PORCENTAJE_EXTRACCION_L_2_B
)

sys.stdout = open(os.devnull, 'w')


# Constante para timeout en tests
N_SECOND = 0.08


class TestDisponibilidadPorPlaneta(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    # función creada solo para este test
    def assertAlmostEqualIn(self, respuesta, esperados):
        try:
            self.assertAlmostEqual(respuesta[0], esperados[0][0])
            self.assertAlmostEqual(respuesta[1], esperados[0][1])
        except AssertionError:
            pass
        else:
            return
        self.assertAlmostEqual(respuesta[0], esperados[1][0], msg=f"\n{' '*0x10}Los valores {respuesta} no son cercanos a alguno de los pares {esperados}")
        self.assertAlmostEqual(respuesta[1], esperados[1][1], msg=f"\n{' '*0x10}Los valores {respuesta} no son cercanos a alguno de los pares {esperados}")

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S.
        """

        tamano = "out_S"

        path = os.path.join("data", tamano, "MisionMineral.csv")

        g_mm = cargar_materiales_mision(path)

        path = os.path.join("data", tamano, "Tripulacion.csv")

        g_t = cargar_tripulaciones(path)

        path = os.path.join("data", tamano, "PlanetaMineral.csv")

        g_p = cargar_planeta_minerales(path)

        mision = Mision(
            id_mision=64,
            hora="16:38",
            fecha="2023-05-27",
            id_equipo=8,
            id_planeta=8,
            lograda=True
        )

        estudiante = porcentaje_extraccion(g_t, g_mm, g_p, mision)

        self.assertIsInstance(estudiante, tuple)

        esperado = [PORCENTAJE_EXTRACCION_S_1_A, PORCENTAJE_EXTRACCION_S_1_B]

        print("Obtenido:", estudiante)
        print("Esperados:", esperado)

        # ahora acepta ambas respuestas
        self.assertAlmostEqualIn(estudiante, esperado)

    def test_1(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S.
        """

        tamano = "out_S"

        path = os.path.join("data", tamano, "MisionMineral.csv")

        g_mm = cargar_materiales_mision(path)

        path = os.path.join("data", tamano, "Tripulacion.csv")

        g_t = cargar_tripulaciones(path)

        path = os.path.join("data", tamano, "PlanetaMineral.csv")

        g_p = cargar_planeta_minerales(path)

        mision = Mision(
            id_mision=43,
            hora="18:16",
            fecha="2024-04-18",
            id_equipo=26,
            id_planeta=13,
            lograda=True
        )

        estudiante = porcentaje_extraccion(g_t, g_mm, g_p, mision)

        self.assertIsInstance(estudiante, tuple)

        esperado = [PORCENTAJE_EXTRACCION_S_2_A, PORCENTAJE_EXTRACCION_S_2_B]

        # ahora acepta ambas respuestas
        self.assertAlmostEqualIn(estudiante, esperado)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """

        tamano = "out_M"

        path = os.path.join("data", tamano, "MisionMineral.csv")

        g_mm = cargar_materiales_mision(path)

        path = os.path.join("data", tamano, "Tripulacion.csv")

        g_t = cargar_tripulaciones(path)

        path = os.path.join("data", tamano, "PlanetaMineral.csv")

        g_p = cargar_planeta_minerales(path)

        mision = Mision(
            id_mision=79,
            hora="22:32",
            fecha="2025-08-25",
            id_equipo=52,
            id_planeta=15,
            lograda=True
        )

        estudiante = porcentaje_extraccion(g_t, g_mm, g_p, mision)

        self.assertIsInstance(estudiante, tuple)

        esperado = [PORCENTAJE_EXTRACCION_M_1_A, PORCENTAJE_EXTRACCION_M_1_B]

        # ahora acepta ambas respuestas
        self.assertAlmostEqualIn(estudiante, esperado)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """

        tamano = "out_M"

        path = os.path.join("data", tamano, "MisionMineral.csv")

        g_mm = cargar_materiales_mision(path)

        path = os.path.join("data", tamano, "Tripulacion.csv")

        g_t = cargar_tripulaciones(path)

        path = os.path.join("data", tamano, "PlanetaMineral.csv")

        g_p = cargar_planeta_minerales(path)

        mision = Mision(
            id_mision=4,
            hora="19:59",
            fecha="2024-11-26",
            id_equipo=100,
            id_planeta=182,
            lograda=True
        )

        estudiante = porcentaje_extraccion(g_t, g_mm, g_p, mision)

        self.assertIsInstance(estudiante, tuple)

        esperado = [PORCENTAJE_EXTRACCION_M_2_A, PORCENTAJE_EXTRACCION_M_2_B]

        # ahora acepta ambas respuestas
        self.assertAlmostEqualIn(estudiante, esperado)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """

        tamano = "out_L"

        path = os.path.join("data", tamano, "MisionMineral.csv")

        g_mm = cargar_materiales_mision(path)

        path = os.path.join("data", tamano, "Tripulacion.csv")

        g_t = cargar_tripulaciones(path)

        path = os.path.join("data", tamano, "PlanetaMineral.csv")

        g_p = cargar_planeta_minerales(path)

        mision = Mision(
                id_mision=3854,
                hora="21:45",
                fecha="2025-01-31",
                id_equipo=697,
                id_planeta=963,
                lograda=True
            )

        estudiante = porcentaje_extraccion(g_t, g_mm, g_p, mision)

        self.assertIsInstance(estudiante, tuple)

        esperado = [PORCENTAJE_EXTRACCION_L_1_A, PORCENTAJE_EXTRACCION_L_1_B]

        # ahora acepta ambas respuestas
        self.assertAlmostEqualIn(estudiante, esperado)

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """

        tamano = "out_L"

        path = os.path.join("data", tamano, "MisionMineral.csv")

        g_mm = cargar_materiales_mision(path)

        path = os.path.join("data", tamano, "Tripulacion.csv")

        g_t = cargar_tripulaciones(path)

        path = os.path.join("data", tamano, "PlanetaMineral.csv")

        g_p = cargar_planeta_minerales(path)

        mision = Mision(
            id_mision=490,
            hora="09:29",
            fecha="2022-11-28",
            id_equipo=32,
            id_planeta=385,
            lograda=True
        )
        estudiante = porcentaje_extraccion(g_t, g_mm, g_p, mision)

        self.assertIsInstance(estudiante, tuple)

        esperado = [PORCENTAJE_EXTRACCION_L_2_A, PORCENTAJE_EXTRACCION_L_2_B]

        # ahora acepta ambas respuestas
        self.assertAlmostEqualIn(estudiante, esperado)
