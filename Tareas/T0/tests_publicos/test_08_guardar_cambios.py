import os
import unittest

from dccolores import DCColores
from tests_publicos.timeout_function import timeout


N_SECOND = 1

def remove_test(ruta: str) -> None:
    if os.path.exists(ruta):
        os.remove(ruta)
    else:
        pass


class TestGuardarCambios(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc if doc else None

    @timeout(N_SECOND)
    def test_00_verifica_crea_archivo(self):
        """
        Se verifica que el método DCColores.guardar_cambios funcione correctamente.
        """
        juego: DCColores = DCColores()
        filename: str = "tablero_2"
        juego.cargar_tablero(filename)
        n_tableros = len(juego.tableros)
        juego.tablero_actual = n_tableros - 1

        filename_guardado = "test_publicos_08_t2_00"
        ruta_guardado = os.path.join('data', filename_guardado + ".chg")
        remove_test(ruta_guardado)
        self.addCleanup(remove_test, ruta_guardado)
        juego.guardar_cambios(filename_guardado)

        self.assertTrue(os.path.exists(ruta_guardado))

    @timeout(N_SECOND)
    def test_01_verifica_contenido_sin_cambios(self):
        """
        Se verifica que el método DCColores.guardar_cambios funcione
        correctamente y verifica su contenido.
        """
        juego: DCColores = DCColores()
        filename: str = "tablero_1"
        juego.cargar_tablero(filename)
        n_tableros = len(juego.tableros)

        filename_guardado = "test_publicos_08_t1_01"
        ruta_guardado = os.path.join('data', filename_guardado + ".chg")
        remove_test(ruta_guardado)
        self.addCleanup(remove_test, ruta_guardado)

        juego.tablero_actual = n_tableros - 1
        juego.guardar_cambios(filename_guardado)

        with open(ruta_guardado, 'r', encoding='utf-8') as f:
            contenido = f.read().strip()

        esperado = (
"""2 2 0
##
##""")

        self.assertEqual(contenido, esperado)

    @timeout(N_SECOND)
    def test_02_verificar_unico_cambio(self):
        """
        Se verifica que el método DCColores.guardar_cambios funcione
        correctamente y verifica su contenido.
        """
        juego: DCColores = DCColores()
        filename: str = "tablero_1"
        juego.cargar_tablero(filename)
        n_tableros = len(juego.tableros)

        filename_guardado = "test_publicos_08_t1_02"
        ruta_guardado = os.path.join('data', filename_guardado + ".chg")
        remove_test(ruta_guardado)
        self.addCleanup(remove_test, ruta_guardado)

        # Acciones
        acciones = [(0, 0)]
        juego.tablero_actual = n_tableros - 1
        last_i = n_tableros - 1
        juego.tableros[last_i].aplicar_cambios(acciones)
        juego.cambios_actuales = acciones

        juego.guardar_cambios(filename_guardado)

        with open(ruta_guardado, 'r', encoding='utf-8') as f:
            contenido = f.read().strip()

        esperado = (
"""2 2 1
##
##
0 0
OO
OO""")

        self.assertEqual(contenido, esperado)

    @timeout(N_SECOND)
    def test_03_verificar_multiples_cambios(self):
        """
        Se verifica que el método DCColores.guardar_cambios funcione
        correctamente y verifica su contenido.
        """
        juego: DCColores = DCColores()
        filename: str = "tablero_4"
        juego.cargar_tablero(filename)

        filename_guardado = "test_publicos_08_t4_03"
        ruta_guardado = os.path.join('data', filename_guardado + ".chg")
        remove_test(ruta_guardado)
        self.addCleanup(remove_test, ruta_guardado)

        # Acciones
        acciones = [(1, 1), (1, 2)]
        n_tableros = len(juego.tableros)
        last_i = n_tableros - 1
        juego.tablero_actual = last_i
        juego.tableros[last_i].aplicar_cambios(acciones)
        juego.cambios_actuales = acciones

        juego.guardar_cambios(filename_guardado)

        with open(ruta_guardado, 'r', encoding='utf-8') as f:
            contenido = f.read().strip()

        esperado = (
"""3 4 2
##O_
#O#O
_#O#
1 1
OO#_
O#OO
_O##
1 2
O#O_
OO##
_#OO"""
        )

        self.assertEqual(contenido, esperado)

    @timeout(N_SECOND)
    def test_04_verificar_multiples_indice(self):
        """
        Se verifica que el método DCColores.guardar_cambios funcione
        correctamente y verifica su contenido.
        """
        juego: DCColores = DCColores()
        filename: str = "tablero_6"
        filename_2: str = "tablero_4"
        juego.cargar_tablero(filename)
        juego.cargar_tablero(filename_2)
        n_tableros = len(juego.tableros)
        last_i = n_tableros - 1

        filename_guardado = "test_publicos_08_t6_t4_04"
        ruta_guardado = os.path.join('data', filename_guardado + ".chg")
        remove_test(ruta_guardado)
        self.addCleanup(remove_test, ruta_guardado)

        # Acciones
        acciones = [(1, 1), (1, 2)]
        juego.tablero_actual = last_i
        juego.tableros[last_i].aplicar_cambios(acciones)
        juego.cambios_actuales = acciones

        juego.guardar_cambios(filename_guardado)

        with open(ruta_guardado, 'r', encoding='utf-8') as f:
            contenido = f.read().strip()

        esperado = (
"""3 4 2
##O_
#O#O
_#O#
1 1
OO#_
O#OO
_O##
1 2
O#O_
OO##
_#OO""")

        self.assertEqual(contenido, esperado)

    @timeout(N_SECOND)
    def test_05_verifica_sobreescritura(self):
        """
        Se verifica que el método DCColores.guardar_cambios funcione
        correctamente y verifica su contenido.
        """
        juego: DCColores = DCColores()
        filename_1: str = "tablero_5"
        filename_2: str = "tablero_4"
        filename_3: str = "tablero_3"
        juego.cargar_tablero(filename_1)

        filename_guardado = "test_publicos_08_t1_01"
        ruta_guardado = os.path.join('data', filename_guardado + ".chg")
        remove_test(ruta_guardado)
        self.addCleanup(remove_test, ruta_guardado)

        n_tableros = len(juego.tableros)
        last_i = n_tableros - 1

        juego.tablero_actual = last_i
        juego.guardar_cambios(filename_guardado)

        del n_tableros
        del last_i

        juego.cargar_tablero(filename_3)
        juego.cargar_tablero(filename_2)

        n_tableros = len(juego.tableros)
        last_i = n_tableros - 1

        with open(ruta_guardado, 'r', encoding='utf-8') as f:
            contenido_1 = f.read().strip()

        esperado_1 = (
"""5 5 0
#####
#####
#####
#####
#####""")

        self.assertEqual(contenido_1, esperado_1)

        juego.tablero_actual = last_i
        acciones = [(1, 1), (1, 2)]
        juego.tableros[last_i].aplicar_cambios(acciones)
        juego.cambios_actuales = acciones
        juego.guardar_cambios(filename_guardado)

        with open(ruta_guardado, 'r', encoding='utf-8') as f:
            contenido_2 = f.read().strip()

        esperado_2 = (
"""3 4 2
##O_
#O#O
_#O#
1 1
OO#_
O#OO
_O##
1 2
O#O_
OO##
_#OO""")

        self.assertEqual(contenido_2, esperado_2)
