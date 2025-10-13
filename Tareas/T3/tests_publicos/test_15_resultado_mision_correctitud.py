import unittest
import sys
import os

from backend.consultas import resultado_mision
from utilidades import Mision, Nave, Tripulacion, PlanetaMineral, MisionMineral
from tests_publicos.timeout_function import timeout

sys.stdout = open(os.devnull, 'w')

# Constante para timeout en tests
N_SECOND = 0.08


class TestResultadoMisionCorrectitud(unittest.TestCase):
    
    @timeout(N_SECOND)
    def test_0(self):
        """
        Test para verificar que resultado_mision devuelve True cuando:
        1. El equipo tiene una tripulación válida
        2. Los minerales requeridos están disponibles en el planeta
        3. Las cantidades requeridas no exceden las disponibles
        4. El total extraído no excede la capacidad de la nave
        """
        # Crear misión
        mision = Mision(
            id_mision=1,
            fecha="2023-11-12",
            hora="20:05",
            id_equipo=1,
            id_planeta=1,
            lograda=False
        )
        
        # Crear nave con capacidad suficiente
        nave = Nave(
            patente="N-001",
            material="Titanio",
            tamano="M",
            capacidad_astronautas=5,
            capacidad_minerales=1000.0,  # Capacidad alta
            autonomia=200.0
        )
        
        # Crear tripulación
        tripulacion = Tripulacion(
            id_equipo=1,
            patente_nave="N-001",
            id_astronauta=1,
            rango=1
        )
        
        # Crear minerales disponibles en el planeta
        planeta_mineral_1 = PlanetaMineral(
            id_planeta=1,
            id_mineral=10,
            cantidad_disponible=500.0,  # Suficiente cantidad
            pureza=0.9
        )
        
        planeta_mineral_2 = PlanetaMineral(
            id_planeta=1,
            id_mineral=20,
            cantidad_disponible=300.0,  # Suficiente cantidad
            pureza=0.8
        )
        
        # Crear minerales requeridos por la misión
        mision_mineral_1 = MisionMineral(
            id_mision=1,
            id_mineral=10,
            cantidad=200.0  # Menor que disponible
        )
        
        mision_mineral_2 = MisionMineral(
            id_mision=1,
            id_mineral=20,
            cantidad=150.0  # Menor que disponible
        )
        
        # Crear generadores
        generador_naves = iter([nave])
        generador_planeta_mineral = iter([planeta_mineral_1, planeta_mineral_2])
        generador_tripulaciones = iter([tripulacion])
        generador_mision_mineral = iter([mision_mineral_1, mision_mineral_2])
        
        # Ejecutar función
        resultado = resultado_mision(
            mision,
            generador_naves,
            generador_planeta_mineral,
            generador_tripulaciones,
            generador_mision_mineral
        )
        
        # Verificar resultado
        self.assertTrue(resultado.lograda)
        self.assertEqual(resultado.id_mision, 1)
        self.assertEqual(resultado.id_equipo, 1)
        self.assertEqual(resultado.id_planeta, 1)
        self.assertEqual(resultado.lograda, True)
    
    @timeout(N_SECOND)
    def test_1(self):
        """
        Test para verificar que resultado_mision devuelve False cuando:
        El mineral requerido no está disponible en el planeta
        """
        # Crear misión
        mision = Mision(
            id_mision=2,
            fecha="2023-11-12",
            hora="20:05",
            id_equipo=2,
            id_planeta=2,
            lograda=False
        )
        
        # Crear nave
        nave = Nave(
            patente="N-002",
            material="Acero",
            tamano="S",
            capacidad_astronautas=3,
            capacidad_minerales=500.0,
            autonomia=150.0
        )
        
        # Crear tripulación
        tripulacion = Tripulacion(
            id_equipo=2,
            patente_nave="N-002",
            id_astronauta=2,
            rango=2
        )
        
        # Crear mineral disponible en el planeta (diferente al requerido)
        planeta_mineral = PlanetaMineral(
            id_planeta=2,
            id_mineral=30,  # Mineral diferente
            cantidad_disponible=1000.0,
            pureza=0.9
        )
        
        # Crear mineral requerido por la misión (no disponible en el planeta)
        mision_mineral = MisionMineral(
            id_mision=2,
            id_mineral=40,  # Mineral no disponible
            cantidad=100.0
        )
        
        # Crear generadores
        generador_naves = iter([nave])
        generador_planeta_mineral = iter([planeta_mineral])
        generador_tripulaciones = iter([tripulacion])
        generador_mision_mineral = iter([mision_mineral])
        
        # Ejecutar función
        resultado = resultado_mision(
            mision,
            generador_naves,
            generador_planeta_mineral,
            generador_tripulaciones,
            generador_mision_mineral
        )
        
        # Verificar resultado
        self.assertFalse(resultado.lograda)
        self.assertEqual(resultado.id_mision, 2)
        self.assertEqual(resultado.id_equipo, 2)
        self.assertEqual(resultado.id_planeta, 2)
    
    @timeout(N_SECOND)
    def test_2(self):
        """
        Test para verificar que resultado_mision devuelve False cuando:
        La cantidad requerida excede la cantidad disponible en el planeta
        """
        # Crear misión
        mision = Mision(
            id_mision=3,
            fecha="2023-11-12",
            hora="20:05",
            id_equipo=3,
            id_planeta=3,
            lograda=False
        )
        
        # Crear nave
        nave = Nave(
            patente="N-003",
            material="Compósito",
            tamano="L",
            capacidad_astronautas=7,
            capacidad_minerales=2000.0,
            autonomia=300.0
        )
        
        # Crear tripulación
        tripulacion = Tripulacion(
            id_equipo=3,
            patente_nave="N-003",
            id_astronauta=3,
            rango=3
        )
        
        # Crear mineral disponible en el planeta (cantidad limitada)
        planeta_mineral = PlanetaMineral(
            id_planeta=3,
            id_mineral=50,
            cantidad_disponible=100.0,  # Cantidad limitada
            pureza=0.7
        )
        
        # Crear mineral requerido por la misión (cantidad mayor a la disponible)
        mision_mineral = MisionMineral(
            id_mision=3,
            id_mineral=50,
            cantidad=200.0  # Mayor que disponible
        )
        
        # Crear generadores
        generador_naves = iter([nave])
        generador_planeta_mineral = iter([planeta_mineral])
        generador_tripulaciones = iter([tripulacion])
        generador_mision_mineral = iter([mision_mineral])
        
        # Ejecutar función
        resultado = resultado_mision(
            mision,
            generador_naves,
            generador_planeta_mineral,
            generador_tripulaciones,
            generador_mision_mineral
        )
        
        # Verificar resultado
        self.assertFalse(resultado.lograda)
        self.assertEqual(resultado.id_mision, 3)
        self.assertEqual(resultado.id_equipo, 3)
        self.assertEqual(resultado.id_planeta, 3)
    
    @timeout(N_SECOND)
    def test_3(self):
        """
        Test para verificar que resultado_mision devuelve False cuando:
        El total extraído excede la capacidad de la nave
        """
        # Crear misión
        mision = Mision(
            id_mision=4,
            fecha="2023-11-12",
            hora="20:05",
            id_equipo=4,
            id_planeta=4,
            lograda=False
        )
        
        # Crear nave con capacidad limitada
        nave = Nave(
            patente="N-004",
            material="Aluminio",
            tamano="S",
            capacidad_astronautas=2,
            capacidad_minerales=100.0,  # Capacidad muy limitada
            autonomia=100.0
        )
        
        # Crear tripulación
        tripulacion = Tripulacion(
            id_equipo=4,
            patente_nave="N-004",
            id_astronauta=4,
            rango=1
        )
        
        # Crear minerales disponibles en el planeta
        planeta_mineral_1 = PlanetaMineral(
            id_planeta=4,
            id_mineral=60,
            cantidad_disponible=1000.0,
            pureza=0.9
        )
        
        planeta_mineral_2 = PlanetaMineral(
            id_planeta=4,
            id_mineral=70,
            cantidad_disponible=1000.0,
            pureza=0.8
        )
        
        # Crear minerales requeridos por la misión (total excede capacidad)
        mision_mineral_1 = MisionMineral(
            id_mision=4,
            id_mineral=60,
            cantidad=80.0  # Total: 80 + 50 = 130 > 100
        )
        
        mision_mineral_2 = MisionMineral(
            id_mision=4,
            id_mineral=70,
            cantidad=50.0
        )
        
        # Crear generadores
        generador_naves = iter([nave])
        generador_planeta_mineral = iter([planeta_mineral_1, planeta_mineral_2])
        generador_tripulaciones = iter([tripulacion])
        generador_mision_mineral = iter([mision_mineral_1, mision_mineral_2])
        
        # Ejecutar función
        resultado = resultado_mision(
            mision,
            generador_naves,
            generador_planeta_mineral,
            generador_tripulaciones,
            generador_mision_mineral
        )
        
        # Verificar resultado
        self.assertFalse(resultado.lograda)
        self.assertEqual(resultado.id_mision, 4)
        self.assertEqual(resultado.id_equipo, 4)
        self.assertEqual(resultado.id_planeta, 4)
    
    @timeout(N_SECOND)
    def test_4(self):
        """
        Test para verificar el caso especial cuando el mineral es ID=1:
        Si el mineral es ID=1 y cantidad > 0, solo se suma esa cantidad y se rompe el bucle
        """
        # Crear misión
        mision = Mision(
            id_mision=5,
            fecha="2023-11-12",
            hora="20:05",
            id_equipo=5,
            id_planeta=5,
            lograda=False
        )
        
        # Crear nave con capacidad suficiente
        nave = Nave(
            patente="N-005",
            material="Titanio",
            tamano="M",
            capacidad_astronautas=5,
            capacidad_minerales=500.0,
            autonomia=200.0
        )
        
        # Crear tripulación
        tripulacion = Tripulacion(
            id_equipo=5,
            patente_nave="N-005",
            id_astronauta=5,
            rango=2
        )
        
        # Crear mineral ID=1 disponible en el planeta
        planeta_mineral = PlanetaMineral(
            id_planeta=5,
            id_mineral=1,  # Mineral especial
            cantidad_disponible=1000.0,
            pureza=0.9
        )
        
        # Crear minerales requeridos por la misión
        mision_mineral_1 = MisionMineral(
            id_mision=5,
            id_mineral=1,  # Mineral especial
            cantidad=200.0
        )
        
        mision_mineral_2 = MisionMineral(
            id_mision=5,
            id_mineral=80,  # Este no debería procesarse
            cantidad=100.0
        )
        
        # Crear generadores
        generador_naves = iter([nave])
        generador_planeta_mineral = iter([planeta_mineral])
        generador_tripulaciones = iter([tripulacion])
        generador_mision_mineral = iter([mision_mineral_1, mision_mineral_2])
        
        # Ejecutar función
        resultado = resultado_mision(
            mision,
            generador_naves,
            generador_planeta_mineral,
            generador_tripulaciones,
            generador_mision_mineral
        )
        
        # Verificar resultado
        self.assertTrue(resultado.lograda)  # Solo se suma 200.0, que es menor que 500.0
        self.assertEqual(resultado.id_mision, 5)
        self.assertEqual(resultado.id_equipo, 5)
        self.assertEqual(resultado.id_planeta, 5)
    
    @timeout(N_SECOND)
    def test_5(self):
        """
        Test para verificar casos edge:
        1. Misión sin minerales requeridos (total_extraido = 0)
        2. Capacidad de nave exactamente igual al total extraído puro (no impuro)
        3. Múltiples minerales con diferentes cantidades
        """
        # Crear misión
        mision = Mision(
            id_mision=6,
            fecha="2023-11-12",
            hora="20:05",
            id_equipo=6,
            id_planeta=6,
            lograda=False
        )
        
        # Crear nave con capacidad exacta
        nave = Nave(
            patente="N-006",
            material="Compósito",
            tamano="M",
            capacidad_astronautas=4,
            capacidad_minerales=350.0,  # Capacidad exacta para el total
            autonomia=180.0
        )
        
        # Crear tripulación
        tripulacion = Tripulacion(
            id_equipo=6,
            patente_nave="N-006",
            id_astronauta=6,
            rango=2
        )
        
        # Crear múltiples minerales disponibles en el planeta
        planeta_mineral_1 = PlanetaMineral(
            id_planeta=6,
            id_mineral=100,
            cantidad_disponible=500.0,
            pureza=0.9
        )
        
        planeta_mineral_2 = PlanetaMineral(
            id_planeta=6,
            id_mineral=200,
            cantidad_disponible=400.0,
            pureza=0.8
        )
        
        planeta_mineral_3 = PlanetaMineral(
            id_planeta=6,
            id_mineral=300,
            cantidad_disponible=300.0,
            pureza=0.7
        )
        
        # Crear múltiples minerales requeridos por la misión (total = 350.0)
        mision_mineral_1 = MisionMineral(
            id_mision=6,
            id_mineral=100,
            cantidad=100.0
        )
        
        mision_mineral_2 = MisionMineral(
            id_mision=6,
            id_mineral=200,
            cantidad=150.0
        )
        
        mision_mineral_3 = MisionMineral(
            id_mision=6,
            id_mineral=300,
            cantidad=100.0
        )
        
        # Crear generadores
        generador_naves = iter([nave])
        generador_planeta_mineral = iter([planeta_mineral_1, planeta_mineral_2, planeta_mineral_3])
        generador_tripulaciones = iter([tripulacion])
        generador_mision_mineral = iter([mision_mineral_1, mision_mineral_2, mision_mineral_3])
        
        # Ejecutar función
        resultado = resultado_mision(
            mision,
            generador_naves,
            generador_planeta_mineral,
            generador_tripulaciones,
            generador_mision_mineral
        )
        
        # Verificar resultado (total = 350.0, capacidad = 350.0, debe ser False)
        self.assertFalse(resultado.lograda)
        self.assertEqual(resultado.id_mision, 6)
        self.assertEqual(resultado.id_equipo, 6)
        self.assertEqual(resultado.id_planeta, 6)

