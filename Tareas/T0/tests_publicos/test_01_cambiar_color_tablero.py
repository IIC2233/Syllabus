import unittest

from tablero import Tablero
from tests_publicos.timeout_function import timeout


N_SECOND = 1

class TestCambiarColorTablero(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc if doc else None

    @timeout(N_SECOND)
    def test_00_tablero_3x4(self):
        """
        Tablero de 3x4, verifica que el método cambiar de color de Tablero
        funcione correctamente según el enunciado.
        """
        _init_state = [[-1, 1, -1, 0], [1, -1, 1, -1], [0, 1, -1, 1]]
        _goal_state = [[-1, 1, -1, 0], [1, -1, 1, -1], [0, 1, -1, 1]]

        _after_change = [[1, -1, 1, 0], [-1, 1, -1, -1], [0, -1, 1, 1]]

        tablero = Tablero(_init_state, _goal_state)
        dsp_1_cambio = tablero.cambiar_color(tablero.inicio, 1, 1)

        self.assertEqual(_after_change, dsp_1_cambio)

        # Inverso: debería ser el inicial de nuevo
        dsp_2_cambio = tablero.cambiar_color(dsp_1_cambio, 1, 1)
        self.assertEqual(_init_state, dsp_2_cambio)

    @timeout(N_SECOND)
    def test_01_tablero_10x3(self):
        """
        Tablero de 10x3, verifica que el método cambiar de color de Tablero
        funcione correctamente según el enunciado.
        """
        _init_state = [[1, 0, -1], [-1, 1, 1], [1, -1, -1], [0, 1, -1], [-1, 1, -1],
                       [0, 1, -1], [1, -1, -1], [0, 1, 0], [0, -1, -1], [0, -1, -1]]
        _goal_state = [[0] * 3 for _ in range(10)]
        _after_change = [[1, 0, -1], [-1, 1, 1], [1, -1, -1], [0, -1, 1], [1, -1, 1],
                         [0, -1, 1], [1, -1, -1], [0, 1, 0], [0, -1, -1], [0, -1, -1]]

        tablero = Tablero(_init_state, _goal_state)
        comparar = tablero.cambiar_color(_init_state, 4, 1)
        self.assertEqual(comparar, _after_change)

    @timeout(N_SECOND)
    def test_02_tablero_esquina(self):
        """
        Tablero de 2x2, verifica que el método cambiar de color de Tablero
        funcione correctamente según el enunciado.
        """
        _init_state = [[1, -1], [1, 1]]
        _goal_state = [[0, 0], [0, 0]]

        _after_change = [[-1, 1], [-1, -1]]

        tablero = Tablero(_init_state, _goal_state)
        comparar = tablero.cambiar_color(_init_state, 0, 0)

        self.assertEqual(comparar, _after_change)

    @timeout(N_SECOND)
    def test_03_tablero_3x3_diagonales(self):
        """
        Tablero de 3x3 con celdas fijas (0), verifica que el método cambiar
        de color de Tablero funcione correctamente según el enunciado.
        """
        _init_state = [[0, 1, 0], [1, -1, 1], [0, 1, 0]]
        _goal_state = [[0] * 3 for _ in range(3)]

        _after_change = [[0, -1, 0], [-1, 1, -1], [0, -1, 0]]

        tablero = Tablero(_init_state, _goal_state)
        comparar = tablero.cambiar_color(_init_state, 1, 1)

        self.assertEqual(comparar, _after_change)

    @timeout(N_SECOND)
    def test_04_tablero_3x2_lateral(self):
        """
        Tablero de 3x2, verifica que el método cambiar de color de Tablero
        funcione correctamente según el enunciado.
        """
        _init_state = [[1, 1], [-1, -1], [1, 1]]
        _goal_state = [[0, 0], [0, 0], [0, 0]]

        _after_change = [[-1, -1], [1, 1], [-1, -1]]

        tablero = Tablero(_init_state, _goal_state)
        comparar = tablero.cambiar_color(_init_state, 1, 0)

        self.assertEqual(comparar, _after_change)

    @timeout(N_SECOND)
    def test_05_tablero_4x5_vacio(self):
        """
        Tablero de 4x5 bloqueado, verifica que el método cambiar de color de
        Tablero funcione correctamente según el enunciado.
        """
        _init_state = [[0] * 5 for _ in range(4)]
        _goal_state = [[0] * 5 for _ in range(4)]

        _after_change = [[0] * 5 for _ in range(4)]

        tablero = Tablero(_init_state, _goal_state)
        comparar = tablero.cambiar_color(_init_state, 1, 1)

        self.assertEqual(comparar, _after_change)
