import os
import sys
import unittest
from collections.abc import Iterable
from tests_privados.timeout_function import timeout
from tests_privados.utils import FLEXIBILIDAD_ADICIONAL
from tests_privados.solution.test_15 import (
    RESULTADO_MISION_S_0,
    RESULTADO_MISION_S_1,
    RESULTADO_MISION_M_0,
    RESULTADO_MISION_M_1,
    RESULTADO_MISION_L_0,
    RESULTADO_MISION_L_1,
)
sys.stdout = open(os.devnull, 'w')

# Constante para timeout en tests
N_SECOND = FLEXIBILIDAD_ADICIONAL*0.08

from backend.consultas import resultado_mision, cargar_naves, cargar_planeta_minerales, cargar_tripulaciones, cargar_materiales_mision
from utilidades import Mision


def _gen(iterable):
    return (item for item in iterable)


class TestResultadoMisionCargaDatos(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Test carga datos S: Misión fallida con minerales disponibles y capacidad suficiente.
        Verifica que resultado_mision procesa correctamente datos reales del tamaño S.
        """
        size = "out_new_S"
        path_naves = os.path.join("data_new", size, "Nave.csv")
        path_planeta_minerales = os.path.join("data_new", size, "PlanetaMineral.csv")
        path_tripulaciones = os.path.join("data_new", size, "Tripulacion.csv")
        path_mision_minerales = os.path.join("data_new", size, "MisionMineral.csv")

        # Caso que debería dar False: Misión 128, Equipo 29, Planeta 36
        mision = Mision(69, "2025-06-06", "01:30", 10, 27, False)

        resultado = resultado_mision(
            mision,
            cargar_naves(path_naves),
            cargar_planeta_minerales(path_planeta_minerales),
            cargar_tripulaciones(path_tripulaciones),
            cargar_materiales_mision(path_mision_minerales)
        )

        # Verificar que el resultado es una Mision
        self.assertIsInstance(resultado, Mision)
        
        # Verificar que tiene los campos esperados
        self.assertIsInstance(resultado.id_mision, int)
        self.assertIsInstance(resultado.fecha, str)
        self.assertIsInstance(resultado.hora, str)
        self.assertIsInstance(resultado.id_equipo, int)
        self.assertIsInstance(resultado.id_planeta, int)
        self.assertIsInstance(resultado.lograda, bool)
        
        # Verificar que los campos coinciden con los valores esperados
        self.assertEqual(resultado.id_mision, RESULTADO_MISION_S_0['id_mision'])
        self.assertEqual(resultado.fecha, RESULTADO_MISION_S_0['fecha'])
        self.assertEqual(resultado.hora, RESULTADO_MISION_S_0['hora'])
        self.assertEqual(resultado.id_equipo, RESULTADO_MISION_S_0['id_equipo'])
        self.assertEqual(resultado.id_planeta, RESULTADO_MISION_S_0['id_planeta'])
        self.assertEqual(resultado.lograda, RESULTADO_MISION_S_0['lograda'])

    @timeout(N_SECOND)
    def test_1(self):
        """
        Test carga datos S: Misión fallida por minerales no disponibles o capacidad insuficiente.
        Verifica manejo de casos de fallo con datos reales del tamaño S.
        """
        size = "out_new_S"
        path_naves = os.path.join("data_new", size, "Nave.csv")
        path_planeta_minerales = os.path.join("data_new", size, "PlanetaMineral.csv")
        path_tripulaciones = os.path.join("data_new", size, "Tripulacion.csv")
        path_mision_minerales = os.path.join("data_new", size, "MisionMineral.csv")

        # Caso que debería dar False: Misión 139, Equipo 1, Planeta 4
        mision = Mision(132, "2026-10-13", "02:11", 14, 5, None)

        resultado = resultado_mision(
            mision,
            cargar_naves(path_naves),
            cargar_planeta_minerales(path_planeta_minerales),
            cargar_tripulaciones(path_tripulaciones),
            cargar_materiales_mision(path_mision_minerales)
        )

        # Verificar que el resultado es una Mision
        self.assertIsInstance(resultado, Mision)
        
        # Verificar que tiene los campos esperados
        self.assertIsInstance(resultado.id_mision, int)
        self.assertIsInstance(resultado.fecha, str)
        self.assertIsInstance(resultado.hora, str)
        self.assertIsInstance(resultado.id_equipo, int)
        self.assertIsInstance(resultado.id_planeta, int)
        self.assertIsInstance(resultado.lograda, bool)
        
        # Verificar que los campos coinciden con los valores esperados
        self.assertEqual(resultado.id_mision, RESULTADO_MISION_S_1['id_mision'])
        self.assertEqual(resultado.fecha, RESULTADO_MISION_S_1['fecha'])
        self.assertEqual(resultado.hora, RESULTADO_MISION_S_1['hora'])
        self.assertEqual(resultado.id_equipo, RESULTADO_MISION_S_1['id_equipo'])
        self.assertEqual(resultado.id_planeta, RESULTADO_MISION_S_1['id_planeta'])
        self.assertEqual(resultado.lograda, RESULTADO_MISION_S_1['lograda'])
        
    @timeout(N_SECOND)
    def test_2(self):
        """
        Test carga datos M: Misión fallida con múltiples minerales y nave de gran capacidad.
        Verifica procesamiento correcto de datos más complejos del tamaño M.
        """
        size = "out_new_M"
        path_naves = os.path.join("data_new", size, "Nave.csv")
        path_planeta_minerales = os.path.join("data_new", size, "PlanetaMineral.csv")
        path_tripulaciones = os.path.join("data_new", size, "Tripulacion.csv")
        path_mision_minerales = os.path.join("data_new", size, "MisionMineral.csv")

        # Caso que debería dar False: Misión 734, Equipo 8, Planeta 156
        mision = Mision(703, "2024-11-07", "07:04", 53, 99, False)

        resultado = resultado_mision(
            mision,
            cargar_naves(path_naves),
            cargar_planeta_minerales(path_planeta_minerales),
            cargar_tripulaciones(path_tripulaciones),
            cargar_materiales_mision(path_mision_minerales)
        )

        # Verificar que el resultado es una Mision
        self.assertIsInstance(resultado, Mision)
        
        # Verificar que tiene los campos esperados
        self.assertIsInstance(resultado.id_mision, int)
        self.assertIsInstance(resultado.fecha, str)
        self.assertIsInstance(resultado.hora, str)
        self.assertIsInstance(resultado.id_equipo, int)
        self.assertIsInstance(resultado.id_planeta, int)
        self.assertIsInstance(resultado.lograda, bool)
        
        # Verificar que los campos coinciden con los valores esperados
        self.assertEqual(resultado.id_mision, RESULTADO_MISION_M_0['id_mision'])
        self.assertEqual(resultado.fecha, RESULTADO_MISION_M_0['fecha'])
        self.assertEqual(resultado.hora, RESULTADO_MISION_M_0['hora'])
        self.assertEqual(resultado.id_equipo, RESULTADO_MISION_M_0['id_equipo'])
        self.assertEqual(resultado.id_planeta, RESULTADO_MISION_M_0['id_planeta'])
        self.assertEqual(resultado.lograda, RESULTADO_MISION_M_0['lograda'])
    @timeout(N_SECOND)
    def test_3(self):
        """
        Test carga datos M: Misión fallida por exceso de minerales o nave inadecuada.
        Verifica detección de limitaciones con datos del tamaño M.
        """
        size = "out_new_M"
        path_naves = os.path.join("data_new", size, "Nave.csv")
        path_planeta_minerales = os.path.join("data_new", size, "PlanetaMineral.csv")
        path_tripulaciones = os.path.join("data_new", size, "Tripulacion.csv")
        path_mision_minerales = os.path.join("data_new", size, "MisionMineral.csv")

        # Caso que debería dar False: Misión 729, Equipo 25, Planeta 241
        mision = Mision(800, "2024-09-10", "10:19", 15, 185, False)

        resultado = resultado_mision(
            mision,
            cargar_naves(path_naves),
            cargar_planeta_minerales(path_planeta_minerales),
            cargar_tripulaciones(path_tripulaciones),
            cargar_materiales_mision(path_mision_minerales)
        )

        # Verificar que el resultado es una Mision
        self.assertIsInstance(resultado, Mision)
        
        # Verificar que tiene los campos esperados
        self.assertIsInstance(resultado.id_mision, int)
        self.assertIsInstance(resultado.fecha, str)
        self.assertIsInstance(resultado.hora, str)
        self.assertIsInstance(resultado.id_equipo, int)
        self.assertIsInstance(resultado.id_planeta, int)
        self.assertIsInstance(resultado.lograda, bool)
        
        # Verificar que los campos coinciden con los valores esperados
        self.assertEqual(resultado.id_mision, RESULTADO_MISION_M_1['id_mision'])
        self.assertEqual(resultado.fecha, RESULTADO_MISION_M_1['fecha'])
        self.assertEqual(resultado.hora, RESULTADO_MISION_M_1['hora'])
        self.assertEqual(resultado.id_equipo, RESULTADO_MISION_M_1['id_equipo'])
        self.assertEqual(resultado.id_planeta, RESULTADO_MISION_M_1['id_planeta'])
        self.assertEqual(resultado.lograda, RESULTADO_MISION_M_1['lograda'])
        
    @timeout(N_SECOND)
    def test_4(self):
        """
        Test carga datos L: Misión fallida en dataset grande con alta complejidad.
        Verifica rendimiento y corrección con datos masivos del tamaño L.
        """
        size = "out_new_L"
        path_naves = os.path.join("data_new", size, "Nave.csv")
        path_planeta_minerales = os.path.join("data_new", size, "PlanetaMineral.csv")
        path_tripulaciones = os.path.join("data_new", size, "Tripulacion.csv")
        path_mision_minerales = os.path.join("data_new", size, "MisionMineral.csv")

        # Caso que debería dar False: Misión 3978, Equipo 53, Planeta 578
        mision = Mision(2222, "2025-10-21", "20:14", 590, 307, None)

        resultado = resultado_mision(
            mision,
            cargar_naves(path_naves),
            cargar_planeta_minerales(path_planeta_minerales),
            cargar_tripulaciones(path_tripulaciones),
            cargar_materiales_mision(path_mision_minerales)
        )

        # Verificar que el resultado es una Mision
        self.assertIsInstance(resultado, Mision)
        
        # Verificar que tiene los campos esperados
        self.assertIsInstance(resultado.id_mision, int)
        self.assertIsInstance(resultado.fecha, str)
        self.assertIsInstance(resultado.hora, str)
        self.assertIsInstance(resultado.id_equipo, int)
        self.assertIsInstance(resultado.id_planeta, int)
        self.assertIsInstance(resultado.lograda, bool)
        
        # Verificar que los campos coinciden con los valores esperados
        self.assertEqual(resultado.id_mision, RESULTADO_MISION_L_0['id_mision'])
        self.assertEqual(resultado.fecha, RESULTADO_MISION_L_0['fecha'])
        self.assertEqual(resultado.hora, RESULTADO_MISION_L_0['hora'])
        self.assertEqual(resultado.id_equipo, RESULTADO_MISION_L_0['id_equipo'])
        self.assertEqual(resultado.id_planeta, RESULTADO_MISION_L_0['id_planeta'])
        self.assertEqual(resultado.lograda, RESULTADO_MISION_L_0['lograda'])
        
    @timeout(N_SECOND)
    def test_5(self):
        """
        Test carga datos L: Segundo caso de fallo con diferentes parámetros de misión.
        Verifica robustez del algoritmo con múltiples escenarios del tamaño L.
        """
        size = "out_new_L"
        path_naves = os.path.join("data_new", size, "Nave.csv")
        path_planeta_minerales = os.path.join("data_new", size, "PlanetaMineral.csv")
        path_tripulaciones = os.path.join("data_new", size, "Tripulacion.csv")
        path_mision_minerales = os.path.join("data_new", size, "MisionMineral.csv")

        # Caso que debería dar False: Misión 1727, Equipo 883, Planeta 259
        mision = Mision(3972, "2024-02-12", "03:29", 983, 210, False)

        resultado = resultado_mision(
            mision,
            cargar_naves(path_naves),
            cargar_planeta_minerales(path_planeta_minerales),
            cargar_tripulaciones(path_tripulaciones),
            cargar_materiales_mision(path_mision_minerales)
        )

        # Verificar que el resultado es una Mision
        self.assertIsInstance(resultado, Mision)
        
        # Verificar que tiene los campos esperados
        self.assertIsInstance(resultado.id_mision, int)
        self.assertIsInstance(resultado.fecha, str)
        self.assertIsInstance(resultado.hora, str)
        self.assertIsInstance(resultado.id_equipo, int)
        self.assertIsInstance(resultado.id_planeta, int)
        self.assertIsInstance(resultado.lograda, bool)
        
        # Verificar que los campos coinciden con los valores esperados
        self.assertEqual(resultado.id_mision, RESULTADO_MISION_L_1['id_mision'])
        self.assertEqual(resultado.fecha, RESULTADO_MISION_L_1['fecha'])
        self.assertEqual(resultado.hora, RESULTADO_MISION_L_1['hora'])
        self.assertEqual(resultado.id_equipo, RESULTADO_MISION_L_1['id_equipo'])
        self.assertEqual(resultado.id_planeta, RESULTADO_MISION_L_1['id_planeta'])
        self.assertEqual(resultado.lograda, RESULTADO_MISION_L_1['lograda'])
        