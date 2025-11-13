import os
import sys
import unittest
from collections.abc import Iterable
from collections import namedtuple
import math

from tests_privados.timeout_function import timeout
from tests_privados.utils import FLEXIBILIDAD_ADICIONAL
from backend.consultas import planetas_por_estadisticas
from utilidades import radio_planeta

sys.stdout = open(os.devnull, 'w')

Mineral = namedtuple("Mineral", ["id_mineral", "nombre", "masa_atomica"])
PlanetaMineral = namedtuple("PlanetaMineral", ["id_planeta", "id_mineral", "cantidad_disponible", "pureza"])
Planeta = namedtuple("Planeta", ["id_planeta", "nombre", "coordenada_x", "coordenada_y", "tamano", "tipo"])

N_SECOND = FLEXIBILIDAD_ADICIONAL*0.08

class TestPlanetasPorEstadisticasCorrectitud(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica que se retorne generador vacío cuando no hay planetas que cumplan los criterios.
        """
        lista_minerales = [
            Mineral(1, "Hierro", 55.845),
            Mineral(2, "Oro", 196.967),
        ]
        
        lista_planeta_minerales = [
            PlanetaMineral(1, 1, 100.0, 0.5),  # 50g puros de hierro
            PlanetaMineral(2, 2, 10.0, 0.8),   # 8g puros de oro
        ]
        
        lista_planetas = [
            Planeta(1, "Tierra", 0, 0, "M", "Rocoso"),
            Planeta(2, "Marte", 100, 100, "S", "Rocoso"),
        ]
        
        generador_minerales = (mineral for mineral in lista_minerales)
        generador_planeta_minerales = (pm for pm in lista_planeta_minerales)
        generador_planetas = (planeta for planeta in lista_planetas)
        
        # Criterios muy altos que ningún planeta puede cumplir
        resultado_estudiante = planetas_por_estadisticas(generador_minerales, generador_planeta_minerales, generador_planetas, 1000000, 1000000, 1000000)
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        
        # Debe retornar generador vacío
        self.assertEqual(lista_resultado, [])

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se retorne generador vacío cuando se entrega generador vacío.
        """
        generador_vacio_minerales = (mineral for mineral in [])
        generador_vacio_planeta_minerales = (pm for pm in [])
        generador_vacio_planetas = (planeta for planeta in [])
        
        resultado_estudiante = planetas_por_estadisticas(generador_vacio_minerales, generador_vacio_planeta_minerales, generador_vacio_planetas, 1, 1, 1)
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        
        self.assertEqual(lista_resultado, [])

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se encuentren planetas que cumplan los criterios de estadísticas.
        """
        lista_minerales = [
            Mineral(1, "Hierro", 55.845),  # masa_atomica en g/mol
        ]
        
        lista_planeta_minerales = [
            PlanetaMineral(1, 1, 1000000.0, 0.8),  # 1,000,000 toneladas con 80% pureza = 800,000 toneladas puras
        ]
        
        lista_planetas = [
            Planeta(1, "Tierra", 0, 0, "M", "Rocoso"),  # Radio ~6371 km
        ]
        
        generador_minerales = (mineral for mineral in lista_minerales)
        generador_planeta_minerales = (pm for pm in lista_planeta_minerales)
        generador_planetas = (planeta for planeta in lista_planetas)
        
        # Criterios muy bajos que el planeta debería cumplir
        resultado_estudiante = planetas_por_estadisticas(generador_minerales, generador_planeta_minerales, generador_planetas, 1, 0.0001, 0.01)
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        
        # Debe encontrar la Tierra
        planetas_esperados = [
            Planeta(1, "Tierra", 0, 0, "M", "Rocoso"),
        ]
        
        self.assertCountEqual(lista_resultado, planetas_esperados)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que se manejen correctamente diferentes tamaños de planetas.
        """
        lista_minerales = [
            Mineral(1, "Hierro", 55.845),
        ]
        
        lista_planeta_minerales = [
            PlanetaMineral(1, 1, 100000.0, 0.5),  # Planeta pequeño - cantidad moderada
            PlanetaMineral(2, 1, 10000000.0, 0.5), # Planeta grande - cantidad muy alta
        ]
        
        lista_planetas = [
            Planeta(1, "Pequeño", 0, 0, "S", "Rocoso"),  # Radio pequeño
            Planeta(2, "Grande", 100, 100, "L", "Rocoso"), # Radio grande
        ]
        
        generador_minerales = (mineral for mineral in lista_minerales)
        generador_planeta_minerales = (pm for pm in lista_planeta_minerales)
        generador_planetas = (planeta for planeta in lista_planetas)
        
        # Criterios que ambos planetas deberían cumplir
        resultado_estudiante = planetas_por_estadisticas(generador_minerales, generador_planeta_minerales, generador_planetas, 1, 0.00001, 0.0001)
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        
        # Ambos planetas deberían cumplir los criterios
        planetas_esperados = [
            Planeta(1, "Pequeño", 0, 0, "S", "Rocoso"),
            Planeta(2, "Grande", 100, 100, "L", "Rocoso"),
        ]
        
        self.assertCountEqual(lista_resultado, planetas_esperados)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que se manejen correctamente diferentes purezas de minerales.
        """
        lista_minerales = [
            Mineral(1, "Hierro", 55.845),
        ]
        
        lista_planeta_minerales = [
            PlanetaMineral(1, 1, 1000000.0, 0.1),  # Baja pureza (10%) - 100,000 toneladas puras
            PlanetaMineral(2, 1, 1000000.0, 0.9),  # Alta pureza (90%) - 900,000 toneladas puras
        ]
        
        lista_planetas = [
            Planeta(1, "BajaPureza", 0, 0, "M", "Rocoso"),
            Planeta(2, "AltaPureza", 100, 100, "M", "Rocoso"),
        ]
        
        generador_minerales = (mineral for mineral in lista_minerales)
        generador_planeta_minerales = (pm for pm in lista_planeta_minerales)
        generador_planetas = (planeta for planeta in lista_planetas)
        
        # Criterios que ambos planetas deberían cumplir
        resultado_estudiante = planetas_por_estadisticas(generador_minerales, generador_planeta_minerales, generador_planetas, 1, 0.00001, 0.0001)
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        
        # Ambos planetas deberían cumplir los criterios
        planetas_esperados = [
            Planeta(1, "BajaPureza", 0, 0, "M", "Rocoso"),
            Planeta(2, "AltaPureza", 100, 100, "M", "Rocoso"),
        ]
        
        self.assertCountEqual(lista_resultado, planetas_esperados)

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica que se manejen correctamente múltiples minerales en un planeta.
        """
        lista_minerales = [
            Mineral(1, "Hierro", 55.845),
            Mineral(2, "Oro", 196.967),
        ]
        
        lista_planeta_minerales = [
            PlanetaMineral(1, 1, 10000000.0, 0.5),  # Hierro en planeta 1 - cantidad muy alta
            PlanetaMineral(1, 2, 1000000.0, 0.8),   # Oro en planeta 1 - cantidad alta
            PlanetaMineral(2, 1, 100000.0, 0.3),    # Hierro en planeta 2 - cantidad baja
        ]
        
        lista_planetas = [
            Planeta(1, "Rico", 0, 0, "M", "Rocoso"),
            Planeta(2, "Pobre", 100, 100, "M", "Rocoso"),
        ]
        
        generador_minerales = (mineral for mineral in lista_minerales)
        generador_planeta_minerales = (pm for pm in lista_planeta_minerales)
        generador_planetas = (planeta for planeta in lista_planetas)
        
        # Criterios que solo el planeta rico debería cumplir
        resultado_estudiante = planetas_por_estadisticas(generador_minerales, generador_planeta_minerales, generador_planetas, 1000000000, 0.0001, 0.01)
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        
        # Solo el planeta rico debería cumplir los criterios
        planetas_esperados = [
            Planeta(1, "Rico", 0, 0, "M", "Rocoso"),
        ]
        
        self.assertCountEqual(lista_resultado, planetas_esperados)

if __name__ == '__main__':
    unittest.main()
