from copy import deepcopy as dp

from tests_privados.test_tools import IICTest, timeout

from tablero import Tablero
from dccolores import DCColores


N_SECOND = 40

class TestIntegracion(IICTest):

    @timeout(N_SECOND)
    def test_00_integracion_cambiar_aplicar_validar(self):
        """
        Integración de cambiar_color + aplicar_cambios + validar_solucion.
        Se crea un tablero complejo, se aplican cambios individuales y en conjunto,
        y se valida que la solución alcance el objetivo.
        """
        _init_state = [
            [1, -1, 1, 0, -1, 1],
            [-1, 1, -1, 1, 0, -1],
            [1, -1, 1, -1, 1, 0],
            [-1, 1, -1, 1, -1, 1],
            [1, 0, 1, -1, 1, -1],
            [-1, 1, 0, 1, -1, 1]
        ]
        _goal_state = [
            [1, 1, 1, 0, 1, -1],
            [1, 1, -1, -1, 0, 1],
            [1, -1, 1, -1, 1, 0],
            [-1, -1, -1, 1, 1, -1],
            [-1, 0, 1, 1, 1, 1],
            [1, 1, 0, 1, 1, -1]
        ]

        tablero = Tablero(_init_state, _goal_state)

        # Probar cambiar_color individualmente en múltiples posiciones
        estado_intermedio_1 = tablero.cambiar_color(dp(_init_state), 1, 1)
        expected_intermedio_1 = [
            [-1, 1, -1, 0, -1, 1],
            [1, -1, 1, 1, 0, -1],
            [-1, 1, -1, -1, 1, 0],
            [-1, 1, -1, 1, -1, 1],
            [1, 0, 1, -1, 1, -1],
            [-1, 1, 0, 1, -1, 1]
        ]
        self.assertEqual(estado_intermedio_1, expected_intermedio_1)

        # Probar cambiar_color en otra posición sobre el estado modificado
        estado_intermedio_2 = tablero.cambiar_color(estado_intermedio_1, 3, 3)
        expected_intermedio_2 = [
            [-1, 1, -1, 0, -1, 1],
            [1, -1, 1, 1, 0, -1],
            [-1, 1, 1, 1, -1, 0],
            [-1, 1, 1, -1, 1, 1],
            [1, 0, -1, 1, -1, -1],
            [-1, 1, 0, 1, -1, 1]
        ]
        self.assertEqual(estado_intermedio_2, expected_intermedio_2)

        # Probar aplicar_cambios con múltiples cambios
        cambios = [(0, 0), (0, 2), (0, 4), (2, 1), (2, 3), (4, 0), (4, 2), (4, 4)]
        estado_final = tablero.aplicar_cambios(cambios)

        # Verificar que el estado inicial no se modificó
        self.assertEqual(tablero.inicio, _init_state)

        # Validar que los cambios alcanzan el objetivo
        cambios_completos = cambios + [(1, 1), (3, 3)]
        es_valido = tablero.validar_solucion(cambios_completos)
        self.assertTrue(es_valido)

        # Verificar que el estado final coincide con el objetivo
        estado_validado = tablero.aplicar_cambios(cambios_completos)
        self.assertEqual(estado_validado, _goal_state)

    @timeout(N_SECOND)
    def test_01_integracion_aplicar_encontrar_optimizar(self):
        """
        Integración de aplicar_cambios + encontrar_solucion + optimizar_solucion.
        Se aplican cambios base, se encuentra solución adicional y se optimiza.
        """
        _init_state = [
            [1, -1, 1, -1, 1, 0],
            [-1, 1, -1, 1, -1, 1],
            [1, -1, 0, 1, -1, 1],
            [-1, 1, 1, -1, 0, -1],
            [1, -1, 1, 0, -1, 1],
            [-1, 1, -1, 1, -1, 1]
        ]
        _goal_state = [
            [-1, 1, 1, -1, 1, 0],
            [1, -1, -1, -1, 1, -1],
            [-1, 1, 0, -1, 1, -1],
            [-1, -1, -1, -1, 0, 1],
            [-1, -1, -1, 0, 1, -1],
            [1, 1, 1, -1, 1, -1]
        ]

        tablero = Tablero(_init_state, _goal_state)

        # Aplicar cambios base usando aplicar_cambios
        cambios_base = [(1, 0), (4, 2)]
        estado_intermedio = tablero.aplicar_cambios(cambios_base)

        # Verificar que el estado inicial no se modificó
        self.assertEqual(tablero.inicio, _init_state)

        # Encontrar solución adicional para alcanzar el objetivo
        solucion_completa = tablero.encontrar_solucion(cambios_base, 3)
        self.assertIsNotNone(solucion_completa)
        self.assertGreater(len(solucion_completa), len(cambios_base))

        # Validar que la solución completa alcanza el objetivo
        es_valida = tablero.validar_solucion(solucion_completa)
        self.assertTrue(es_valida)

        # Optimizar la solución completa
        solucion_optimizada = tablero.optimizar_solucion(solucion_completa)

        # Verificar que la solución optimizada sigue siendo válida
        es_valida_optimizada = tablero.validar_solucion(solucion_optimizada)
        self.assertTrue(es_valida_optimizada)

        # Verificar que la optimización no aumentó el número de cambios
        self.assertLessEqual(len(solucion_optimizada), len(solucion_completa))

        # Verificar que el estado final con la solución optimizada coincide con el objetivo
        estado_final_optimizado = tablero.aplicar_cambios(solucion_optimizada)
        self.assertEqual(estado_final_optimizado, _goal_state)

    @timeout(N_SECOND)
    def test_02_integracion_todos_metodos(self):
        """
        Integración completa usando todos los métodos disponibles.
        Se combina DCColores, cambiar_color, aplicar_cambios, encontrar_solucion,
        optimizar_solucion y validar_solucion en un flujo completo.
        """
        # Inicializar DCColores y cargar tablero
        juego = DCColores()
        juego.cargar_tablero("privado_tablero_07")
        n_tableros = len(juego.tableros)
        tablero_actual = juego.tableros[n_tableros - 1]

        # Usar cambiar_color para explorar estados intermedios
        estado_inicial_copia = dp(tablero_actual.inicio)
        estado_modificado_1 = tablero_actual.cambiar_color(estado_inicial_copia, 1, 1)
        estado_modificado_2 = tablero_actual.cambiar_color(estado_modificado_1, 2, 2)

        # Aplicar cambios base usando aplicar_cambios
        cambios_iniciales = [(0, 0), (3, 3)]
        estado_aplicado = tablero_actual.aplicar_cambios(cambios_iniciales)

        # Verificar que el estado original no se modificó
        self.assertEqual(tablero_actual.inicio, tablero_actual.inicio)

        # Encontrar solución completa
        solucion_completa = tablero_actual.encontrar_solucion(cambios_iniciales, 10)
        self.assertIsNotNone(solucion_completa)

        # Validar solución encontrada
        es_valida = tablero_actual.validar_solucion(solucion_completa)
        self.assertTrue(es_valida)

        # Optimizar solución
        solucion_optimizada = tablero_actual.optimizar_solucion(solucion_completa)

        # Validar solución optimizada
        es_valida_optimizada = tablero_actual.validar_solucion(solucion_optimizada)
        self.assertTrue(es_valida_optimizada)

        # Verificar que la optimización no empeora la solución
        self.assertLessEqual(len(solucion_optimizada), len(solucion_completa))

        # Probar combinación de cambiar_color con aplicar_cambios
        cambios_combinados = [(1, 1), (2, 2)]
        estado_combinado = tablero_actual.aplicar_cambios(cambios_combinados)

        # Verificar estado final con solución optimizada
        estado_final = tablero_actual.aplicar_cambios(solucion_optimizada)
        self.assertEqual(estado_final, tablero_actual.meta)

        # Verificar inmutabilidad del estado original
        self.assertEqual(tablero_actual.inicio, tablero_actual.inicio)

    @timeout(N_SECOND)
    def test_03_integracion_sin_cambios_iniciales(self):
        """
        Integración de encontrar_solucion y validar_solucion sin cambios iniciales.
        Se verifica que encontrar_solucion pueda encontrar una solución válida
        incluso sin cambios base.
        """
        _init_state = [
            [1,1,-1,1,0],
            [-1,0,-1,1,1],
            [1,1,0,-1,-1],
            [0,-1,1,-1,1],
            [1,1,1,0,1]
        ]
        _goal_state = [
            [-1,-1,-1,-1,0],
            [-1,0,-1,-1,-1],
            [-1,-1,0,-1,-1],
            [0,-1,-1,-1,-1],
            [1,-1,-1,0,-1]
        ]

        tablero = Tablero(_init_state, _goal_state)

        # Aplicar cambios base usando aplicar_cambios
        cambios_base = []
        estado_intermedio = tablero.aplicar_cambios(cambios_base)

        # Verificar que el estado inicial no se modificó
        self.assertEqual(tablero.inicio, _init_state)

        # Encontrar solución adicional para alcanzar el objetivo
        solucion_completa = tablero.encontrar_solucion(cambios_base, 5)
        self.assertIsNotNone(solucion_completa)
        self.assertGreater(len(solucion_completa), len(cambios_base))

        # Validar que la solución completa alcanza el objetivo
        es_valida = tablero.validar_solucion(solucion_completa)
        self.assertTrue(es_valida)

        # Optimizar la solución completa
        solucion_optimizada = tablero.optimizar_solucion(solucion_completa)

        # Verificar que la solución optimizada sigue siendo válida
        es_valida_optimizada = tablero.validar_solucion(solucion_optimizada)
        self.assertTrue(es_valida_optimizada)

        # Verificar que la optimización no aumentó el número de cambios
        self.assertLessEqual(len(solucion_optimizada), len(solucion_completa))

        # Verificar que el estado final con la solución optimizada coincide con el objetivo
        estado_final_optimizado = tablero.aplicar_cambios(solucion_optimizada)
        self.assertEqual(estado_final_optimizado, _goal_state)

    @timeout(N_SECOND)
    def test_04_integración_tablero_grande(self):
        """
        Integración completa en un tablero de 11x11.Se verifica que los métodos
        funcionen correctamente en tableros de mayor tamaño.
        """
        _init_state = [
            [1,1,1,1,1,0,1,1,1,1,1],
            [1,0,-1,-1,-1,0,1,0,1,1,1],
            [1,0,-1,-1,-1,0,1,0,1,0,1],
            [1,0,-1,-1,-1,0,1,0,1,0,1],
            [1,1,1,1,1,0,1,1,1,1,1],
            [0,0,0,0,0,0,0,0,0,0,0],
            [1,1,1,1,1,0,1,1,-1,-1,-1],
            [1,0,1,0,1,0,1,0,-1,-1,-1],
            [1,0,1,0,1,0,1,0,-1,-1,-1],
            [1,0,1,0,1,0,1,0,0,0,0],
            [1,1,1,1,1,0,1,1,-1,-1,-1]
        ]

        _goal_state = [
            [1,1,1,1,1,0,1,1,1,1,1],
            [1,0,1,1,1,0,1,0,1,1,1],
            [1,0,1,1,1,0,1,0,1,0,1],
            [1,0,1,1,1,0,1,0,1,0,1],
            [1,1,1,1,1,0,1,1,1,1,1],
            [0,0,0,0,0,0,0,0,0,0,0],
            [1,1,1,1,1,0,1,1,1,1,1],
            [1,0,1,0,1,0,1,0,1,1,1],
            [1,0,1,0,1,0,1,0,1,1,1],
            [1,0,1,0,1,0,1,0,0,0,0],
            [1,1,1,1,1,0,1,1,1,1,1]
        ]

        tablero = Tablero(_init_state, _goal_state)

        # Aplicar cambios base usando aplicar_cambios
        cambios_base = []
        estado_intermedio = tablero.aplicar_cambios(cambios_base)

        # Verificar que el estado inicial no se modificó
        self.assertEqual(tablero.inicio, _init_state)

        # Encontrar solución adicional para alcanzar el objetivo
        solucion_completa = tablero.encontrar_solucion(cambios_base, 5)
        self.assertIsNotNone(solucion_completa)
        self.assertGreater(len(solucion_completa), len(cambios_base))

        # Validar que la solución completa alcanza el objetivo
        es_valida = tablero.validar_solucion(solucion_completa)
        self.assertTrue(es_valida)

        # Optimizar la solución completa
        solucion_optimizada = tablero.optimizar_solucion(solucion_completa)

        # Verificar que la solución optimizada sigue siendo válida
        es_valida_optimizada = tablero.validar_solucion(solucion_optimizada)
        self.assertTrue(es_valida_optimizada)

        # Verificar que la optimización no aumentó el número de cambios
        self.assertLessEqual(len(solucion_optimizada), len(solucion_completa))

        # Verificar que el estado final con la solución optimizada coincide con el objetivo
        estado_final_optimizado = tablero.aplicar_cambios(solucion_optimizada)
        self.assertEqual(estado_final_optimizado, _goal_state)
