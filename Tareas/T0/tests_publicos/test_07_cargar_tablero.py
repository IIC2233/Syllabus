import unittest

from tablero import Tablero
from dccolores import DCColores
from tests_publicos.timeout_function import timeout


N_SECOND = 1

class TestCargarTablero(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc if doc else None

    @timeout(N_SECOND)
    def test_00_cargar_1_tablero(self):
        """
        Se verifica que el método DCColores.cargar_tablero funcione correctamente.
        """
        juego: DCColores = DCColores()
        filename: str = "tablero_1"

        juego.cargar_tablero(filename)
        n_tableros = len(juego.tableros)
        last_i = n_tableros - 1

        # Verifica que el tablero cargado sea de la clase Tablero
        self.assertIsInstance(juego.tableros[last_i], Tablero)

        # Verifica que la clase Tablero este correcta
        tablero_inicial = [[1, 1]] * 2
        tablero_meta = [[-1, -1]] * 2
        self.assertEqual(juego.tableros[last_i].inicio, tablero_inicial)
        self.assertEqual(juego.tableros[last_i].meta, tablero_meta)

    def test_01_cargar_2_tableros(self):
        """
        Se verifica que el método DCColores.cargar_tablero funcione correctamente.
        """
        juego: DCColores = DCColores()
        filename_1: str = "tablero_2"
        filename_2: str = "tablero_3"

        juego.cargar_tablero(filename_1)
        n_tableros = len(juego.tableros)
        last_i = n_tableros - 1

        # Verifica que el tablero cargado sea de la clase Tablero
        self.assertIsInstance(juego.tableros[last_i], Tablero)

        # Verifica que la clase Tablero este correcta
        tablero_1_inicial = [[1, -1, 1], [-1, 1, -1], [1, -1, 1]]
        tablero_1_meta = [[-1, 1, -1], [1, -1, 1], [-1, 1, -1]]

        self.assertEqual(juego.tableros[last_i].inicio, tablero_1_inicial)
        self.assertEqual(juego.tableros[last_i].meta, tablero_1_meta)

        # Verifica que el segundo tablero se cargado correctamente
        juego.cargar_tablero(filename_2)
        tablero_2_inicial = [[1] * 4 for _ in range(4)]

        self.assertEqual(len(juego.tableros), n_tableros + 1)
        self.assertIsInstance(juego.tableros[n_tableros], Tablero)

        # Verifica orden
        self.assertEqual(juego.tableros[n_tableros].inicio, tablero_2_inicial)

    @timeout(N_SECOND)
    def test_02_cargar_tableros_sin_eliminar(self):
        """
        Se verifica que el método DCColores.cargar_tablero funcione correctamente
        sin eliminar los tableros anteriores.
        """
        juego = DCColores()

        n_original = len(juego.tableros)

        juego.cargar_tablero("tablero_4")
        juego.cargar_tablero("tablero_4")

        n_tableros = len(juego.tableros)
        last_i = n_tableros - 1

        self.assertEqual(len(juego.tableros), n_original + 2)
        self.assertTrue(id(juego.tableros[last_i]) != id(juego.tableros[last_i - 1]))

    @timeout(N_SECOND)
    def test_03_verifica_inicio_meta(self):
        """
        Se verifica que el método DCColores.cargar_tablero funcione correctamente
        agregando correctamente el inicio y meta del tablero.
        """
        juego = DCColores()
        juego.cargar_tablero("tablero_5")

        n_tableros = len(juego.tableros)
        last_i = n_tableros - 1

        self.assertIsNot(juego.tableros[last_i].inicio, juego.tableros[last_i].meta)
