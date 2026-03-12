import unittest
from copy import deepcopy as dp

from tablero import Tablero
from dccolores import DCColores
from tests_publicos.timeout_function import timeout


N_SECOND = 1

class TestIntegracion(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc if doc else None

    @timeout(N_SECOND)
    def test_00_integracion_tablero_cambiar_color_aplicar_validar(self):
        """
        Integración de Tablero + cambiar_color + aplicar_cambios + validar_solucion.
        Se crea un tablero, se aplican cambios individuales y en conjunto, 
        y se valida que la solución alcance el objetivo.
        """
        _init_state = [[1, -1, 1],
                       [-1, 0, -1],
                       [1, -1, 1]]
        _goal_state = [[-1, 1, -1],
                       [1, 0, 1],
                       [-1, 1, -1]]

        tablero = Tablero(_init_state, _goal_state)

        # Probar cambiar_color individualmente
        estado_intermedio = tablero.cambiar_color(dp(_init_state), 0, 0)
        expected_intermedio =  [[-1, 1, 1],
                                [1, 0, -1],
                                [1, -1, 1]]
        self.assertEqual(estado_intermedio, expected_intermedio)

        # Probar aplicar_cambios con múltiples cambios
        cambios = [(0, 0), (0, 2), (1, 0), (1, 2), (2, 0), (2, 2)]
        estado_final = tablero.aplicar_cambios(cambios)

        # Matriz esperada después de aplicar todos los cambios
        expected_final = [[1, -1, 1],
                          [1, 0, 1],
                          [1, -1, 1]]
        self.assertEqual(estado_final, expected_final)

        # Verificar que el estado inicial no se modificó
        self.assertEqual(tablero.inicio, _init_state)

        # Validar que los cambios alcanzan el objetivo
        cambios_adicionales = [(0, 1), (2, 1)]
        es_valido = tablero.validar_solucion((cambios + cambios_adicionales))
        self.assertTrue(es_valido)

    @timeout(N_SECOND)
    def test_01_integracion_dccolores_cargar_encontrar_optimizar(self):
        """
        Integración de DCColores + cargar_tablero + encontrar_solucion + optimizar_solucion.
        Se carga un tablero, se encuentra una solución con cambios adicionales,
        y se optimiza la solución eliminando redundancias.
        """
        juego = DCColores()

        # Cargar un tablero específico
        juego.cargar_tablero("tablero_2")
        n_tableros = len(juego.tableros)
        tablero_actual = juego.tableros[n_tableros - 1]

        # Configurar cambios iniciales
        cambios_iniciales = [(0, 1), (1, 0)]

        # Encontrar solución con cambios adicionales
        solucion = tablero_actual.encontrar_solucion(cambios_iniciales, 7)
        self.assertIsNotNone(solucion)
        self.assertGreater(len(solucion), len(cambios_iniciales))

        # Optimizar la solución
        solucion_optimizada = tablero_actual.optimizar_solucion(solucion)

        # Verificar que la solución optimizada es válida
        es_valida = tablero_actual.validar_solucion(solucion_optimizada)
        self.assertTrue(es_valida)

        # Verificar que la optimización no aumentó el número de cambios
        self.assertLessEqual(len(solucion_optimizada), len(solucion))

    @timeout(N_SECOND)
    def test_02_integracion_tablero_aplicar_encontrar_validar(self):
        """
        Integración de Tablero + aplicar_cambios + encontrar_solucion + validar_solucion.
        Se aplican cambios, se busca solución adicional y se valida el resultado completo.
        """
        _init_state =  [[-1, 1, -1, 1],
                        [1, -1, 1, -1],
                        [-1, 1, -1, 1]]
        _goal_state = [[1, -1, 1, -1],
                        [-1, 1, -1, 1],
                        [1, -1, 1, -1]]

        tablero = Tablero(_init_state, _goal_state)
        cambios_base = [(0, 1), (1, 0), (1, 2), (2, 1)]

        # Encontrar solución adicional para alcanzar el objetivo
        solucion_completa = tablero.encontrar_solucion(cambios_base, 10)
        self.assertIsNotNone(solucion_completa)

        # Validar que la solución completa alcanza el objetivo
        es_valida = tablero.validar_solucion(solucion_completa)
        self.assertTrue(es_valida)

        # Verificar que el estado final coincide con el objetivo
        estado_final = tablero.aplicar_cambios(solucion_completa)
        self.assertEqual(estado_final, _goal_state)
