import os
import sys
import unittest
from collections.abc import Iterable
from tests_publicos.timeout_function import timeout
from tests_publicos.solution.test_8 import *
from backend.consultas import cargar_mision, cargar_planetas, misiones_por_tipo_planeta
sys.stdout = open(os.devnull, 'w')

# Constante para timeout en tests
N_SECOND = 0.08

class TestMisionesPorTipoPlanetaCargaDatos(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S - tipo Plasma.
        """
        size = "out_S"

        path_misiones = os.path.join("data", size, "Mision.csv")
        path_planetas = os.path.join("data", size, "Planeta.csv")
        
        generador_misiones = cargar_mision(path_misiones)
        generador_planetas = cargar_planetas(path_planetas)
        
        resultado_estudiante = misiones_por_tipo_planeta(generador_misiones, generador_planetas, "Plasma")
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        resultado_esperado = DATOS_MISIONES_S_0
        
        self.assertCountEqual(lista_resultado, resultado_esperado)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S - tipo Rocoso.
        """
        size = "out_S"

        path_misiones = os.path.join("data", size, "Mision.csv")
        path_planetas = os.path.join("data", size, "Planeta.csv")
        
        generador_misiones = cargar_mision(path_misiones)
        generador_planetas = cargar_planetas(path_planetas)
        
        resultado_estudiante = misiones_por_tipo_planeta(generador_misiones, generador_planetas, "Rocoso")
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        resultado_esperado = DATOS_MISIONES_S_1
        
        self.assertCountEqual(lista_resultado, resultado_esperado)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M - tipo Gas.
        """
        size = "out_M"

        path_misiones = os.path.join("data", size, "Mision.csv")
        path_planetas = os.path.join("data", size, "Planeta.csv")
        
        generador_misiones = cargar_mision(path_misiones)
        generador_planetas = cargar_planetas(path_planetas)
        
        resultado_estudiante = misiones_por_tipo_planeta(generador_misiones, generador_planetas, "Gas")
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        resultado_esperado = DATOS_MISIONES_M_0
        
        self.assertCountEqual(lista_resultado, resultado_esperado)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M - tipo Sólido.
        """
        size = "out_M"

        path_misiones = os.path.join("data", size, "Mision.csv")
        path_planetas = os.path.join("data", size, "Planeta.csv")
        
        generador_misiones = cargar_mision(path_misiones)
        generador_planetas = cargar_planetas(path_planetas)
        
        resultado_estudiante = misiones_por_tipo_planeta(generador_misiones, generador_planetas, "Sólido")
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        resultado_esperado = DATOS_MISIONES_M_1
        
        self.assertCountEqual(lista_resultado, resultado_esperado)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L - tipo Líquido.
        """
        size = "out_L"

        path_misiones = os.path.join("data", size, "Mision.csv")
        path_planetas = os.path.join("data", size, "Planeta.csv")
        
        generador_misiones = cargar_mision(path_misiones)
        generador_planetas = cargar_planetas(path_planetas)
        
        resultado_estudiante = misiones_por_tipo_planeta(generador_misiones, generador_planetas, "Líquido")
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        resultado_esperado = DATOS_MISIONES_L_0
        
        self.assertCountEqual(lista_resultado, resultado_esperado)

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L - tipo Criogénico.
        """
        size = "out_L"

        path_misiones = os.path.join("data", size, "Mision.csv")
        path_planetas = os.path.join("data", size, "Planeta.csv")
        
        generador_misiones = cargar_mision(path_misiones)
        generador_planetas = cargar_planetas(path_planetas)
        
        resultado_estudiante = misiones_por_tipo_planeta(generador_misiones, generador_planetas, "Criogénico")
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        resultado_esperado = DATOS_MISIONES_L_1
        
        self.assertCountEqual(lista_resultado, resultado_esperado)
