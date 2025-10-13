import os
import sys
import unittest
from collections.abc import Iterable
from collections import namedtuple
from tests_publicos.timeout_function import timeout
from tests_publicos.solution.test_5 import *
from backend.consultas import cargar_tripulaciones, cambiar_rango_astronauta
sys.stdout = open(os.devnull, 'w')

Tripulacion = namedtuple("Tripulacion", ["id_equipo", "patente_nave", "id_astronauta", "rango"])
# Constante para timeout en tests
N_SECOND = 0.08

class TestCambiarRangoAstronautaCargaDatos(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S.
        """
        tamano = "out_S"
        id = 1
        rango = 9
        
        path_tripulaciones = os.path.join("data", tamano, "Tripulacion.csv")
        
        generador_tripulaciones = cargar_tripulaciones(path_tripulaciones)
        
        resultado_estudiante = cambiar_rango_astronauta(generador_tripulaciones, id, rango)
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        
        self.assertEqual(len(lista_resultado), len(DATOS_TRIPULACIONES_S_0))
        
        # Debe retornar el mismo tripulacion con el nuevo rango
        
        self.assertCountEqual(lista_resultado, DATOS_TRIPULACIONES_S_0)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S.
        """
        tamano = "out_S"
        id = 2
        rango = 21
        
        path_tripulaciones = os.path.join("data", tamano, "Tripulacion.csv")
        
        generador_tripulaciones = cargar_tripulaciones(path_tripulaciones)
        
        resultado_estudiante = cambiar_rango_astronauta(generador_tripulaciones, id, rango)
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        
        # Debe retornar el mismo número de tripulaciones
        self.assertEqual(len(lista_resultado), len(DATOS_TRIPULACIONES_S_1))
        
        # Debe retornar el mismo astronauta con el nuevo rango
        self.assertCountEqual(lista_resultado, DATOS_TRIPULACIONES_S_1)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        tamano = "out_M"
        id = 21
        rango = 1
        
        path_tripulaciones = os.path.join("data", tamano, "Tripulacion.csv")
        
        generador_tripulaciones = cargar_tripulaciones(path_tripulaciones)
        
        resultado_estudiante = cambiar_rango_astronauta(generador_tripulaciones, id, rango)
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        
        # Debe retornar el mismo número de tripulaciones
        self.assertEqual(len(lista_resultado), len(DATOS_TRIPULACIONES_M_0))
        
        # Debe retornar el mismo astronauta con el nuevo rango
        self.assertCountEqual(lista_resultado, DATOS_TRIPULACIONES_M_0)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        tamano = "out_M"
        id = 69
        rango = 99
        
        path_tripulaciones = os.path.join("data", tamano, "Tripulacion.csv")
        
        generador_tripulaciones = cargar_tripulaciones(path_tripulaciones)
        
        resultado_estudiante = cambiar_rango_astronauta(generador_tripulaciones, id, rango)
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        
        # Debe retornar el mismo número de tripulaciones
        self.assertEqual(len(lista_resultado), len(DATOS_TRIPULACIONES_M_1))
        
        # Debe retornar el mismo astronauta con el nuevo rango
        self.assertCountEqual(lista_resultado, DATOS_TRIPULACIONES_M_1)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        tamano = "out_L"
        id = 14
        rango = 2
        
        path_tripulaciones = os.path.join("data", tamano, "Tripulacion.csv")
        
        generador_tripulaciones = cargar_tripulaciones(path_tripulaciones)
        
        resultado_estudiante = cambiar_rango_astronauta(generador_tripulaciones, id, rango)
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        
        # Debe retornar el mismo número de tripulaciones
        self.assertEqual(len(lista_resultado), len(DATOS_TRIPULACIONES_L_0))
        
        # Debe retornar el mismo astronauta con el nuevo rango
        self.assertCountEqual(lista_resultado, DATOS_TRIPULACIONES_L_0)

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        tamano = "out_L"
        id = 3
        rango = 4
        
        path_tripulaciones = os.path.join("data", tamano, "Tripulacion.csv")
        
        generador_tripulaciones = cargar_tripulaciones(path_tripulaciones)
        
        resultado_estudiante = cambiar_rango_astronauta(generador_tripulaciones, id, rango)
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        
        # Debe retornar el mismo número de tripulaciones
        self.assertEqual(len(lista_resultado), len(DATOS_TRIPULACIONES_L_1))
        
        # Debe retornar el mismo astronauta con el nuevo rango
        self.assertCountEqual(lista_resultado, DATOS_TRIPULACIONES_L_1)