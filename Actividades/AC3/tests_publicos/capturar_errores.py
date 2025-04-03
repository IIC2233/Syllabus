import unittest

from io import StringIO
from unittest.mock import patch

from utils import Conductor
from main import DCConductor


class VerificarChequearConductoresApp(unittest.TestCase):
    def test_no_hay_conductores_o_registro(self):
        """
        Verifica que se imprima el texto correspondiente cuando
        faltan todos los conductores y/o el registro.
        """
        casos = (
            (dict(), list()),
            ({"Joao": 'LOLXD1'}, list()),
            (dict(), ['Joao'])
        )

        for caso in casos:
            retorno = DCConductor(*caso).chequear_conductores_app()
            self.assertEqual(retorno,
                             "Falta parte de los datos"
                             " necesarios para hacer la revision.")

    def test_no_hay_errores(self):
        """
        Verifica que se retorne correctamente cuando no ocurren errores.
        """

        conductores = [
            Conductor("Joao", "9312320-6", "j@mail.com",
                      "940404040", "LOLXSA"),
            Conductor("Maria", "4567891-2", "maria@mail.com",
                      "987654321", "ABCDEF"),
            Conductor("Carlos", "1234567-8",
                      "carlos@mail.com", "912345678", "GHIJKL")
        ]

        registro = {
            "Joao": "LOLXSA",
            "Maria": "ABCDEF",
            "Carlos": "GHIJKL"
        }

        with patch('sys.stdout', new=StringIO()) as output:
            retorno = DCConductor(
                registro, conductores).chequear_conductores_app()

        texto_print = output.getvalue().strip()
        self.assertEqual(texto_print, '')

        self.assertEqual(retorno,
                         "La cuenta de datos erroneos fue: 0.")

    def test_hay_errores(self):
        """
        Verifica que imprima y retorne de forma correcta cuando
        hay al menos un error de cada dato, y solo 1 conductor es válido.
        """

        conductores = [
            Conductor("Joao", "93123200-6", "j@mail.com",
                      "940404040", "LOLXSA"),
            Conductor("Maria", "45267991-2", "maria@mail.com",
                      "287654321", "ABCDEF"),
            Conductor("Carlos", "12.334.567-8",
                      "carlos@mail.com", "912345678", "GHIJKL"),
            Conductor("Ana", "7654321-9", "ana@mail.com",
                      "933344455", "MNOPQR")
        ]

        registro = {
            "Joao": "",
            "Maria": "ABCDEF",
            "Carlos": "GHIJKL",
            "Ana": "MNOPQR"
        }

        errores = [
            "La patente LOLXSA no es la registrada para Joao.",
            "El celular 287654321 no comienza con 9.",
            "El rut 12.334.567-8 contiene puntos."
        ]

        with patch('sys.stdout', new=StringIO()) as output:
            retorno = DCConductor(
                registro, conductores).chequear_conductores_app()

        self.assertEqual(retorno,
                         'La cuenta de datos erroneos fue: 3.')
        for error in errores:
            self.assertIn(error, output.getvalue())
