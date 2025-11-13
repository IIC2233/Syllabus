import os
import sys
import unittest
from backend.consultas import (
    porcentaje_extraccion, cargar_planeta_minerales, cargar_tripulaciones, cargar_materiales_mision)
from utilidades import Mision
from tests_privados.timeout_function import timeout
from tests_privados.utils import FLEXIBILIDAD_ADICIONAL
from tests_privados.solution.test_14 import (
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
N_SECOND = FLEXIBILIDAD_ADICIONAL*0.08


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

        tamano = "out_new_S"

        path = os.path.join("data_new", tamano, "MisionMineral.csv")

        g_mm = cargar_materiales_mision(path)

        path = os.path.join("data_new", tamano, "Tripulacion.csv")

        g_t = cargar_tripulaciones(path)

        path = os.path.join("data_new", tamano, "PlanetaMineral.csv")

        g_p = cargar_planeta_minerales(path)

        mision = Mision(
            id_mision=29,
            fecha="2024-05-06",
            hora="20:08",
            id_equipo=3,
            id_planeta=31,
            lograda=True)

        estudiante = porcentaje_extraccion(g_t, g_mm, g_p, mision)

        self.assertIsInstance(estudiante, tuple)

        esperado = [PORCENTAJE_EXTRACCION_S_1_A, PORCENTAJE_EXTRACCION_S_1_B]

        # ahora acepta ambas respuestas
        self.assertAlmostEqualIn(estudiante, esperado)

    def test_1(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S.
        """

        tamano = "out_new_S"

        path = os.path.join("data_new", tamano, "MisionMineral.csv")

        g_mm = cargar_materiales_mision(path)

        path = os.path.join("data_new", tamano, "Tripulacion.csv")

        g_t = cargar_tripulaciones(path)

        path = os.path.join("data_new", tamano, "PlanetaMineral.csv")

        g_p = cargar_planeta_minerales(path)

        mision = Mision(
            id_mision=111,
            fecha="2023-09-10",
            hora="10:08",
            id_equipo=12,
            id_planeta=7,
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

        tamano = "out_new_M"

        path = os.path.join("data_new", tamano, "MisionMineral.csv")

        g_mm = cargar_materiales_mision(path)

        path = os.path.join("data_new", tamano, "Tripulacion.csv")

        g_t = cargar_tripulaciones(path)

        path = os.path.join("data_new", tamano, "PlanetaMineral.csv")

        g_p = cargar_planeta_minerales(path)

        mision = Mision(
            id_mision=636,
            fecha="2024-07-24",
            hora="12:28",
            id_equipo=95,
            id_planeta=45,
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

        tamano = "out_new_M"

        path = os.path.join("data_new", tamano, "MisionMineral.csv")

        g_mm = cargar_materiales_mision(path)

        path = os.path.join("data_new", tamano, "Tripulacion.csv")

        g_t = cargar_tripulaciones(path)

        path = os.path.join("data_new", tamano, "PlanetaMineral.csv")

        g_p = cargar_planeta_minerales(path)

        mision = Mision(
            id_mision=273,
            fecha="2025-10-11",
            hora="10:04",
            id_equipo=41,
            id_planeta=83,
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

        tamano = "out_new_L"

        path = os.path.join("data_new", tamano, "MisionMineral.csv")

        g_mm = cargar_materiales_mision(path)

        path = os.path.join("data_new", tamano, "Tripulacion.csv")

        g_t = cargar_tripulaciones(path)

        path = os.path.join("data_new", tamano, "PlanetaMineral.csv")

        g_p = cargar_planeta_minerales(path)

        mision = Mision(
            id_mision=3373,
            fecha="2022-12-18",
            hora="13:38",
            id_equipo=77,
            id_planeta=552,
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

        tamano = "out_new_L"

        path = os.path.join("data_new", tamano, "MisionMineral.csv")

        g_mm = cargar_materiales_mision(path)

        path = os.path.join("data_new", tamano, "Tripulacion.csv")

        g_t = cargar_tripulaciones(path)

        path = os.path.join("data_new", tamano, "PlanetaMineral.csv")

        g_p = cargar_planeta_minerales(path)

        mision = Mision(
            id_mision=1129,
            fecha="2023-01-02",
            hora="12:25",
            id_equipo=885,
            id_planeta=346,
            lograda=True
        )
        estudiante = porcentaje_extraccion(g_t, g_mm, g_p, mision)

        self.assertIsInstance(estudiante, tuple)

        esperado = [PORCENTAJE_EXTRACCION_L_2_A, PORCENTAJE_EXTRACCION_L_2_B]

        # ahora acepta ambas respuestas
        self.assertAlmostEqualIn(estudiante, esperado)
