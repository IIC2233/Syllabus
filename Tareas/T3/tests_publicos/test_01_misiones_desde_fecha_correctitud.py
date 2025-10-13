import os
import sys
import unittest
from collections.abc import Iterable

from tests_publicos.timeout_function import timeout
sys.stdout = open(os.devnull, 'w')
from collections import namedtuple        
from backend.consultas import misiones_desde_fecha, cargar_mision
Mision = namedtuple("Mision", ["id_mision", "fecha", "hora", "id_equipo", "id_planeta", "lograda"])
# Constante para timeout en tests
N_SECOND = 0.08

class TestMisionesPorFechaCorrectitud(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica que se retorne lista vacía cuando no hay misiones después de la fecha.
        """
        
        lista_misiones = [
            Mision(1, "2024-01-10", "10:00", 1, 1, True),
            Mision(2, "2024-01-12", "11:00", 2, 2, False),
            Mision(3, "2024-01-14", "12:00", 3, 3, True),
        ]
        
        generador_misiones = (mision for mision in lista_misiones)
        
        resultado_estudiante = misiones_desde_fecha(generador_misiones, "2024-01-20", False)
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        
        self.assertEqual(lista_resultado, [])

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se retorne lista vacía cuando no hay misiones antes de la fecha.
        """
        
        lista_misiones = [
            Mision(1, "2024-01-20", "10:00", 1, 1, True),
            Mision(2, "2024-01-22", "11:00", 2, 2, False),
            Mision(3, "2024-01-24", "12:00", 3, 3, True),
        ]
        
        generador_misiones = (mision for mision in lista_misiones)
        
        resultado_estudiante = misiones_desde_fecha(generador_misiones, "2024-01-15", True)
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        
        self.assertEqual(lista_resultado, [])

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que la fecha límite sea inclusiva en ambos casos.
        """
        
        lista_misiones = [
            Mision(1, "2024-01-10", "10:00", 1, 1, True),
            Mision(2, "2024-01-15", "11:00", 2, 2, False),  # Fecha límite
            Mision(3, "2024-01-20", "12:00", 3, 3, True),
        ]
        
        generador_misiones = (mision for mision in lista_misiones)
        
        # Test inverso False - debe incluir la fecha límite y las posteriores
        resultado_false = misiones_desde_fecha(generador_misiones, "2024-01-15", False)
        lista_false = list(resultado_false)
        
        # Test inverso True - debe incluir la fecha límite y las anteriores
        generador_misiones2 = (mision for mision in lista_misiones)
        resultado_true = misiones_desde_fecha(generador_misiones2, "2024-01-15", True)
        lista_true = list(resultado_true)
        
        self.assertIsInstance(resultado_false, (Iterable))
        self.assertIsInstance(resultado_true, (Iterable))
        
        # Verificar que ambas listas contienen la misión con fecha límite
        self.assertIn(Mision(2, "2024-01-15", "11:00", 2, 2, False), lista_false)
        self.assertIn(Mision(2, "2024-01-15", "11:00", 2, 2, False), lista_true)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que se retorne lista vacía con generador vacío.
        """
        generador_vacio = (mision for mision in [])
        
        resultado_estudiante = misiones_desde_fecha(generador_vacio, "2024-01-15", False)
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        
        self.assertEqual(lista_resultado, [])

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que se retornen todas las misiones cuando la fecha es muy temprana.
        """
        
        lista_misiones = [
            Mision(1, "2024-01-10", "10:00", 1, 1, True),
            Mision(2, "2024-01-12", "11:00", 2, 2, False),
            Mision(3, "2024-01-14", "12:00", 3, 3, True),
        ]
        
        generador_misiones = (mision for mision in lista_misiones)
        
        resultado_estudiante = misiones_desde_fecha(generador_misiones, "2024-01-15", True)
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        
        # Debe retornar todas las misiones
        self.assertCountEqual(lista_resultado, lista_misiones)

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica que se retornen todas las misiones cuando la fecha es muy tardía.
        """
        
        lista_misiones = [
            Mision(id_mision=1, fecha="2024-01-10", hora="10:00", id_equipo=1, id_planeta=1, lograda=True),
            Mision(id_mision=2, fecha="2024-01-12", hora="11:00", id_equipo=2, id_planeta=2, lograda=False),
            Mision(id_mision=3, fecha="2024-01-14", hora="12:00", id_equipo=3, id_planeta=3, lograda=True),
        ]
        
        generador_misiones = (mision for mision in lista_misiones)
        
        resultado_estudiante = misiones_desde_fecha(generador_misiones, "2024-01-09", False)
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        
        # Debe retornar todas las misiones
        self.assertCountEqual(lista_resultado, lista_misiones)
