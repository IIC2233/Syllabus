import os

from tests_privados.test_tools import IICTest, timeout
from dccolores import DCColores


N_SECOND = 1


def remove_file(ruta: str) -> None:
    if os.path.exists(ruta):
        os.remove(ruta)


class TestGuardarCambios(IICTest):
    """
    Verifica la funcionalidad del método DCColores.guardar_cambios
    siguiendo las condiciones del enunciado.
    """

    @timeout(N_SECOND)
    def test_00_verifica_crea_archivo(self):
        """
        Se verifica que guardar_cambios cree el archivo .chg en data/.
        """
        juego = DCColores()
        juego.cargar_tablero("privado_tablero_03")
        juego.tablero_actual = len(juego.tableros) - 1

        filename_guardado = "test_privados_guardar_00"
        ruta_guardado = os.path.join("data", filename_guardado + ".chg")
        remove_file(ruta_guardado)
        self.addCleanup(remove_file, ruta_guardado)

        juego.guardar_cambios(filename_guardado)

        self.assertTrue(os.path.exists(ruta_guardado))

    @timeout(N_SECOND)
    def test_01_verifica_contenido_sin_cambios(self):
        """
        Se verifica el contenido del archivo cuando no hay cambios.
        """
        juego = DCColores()
        juego.cargar_tablero("privado_tablero_06")
        juego.tablero_actual = len(juego.tableros) - 1

        filename_guardado = "test_privados_guardar_01"
        ruta_guardado = os.path.join("data", filename_guardado + ".chg")
        remove_file(ruta_guardado)
        self.addCleanup(remove_file, ruta_guardado)

        juego.guardar_cambios(filename_guardado)

        with open(ruta_guardado, "r", encoding="utf-8") as f:
            contenido = f.read().strip()

        esperado = (
"""4 4 0
####
####
####
####""")

        self.assertEqual(contenido, esperado)

    @timeout(N_SECOND)
    def test_02_verifica_un_cambio(self):
        """
        Se verifica el contenido del archivo con un único cambio.
        """
        juego = DCColores()
        juego.cargar_tablero("privado_tablero_03")
        last_i = len(juego.tableros) - 1
        juego.tablero_actual = last_i

        acciones = [(1, 1)]
        juego.cambios_actuales = acciones

        filename_guardado = "test_privados_guardar_02"
        ruta_guardado = os.path.join("data", filename_guardado + ".chg")
        remove_file(ruta_guardado)
        self.addCleanup(remove_file, ruta_guardado)

        juego.guardar_cambios(filename_guardado)

        with open(ruta_guardado, "r", encoding="utf-8") as f:
            contenido = f.read().strip()

        esperado = (
"""3 3 1
###
###
###
1 1
OOO
OOO
OOO""")

        self.assertEqual(contenido, esperado)

    @timeout(N_SECOND)
    def test_03_verifica_dos_cambios(self):
        """
        Se verifica el contenido del archivo con dos cambios.
        """
        juego = DCColores()
        juego.cargar_tablero("privado_tablero_05")
        last_i = len(juego.tableros) - 1
        juego.tablero_actual = last_i

        acciones = [(0, 1), (2, 2)]
        juego.cambios_actuales = acciones

        filename_guardado = "test_privados_guardar_03"
        ruta_guardado = os.path.join("data", filename_guardado + ".chg")
        remove_file(ruta_guardado)
        self.addCleanup(remove_file, ruta_guardado)

        juego.guardar_cambios(filename_guardado)

        with open(ruta_guardado, "r", encoding="utf-8") as f:
            contenido = f.read().strip()

        esperado = (
"""3 4 2
####
####
####
0 1
OOO#
OOO#
####
2 2
OOO#
O##O
#OOO""")

        self.assertEqual(contenido, esperado)

    @timeout(N_SECOND)
    def test_04_verifica_sobrescritura(self):
        """
        Se verifica que guardar_cambios sobreescriba el archivo si ya existe.
        """
        juego = DCColores()
        juego.cargar_tablero("privado_tablero_03")
        last_i = len(juego.tableros) - 1
        juego.tablero_actual = last_i

        filename_guardado = "test_privados_guardar_04"
        ruta_guardado = os.path.join("data", filename_guardado + ".chg")
        remove_file(ruta_guardado)
        self.addCleanup(remove_file, ruta_guardado)

        # Primer guardado
        juego.guardar_cambios(filename_guardado)

        with open(ruta_guardado, "r", encoding="utf-8") as f:
            contenido_1 = f.read().strip()

        esperado_1 = (
"""3 3 1
###
###
###
1 1
OOO
OOO
OOO""")
        # Segundo guardado (sobreescritura)
        juego.cambios_actuales = [(1, 1)]
        juego.guardar_cambios(filename_guardado)

        with open(ruta_guardado, "r", encoding="utf-8") as f:
            contenido_2 = f.read().strip()

        self.assertNotEqual(contenido_1, contenido_2)
        self.assertEqual(contenido_2, esperado_1)

    @timeout(N_SECOND)
    def test_06_verifica_salto_final(self):
        """
        Se verifica la línea en blanco al final del archivo.
        """
        juego = DCColores()
        juego.cargar_tablero("privado_tablero_03")
        last_i = len(juego.tableros) - 1
        juego.tablero_actual = last_i
        juego.cambios_actuales = [(1, 1)]

        filename_guardado = "test_privados_guardar_06"
        ruta_guardado = os.path.join("data", filename_guardado + ".chg")
        remove_file(ruta_guardado)
        self.addCleanup(remove_file, ruta_guardado)

        juego.guardar_cambios(filename_guardado)

        with open(ruta_guardado, "r", encoding="utf-8") as f:
            contenido_raw = f.read()

        condition: bool = (contenido_raw.endswith("\n") or contenido_raw.endswith("\r\n"))

        self.assertTrue(condition)

    @timeout(N_SECOND)
    def test_07_verifica_tablero_actual(self):
        """
        Se verifica que guardar_cambios use el tablero dado por tablero_actual
        """
        juego = DCColores()
        juego.cargar_tablero("privado_tablero_03")
        juego.cargar_tablero("privado_tablero_05")
        juego.cargar_tablero("privado_tablero_06")

        idx = len(juego.tableros) - 3
        juego.tablero_actual = idx
        juego.cambios_actuales = [(1, 1)]

        filename_guardado = "test_privados_guardar_07"
        ruta_guardado = os.path.join("data", filename_guardado + ".chg")
        remove_file(ruta_guardado)
        self.addCleanup(remove_file, ruta_guardado)

        juego.guardar_cambios(filename_guardado)

        with open(ruta_guardado, "r", encoding="utf-8") as f:
            contenido = f.read().strip()


        primera_linea = contenido.splitlines()[0]
        self.assertEqual(primera_linea, "3 3 1")

        juego = DCColores()
        juego.cargar_tablero("privado_tablero_12")
        last_i = len(juego.tableros) - 1
        juego.tablero_actual = last_i

        acciones = [(0, 5), (2, 2), (3, 3), (5, 0)]
        juego.cambios_actuales = acciones

        filename_guardado = "test_privados_guardar_05"
        ruta_guardado = os.path.join("data", filename_guardado + ".chg")
        remove_file(ruta_guardado)
        self.addCleanup(remove_file, ruta_guardado)

        juego.guardar_cambios(filename_guardado)

        with open(ruta_guardado, "r", encoding="utf-8") as f:
            contenido = f.read().strip()

        esperado = (
"""6 6 4
######
######
######
######
######
######
0 5
####OO
####OO
######
######
######
######
2 2
####OO
#OOOOO
#OOO##
#OOO##
######
######
3 3
####OO
#OOOOO
#O##O#
#O##O#
##OOO#
######
5 0
####OO
#OOOOO
#O##O#
#O##O#
OOOOO#
OO####""")

        self.assertEqual(contenido, esperado)
