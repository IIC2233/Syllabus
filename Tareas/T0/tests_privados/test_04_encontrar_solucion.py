from tests_privados.test_tools import IICTest, timeout
from tests_privados.functions import apply_changes

from tablero import Tablero


N_SECOND_0 = 10
N_SECOND_1 = 20
N_SECOND_2 = 32

class TestEncontrarSolucion(IICTest):

    @timeout(N_SECOND_0)
    def test_00_objetivo_imposible(self):
        """
        Verificar que se retorne una lista vacía cuando el caso objetivo
        es imposible de alcanzar.
        """

        _init_state = [[-1, 1, 0, -1, 1, -1, 1],
                        [1, -1, 1, 0, -1, 1, -1],
                        [0, 1, -1, 1, -1, 1, 0],
                        [-1, 0, 1, -1, 1, -1, 1],
                        [1, -1, 1, 0, -1, 1, -1],
                        [0, 1, -1, 1, -1, 1, 0],
                        [-1, 1, 0, -1, 1, -1, 1],
                        [1, 0, -1, 1, -1, 1, -1]]

        _goal_state = [
                        [0, -1, 0, -1, -1, 1, 1],
                        [-1, -1, -1, 0, 1, -1, -1],
                        [0, 1, 1, -1, -1, -1, 0],
                        [1, 0, 1, 1, 1, 1, -1],
                        [-1, 1, 1, 0, -1, -1, 1],
                        [0, -1, 1, 1, -1, 1, 0],
                        [1, -1, 0, -1, 1, -1, 1],
                        [1, 0, -1, 1, -1, 1, -1]
                    ]

        board = Tablero(_init_state, _goal_state)
        change_list = [(0, 1), (1, 2), (1, 4), (2, 1), (3, 3), (5, 1), (7, 5)]
        max_changes = 3
        expected = []

        result = board.encontrar_solucion(change_list, max_changes)

        self.assertIsNotNone(result)
        self.assertListEqual(result, expected)

    @timeout(N_SECOND_1)
    def test_01_cambios_excesivos(self):
        """
        Verificar que se llegue a una solución cuando se entregan muchos 
        más cambios de los necesarios para llegar al objetivo.
        """

        _init_state = [
                        [1, -1, 1, -1, 1, 0, -1, 1],
                        [-1, 1, -1, 1, -1, 1, 1, -1],
                        [1, -1, 0, 1, -1, 1, -1, 1],
                        [-1, 1, 1, -1, 0, -1, 1, -1],
                        [1, -1, 1, 0, -1, 1, -1, 1],
                        [-1, 1, -1, 1, -1, 1, 0, 1],
                        [1, -1, 1, -1, 1, -1, 1, 0],
                        [0, 1, -1, 1, -1, 1, -1, 1]
                    ]

        _goal_state = [[1, -1, 1, -1, 1, 0, 1, -1],
                        [-1, 1, -1, -1, 1, -1, -1, 1],
                        [1, -1, 0, -1, 1, -1, -1, 1],
                        [-1, -1, -1, -1, 0, 1, 1, -1],
                        [1, 1, -1, 0, 1, -1, 1, 1],
                        [-1, -1, 1, -1, 1, -1, 0, 1],
                        [1, -1, 1, -1, -1, 1, -1, 0],
                        [0, 1, -1, 1, -1, 1, -1, 1]]

        board = Tablero(_init_state, _goal_state)
        change_list =  [(1, 0), (4, 2), (2, 4)]
        max_changes = 5
        student_list = board.encontrar_solucion(change_list, max_changes)

        result = apply_changes(_init_state, student_list)

        self.assertIsNotNone(student_list)
        self.assertListEqual(result, _goal_state)

    @timeout(N_SECOND_2)
    def test_02_cambios_insuficientes(self):
        """
        Verificar que se retorne una lista vacía cuando la cantidad de cambios
        extras no es suficiente para alcanzar el estado objetivo.
        """
        _init_state = [
                        [1, -1, 1, -1, 1, 0],
                        [-1, 1, -1, 1, -1, 1],
                        [1, -1, 0, 1, -1, 1],
                        [-1, 1, 1, -1, 0, -1],
                        [1, -1, 1, 0, -1, 1],
                        [-1, 1, -1, 1, -1, 1]
                    ]

        _goal_state = [[-1, 1, 1, -1, 1, 0],
                        [1, 1, -1, -1, 1, -1],
                        [-1, 1, 0, -1, 1, -1],
                        [-1, -1, -1, -1, 0, 1],
                        [-1, -1, -1, 0, 1, -1],
                        [1, 1, 1, -1, 1, -1]]

        board = Tablero(_init_state, _goal_state)
        change_list =  [(1, 0), (4, 2)]
        max_changes = 4
        result = []

        student_list = board.encontrar_solucion(change_list, max_changes)

        self.assertIsNotNone(student_list)
        self.assertListEqual(result, student_list)

    @timeout(N_SECOND_0)
    def test_03_cambios_tablero_grande(self):
        """
        Verificar que se llegue a una solución cuando se trabaja
        con un tablero de 10x10.
        """

        _init_state = [[0, 0, 0, -1, -1, -1, -1, 0, 0, 0],
                       [0, 0, -1, -1, -1, -1, -1, -1, 0, 0],
                       [0, -1, 0, 1, -1, -1, 1, 0, -1, 0],
                       [-1, -1, 0, 1, -1, -1, 1, 0, -1, -1],
                       [-1, -1, -1, 1, -1, -1, 1, 1, 1, 1],
                       [-1, -1, -1, 1, 1, 1, -1, 1, 1, 1],
                       [-1, -1, 0, 1, 1, 1, 1, 0, -1, 1],
                       [0, -1, -1, 0, 0, 0, 0, 1, 1, 0],
                       [0, 0, -1, -1, -1, -1, 1, 1, 0, 0],
                       [0, 0, 0, -1, -1, -1, -1, 0, 0, 0]]

        _goal_state = [[0, 0, 0, -1, -1, -1, -1, 0, 0, 0],
                       [0, 0, -1, -1, -1, -1, -1, -1, 0, 0],
                       [0, -1, 0, -1, -1, -1, -1, 0, -1, 0],
                       [-1, -1, 0, -1, -1, -1, -1, 0, -1, -1],
                       [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                       [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                       [-1, -1, 0, -1, -1, -1, -1, 0, -1, -1],
                       [0, -1, -1, 0, 0, 0, 0, -1, -1, 0],
                       [0, 0, -1, -1, -1, -1, -1, -1, 0, 0],
                       [0, 0, 0, -1, -1, -1, -1, 0, 0, 0]]

        board = Tablero(_init_state, _goal_state)
        change_list =  [(6,4), (5,8), (7, 7)]
        max_changes = 6

        student_list = board.encontrar_solucion(change_list, max_changes)

        result = apply_changes(_init_state, student_list)

        self.assertIsNotNone(student_list)
        self.assertListEqual(result, _goal_state)

    @timeout(N_SECOND_0)
    def test_04_sin_cambios_iniciales(self):
        """
        Verificar que logre llegar al objetivo cuando los cambios iniciales son vacíos.
        """
        _init_state = [
            [-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1]
        ]

        _goal_state = [
            [1,1,-1,1,1],
            [1,1,-1,1,1],
            [-1,1,1,1,-1],
            [1,-1,1,-1,1],
            [1,-1,1,-1,1]
        ]

        board = Tablero(_init_state, _goal_state)
        change_list =  []
        max_changes = 5
        expected = [(1,1), (1,3), (3,1), (3,2), (3,3)]

        student_list = board.encontrar_solucion(change_list, max_changes)

        result = apply_changes(_init_state, student_list)

        print(student_list)

        self.assertIsNotNone(student_list)
        self.assertListEqual(result, _goal_state)
