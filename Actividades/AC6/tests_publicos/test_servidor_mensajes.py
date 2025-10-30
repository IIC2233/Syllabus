import unittest
import pickle
from socket import socket

from servidor.main import Servidor
from servidor.utils import Mensaje
from tests_publicos.utils import get_port


class VerificarManejoDeMensajes(unittest.TestCase):
    def __init__(self, methodName = "runTest"):
        super().__init__(methodName)
        self.host = '127.0.0.1'
        self.port = 0

    def setUp(self):
        """
        Preparara un nuevo servidor para los tests.
        """
        self.port = get_port()

        self.servidor = Servidor(self.host, self.port)
        self.servidor.bind_listen()

    def tearDown(self):
        self.servidor.socket_servidor.close()

    def test_enviar_mensaje(self):
        """
        Verifica que sea posible enviar mensajes desde
        el servidor hacia algún cliente.
        """
        message = Mensaje('saludar')
        servidor = self.servidor

        with servidor.socket_servidor as socket_servidor, socket() as cliente:
            cliente.connect(socket_servidor.getsockname())
            servidor.clientes[3] = tuple(socket_servidor.accept())

            msg_sent = pickle.loads(servidor.enviar_mensaje(3, message))
            self.assertEqual(str(msg_sent), str(message))

            msg_received = pickle.loads(cliente.recv(4100))
            self.assertEqual(str(msg_received), str(message))

    def test_recibir_mensaje(self):
        """
        Verifica que el servidor pueda recibir mensajes.
        """
        message = Mensaje('saludar')
        servidor = self.servidor

        with servidor.socket_servidor as sock, socket() as cliente:
            cliente.connect(sock.getsockname())
            servidor.clientes[3] = tuple(sock.accept())

            cliente.sendall(pickle.dumps(message))

            msg_sent = servidor.recibir_mensaje(3)
            self.assertEqual(str(msg_sent), str(message))
