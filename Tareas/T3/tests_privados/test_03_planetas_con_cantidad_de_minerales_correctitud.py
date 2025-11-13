import os
import sys
import unittest
from collections.abc import Iterable
from collections import namedtuple
from tests_privados.timeout_function import timeout
from tests_privados.utils import FLEXIBILIDAD_ADICIONAL
sys.stdout = open(os.devnull, 'w')
from backend.consultas import planetas_con_cantidad_de_minerales
# Constante para timeout en tests
N_SECOND = FLEXIBILIDAD_ADICIONAL*0.08

PlanetaMineral = namedtuple("PlanetaMineral", ["id_planeta", "id_mineral", "cantidad_disponible", "pureza"])

class TestPlanetasConCantidadDeMineralesCorrectitud(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica que se retorne lista vacía cuando no hay planetas que cumplan la cuota.
        """
        
        lista_planeta_minerales = [
            PlanetaMineral(1, 1, 50.0, 0.8),
            PlanetaMineral(2, 1, 75.0, 0.9),
            PlanetaMineral(3, 1, 25.0, 0.7),
        ]
        
        generador_planeta_minerales = (pm for pm in lista_planeta_minerales)
        
        resultado_estudiante = planetas_con_cantidad_de_minerales(generador_planeta_minerales, 1, 100)
        
        self.assertIsInstance(resultado_estudiante, list)
        
        self.assertEqual(resultado_estudiante, [])

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se retornen todos los planetas con cantidad mínima negativa.
        """
        
        lista_planeta_minerales = [
            PlanetaMineral(1, 1, 50.0, 0.8),
            PlanetaMineral(2, 1, 75.0, 0.9),
            PlanetaMineral(3, 1, 25.0, 0.7),
        ]
        
        generador_planeta_minerales = (pm for pm in lista_planeta_minerales)
        
        resultado_estudiante = planetas_con_cantidad_de_minerales(generador_planeta_minerales, 1, -50)
        
        self.assertIsInstance(resultado_estudiante, list)
        
        # Con cantidad mínima negativa, todos los planetas cumplen (cantidad efectiva >= -50)
        resultado_esperado = [1, 2, 3]
        
        self.assertCountEqual(resultado_estudiante, resultado_esperado)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se retorne lista vacía con mineral que no existe.
        """
        
        lista_planeta_minerales = [
            PlanetaMineral(1, 1, 50.0, 0.8),
            PlanetaMineral(2, 2, 75.0, 0.9),
            PlanetaMineral(3, 3, 25.0, 0.7),
        ]
        
        generador_planeta_minerales = (pm for pm in lista_planeta_minerales)
        
        resultado_estudiante = planetas_con_cantidad_de_minerales(generador_planeta_minerales, 999, 100)
        
        self.assertIsInstance(resultado_estudiante, list)
        
        self.assertEqual(resultado_estudiante, [])

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que se retorne todos los planetas con cantidad mínima cero.
        """
        
        lista_planeta_minerales = [
            PlanetaMineral(1, 1, 50.0, 0.8),
            PlanetaMineral(2, 1, 75.0, 0.9),
            PlanetaMineral(3, 1, 25.0, 0.7),
        ]
        
        generador_planeta_minerales = (pm for pm in lista_planeta_minerales)
        
        resultado_estudiante = planetas_con_cantidad_de_minerales(generador_planeta_minerales, 1, 0)
        
        self.assertIsInstance(resultado_estudiante, list)
        
        # Debe retornar todos los planetas que tengan al menos 0 del mineral
        resultado_esperado = [1, 2, 3]
        
        self.assertCountEqual(resultado_estudiante, resultado_esperado)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que se retorne lista vacía con generador vacío.
        """
        generador_vacio = (pm for pm in [])
        
        resultado_estudiante = planetas_con_cantidad_de_minerales(generador_vacio, 1, 100)
        
        self.assertIsInstance(resultado_estudiante, list)
        
        self.assertEqual(resultado_estudiante, [])

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica casos con valores decimales complejos.
        """
        
        lista_planeta_minerales = [
            PlanetaMineral(1, 123, 1234.567, 0.123456),  # 152.415 >= 150
            PlanetaMineral(2, 123, 2345.678, 0.098765),   # 231.671 >= 150
            PlanetaMineral(3, 123, 3456.789, 0.045678),   # 157.899 >= 150
            PlanetaMineral(4, 123, 4567.890, 0.032109),  # 146.670 < 150
        ]
        
        generador_planeta_minerales = (pm for pm in lista_planeta_minerales)
        
        resultado_estudiante = planetas_con_cantidad_de_minerales(generador_planeta_minerales, 123, 150)
        
        self.assertIsInstance(resultado_estudiante, list)
        
        # Debe retornar planetas 1, 2 y 3
        resultado_esperado = [1, 2, 3]
        
        self.assertCountEqual(resultado_estudiante, resultado_esperado)
        

    @timeout(N_SECOND)
    def test_6(self):
        """
        Verifica casos con múltiples minerales diferentes.
        """
        
        lista_planeta_minerales = [
            PlanetaMineral(1, 200, 1000.0, 0.8),   # 800.0 >= 500
            PlanetaMineral(2, 201, 2000.0, 0.3),   # 600.0 >= 500 (mineral diferente)
            PlanetaMineral(3, 200, 500.0, 0.9),    # 450.0 < 500
            PlanetaMineral(4, 200, 1500.0, 0.4),  # 600.0 >= 500
            PlanetaMineral(5, 202, 3000.0, 0.2),   # 600.0 >= 500 (mineral diferente)
        ]
        
        generador_planeta_minerales = (pm for pm in lista_planeta_minerales)
        
        resultado_estudiante = planetas_con_cantidad_de_minerales(generador_planeta_minerales, 200, 500)
        
        self.assertIsInstance(resultado_estudiante, list)
        
        # Debe retornar solo planetas con mineral 200 que cumplan
        resultado_esperado = [1, 4]
        
        self.assertCountEqual(resultado_estudiante, resultado_esperado)