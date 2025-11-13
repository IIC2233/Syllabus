from unittest import TestCase

from main import limpiar_header_corrompido
from tests_publicos.data import headers


class VerificaRegexp(TestCase):

    def test_limpiar_header_corrompido(self):
        """
        Verifica que limpiar_header_corrompido sea capaz de remover los caracteres solicitados.
        """

        for header in headers:
            with self.subTest(header=header):
                header_limpio = limpiar_header_corrompido(header[0])
                header_esperado = header[1]

                self.assertEqual(header_limpio, header_esperado)
