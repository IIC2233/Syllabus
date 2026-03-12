
import unittest

from tablero import Tablero
from dccolores import DCColores
from tests_publicos.timeout_function import timeout


N_SECOND = 1

class TestInicializarDCColores(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc if doc else None

    @timeout(N_SECOND)
    def test_00_iniciar_juego_vacio(self):
        """
        Se verifica que el objeto de la clase DCColores se haya iniciado correctamente.
        """
        juego: DCColores = DCColores()

        self.assertEqual(-1, juego.tablero_actual)
        self.assertEqual([], juego.cambios_actuales)

    @timeout(N_SECOND * 3)
    def test_01_iniciar_juego_dir_data(self):
        """
        Se verifica que se carguen todos los .brd bajo la carpeta data.
        (Al menos, como mínimo, los incluidos originalmente en la tarea)
        """
        # Check tablero_1-6.brd
        check_map: dict = {
            "tablero_1": False,
            "tablero_2": False,
            "tablero_3": False,
            "tablero_4": False,
            "tablero_5": False,
            "tablero_6": False,
        }

        check_content: dict = {
            "tablero_1": {
                "init": [[1, 1], [1, 1]],
                "goal": [[-1, -1], [-1, -1]]
                },
            "tablero_2": {
                "init": [[1, -1, 1], [-1, 1, -1], [1, -1, 1]],
                "goal": [[-1, 1, -1], [1, -1, 1], [-1, 1, -1]]
                },
            "tablero_3": {
                "init": [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]],
                "goal": [[-1, -1, 1, 1], [-1, -1, 1, 1], [1, 1, -1, -1], [1, 1, -1, -1]]
                },
            "tablero_4": {
                "init": [[1, 1, -1, 0], [1, -1, 1, -1], [0, 1, -1, 1]],
                "goal": [[-1, 1, -1, 0], [-1, -1, 1, 1], [0, 1, -1, -1]]
                },
            "tablero_5": {
                "init": [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1],
                         [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]],
                "goal": [[-1, -1, 1, 1, 1], [-1, 1, -1, -1, 1], [1, -1, -1, -1, 1],
                         [1, -1, -1, 1, -1], [1, 1, 1, -1, -1]]
                },
            "tablero_6": {
                "init": [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0],
                         [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]],
                "goal": [[-1, 1, 0, 0, 0], [1, -1, 0, 0, 0], [0, 0, 0, 0, 0],
                         [0, 0, 0, -1, 1], [0, 0, 0, 1, -1]]
                },
        }

        juego = DCColores()
        self.assertEqual(-1, juego.tablero_actual)
        self.assertEqual([], juego.cambios_actuales)

        for tab in juego.tableros:
            for check_key, check_tab in check_content.items():
                if check_tab['init'] == tab.inicio and check_tab['goal'] == tab.meta:
                    check_map[check_key] = True

        self.assertTrue(all(check_map.values()))

    def test_02_verifica_clase(self):
        """
        Se verifica que los tableros sean efectivamente instancias de Tablero.
        """
        juego = DCColores()

        check = True
        for tablero in juego.tableros:
            if not isinstance(tablero, Tablero):
                check = False
                break

        self.assertTrue(check)
