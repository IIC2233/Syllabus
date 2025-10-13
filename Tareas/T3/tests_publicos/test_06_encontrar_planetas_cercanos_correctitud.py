import os
import sys
import unittest
from collections.abc import Iterable
from collections import namedtuple

from tests_publicos.timeout_function import timeout
from backend.consultas import encontrar_planetas_cercanos
sys.stdout = open(os.devnull, 'w')

Planeta = namedtuple("Planeta", ["id_planeta", "nombre", "coordenada_x", "coordenada_y", "tamano", "tipo"])

# Constante para timeout en tests
N_SECOND = 0.08

class TestEncontrarPlanetasCercanosCorrectitud(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica que se retorne generador vacío cuando no hay planetas en el área.
        """
        lista_planetas = [
            Planeta(1, "Tierra", 0, 0, "M", "Rocoso"),
            Planeta(2, "Marte", 100, 999, "S", "Rocoso"),
            Planeta(3, "Jupiter", 1001, 1, "L", "Gaseoso"),
        ]
        
        generador_planetas = (planeta for planeta in lista_planetas)
        
        resultado_estudiante = encontrar_planetas_cercanos(generador_planetas, 0, 1000, 1000, 2000, None)
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        
        # Debe retornar generador vacío (no hay planetas en esa área)
        self.assertEqual(lista_resultado, [])

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se retorne generador vacío cuando se entrega generador vacío. Y que pueda recibir parámetro opcional None
        """
        generador_vacio = (planeta for planeta in [])
        
        resultado_estudiante = encontrar_planetas_cercanos(generador_vacio, 0, 0, 100, 100)
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        
        self.assertEqual(lista_resultado, [])

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se encuentren planetas correctamente en el área especificada.
        """
        lista_planetas = [
            Planeta(1, "Tierra", 88, 11, "M", "Rocoso"),
            Planeta(2, "Marte", 51, 1, "S", "Rocoso"),
            Planeta(3, "Jupiter", 50, 150, "L", "Gaseoso"),
            Planeta(4, "Venus", 150, 50, "S", "Rocoso"),
        ]
        
        generador_planetas = (planeta for planeta in lista_planetas)
        
        resultado_estudiante = encontrar_planetas_cercanos(generador_planetas, 50, 0, 100, 20, None)
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        
        # Debe encontrar Tierra y Marte (están en el área 0,0 a 100,100)
        planetas_esperados = [
            Planeta(1, "Tierra", 88, 11, "M", "Rocoso"),
            Planeta(2, "Marte", 51, 1, "S", "Rocoso"),
        ]
        
        self.assertCountEqual(lista_resultado, planetas_esperados)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que se manejen correctamente coordenadas negativas.
        """
        lista_planetas = [
            Planeta(1, "Tierra", 0, 0, "M", "Rocoso"),
            Planeta(2, "Marte", -50, -50, "S", "Rocoso"),
            Planeta(3, "Jupiter", -90, -40, "L", "Gaseoso"),
            Planeta(4, "Venus", -40, -90, "S", "Rocoso"),
            Planeta(5, "Furyu", -50, 50, "L", "Gaseoso"),
            Planeta(6, "Hoenn", 50, -50, "L", "Gaseoso"),
        ]
        
        generador_planetas = (planeta for planeta in lista_planetas)
        
        resultado_estudiante = encontrar_planetas_cercanos(generador_planetas, -100, -100, -10, -49, None)
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        
        planetas_esperados = [
            Planeta(2, "Marte", -50, -50, "S", "Rocoso"),
            Planeta(4, "Venus", -40, -90, "S", "Rocoso"),
        ]
        
        self.assertCountEqual(lista_resultado, planetas_esperados)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que se respete el límite de cantidad especificado.
        """
        lista_planetas = [
            Planeta(1, "Tierra", 0, 0, "M", "Rocoso"),
            Planeta(2, "Marte", 10, 10, "S", "Rocoso"),
            Planeta(3, "Jupiter", 20, 20, "L", "Gaseoso"),
            Planeta(4, "Venus", 30, 30, "S", "Rocoso"),
            Planeta(5, "Saturno", 40, 40, "L", "Gaseoso"),
        ]
        
        generador_planetas = (planeta for planeta in lista_planetas)
        
        resultado_estudiante = encontrar_planetas_cercanos(generador_planetas, 0, 0, 50, 50, 3)
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        
        # Debe retornar exactamente 3 planetas (límite especificado)
        self.assertEqual(len(lista_resultado), 3)
        
        # Todos los planetas retornados deben estar en el área especificada
        for planeta in lista_resultado:
            self.assertTrue(0 <= planeta.coordenada_x <= 50)
            self.assertTrue(0 <= planeta.coordenada_y <= 50)
            self.assertIn(planeta, lista_planetas)

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica que se encuentren planetas en el borde del área especificada.
        """
        lista_planetas = [
            Planeta(1, "Tierra", 2, 3, "M", "Rocoso"),
            Planeta(2, "Marte", 150, 50, "S", "Rocoso"),
            Planeta(3, "Jupiter", 0, 50, "L", "Gaseoso"),
            Planeta(4, "Venus", 101, 101, "S", "Rocoso"),  # Fuera del área
        ]
        
        generador_planetas = (planeta for planeta in lista_planetas)

        resultado_estudiante = encontrar_planetas_cercanos(generador_planetas, 2, 3, 2, 3, None)
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)

        planetas_esperados = [
            Planeta(1, "Tierra", 2, 3, "M", "Rocoso"),
        ]
        
        self.assertCountEqual(lista_resultado, planetas_esperados)
