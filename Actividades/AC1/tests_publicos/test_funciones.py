import unittest
from unittest.mock import patch
from main import cargar_medallistas, crear_tabla

TEST_FILE = "utils/results.dcc"

class VerificarFunciones(unittest.TestCase):

    def test_leer_medallistas(self):
        """
        Verifica que los medallistas son creados correctamente.
        """
        # Ejecutar cargar_medallistas
        medallistas = cargar_medallistas(TEST_FILE)

        self.assertEqual(medallistas[4].nombre, "Elin Andersson")
        self.assertEqual(medallistas[4].deporte, "Patinaje Artístico")
        self.assertEqual(medallistas[4].medalla, "Bronce")
        self.assertEqual(medallistas[4].nombre_pais, "Suecia")

    def test_crear_tabla(self):
        """
        Verifica que se crea correctamnete el tabla con los resiltados.
        """
        medallistas = cargar_medallistas(TEST_FILE)
        tp = crear_tabla(medallistas)

        self.assertEqual(len(tp.paises), 10)
        self.assertIn("Italia", tp.paises)
        italia = tp.paises["Italia"]
        self.assertEqual(italia.oros, 0)
        self.assertEqual(italia.platas, 1)
        self.assertEqual(italia.bronces, 2)
        self.assertEqual(italia.puntaje, 5)