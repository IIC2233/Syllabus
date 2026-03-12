import unittest

from tablero import Tablero
from tests_publicos.timeout_function import timeout


N_SECOND = 1

class TestValidarSolucion(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc if doc else None

    @timeout(N_SECOND)
    def test_00_lista_vacia(self):
        """
        Se verifica que al validar la solución con una lista vacía
        de modificaciones el método entregue False como resultado.
        """
        _init_state =  [[-1, -1, -1, 1, 1],
                        [-1, 1, -1, 1, -1],
                        [0, 0, -1, 1, 1]]

        _goal_state =  [[-1, -1, -1, 1, 1],
                        [-1, 1, -1, 1, -1],
                        [0, 0, -1, 0, 1]]

        board = Tablero(_init_state, _goal_state)

        change_list = []

        expected = False

        result = board.validar_solucion(change_list)

        self.assertIsNotNone(result)
        self.assertEqual(result, expected)

    @timeout(N_SECOND)
    def test_01_lista_logra_objetivo_un_cambio(self):
        """
        Se verifica que al validar la solución con una lista con solo una
        modificación con la  que se llega al objetivo el método entregue True.
        """

        _init_state =  [[-1, -1, -1, 1, 1],
                        [-1, 1, -1, 1, -1],
                        [0, 0, -1, 1, 1]]

        _goal_state =  [[-1, -1, -1, -1, -1],
                        [-1, 1, -1, -1, 1],
                        [0, 0, -1, 1, 1]]

        board = Tablero(_init_state, _goal_state)

        change_list = [(0, 4)]

        expected = True

        result = board.validar_solucion(change_list)

        self.assertIsNotNone(result)
        self.assertEqual(result, expected)

    @timeout(N_SECOND)
    def test_02_lista_no_logra_objetivo_un_cambio(self):
        """
        Se verifica que al validar la solución con una lista con solo una
        modificación con la  que no se llega al objetivo el método entregue False.
        """
        _init_state =  [[-1, -1],
                        [-1, 1]]

        _goal_state =  [[-1, -1],
                        [-1, 1]]

        board = Tablero(_init_state, _goal_state)

        change_list = [(0, 1)]

        expected = False

        result = board.validar_solucion(change_list)

        self.assertIsNotNone(result)
        self.assertEqual(result, expected)

    @timeout(N_SECOND)
    def test_03_lista_logra_objetivo_multiples_cambios(self):
        """
        Se verifica que al validar la solución con una lista con múltiples 
        modificaciones con las que se llega al objetivo el método entregue True.
        """
        _init_state =  [[-1, -1, -1, 1, 1],
                        [-1, 1, -1, 1, -1],
                        [0, 0, -1, 1, 1]]

        _goal_state =  [[1, 1, -1, -1, -1],
                        [1, -1, 1, 1, -1],
                        [0, 0, 1, -1, -1]]

        board = Tablero(_init_state, _goal_state)

        change_list = [(0, 4), (0, 0), (2, 3)]

        expected = True

        result = board.validar_solucion(change_list)

        self.assertIsNotNone(result)
        self.assertEqual(result, expected)

    @timeout(N_SECOND)
    def test_04_lista_no_logra_objetivo_multiples_cambios(self):
        """
        Se verifica que al validar la solución con una lista con múltiples
        modificaciones con las  que no se llega al objetivo el método entregue False.
        """
        _init_state =  [[-1, -1, -1, 1, 1, 0],
                        [-1, 1, 1, 1, -1, -1],
                        [0, 0, -1, -1, 1, 1],
                        [-1, 1, -1, 1, 1, 0],
                        [0, 1, -1, 1, 1, 1]]

        _goal_state =  [[-1, 1, 1, -1, -1, 0],
                        [-1, 1, 1, 1, -1, -1],
                        [0, 0, -1, 1, 1, 1],
                        [-1, 1, -1, 1, 1, 0],
                        [0, -1, -1, 1, 1, -1]]

        board = Tablero(_init_state, _goal_state)

        change_list = [(0, 4), (0, 0), (2, 3), (2, 0), (2, 1)]

        expected = False

        result = board.validar_solucion(change_list)

        self.assertIsNotNone(result)
        self.assertEqual(result, expected)
