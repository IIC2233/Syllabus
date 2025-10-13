import os
import sys
import unittest
from collections.abc import Iterable
from collections import namedtuple
from tests_publicos.timeout_function import timeout
from backend.consultas import cargar_tripulaciones, cambiar_rango_astronauta
sys.stdout = open(os.devnull, 'w')

Tripulacion = namedtuple("Tripulacion", ["id_equipo", "patente_nave", "id_astronauta", "rango"])
# Constante para timeout en tests
N_SECOND = 0.08

class TestCambiarRangoAstronautaCorrectitud(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica que se modifique correctamente el astronauta existente.
        """
        lista_tripulaciones = [
            Tripulacion(617, "N-110", 501, 5),
            Tripulacion(618, "N-111", 502, 3),
            Tripulacion(619, "N-112", 503, 7),
        ]
        
        generador_tripulaciones = (tripulacion for tripulacion in lista_tripulaciones)
        
        resultado_estudiante = cambiar_rango_astronauta(generador_tripulaciones, 501, 10)
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        
        # Debe retornar todas las tripulaciones (mismo largo que la lista original)
        self.assertEqual(len(lista_resultado), len(lista_tripulaciones))
        
        # Verificar que el astronauta con ID 501 fue modificado
        tripulacion_modificada = None
        for tripulacion in lista_resultado:
            if tripulacion.id_astronauta == 501:
                tripulacion_modificada = tripulacion
                break
        
        self.assertIsNotNone(tripulacion_modificada)
        self.assertEqual(tripulacion_modificada.rango, 10)
        self.assertEqual(tripulacion_modificada.id_equipo, 617)
        self.assertEqual(tripulacion_modificada.patente_nave, "N-110")

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se retorne generador vacío cuando se entrega generador vacío.
        """
        generador_vacio = (tripulacion for tripulacion in [])
        
        resultado_estudiante = cambiar_rango_astronauta(generador_vacio, 501, 10)
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        
        self.assertEqual(lista_resultado, [])

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se modifique correctamente el astronauta existente.
        """
        lista_tripulaciones = [
            Tripulacion(617, "N-110", 501, 5),
            Tripulacion(618, "N-111", 502, 3),
            Tripulacion(619, "N-112", 503, 7),
        ]
        
        generador_tripulaciones = (tripulacion for tripulacion in lista_tripulaciones)
        
        resultado_estudiante = cambiar_rango_astronauta(generador_tripulaciones, 502, 15)
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        
        # Debe retornar todas las tripulaciones (mismo largo que la lista original)
        self.assertEqual(len(lista_resultado), len(lista_tripulaciones))
        
        # Verificar que el astronauta con ID 502 fue modificado
        tripulacion_modificada = None
        for tripulacion in lista_resultado:
            if tripulacion.id_astronauta == 502:
                tripulacion_modificada = tripulacion
                break
        
        self.assertIsNotNone(tripulacion_modificada)
        self.assertEqual(tripulacion_modificada.rango, 15)
        self.assertEqual(tripulacion_modificada.id_equipo, 618)
        self.assertEqual(tripulacion_modificada.patente_nave, "N-111")

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que se modifique correctamente con rango mínimo.
        """
        lista_tripulaciones = [
            Tripulacion(617, "N-110", 501, 5),
            Tripulacion(618, "N-111", 502, 3),
            Tripulacion(619, "N-112", 503, 7),
        ]
        
        generador_tripulaciones = (tripulacion for tripulacion in lista_tripulaciones)
        
        resultado_estudiante = cambiar_rango_astronauta(generador_tripulaciones, 502, 1)
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        
        # Debe retornar todas las tripulaciones (mismo largo que la lista original)
        self.assertEqual(len(lista_resultado), len(lista_tripulaciones))
        
        # Verificar que el astronauta con ID 502 fue modificado con rango mínimo
        tripulacion_modificada = None
        for tripulacion in lista_resultado:
            if tripulacion.id_astronauta == 502:
                tripulacion_modificada = tripulacion
                break
        
        self.assertIsNotNone(tripulacion_modificada)
        self.assertEqual(tripulacion_modificada.rango, 1)
        self.assertEqual(tripulacion_modificada.id_equipo, 618)
        self.assertEqual(tripulacion_modificada.patente_nave, "N-111")

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que se modifique correctamente con rango máximo.
        """
        lista_tripulaciones = [
            Tripulacion(617, "N-110", 501, 5),
            Tripulacion(618, "N-111", 502, 3),
        ]
        
        generador_tripulaciones = (tripulacion for tripulacion in lista_tripulaciones)
        
        resultado_estudiante = cambiar_rango_astronauta(generador_tripulaciones, 501, 99)
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        
        # Debe retornar todas las tripulaciones (mismo largo que la lista original)
        self.assertEqual(len(lista_resultado), len(lista_tripulaciones))
        
        # Verificar que el astronauta con ID 501 fue modificado con rango máximo
        tripulacion_modificada = None
        for tripulacion in lista_resultado:
            if tripulacion.id_astronauta == 501:
                tripulacion_modificada = tripulacion
                break
        
        self.assertIsNotNone(tripulacion_modificada)
        self.assertEqual(tripulacion_modificada.rango, 99)
        self.assertEqual(tripulacion_modificada.id_equipo, 617)
        self.assertEqual(tripulacion_modificada.patente_nave, "N-110")

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica que se modifique correctamente con rango intermedio.
        """
        lista_tripulaciones = [
            Tripulacion(617, "N-110", 501, 5),
            Tripulacion(618, "N-111", 502, 3),
            Tripulacion(619, "N-112", 503, 7),
            Tripulacion(620, "N-113", 504, 2),
        ]
        
        generador_tripulaciones = (tripulacion for tripulacion in lista_tripulaciones)
        
        resultado_estudiante = cambiar_rango_astronauta(generador_tripulaciones, 503, 50)
        
        self.assertIsInstance(resultado_estudiante, (Iterable))
        
        lista_resultado = list(resultado_estudiante)
        
        # Debe retornar todas las tripulaciones (mismo largo que la lista original)
        self.assertEqual(len(lista_resultado), len(lista_tripulaciones))
        
        # Verificar que el astronauta con ID 503 fue modificado con rango intermedio
        tripulacion_modificada = None
        for tripulacion in lista_resultado:
            if tripulacion.id_astronauta == 503:
                tripulacion_modificada = tripulacion
                break
        
        self.assertIsNotNone(tripulacion_modificada)
        self.assertEqual(tripulacion_modificada.rango, 50)
        self.assertEqual(tripulacion_modificada.id_equipo, 619)
        self.assertEqual(tripulacion_modificada.patente_nave, "N-112")
