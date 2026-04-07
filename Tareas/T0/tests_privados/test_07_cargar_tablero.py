from tests_privados.test_tools import IICTest, timeout
from tests_privados.test_static import CONTENT_MAP

from tablero import Tablero
from dccolores import DCColores


N_SECOND = 1


class TestCargarTablero(IICTest):
    """
    Verifica la funcionalidad del método DCColores.cargar_tablero.
    """

    @timeout(N_SECOND)
    def test_00_verifica_indice(self):
        """
        Se verifica que cargar_tablero agrega una instancia de Tablero
        al final de juego.tableros.
        """
        juego = DCColores()
        juego.cargar_tablero("privado_tablero_03")

        last_i = len(juego.tableros) - 1
        self.assertIsInstance(juego.tableros[last_i], Tablero)

    @timeout(N_SECOND)
    def test_01_verifica_tablero(self):
        """
        Se verifica que el inicio y la meta del tablero cargado sean correctos
        para un tablero privado con ceros.
        """
        juego = DCColores()
        juego.cargar_tablero("privado_tablero_08")

        last_i = len(juego.tableros) - 1

        expected_init = [[1, 1, 1, 1, 1], [1, 0, 1, 0, 1],
                         [1, 1, 1, 1, 1], [1, 0, 1, 0, 1]]
        expected_goal = [[-1, -1, 1, 1, 1], [-1, 0, 1, 0, -1],
                         [1, -1, -1, 1, -1], [1, 0, -1, 0, -1]]

        self.assertEqual(juego.tableros[last_i].inicio, expected_init)
        self.assertEqual(juego.tableros[last_i].meta, expected_goal)

    @timeout(N_SECOND)
    def test_02_varios_tableros_permanecen(self):
        """
        Se verifica que al cargar tableros privados distintos los agregue
        ambos al final de la lista sin eliminar previos.
        """
        juego = DCColores()
        n_original = len(juego.tableros)

        juego.cargar_tablero("privado_tablero_05")
        juego.cargar_tablero("privado_tablero_06")

        self.assertEqual(len(juego.tableros), n_original + 2)

        expected_init_05 = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
        expected_init_06 = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]

        self.assertEqual(juego.tableros[n_original].inicio, expected_init_05)
        self.assertEqual(juego.tableros[n_original + 1].inicio, expected_init_06)

    @timeout(N_SECOND)
    def test_03_tableros_objetos_distintos(self):
        """
        Se verifica que cargar el mismo tablero dos veces genere dos instancias distintas.
        """
        juego = DCColores()
        n_original = len(juego.tableros)

        juego.cargar_tablero("privado_tablero_11")
        juego.cargar_tablero("privado_tablero_11")
        juego.cargar_tablero("privado_tablero_11")

        last_i = len(juego.tableros) - 1

        self.assertEqual(len(juego.tableros), n_original + 3)
        self.assertIsNot(juego.tableros[last_i], juego.tableros[last_i - 1])

    @timeout(N_SECOND)
    def test_04_verifica_inicio_meta(self):
        """
        Se verifica que inicio y meta del tablero cargado sean objetos distintos.
        """
        juego = DCColores()
        juego.cargar_tablero("privado_tablero_18")

        last_i = len(juego.tableros) - 1
        self.assertIsNot(juego.tableros[last_i].inicio, juego.tableros[last_i].meta)

    @timeout(N_SECOND * 3)
    def test_05_cargar_todo(self):
        """
        Se verifica que se carguen todos los tableros privados y
        estén en el orden correcto.
        """

        check_content = CONTENT_MAP

        juego = DCColores()
        n_original = len(juego.tableros)

        for filename in check_content:
            juego.cargar_tablero(filename)

        self.assertEqual(len(juego.tableros), n_original + len(check_content))

        check_map = {key: False for key in check_content}
        for tab in juego.tableros:
            self.assertIsInstance(tab, Tablero)
            for key, expected in check_content.items():
                if tab.inicio == expected["init"] and tab.meta == expected["goal"]:
                    check_map[key] = True

        self.assertTrue(all(check_map.values()))
