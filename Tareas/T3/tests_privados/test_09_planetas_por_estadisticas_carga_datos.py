import os
import sys
import unittest
from collections.abc import Iterable

from tests_privados.timeout_function import timeout
from tests_privados.utils import FLEXIBILIDAD_ADICIONAL
from backend.consultas import planetas_por_estadisticas, cargar_minerales, cargar_planeta_minerales, cargar_planetas
from tests_privados.solution.test_9 import *

sys.stdout = open(os.devnull, 'w')

# Constante para timeout en tests
N_SECOND = FLEXIBILIDAD_ADICIONAL*0.08

class TestPlanetasPorEstadisticasCargaDatos(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica que se carguen correctamente los datos del archivo S con estadísticas 0.000001, 0.000001, 0.000001.
        """
        tamano = "out_new_S"
        
        path_minerales = os.path.join("data_new", tamano, "Mineral.csv")
        path_planeta_minerales = os.path.join("data_new", tamano, "PlanetaMineral.csv")
        path_planetas = os.path.join("data_new", tamano, "Planeta.csv")
        
        generador_minerales = cargar_minerales(path_minerales)
        generador_planeta_minerales = cargar_planeta_minerales(path_planeta_minerales)
        generador_planetas = cargar_planetas(path_planetas)
        
        resultado_estudiante = planetas_por_estadisticas(generador_minerales, generador_planeta_minerales, generador_planetas, 0.000001, 0.000001, 0.000001)
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        
        self.assertCountEqual(lista_resultado, PLANETAS_POR_ESTADISTICAS_S_0)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se carguen correctamente los datos del archivo S con estadísticas 0.00000001, 0.000005, 0.005.
        """
        tamano = "out_new_S"
        
        path_minerales = os.path.join("data_new", tamano, "Mineral.csv")
        path_planeta_minerales = os.path.join("data_new", tamano, "PlanetaMineral.csv")
        path_planetas = os.path.join("data_new", tamano, "Planeta.csv")
        
        generador_minerales = cargar_minerales(path_minerales)
        generador_planeta_minerales = cargar_planeta_minerales(path_planeta_minerales)
        generador_planetas = cargar_planetas(path_planetas)
        
        resultado_estudiante = planetas_por_estadisticas(generador_minerales, generador_planeta_minerales, generador_planetas, 0.00000001, 0.000005, 0.005)
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        
        self.assertCountEqual(lista_resultado, PLANETAS_POR_ESTADISTICAS_S_1)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se carguen correctamente los datos del archivo M con estadísticas 0.00000001, 0.000003, 0.0000003.
        """
        tamano = "out_new_M"
        
        path_minerales = os.path.join("data_new", tamano, "Mineral.csv")
        path_planeta_minerales = os.path.join("data_new", tamano, "PlanetaMineral.csv")
        path_planetas = os.path.join("data_new", tamano, "Planeta.csv")
        
        generador_minerales = cargar_minerales(path_minerales)
        generador_planeta_minerales = cargar_planeta_minerales(path_planeta_minerales)
        generador_planetas = cargar_planetas(path_planetas)
        
        resultado_estudiante = planetas_por_estadisticas(generador_minerales, generador_planeta_minerales, generador_planetas, 0.00000001, 0.000003, 0.0000003)
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        
        self.assertCountEqual(lista_resultado, PLANETAS_POR_ESTADISTICAS_M_0)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que se carguen correctamente los datos del archivo M con estadísticas 0.0000000001, 0.000000001, 0.00000001.
        """
        tamano = "out_new_M"
        
        path_minerales = os.path.join("data_new", tamano, "Mineral.csv")
        path_planeta_minerales = os.path.join("data_new", tamano, "PlanetaMineral.csv")
        path_planetas = os.path.join("data_new", tamano, "Planeta.csv")
        
        generador_minerales = cargar_minerales(path_minerales)
        generador_planeta_minerales = cargar_planeta_minerales(path_planeta_minerales)
        generador_planetas = cargar_planetas(path_planetas)
        
        resultado_estudiante = planetas_por_estadisticas(generador_minerales, generador_planeta_minerales, generador_planetas, 0.0000000001, 0.000000001, 0.00000001)
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        
        self.assertCountEqual(lista_resultado, PLANETAS_POR_ESTADISTICAS_M_1)

    @timeout(N_SECOND*4)
    def test_4(self):
        """
        Verifica que se carguen correctamente los datos del archivo L con estadísticas 1, 1, 1.
        """
        tamano = "out_new_L"
        
        path_minerales = os.path.join("data_new", tamano, "Mineral.csv")
        path_planeta_minerales = os.path.join("data_new", tamano, "PlanetaMineral.csv")
        path_planetas = os.path.join("data_new", tamano, "Planeta.csv")
        
        generador_minerales = cargar_minerales(path_minerales)
        generador_planeta_minerales = cargar_planeta_minerales(path_planeta_minerales)
        generador_planetas = cargar_planetas(path_planetas)
        
        resultado_estudiante = planetas_por_estadisticas(generador_minerales, generador_planeta_minerales, generador_planetas, 1, 1, 1)
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        
        self.assertCountEqual(lista_resultado, PLANETAS_POR_ESTADISTICAS_L_0)

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica que se carguen correctamente los datos del archivo L con estadísticas 0.0000000317, 0.0000000468, 0.0000000626.
        """
        tamano = "out_new_L"
        
        path_minerales = os.path.join("data_new", tamano, "Mineral.csv")
        path_planeta_minerales = os.path.join("data_new", tamano, "PlanetaMineral.csv")
        path_planetas = os.path.join("data_new", tamano, "Planeta.csv")
        
        generador_minerales = cargar_minerales(path_minerales)
        generador_planeta_minerales = cargar_planeta_minerales(path_planeta_minerales)
        generador_planetas = cargar_planetas(path_planetas)
        
        resultado_estudiante = planetas_por_estadisticas(generador_minerales, generador_planeta_minerales, generador_planetas, 0.0000000317, 0.0000000468, 0.0000000626)
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        
        self.assertCountEqual(lista_resultado, PLANETAS_POR_ESTADISTICAS_L_1)
