import unittest

from tablero import Tablero
from tests_publicos.timeout_function import timeout


N_SECOND = 1

class TestOptimizarSolucion(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc if doc else None

    @timeout(N_SECOND)
    def test_00_lista_vacia(self):
        """
        Verificar que se retorna una lista vacía cuando la solución inicial está vacía.
        """
        _init_state =  [[0, -1, 1, 0],
                        [-1, 1, -1, 1],
                        [0, 1, 1, -1],
                        [1, 0, -1, -1]]

        _goal_state =  [[0, -1, 1, 0],
                        [1, 1, -1, -1],
                        [0, 1, 1, 1],
                        [-1, 0, -1, -1]]

        board = Tablero(_init_state, _goal_state)

        solution = []

        result = board.optimizar_solucion(solution)

        expected = []

        self.assertIsNotNone(result)
        self.assertListEqual(result, expected)

    @timeout(N_SECOND)
    def test_01_no_redundancia(self):
        """
        Verificar que no se eliminan movimientos que no son redundantes.
        """
        _init_state =  [[0, -1, 1, 0],
                        [-1, 1, -1, 1],
                        [0, 1, 1, -1],
                        [1, 0, -1, -1]]

        _goal_state =  [[0, -1, 1, 0],
                        [1, 1, -1, -1],
                        [0, 1, 1, 1],
                        [-1, 0, -1, -1]]

        board = Tablero(_init_state, _goal_state)

        solution = [(1, 0), (0, 1), (2, 3), (1, 1)]

        result = board.optimizar_solucion(solution)

        expected = [(1, 0), (0, 1), (2, 3), (1, 1)]

        self.assertIsNotNone(result)
        self.assertListEqual(result, expected)

    @timeout(N_SECOND)
    def test_02_redundancia_par(self):
        """
        Verificar que se eliminan movimientos redundantes cuando la cantidad de
        apariciones de la modificación redundante es par.
        """
        _init_state =  [[0, -1, 1, 0],
                        [-1, 1, -1, 1],
                        [0, 1, 1, -1],
                        [1, 0, -1, -1]]

        _goal_state =  [[0, -1, 1, 0],
                        [1, 1, -1, -1],
                        [0, 1, 1, 1],
                        [-1, 0, -1, -1]]

        board = Tablero(_init_state, _goal_state)

        solution = [(0, 1), (1, 0), (0, 1), (2, 3), (0, 1), (1, 1), (2, 0), (0, 1)]

        result = board.optimizar_solucion(solution)

        expected = [(1, 0), (2, 3), (1, 1), (2, 0)]

        self.assertIsNotNone(result)
        self.assertListEqual(result, expected)

    @timeout(N_SECOND)
    def test_03_redundancia_impar(self):
        """
        Verificar que se eliminan movimientos redundantes cuando la cantidad de
        apariciones de la modificación redundante es impar.
        """
        _init_state =  [[0, -1, 1, 0],
                        [-1, 1, -1, 1],
                        [0, 1, 1, -1],
                        [1, 0, -1, -1]]

        _goal_state =  [[0, -1, 1, 0],
                        [1, 1, -1, -1],
                        [0, 1, 1, 1],
                        [-1, 0, -1, -1]]

        board = Tablero(_init_state, _goal_state)

        solution = [(1, 0), (2, 3), (0, 1), (2, 3), (1, 1), (3, 3), (2, 2), (2, 3)]

        result = board.optimizar_solucion(solution)

        expected = [(1, 0), (0, 1), (1, 1), (3, 3), (2, 2), (2, 3)]

        self.assertIsNotNone(result)
        self.assertListEqual(result, expected)

    @timeout(N_SECOND)
    def test_04_multiple_redundancia(self):
        """
        Verificar que se eliminan múltiples movimientos redundantes, incluyendo
        casos pares e impares.
        """
        _init_state =  [[0, -1, 1, 0],
                        [-1, 1, -1, 1],
                        [0, 1, 1, -1],
                        [1, 0, -1, -1]]

        _goal_state =  [[0, -1, 1, 0],
                        [1, 1, -1, -1],
                        [0, 1, 1, 1],
                        [-1, 0, -1, -1]]

        board = Tablero(_init_state, _goal_state)

        solution = [(1, 0), (1, 1), (2, 3), (0, 1), (2, 3), (1, 1), (3, 3), (2, 2), (2, 3)]

        result = board.optimizar_solucion(solution)

        expected = [(1, 0), (0, 1), (3, 3), (2, 2), (2, 3)]

        self.assertIsNotNone(result)
        self.assertListEqual(result, expected)
