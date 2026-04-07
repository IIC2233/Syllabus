from copy import deepcopy

from tests_privados.test_tools import IICTest, timeout
from tablero import Tablero


N_SECOND = 1


def chess_board(h: int, l: int) -> list[list[int]]:
    out = [[1 if (r + c) % 2 == 0 else -1 for c in range(l)] for r in range(h)]
    return out


class TestAplicarCambiosTablero(IICTest):
    """
    Verifica la funcionalidad del método aplicar_cambios de
    la clase Tablero.
    """

    @timeout(N_SECOND)
    def test_00_11x11_un_cambio_central(self):
        """
        Tablero de 11x11. Aplica un único cambio en el centro (5,5).
        """
        init_board = [[1] * 11 for _ in range(11)]
        goal_board = [[0] * 11 for _ in range(11)]

        expected_board = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                          [1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 1],
                          [1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 1],
                          [1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

        cp_init_board = deepcopy(init_board)
        board = Tablero(init_board, goal_board)
        changes: list[tuple[int, int]] = [(5, 5)]

        new_board = board.aplicar_cambios(changes)

        self.assertEqual(new_board, expected_board)
        self.assertEqual(board.inicio, cp_init_board)

    @timeout(N_SECOND)
    def test_01_12x12_ajedrez_esquinas(self):
        """
        Tablero de 12x12. Aplica cambios en las esquinas superior izquierda y esquina
        diagonal opuesta.
        """
        init_board = [[1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],
                      [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1],
                      [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],
                      [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1],
                      [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],
                      [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1],
                      [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],
                      [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1],
                      [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],
                      [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1],
                      [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],
                      [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]]
        goal_board = [[0] * 12 for _ in range(12)]

        expected_board = [[-1, 1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],
                          [1, -1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1],
                          [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],
                          [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1],
                          [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],
                          [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1],
                          [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],
                          [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1],
                          [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],
                          [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1],
                          [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1],
                          [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 1, -1]]

        cp_init_board = deepcopy(init_board)
        board = Tablero(init_board, goal_board)
        changes: list[tuple[int, int]] = [(0, 0), (11, 11)]

        new_board = board.aplicar_cambios(changes)

        self.assertEqual(new_board, expected_board)
        self.assertEqual(board.inicio, cp_init_board)

    @timeout(N_SECOND)
    def test_02_14x13_ceros(self):
        """
        Tablero de 14x13. Verifica que los ceros no se alteren.
        """
        init_board = [[1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1]]
        goal_board = [[0] * 13 for _ in range(14)]

        expected_board = [[1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                          [1, 1, -1, -1, -1, 1, 0, 1, 1, 1, 1, 1, 1],
                          [1, 1, -1, -1, -1, 1, 0, 1, 1, 1, 1, 1, 1],
                          [1, 1, -1, -1, -1, 1, 0, 1, 1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1, 1, 0, 1, -1, -1, -1, 1, 1],
                          [1, 1, 1, 1, 1, 1, 0, 1, -1, -1, -1, 1, 1],
                          [1, 1, 1, 1, 1, 1, 0, 1, -1, -1, -1, 1, 1],
                          [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                          [1, -1, -1, -1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                          [1, -1, -1, -1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                          [1, -1, -1, -1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1]]

        cp_init_board = deepcopy(init_board)
        board = Tablero(init_board, goal_board)
        changes: list[tuple[int, int]] = [(3, 3), (7, 9), (11, 2)]

        new_board = board.aplicar_cambios(changes)

        self.assertEqual(new_board, expected_board)
        self.assertEqual(board.inicio, cp_init_board)

    @timeout(N_SECOND)
    def test_03_11x15_cambios_redundantes(self):
        """
        Tablero de 11x15. Aplica el mismo cambio y verifica que el efecto sea nulo.
        """
        init_board = [[-1] * 15 for _ in range(11)]
        goal_board = [[0] * 15 for _ in range(11)]

        expected_board = [[1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                          [1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                          [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                          [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                          [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                          [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                          [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                          [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                          [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                          [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                          [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]

        cp_init_board = deepcopy(init_board)
        board = Tablero(init_board, goal_board)
        changes: list[tuple[int, int]] = [(5, 7), (5, 7), (0, 0)]

        new_board = board.aplicar_cambios(changes)

        self.assertEqual(new_board, expected_board)
        self.assertEqual(board.inicio, cp_init_board)

    @timeout(N_SECOND)
    def test_04_16x11_tres_cambios_bordes(self):
        """
        Tablero de 16x11. APlica tres cambios en los distintos bordes del tablero.
        """
        init_board = [[1] * 11 for _ in range(16)]
        goal_board = [[0] * 11 for _ in range(16)]

        expected_board = [[1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                          [1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 1],
                          [1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 1],
                          [1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                          [-1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                          [-1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1], ]

        cp_init_board = deepcopy(init_board)
        board = Tablero(init_board, goal_board)
        changes: list[tuple[int, int]] = [(0, 10), (8, 5), (15, 0)]

        new_board = board.aplicar_cambios(changes)

        self.assertEqual(new_board, expected_board)
        self.assertEqual(board.inicio, cp_init_board)


    @timeout(N_SECOND)
    def test_05_12x13_sin_cambios(self):
        """
        Tablero de 12x13. Lista de cambios vacía, verifica que se retorne
        el mismo tablero original.
        """
        init_board = [[1] * 13 for _ in range(12)]
        goal_board = [[0] * 13 for _ in range(12)]

        cp_init_board = deepcopy(init_board)
        board = Tablero(init_board, goal_board)
        changes: list[tuple[int, int]] = []

        new_board = board.aplicar_cambios(changes)

        self.assertEqual(new_board, cp_init_board)
        self.assertEqual(board.inicio, cp_init_board)
