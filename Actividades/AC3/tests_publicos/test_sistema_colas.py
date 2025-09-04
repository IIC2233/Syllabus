import unittest
from unittest.mock import patch

from main import SistemaColas, NodoCliente
from tests_publicos.utils import timeout


class VerificarAgregarPersona(unittest.TestCase):

    @timeout()
    def test_agregar_persona_retorno(self):
        """
        Verifica que el método no retorne nada al ser llamado.
        """
        queues = SistemaColas()
        value = queues.agregar_persona(False)
        self.assertIsNone(value)

    @timeout()
    def test_agregar_persona_crear_nodo(self):
        """
        Verifica que el método cree un nodo cliente cada vez que sea llamado.
        """
        queues = SistemaColas()
        with patch("main.NodoCliente") as mock:
            queues.agregar_persona(True)
            mock.assert_called()
            queues.agregar_persona(False)
            self.assertEqual(mock.call_count, 2)

    @timeout()
    def test_agregar_persona_normal(self):
        """
        Verifica que el método agregue correctamente una persona normal.
        """
        queues = SistemaColas()
        self.assertIsNone(queues.cola_normal)

        queues.agregar_persona(False)
        self.assertIsInstance(queues.cola_normal, NodoCliente)
        self.assertFalse(queues.cola_normal.preferencial)


    @timeout()
    def test_agregar_persona_preferencial(self):
        """
        Verifica que el método agregue correctamente una persona preferencial.
        """
        queues = SistemaColas()
        self.assertIsNone(queues.cola_preferencial)

        queues.agregar_persona(True)
        self.assertIsInstance(queues.cola_preferencial, NodoCliente)
        self.assertTrue(queues.cola_preferencial.preferencial)

    @timeout()
    def test_agregar_personas_normales(self):
        """
        Verifica que el método agregue correctamente las personas normales
        en su cola correspondiente.
        """
        clients = 10
        queues = SistemaColas()

        count = 0
        for client in range(clients):
            queues.agregar_persona(False)

            if client == 0:
                next_client = queues.cola_normal
            else:
                next_client = next_client.siguiente

            if next_client:
                self.assertFalse(next_client.preferencial)
                count += 1

        self.assertEqual(count, clients)

    @timeout()
    def test_agregar_personas_preferenciales(self):
        """
        Verifica que el método agregue correctamente las personas
        preferenciales en su cola correspondiente.
        """
        clients = 10
        queues = SistemaColas()

        count = 0
        for client in range(clients):
            queues.agregar_persona(True)

            if client == 0:
                next_client = queues.cola_preferencial
            else:
                next_client = next_client.siguiente

            if next_client:
                self.assertTrue(next_client.preferencial)
                count += 1

        self.assertEqual(count, clients)

    @timeout()
    def test_agregar_personas(self):
        """
        Verifica que el método agregue correctamente tanto personas
        preferenciales como normales en sus colas correspondientes.
        """
        preferentials = [True, False, False, True, True, False, True, False,
                         False, True, True]

        queues = SistemaColas()
        count_preferential = 0
        count_normal = 0

        for preferential in preferentials:
            queues.agregar_persona(preferential)

            # Se obtiene el NodoCliente que contiene la persona que
            # acaba de ser agregada al SistemaColas.
            if preferential:
                if count_preferential == 0:
                    preferential_next = queues.cola_preferencial
                else:
                    preferential_next = preferential_next.siguiente

                count_preferential += 1

            else:
                if count_normal == 0:
                    normal_next = queues.cola_normal
                else:
                    normal_next = normal_next.siguiente

                count_normal += 1

            if preferential and preferential_next:
                next_client = preferential_next
            if (not preferential) and normal_next:
                next_client = normal_next

            # Se verifica que el nodo obtenido corresponda al esperado.
            if next_client:
                self.assertEqual(next_client.preferencial, preferential)


class Verificar__len__(unittest.TestCase):

    @timeout()
    def test__len__retorno(self):
        """
        Verifica que el método retorne el tipo de dato esperado.
        """
        queues = SistemaColas()
        length = len(queues)
        self.assertIsInstance(length, int)

    @timeout()
    def test__len__normal(self):
        """
        Verifica que el método retorne la cantidad esperada cuando
        solo se agregan personas normales.
        """
        expected_length = 10

        queues = SistemaColas()
        for _ in range(expected_length):
            queues.agregar_persona(False)

        length = len(queues)
        self.assertEqual(length, expected_length)

    @timeout()
    def test__len__preferencial(self):
        """
        Verifica que el método retorne la cantidad esperada cuando
        solo se agregan personas preferenciales.
        """
        expected_length = 12

        queues = SistemaColas()
        for _ in range(expected_length):
            queues.agregar_persona(True)

        length = len(queues)
        self.assertEqual(length, expected_length)

    @timeout()
    def test__len__revuelto(self):
        """
        Verifica que el método retorne la cantidad esperada cuando
        se agregan tanto personas preferenciales como normales.
        """
        expected_length = 12

        queues = SistemaColas()
        for _ in range(expected_length):
            queues.agregar_persona(True)
            queues.agregar_persona(False)

        expected_length *= 2

        length = len(queues)
        self.assertEqual(length, expected_length)
