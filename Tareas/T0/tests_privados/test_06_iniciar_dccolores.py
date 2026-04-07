from tests_privados.test_static import CONTENT_MAP
from tests_privados.test_tools import IICTest, timeout

from dccolores import DCColores
from tablero import Tablero


N_SECOND = 1

class TestInicializarDCColores(IICTest):
    """
    Verifica que el objeto de la clase DCColores se haya iniciado
    correctamente, junto a las acciones que esto conlleva.
    """

    @timeout(N_SECOND)
    def test_00_iniciar_juego_vacio(self):
        """
        Se verifica que el objeto de la clase DCColores se haya iniciado correctamente.
        """
        juego: DCColores = DCColores()

        self.assertIsInstance(juego, DCColores)
        self.assertEqual(-1, juego.tablero_actual)
        self.assertEqual([], juego.cambios_actuales)

    @timeout(N_SECOND * 3)
    def test_01_iniciar_juego_dir_data(self):
        """
        Se verifica que se carguen todos los .brd bajo la carpeta data/
        (Revisa por lo menos que se hayan cargado los 20 tableros privados)
        """
        # Check privado_tablero_1-20.brd
        check_map = {
            "privado_tablero_01": False,
            "privado_tablero_02": False,
            "privado_tablero_03": False,
            "privado_tablero_04": False,
            "privado_tablero_05": False,
            "privado_tablero_06": False,
            "privado_tablero_07": False,
            "privado_tablero_08": False,
            "privado_tablero_09": False,
            "privado_tablero_10": False,
            "privado_tablero_11": False,
            "privado_tablero_12": False,
            "privado_tablero_13": False,
            "privado_tablero_14": False,
            "privado_tablero_15": False,
            "privado_tablero_16": False,
            "privado_tablero_17": False,
            "privado_tablero_18": False,
            "privado_tablero_19_nosolucion": False,
            "privado_tablero_20_nosolucion": False,
        }

        # Revisar contenido
        check_content = CONTENT_MAP

        game = DCColores()
        self.assertEqual(-1, game.tablero_actual)
        self.assertEqual([], game.cambios_actuales)

        for tab in game.tableros:
            for check_key, check_tab in check_content.items():
                if check_tab['init'] == tab.inicio and check_tab['goal'] == tab.meta:
                    check_map[check_key] = True

        self.assertTrue(all(check_map.values()))

    @timeout(N_SECOND * 3)
    def test_02_verifica_clase(self):
        """
        Se verifica que los tableros sean instancias correctas de Tablero.
        """
        game = DCColores()

        check = True
        for tablero in game.tableros:
            if not isinstance(tablero, Tablero):
                check = False
                break

        self.assertTrue(check)
