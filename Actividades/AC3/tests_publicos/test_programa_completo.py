import unittest

from main import SistemaColas, NodoCliente
from tests_publicos.utils import timeout


class VerificarProgramaCompleto(unittest.TestCase):

    def setUp(self):
        """
        Para cada tests que se ejecute, se reiniciará el valor del
        atributo de clase 'identificador'
        """
        NodoCliente.identificador = 0

    @timeout()
    def test_completo(self):
        """
        Verifica el correcto funcionamiento del SistemaColas completo.
        """
        expected_order = [0, 1, 2, 5, 3, 4, 6]
        queue = SistemaColas()

        for _ in range(5):
            queue.agregar_persona(True)

        for _ in range(5, 7):
            queue.agregar_persona(False)

        iterator = iter(queue)

        for expected_index in expected_order:
            person = next(iterator)
            self.assertEqual(person.identificador, expected_index)

        with self.assertRaises(StopIteration):
            next(iterator)
