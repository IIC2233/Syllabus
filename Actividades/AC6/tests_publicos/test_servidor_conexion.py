from unittest import TestCase
from unittest.mock import patch
from threading import Thread
from socket import AF_INET, SOCK_STREAM, socket

from tests_publicos.utils import get_port
from servidor.main import Servidor


class VerificarServidorParteI(TestCase):

    def setUp(self):
        self.host = '127.0.0.1'
        self.port = get_port()

        self.servidor = Servidor(host=self.host, port=self.port)

    def test_init(self):
        """
        Verifica que un servidor cree correctamente un socket.
        """
        with self.servidor.socket_servidor as sock:
            self.assertIsInstance(sock, socket)

            self.assertEqual(AF_INET, sock.family)
            self.assertEqual(SOCK_STREAM, sock.type)

    def test_bind_listen(self):
        """
        Verifica que el método bind_listen asocie correctamente los datos y habilite conexiones.
        """

        with self.servidor.socket_servidor as socket_servidor, socket() as cliente:
            self.servidor.bind_listen()

            self.assertEqual((self.host, self.port), socket_servidor.getsockname())

            cliente.connect((self.host, self.port))

    @patch("servidor.main.Servidor.manejar_flujo_cliente")
    def test_aceptar_clientes(self, manejar_flujo_cliente):
        """
        Verifica que el método aceptar_clientes acepte correctamente los clientes, debes pasar bind_listen()
        """

        self.test_bind_listen()

        self.setUp()
        servidor = self.servidor

        servidor.bind_listen()
        with servidor.socket_servidor as sock, \
             socket() as cliente_1, \
             socket() as cliente_2:

            thread_server = Thread(
                target=servidor.aceptar_clientes,
                daemon=True
            )

            thread_server.start()

            cliente_1.connect(sock.getsockname())
            cliente_2.connect(sock.getsockname())

            thread_server.join(0.1)

            self.assertEqual(2, len(servidor.clientes))

            for id, cliente in enumerate([cliente_1, cliente_2]):
                self.assertIsInstance(servidor.clientes[id][0], socket)
                self.assertEqual(servidor.clientes[id][1], cliente.getsockname())

    def test_desconectar_cliente(self):
        """
        Robado del semestre pasado
        """
        servidor = Servidor(self.host, self.port)

        with servidor.socket_servidor as sock, socket() as client:
            servidor.clientes[3] = (client, 'Bellota 8')

            servidor.desconectar_cliente(3)

            self.assertEqual(-1, client.fileno())
            self.assertNotIn(3, servidor.clientes.keys())
