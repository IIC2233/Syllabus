import unittest

from tablero import Tablero
from tests_publicos.timeout_function import timeout


N_SECOND = 1

class TestEncontrarSolucion(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc if doc else None

    @timeout(N_SECOND)
    def test_00_cero_modificaciones_adicionales_true(self):
        """
        Verificar que se retorna la lista de cambios cuando no hay posibilidad
        de modificaciones adicionales y el estado actual es igual al objetivo.
        """
        _init_state =  [[-1, -1, -1, 1, 1],
                        [-1, 1, -1, 1, -1],
                        [1, 0, -1, 1, 1]]

        _goal_state =  [[1, -1, -1, -1, 1],
                        [-1, -1, -1, -1, -1],
                        [1, 0, 1, 1, 1]]

        board = Tablero(_init_state, _goal_state)

        change_list = [(2, 0), (1, 1), (0, 2)]

        max_changes = 0

        result = board.encontrar_solucion(change_list, max_changes)

        expected = [(2, 0), (1, 1), (0, 2)]

        self.assertIsNotNone(result)
        self.assertCountEqual(result, expected)

    @timeout(N_SECOND)
    def test_01_una_modificacion_con_solucion(self):
        """
        Verificar que se retorna la lista de cambios cuando hay una modificación
        adicional y el estado objetivo es alcanzable.
        """
        _init_state =  [[-1, -1, -1],
                        [-1, 1, -1],
                        [-1, 0, -1]]

        _goal_state =  [[1, -1, -1],
                        [-1, -1, -1],
                        [-1, 0, 1]]

        board = Tablero(_init_state, _goal_state)

        change_list = [(2, 0), (1, 1)]

        max_changes = 1

        result = board.encontrar_solucion(change_list, max_changes)

        expected = [(2, 0), (1, 1), (0, 2)]

        self.assertIsNotNone(result)
        self.assertCountEqual(result, expected)

    @timeout(N_SECOND)
    def test_02_una_modificacion_sin_solucion(self):
        """
        Verificar que se retorna una lista vacía cuando hay una modificación
        adicional y el estado objetivo no es alcanzable.
        """
        _init_state =  [[-1, -1, -1, 1, 1],
                        [-1, 1, -1, 1, -1],
                        [0, 0, -1, 1, 1]]

        _goal_state =  [[1, -1, -1, -1, 1],
                        [-1, -1, -1, 1, -1],
                        [0, 0, 1, -1, -1]]

        board = Tablero(_init_state, _goal_state)

        change_list = [(2, 0), (1, 1), (0, 2)]

        max_changes = 1

        result = board.encontrar_solucion(change_list, max_changes)

        expected = []

        self.assertIsNotNone(result)
        self.assertListEqual(result, expected)

    @timeout(N_SECOND)
    def test_03_dos_modificaciones_con_solucion(self):
        """
        Verificar que se retorna la lista de cambios cuando hay dos modificaciones
        adicionales y el estado objetivo es alcanzable.
        """
        _init_state =  [[-1, -1, -1, 1, 1],
                        [-1, 1, -1, 1, -1],
                        [-1, 0, -1, 1, 1]]

        _goal_state =  [[-1, 1, -1, 1, -1],
                        [1, 1, -1, 1, 1],
                        [-1, 0, 1, 1, 1]]

        board = Tablero(_init_state, _goal_state)

        change_list = [(2, 0), (1, 1), (0, 2)]

        max_changes = 2

        result = board.encontrar_solucion(change_list, max_changes)

        expected = [(2, 0), (1, 1), (0, 2), (0, 0), (0, 4)]

        self.assertIsNotNone(result)
        self.assertCountEqual(result, expected)

    @timeout(N_SECOND)
    def test_04_dos_modificaciones_tres_necesarias(self):
        """
        Verificar que se retorna una lista vacía cuando hay dos modificaciones
        adicionales y el estado objetivo no es alcanzable con solo 2 cambios.
        """

        _init_state =  [[-1, -1, -1, 1, 1],
                        [-1, 1, -1, 1, -1],
                        [0, 0, -1, 1, 1],
                        [1, -1, 1, 0, 1]]

        _goal_state =  [[1, -1, -1, 1, -1],
                        [-1, -1, -1, 1, 1],
                        [0, 0, 1, -1, -1],
                        [1, -1, 1, 0, -1]]

        board = Tablero(_init_state, _goal_state)

        change_list = [(2, 0), (1, 1), (0, 2)]

        max_changes = 2

        result = board.encontrar_solucion(change_list, max_changes)

        expected = []

        self.assertIsNotNone(result)
        self.assertListEqual(result, expected)
