import os
import sys
import unittest
from collections.abc import Iterable
from tests_privados.timeout_function import timeout
from tests_privados.utils import FLEXIBILIDAD_ADICIONAL
sys.stdout = open(os.devnull, 'w')
from backend.consultas import misiones_por_tipo_planeta
from utilidades import Mision, Planeta

# Constante para timeout en tests
N_SECOND = FLEXIBILIDAD_ADICIONAL*0.08



def _gen(iterable):
    return (item for item in iterable)


class TestMisionesPorTipoPlanetaCorrectitud(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica que se retorne lista vacía cuando no hay misiones en planetas del tipo especificado.
        """
        lista_misiones = [
            Mision(1, "2024-01-10", "10:00", 1, 1, True),
            Mision(2, "2024-01-12", "11:00", 2, 2, False),
            Mision(3, "2024-01-14", "12:00", 3, 3, True),
        ]
        
        lista_planetas = [
            Planeta(1, "P-001", 0.0, 0.0, "S", "Plasma"),
            Planeta(2, "P-002", 100.0, 100.0, "M", "Gas"),
            Planeta(3, "P-003", 200.0, 200.0, "L", "Rocoso"),
        ]
        
        generador_misiones = _gen(lista_misiones)
        generador_planetas = _gen(lista_planetas)
        
        resultado_estudiante = misiones_por_tipo_planeta(generador_misiones, generador_planetas, "Sólido")
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        
        self.assertEqual(lista_resultado, [])

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se retorne lista vacía cuando no hay planetas del tipo especificado.
        """
        lista_misiones = [
            Mision(1, "2024-01-10", "10:00", 1, 1, True),
            Mision(2, "2024-01-12", "11:00", 2, 2, False),
        ]
        
        lista_planetas = [
            Planeta(1, "P-001", 0.0, 0.0, "S", "Plasma"),
            Planeta(2, "P-002", 100.0, 100.0, "M", "Gas"),
        ]
        
        generador_misiones = _gen(lista_misiones)
        generador_planetas = _gen(lista_planetas)
        
        resultado_estudiante = misiones_por_tipo_planeta(generador_misiones, generador_planetas, "Criogénico")
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        
        self.assertEqual(lista_resultado, [])

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se retornen todas las misiones cuando todas están en planetas del tipo especificado.
        """
        lista_misiones = [
            Mision(1, "2024-01-10", "10:00", 1, 1, True),
            Mision(2, "2024-01-12", "11:00", 2, 2, False),
            Mision(3, "2024-01-14", "12:00", 3, 3, True),
        ]
        
        lista_planetas = [
            Planeta(1, "P-001", 0.0, 0.0, "S", "Plasma"),
            Planeta(2, "P-002", 100.0, 100.0, "M", "Plasma"),
            Planeta(3, "P-003", 200.0, 200.0, "L", "Plasma"),
        ]
        
        generador_misiones = _gen(lista_misiones)
        generador_planetas = _gen(lista_planetas)
        
        resultado_estudiante = misiones_por_tipo_planeta(generador_misiones, generador_planetas, "Plasma")
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        
        # Debe retornar todas las misiones
        self.assertCountEqual(lista_resultado, lista_misiones)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que se retorne lista vacía con generador vacío de misiones.
        """
        lista_planetas = [
            Planeta(1, "P-001", 0.0, 0.0, "S", "Plasma"),
        ]
        
        generador_misiones = _gen([])
        generador_planetas = _gen(lista_planetas)
        
        resultado_estudiante = misiones_por_tipo_planeta(generador_misiones, generador_planetas, "Plasma")
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        
        self.assertEqual(lista_resultado, [])

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que se retorne lista vacía con generador vacío de planetas.
        """
        lista_misiones = [
            Mision(1, "2024-01-10", "10:00", 1, 1, True),
        ]
        
        generador_misiones = _gen(lista_misiones)
        generador_planetas = _gen([])
        
        resultado_estudiante = misiones_por_tipo_planeta(generador_misiones, generador_planetas, "Plasma")
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        
        self.assertEqual(lista_resultado, [])

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica que se filtren correctamente las misiones por tipo de planeta con datos mixtos.
        """
        lista_misiones = [
            Mision(1, "2024-01-10", "10:00", 1, 1, True),   # Plasma
            Mision(2, "2024-01-12", "11:00", 2, 2, False),  # Gas
            Mision(3, "2024-01-14", "12:00", 3, 3, True),  # Plasma
            Mision(4, "2024-01-16", "13:00", 4, 4, False), # Rocoso
            Mision(5, "2024-01-18", "14:00", 5, 5, True),  # Plasma
        ]
        
        lista_planetas = [
            Planeta(1, "P-001", 0.0, 0.0, "S", "Plasma"),
            Planeta(2, "P-002", 100.0, 100.0, "M", "Gas"),
            Planeta(3, "P-003", 200.0, 200.0, "L", "Plasma"),
            Planeta(4, "P-004", 300.0, 300.0, "XL", "Rocoso"),
            Planeta(5, "P-005", 400.0, 400.0, "S", "Plasma"),
        ]
        
        generador_misiones = _gen(lista_misiones)
        generador_planetas = _gen(lista_planetas)
        
        resultado_estudiante = misiones_por_tipo_planeta(generador_misiones, generador_planetas, "Plasma")
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        
        # Debe retornar solo las misiones en planetas Plasma (1, 3, 5)
        misiones_esperadas = [lista_misiones[0], lista_misiones[2], lista_misiones[4]]
        self.assertCountEqual(lista_resultado, misiones_esperadas)
