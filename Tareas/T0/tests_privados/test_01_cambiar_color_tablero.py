from copy import deepcopy
from tests_privados.test_tools import IICTest, timeout

from tablero import Tablero


N_SECOND = 1


def chess_board(h: int, l: int) -> list[list[int]]:
    out = [[1 if (r + c) % 2 == 0 else -1 for c in range(l)] for r in range(h)]
    return out


class TestTableroCambiarColor(IICTest):
    """
    Verifica la funcionalidad del método cambiar_color de la clase
    Tablero.
    """

    @timeout(N_SECOND)
    def test_00_5x5_centro(self):
        """
        Tablero de 5x5, aplica un cambio en la celda central y verifica que 
        las 9 al alrededor hayan cambiado.
        """
        init_board = [[1] * 5 for _ in range(5)]
        goal_board = [[0] * 5 for _ in range(5)]

        after_change_board = [[1, 1, 1, 1, 1], [1, -1, -1, -1, 1], [1, -1, -1, -1, 1],
                              [1, -1, -1, -1, 1], [1, 1, 1, 1, 1]]

        board = Tablero(init_board, goal_board)
        compare = board.cambiar_color(deepcopy(init_board), 2, 2)

        self.assertEqual(compare, after_change_board)

    @timeout(N_SECOND)
    def test_01_4x4_esquina(self):
        """
        Tablero de 4x4, aplica un cambio en la celda de la esquina inferior
        derecha y verifica que sólo 4 celdas hayan cambiado.
        """
        init_board = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
        goal_state = [[0] * 4 for _ in range(4)]

        after_change_board = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, -1, -1], [1, 1, -1, -1]]

        board = Tablero(init_board, goal_state)
        compare = board.cambiar_color(deepcopy(init_board), 3, 3)

        self.assertEqual(compare, after_change_board)

    @timeout(N_SECOND)
    def test_02_13x11_borde_superior(self):
        """
        Tablero de 13x11. Verifica que no se acceda a filas no existentes
        o fuera del tablero.
        """
        init_board = [[-1] * 11 for _ in range(13)]
        goal_board = [[0] * 11 for _ in range(13)]

        after_change_board = [[-1, -1, -1, -1, 1, 1, 1, -1, -1, -1, -1],
                              [-1, -1, -1, -1, 1, 1, 1, -1, -1, -1, -1],
                              [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                              [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                              [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                              [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                              [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                              [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                              [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                              [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                              [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                              [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                              [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]

        board = Tablero(init_board, goal_board)
        compare = board.cambiar_color(deepcopy(init_board), 0, 5)

        self.assertEqual(compare, after_change_board)

    @timeout(N_SECOND)
    def test_03_15x12_con_ceros(self):
        """
        Tablero de 15x12. Verifica que no se modifiquen las celdas con (0)s.
        """
        # 0 -> No cambia
        # -1 -> Cambia (-1)
        # 1 -> Cambia (1)
        init_board = [[1 if c < 11 else 0 for c in range(12)] for _ in range(15)]
        goal_board = [[0] * 12 for _ in range(15)]

        after_change_1 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                          [-1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                          [-1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                          [-1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]]

        after_change_2 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, 0],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, 0],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, 0],
                          [-1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                          [-1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                          [-1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]]

        board = Tablero(init_board, goal_board)

        compare_left = board.cambiar_color(deepcopy(init_board), 7, 0)
        self.assertEqual(compare_left, after_change_1)

        compare_right = board.cambiar_color(compare_left, 4, 10)
        self.assertEqual(compare_right, after_change_2)

    def test_04_20x21_ajedrez(self):
        """
        Tablero de 20x21. Verifica dos cambios consecutivos en múltiples posiciones, donde
        se espera que el cambio total sea nulo, pues se oprime dos veces la misma celda.
        """

        init_board = chess_board(20, 21)
        goal_board = [[0] * 21 for _ in range(20)]

        board = Tablero(init_board, goal_board)
        compare = board.cambiar_color(deepcopy(init_board), 10, 10)
        compare = board.cambiar_color(compare, 10, 10)

        self.assertEqual(compare, init_board)

        compare = board.cambiar_color(compare, 19, 20)
        compare = board.cambiar_color(compare, 19, 20)
        self.assertEqual(compare, init_board)

        compare = board.cambiar_color(compare, 6, 20)
        compare = board.cambiar_color(compare, 6, 20)
        self.assertEqual(compare, init_board)

    @timeout(N_SECOND)
    def test_05_12x11_no_modifica_objeto(self):
        """
        Tablero de 12x11. Verifica que llamar a cambiar_color no se
        modifique el atributo tablero.inicio.
        """
        init_board = [[1] * 11 for _ in range(12)]
        goal_board = [[0] * 11 for _ in range(12)]
        init_expected = deepcopy(init_board)

        tablero = Tablero(init_board, goal_board)
        tablero.cambiar_color(deepcopy(init_board), 6, 5)

        self.assertEqual(tablero.inicio, init_expected)
