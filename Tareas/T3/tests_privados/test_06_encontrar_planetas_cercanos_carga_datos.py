import os
import sys
import unittest
from collections.abc import Iterable
from collections import namedtuple
from tests_privados.timeout_function import timeout
from tests_privados.utils import FLEXIBILIDAD_ADICIONAL
from tests_privados. solution.test_6 import *
from backend.consultas import cargar_planetas, encontrar_planetas_cercanos
sys.stdout = open(os.devnull, 'w')

Planeta = namedtuple("Planeta", ["id_planeta", "nombre", "coordenada_x", "coordenada_y", "tamano", "tipo"])

# Constante para timeout en tests
N_SECOND = FLEXIBILIDAD_ADICIONAL*0.08

class TestEncontrarPlanetasCercanosCargaDatos(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S - coordenadas grandes.
        """
        tamano = "out_new_S"
        
        datos = os.path.join("data_new", tamano, "Planeta.csv")
        
        generador_planetas = cargar_planetas(datos)
        
        resultado_estudiante = encontrar_planetas_cercanos(generador_planetas, -1234567, -1234567, 1234567, 1234567, 10)
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        resultado_esperado = PLANETAS_CERCANOS_S_0
        
        self.assertCountEqual(lista_resultado, resultado_esperado)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S - coordenadas medianas.
        """
        tamano = "out_new_S"
        
        datos = os.path.join("data_new", tamano, "Planeta.csv")
        
        generador_planetas = cargar_planetas(datos)
        
        resultado_estudiante = encontrar_planetas_cercanos(generador_planetas, -100000000, -100000000, 100000000, 100000000, None)
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        resultado_esperado = PLANETAS_CERCANOS_S_1
        
        self.assertCountEqual(lista_resultado, resultado_esperado)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M - coordenadas grandes.
        """
        tamano = "out_new_M"
        
        datos = os.path.join("data_new", tamano, "Planeta.csv")
        
        generador_planetas = cargar_planetas(datos)
        
        resultado_estudiante = encontrar_planetas_cercanos(generador_planetas, -9876543, -9876543, 9876543, 9876543, 3)
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        resultado_esperado = PLANETAS_CERCANOS_M_0
        
        self.assertCountEqual(lista_resultado, resultado_esperado)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M - coordenadas muy grandes.
        """
        tamano = "out_new_M"
        
        datos = os.path.join("data_new", tamano, "Planeta.csv")
        
        generador_planetas = cargar_planetas(datos)
        
        resultado_estudiante = encontrar_planetas_cercanos(generador_planetas, 0, 0, 0, 0, None)
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        resultado_esperado = PLANETAS_CERCANOS_M_1
        
        self.assertCountEqual(lista_resultado, resultado_esperado)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L - coordenadas enormes.
        """
        tamano = "out_new_L"
        
        datos = os.path.join("data_new", tamano, "Planeta.csv")
        
        generador_planetas = cargar_planetas(datos)
        
        resultado_estudiante = encontrar_planetas_cercanos(generador_planetas, -120000000, -120000000, 120000000, 120000000, 69)
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        resultado_esperado = PLANETAS_CERCANOS_L_0
        
        self.assertCountEqual(lista_resultado, resultado_esperado)

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L - coordenadas masivas.
        """
        tamano = "out_new_L"
        
        datos = os.path.join("data_new", tamano, "Planeta.csv")
        
        generador_planetas = cargar_planetas(datos)
        
        resultado_estudiante = encontrar_planetas_cercanos(generador_planetas, -150000000, -150000000, 150000000, 150000000, None)
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        resultado_esperado = PLANETAS_CERCANOS_L_1
        
        self.assertCountEqual(lista_resultado, resultado_esperado)
