import os
import sys
import unittest
from collections.abc import Iterable

from tests_publicos.timeout_function import timeout
from tests_publicos.solution.test_1 import *
sys.stdout = open(os.devnull, 'w')
from backend.consultas import cargar_mision, misiones_desde_fecha

# Constante para timeout en tests
N_SECOND = 0.08

class TestMisionesPorFechaCargaDatos(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S - inverso False.
        
        """
        tamano = "out_S"
        
        datos = os.path.join("data", tamano, "Mision.csv")
        
        generador_misiones = cargar_mision(datos)
        
        resultado_estudiante = misiones_desde_fecha(generador_misiones, "2023-05-05", False)
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        resultado_esperado = DATOS_MISIONES_S_0
        self.assertCountEqual(lista_resultado, resultado_esperado)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S - inverso True.
        """
        tamano = "out_S"
        
        datos = os.path.join("data", tamano, "Mision.csv")
        
        generador_misiones = cargar_mision(datos)
        
        resultado_estudiante = misiones_desde_fecha(generador_misiones, "2023-05-05", True)
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        resultado_esperado = DATOS_MISIONES_S_1
        
        self.assertCountEqual(lista_resultado, resultado_esperado)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M - inverso False.
        """
        tamano = "out_M"
        
        datos = os.path.join("data", tamano, "Mision.csv")
        
        generador_misiones = cargar_mision(datos)
        
        resultado_estudiante = misiones_desde_fecha(generador_misiones, "2025-04-08", False)
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        resultado_esperado = DATOS_MISIONES_M_0
        
        self.assertCountEqual(lista_resultado, resultado_esperado)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M - inverso True.
        """
        tamano = "out_M"
        
        datos = os.path.join("data", tamano, "Mision.csv")
        
        generador_misiones = cargar_mision(datos)
        
        resultado_estudiante = misiones_desde_fecha(generador_misiones, "2025-04-08", True)
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        resultado_esperado = DATOS_MISIONES_M_1
        
        self.assertCountEqual(lista_resultado, resultado_esperado)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L - inverso False.
        """
        tamano = "out_L"
        
        datos = os.path.join("data", tamano, "Mision.csv")
        
        generador_misiones = cargar_mision(datos)
        
        resultado_estudiante = misiones_desde_fecha(generador_misiones, "2024-06-01", False)
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        resultado_esperado = DATOS_MISIONES_L_0
        
        self.assertCountEqual(lista_resultado, resultado_esperado)

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L - inverso True.
        """
        tamano = "out_L"
        
        datos = os.path.join("data", tamano, "Mision.csv")
        
        generador_misiones = cargar_mision(datos)
        
        resultado_estudiante = misiones_desde_fecha(generador_misiones, "2024-06-01", True)
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        resultado_esperado = DATOS_MISIONES_L_1
        
        self.assertCountEqual(lista_resultado, resultado_esperado)