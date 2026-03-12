import unittest
from copy import deepcopy as dp

from tablero import Tablero
from tests_publicos.timeout_function import timeout


N_SECOND = 1

class TestAplicarCambiosTablero(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc if doc else None

    @timeout(N_SECOND)
    def test_00_cambios_3x3_unico(self):
        """
        Se verifica que la lista de cambios a aplicar sea aplicada correctamente
        sin modificar algunos de los atributos iniciales de la clase Tablero,
        según lo pedido por el enunciado.
        """
        init_state = [[0, 1, 0],
                       [1, 0, 1],
                       [0, 1, 0]]
        goal_state = [[0, 1, 0], [-1, 0, -1], [0, 1, 0]]

        expected_state = [[0, -1, 0],
                           [-1, 0, 1],
                           [0, -1, 0]]

        cpinit_state = dp(init_state)
        tablero = Tablero(init_state, goal_state)
        cambios: list[tuple[int, int]] = [(1, 0)]

        nuevo_tablero = tablero.aplicar_cambios(cambios)

        self.assertEqual(expected_state, nuevo_tablero)
        self.assertEqual(cpinit_state, tablero.inicio)

    @timeout(N_SECOND)
    def test_01_cambios_secuenciales_4x4(self):
        """
        Se verifica que la lista de cambios a aplicar sea aplicada correctamente
        sin modificar algunos de los atributos iniciales de la clase Tablero,
        según lo pedido por el enunciado.
        """
        init_state = [[ 1,  1,  1,  1],
                       [ 1, -1, -1,  1],
                       [ 1, -1, -1,  1],
                       [ 1,  1,  1,  1]]
        goal_state = [[0] * 4 for _ in range(4)]

        expected_state = [[-1, -1, -1,  1],
                           [-1, -1, -1, -1],
                           [-1, -1, -1, -1],
                           [ 1, -1, -1, -1]]

        cpinit_state = dp(init_state)
        tablero = Tablero(init_state, goal_state)
        cambios: list[tuple[int, int]] = [(1, 1), (2, 2)]

        nuevo_tablero = tablero.aplicar_cambios(cambios)

        self.assertEqual(expected_state, nuevo_tablero)
        self.assertEqual(cpinit_state, tablero.inicio)

    @timeout(N_SECOND)
    def test_02_cambios_con_ceros(self):
        """
        Se verifica que la lista de cambios a aplicar sea aplicada correctamente
        sin modificar algunos de los atributos iniciales de la clase Tablero,
        según lo pedido por el enunciado.
        """
        init_state = [[ 0,  1,  1,  1,  0],
                       [ 1,  0, -1,  0,  1],
                       [ 0,  1,  1,  1,  0]]
        goal_state = [[0] * 5 for _ in range(3)]

        expected_state = [[ 0, -1, -1, -1,  0],
                          [-1,  0,  1,  0, -1],
                          [ 0,  1,  1, -1,  0]]

        cpinit_state = dp(init_state)
        tablero = Tablero(init_state, goal_state)
        cambios: list[tuple[int, int]] = [(0, 1), (1, 4), (2, 2), (2, 2)]

        nuevo_tablero = tablero.aplicar_cambios(cambios)

        self.assertEqual(expected_state, nuevo_tablero)
        self.assertEqual(cpinit_state, tablero.inicio)

    @timeout(N_SECOND)
    def test_03_cambios_unidimensional_1x6(self):
        """
        Se verifica que la lista de cambios a aplicar sea aplicada correctamente
        sin modificar algunos de los atributos iniciales de la clase Tablero,
        según lo pedido por el enunciado.
        """
        init_state = [[1, -1, 1, -1, 1, -1]]
        goal_state = [[0] * 6]

        expected_state = [[1, 1, 1, -1, -1, -1]]

        cpinit_state = dp(init_state)
        tablero = Tablero(init_state, goal_state)
        cambios: list[tuple[int, int]] = [(0, 2), (0, 3)]

        nuevo_tablero = tablero.aplicar_cambios(cambios)

        self.assertEqual(expected_state, nuevo_tablero)
        self.assertEqual(cpinit_state, tablero.inicio)

    @timeout(N_SECOND)
    def test_04_cambios_reversibles_5x2(self):
        """
        Se verifica que la lista de cambios a aplicar sea aplicada correctamente
        sin modificar algunos de los atributos iniciales de la clase Tablero,
        según lo pedido por el enunciado.
        """
        init_state = [[ 1,  1],
                       [-1, -1],
                       [ 1,  1],
                       [-1, -1],
                       [ 1,  1]]
        goal_state = [[0, 0] for _ in range(5)]

        expected_state = [[-1, -1],
                           [ 1,  1],
                           [ 1,  1],
                           [ 1,  1],
                           [-1, -1]]

        cpinit_state = dp(init_state)
        tablero = Tablero(init_state, goal_state)
        cambios: list[tuple[int, int]] = [(0, 0), (4, 1), (2, 0), (2, 0)]

        nuevo_tablero = tablero.aplicar_cambios(cambios)

        self.assertEqual(expected_state, nuevo_tablero)
        self.assertEqual(cpinit_state, tablero.inicio)
