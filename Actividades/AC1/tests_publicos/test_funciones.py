import unittest
from unittest.mock import patch
import main


class VerificarFunciones(unittest.TestCase):

    def test_cargar_items(self):
        """
        Verifica que los items fueron cargados en una lista.
        """
        # Ejecutar cargar_items
        items = main.cargar_items()

        self.assertEqual(items[4].nombre, "queso azul")
        self.assertEqual(items[4].puntos, 70)
        self.assertEqual(items[4].precio, 6800)

    def test_crear_usuario(self):
        """
        Verifica que se instancia correctamente Usuario al crear usuario.
        """
        user_sin = main.crear_usuario(False)
        user_con = main.crear_usuario(True)
        self.assertEqual(user_sin.suscripcion, False)
        self.assertEqual(user_con.suscripcion, True)

    def test_print_crear_usuario(self):
        """
        Verifica el contenido al momento de imprimir
        """
        with patch("builtins.print") as mock_print:
            # Llamar la función que imprime algo
            main.crear_usuario(True)

            # Validar el contenido impreso
            mock_print.assert_called_once_with("> Usuario con suscripcion. Puntos: 0")
