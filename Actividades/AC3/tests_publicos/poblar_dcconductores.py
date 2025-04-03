import unittest

from io import StringIO
from os import path
from unittest.mock import patch

from main import CargadorArchivos


class VerificarCargarAutos(unittest.TestCase):

    def test_cargar_datos_vacio_conductores(self):
        """
        Verifica que se imprima el texto cuando
        solo hay conductores.
        """

        with patch('sys.stdout', new=StringIO()) as output:
            CargadorArchivos().cargar_datos(
                path.join("data", "no_existo.json"),
                path.join("data", "conductores.csv")
            )

            texto_print = output.getvalue().strip()
            self.assertEqual(texto_print,
                             'El archivo data/no_existo.json no existe.')

    def test_cargar_datos_vacio_registro_oficial(self):
        """
        Verifica que se imprima el texto cuando
        solo hay registro_oficial.
        """

        with patch('sys.stdout', new=StringIO()) as output:
            CargadorArchivos().cargar_datos(
                path.join("data", "registro_oficial.json"),
                path.join("data", "conductores.UwU")
            )

            texto_print = output.getvalue().strip()
            self.assertEqual(texto_print,
                             'El archivo data/conductores.UwU no existe.')

    def test_cargar_datos_vacio(self):
        """
        Verifica que se impriman los textos cuando
        no hay ningún archivo existente.
        """

        with patch('sys.stdout', new=StringIO()) as output:
            CargadorArchivos().cargar_datos(
                path.join("data", "registro_oficial.yeison"),
                path.join("data", "conductores.ceuveese")
            )

            texto_print = output.getvalue()

            self.assertIn(
                'El archivo data/conductores.ceuveese no existe.',
                texto_print)

            self.assertIn(
                'El archivo data/registro_oficial.yeison no existe.',
                texto_print)

    def test_cargar_datos_correctamente(self):
        """
        Verifica que no se imprima nada al cargar datos existentes.
        """
        with patch('sys.stdout', new=StringIO()) as output:
            CargadorArchivos().cargar_datos(
                path.join("data", "registro_oficial.json"),
                path.join("data", "conductores.csv")
            )

            texto_print = output.getvalue().strip()
            self.assertEqual(texto_print,
                             '')
