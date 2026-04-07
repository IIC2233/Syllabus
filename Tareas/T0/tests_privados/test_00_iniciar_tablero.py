from tests_privados.test_tools import IICTest, timeout
from tablero import Tablero


N_SECOND = 1

class TestTableroInicio(IICTest):
    """
    Valida el correcto funcionamiento al crear un objeto de la clase Tablero.
    """

    @timeout(N_SECOND)
    def test_00_tablero_es_clase(self):
        """
        Verifica que Tablero sea una clase.
        """
        self.assertTrue(isinstance(Tablero, type), msg="Tablero no es una clase.")

    @timeout(N_SECOND)
    def test_01_tablero_cuadrado_1x1(self):
        """
        Tablero de 2x2. Se verifica que inicio y meta queden almacenados correctamente.
        """
        init_state = [[1, 0]]
        goal_state = [[-1, 0]]

        tablero = Tablero(init_state, goal_state)

        self.assertEqual(tablero.inicio, init_state)
        self.assertEqual(tablero.meta, goal_state)

    @timeout(N_SECOND)
    def test_02_tablero_rectangular_2x5(self):
        """
        Tablero 2x5. Se verifica que inicio y meta queden almacenados correctamente.
        """
        init_state = [[1, 0, 1, 0, 1],
                      [0, 1, 0, 1, 0]]
        goal_state = [[-1, 0, -1, 0, -1],
                      [0, -1, 0, -1, 0]]

        tablero = Tablero(init_state, goal_state)

        self.assertEqual(tablero.inicio, init_state)
        self.assertEqual(tablero.meta, goal_state)

    @timeout(N_SECOND)
    def test_03_tablero_cuadrado_4x4(self):
        """
        Tablero 4x4. Se verifica que inicio y meta queden almacenados correctamente.
        """
        init_state = [[1, -1, 1, -1],
                      [-1, 1, -1, 1],
                      [1, -1, 1, -1],
                      [-1, 1, -1, 1]]
        goal_state = [[-1, 1, -1, 1],
                      [1, -1, 1, -1],
                      [-1, 1, -1, 1],
                      [1, -1, 1, -1]]

        tablero = Tablero(init_state, goal_state)

        self.assertEqual(tablero.inicio, init_state)
        self.assertEqual(tablero.meta, goal_state)
