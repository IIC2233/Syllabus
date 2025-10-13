import os
import sys
import unittest
from collections.abc import Iterable
from backend.consultas import planetas_con_cantidad_de_minerales, cargar_planeta_minerales
from tests_publicos.timeout_function import timeout
from tests_publicos.solution.test_3 import *

# Constante para timeout en tests
N_SECOND = 0.08
sys.stdout = open(os.devnull, 'w')

class TestPlanetasConCantidadDeMineralesCargaDatos(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S.
        """
        tamano = "out_S"
        
        path = os.path.join("data", tamano, "PlanetaMineral.csv")
        
        g_pm = cargar_planeta_minerales(path)
        
        resultado_estudiante = planetas_con_cantidad_de_minerales(generador_planeta_mineral=g_pm, id_mineral=38, cantidad_minima=1000)
        
        self.assertIsInstance(resultado_estudiante, list)
        
        resultado_esperado = PLANETAS_CON_CANTIDAD_S_0
        
        self.assertCountEqual(resultado_estudiante, resultado_esperado)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S.
        """
        tamano = "out_S"
        
        path = os.path.join("data", tamano, "PlanetaMineral.csv")
        
        g_pm = cargar_planeta_minerales(path)
        
        resultado_estudiante = planetas_con_cantidad_de_minerales(generador_planeta_mineral=g_pm, id_mineral=40, cantidad_minima=1)
        
        self.assertIsInstance(resultado_estudiante, list)
        
        resultado_esperado = PLANETAS_CON_CANTIDAD_S_1
        
        self.assertCountEqual(resultado_estudiante, resultado_esperado)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        tamano = "out_M"
        
        path = os.path.join("data", tamano, "PlanetaMineral.csv")
        
        g_pm = cargar_planeta_minerales(path)
        
        resultado_estudiante = planetas_con_cantidad_de_minerales(generador_planeta_mineral=g_pm, id_mineral=38, cantidad_minima=100000)
        
        self.assertIsInstance(resultado_estudiante, list)
        
        resultado_esperado = PLANETAS_CON_CANTIDAD_M_0
        
        self.assertCountEqual(resultado_estudiante, resultado_esperado)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        tamano = "out_M"
        
        path = os.path.join("data", tamano, "PlanetaMineral.csv")
        
        g_pm = cargar_planeta_minerales(path)
        
        resultado_estudiante = planetas_con_cantidad_de_minerales(generador_planeta_mineral=g_pm, id_mineral=69, cantidad_minima=1)
        
        self.assertIsInstance(resultado_estudiante, list)
        
        resultado_esperado = PLANETAS_CON_CANTIDAD_M_1
        
        self.assertCountEqual(resultado_estudiante, resultado_esperado)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        tamano = "out_L"
        
        path = os.path.join("data", tamano, "PlanetaMineral.csv")
        
        g_pm = cargar_planeta_minerales(path)
        
        resultado_estudiante = planetas_con_cantidad_de_minerales(generador_planeta_mineral=g_pm, id_mineral=33, cantidad_minima=1)
        
        self.assertIsInstance(resultado_estudiante, list)
        
        resultado_esperado = PLANETAS_CON_CANTIDAD_L_0
        
        self.assertCountEqual(resultado_estudiante, resultado_esperado)

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        tamano = "out_L"
        
        path = os.path.join("data", tamano, "PlanetaMineral.csv")
        
        g_pm = cargar_planeta_minerales(path)
        
        resultado_estudiante = planetas_con_cantidad_de_minerales(generador_planeta_mineral=g_pm, id_mineral=262, cantidad_minima=182000)
        
        self.assertIsInstance(resultado_estudiante, list)
        
        resultado_esperado = PLANETAS_CON_CANTIDAD_L_1
        
        self.assertCountEqual(resultado_estudiante, resultado_esperado)