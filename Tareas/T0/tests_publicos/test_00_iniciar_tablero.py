import unittest

from tablero import Tablero
from tests_publicos.timeout_function import timeout


N_SECOND = 1

class TestInicializarClaseTablero(unittest.TestCase):

    def shortDescription(self):
        doc = self.__doc__
        return doc if doc else None

    @timeout(N_SECOND)
    def test_00_tablero_cuadrado_3x3(self):
        """
        Tablero de 3x3, se verifica que el objeto de la clase Tablero
        haya sido creado correctamente, según lo pedido por el enunciado.
        """
        _init_state = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
        _goal_state = [[0, 1, 0], [-1, 0, -1], [0, 1, 0]]

        tablero = Tablero(_init_state, _goal_state)

        self.assertEqual(tablero.inicio, _init_state)
        self.assertEqual(tablero.meta, _goal_state)

    @timeout(N_SECOND)
    def test_01_tablero_rectangular_10x3(self):
        """
        Tablero de 10x3, se verifica que el objeto de la clase Tablero
        haya sido creado correctamente, según lo pedido por el enunciado.
        """
        _init_state = [[0, 1, 0], [1, 0, 1], [0, 1, 0], [1, 1, 1], [0, 0, 0],
                       [1, 0, 1], [0, 1, 0], [1, 1, 0], [0, 0, 1], [1, 1, 1]]
        _goal_state = [[0, 1, 0], [-1, 0, -1], [0, 1, 0], [-1, -1, -1], [0, 0, 0],
                       [-1, 0, -1], [0, 1, 0], [-1, -1, 0], [0, 0, -1], [-1, -1, -1]]

        tablero = Tablero(_init_state, _goal_state)

        self.assertEqual(tablero.inicio, _init_state)
        self.assertEqual(tablero.meta, _goal_state)
