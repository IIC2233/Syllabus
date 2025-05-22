import unittest
import pickle

from random import randint
from socket import error, socket, AF_INET, SOCK_STREAM

from servidor.main import Servidor
from servidor.utils import Mensaje


class VerificarManejoDeMensajes(unittest.TestCase):
    def __init__(self, methodName = "runTest"):
        super().__init__(methodName)
        self.host = '127.0.0.1'
        self.port = randint(4000, 10000)

    def setUp(self):
        sock = socket(AF_INET, SOCK_STREAM)

        while True:
            try:
                sock.bind((self.host, self.port))
                sock.close()
                return
            except error:
                pass
            self.port = randint(4000, 10000)

    def test_enviar_mensaje(self):
        """
        Verifica que sea posible enviar mensajes desde
        el servidor hacia algún cliente.
        """
        server = Servidor(self.host, self.port)

        message = Mensaje('consultar_deudas', 'Juanito Pérez')

        if not isinstance(server.socket_servidor, socket):
            server.socket_servidor = socket(AF_INET, SOCK_STREAM)

        with server.socket_servidor as sock:
            if sock.getsockname() == ('0.0.0.0', 0):
                sock.bind((self.host, self.port))
                sock.listen()

            with socket() as programming_sock:
                programming_sock.connect(sock.getsockname())

                server.clientes[3] = tuple(sock.accept())

                msg_sent = pickle.loads(server.enviar_mensaje(3, message))
                self.assertEqual(str(msg_sent), str(message))

                msg_received = pickle.loads(programming_sock.recv(4100))
                self.assertEqual(str(msg_received), str(message))

    def test_recibir_mensaje(self):
        """
        Verifica que el servidor pueda recibir mensajes.
        """
        server = Servidor(self.host, self.port)
        message = Mensaje('agregar_transaccion', {'Joao': 10})

        if not isinstance(server.socket_servidor, socket):
            server.socket_servidor = socket(AF_INET, SOCK_STREAM)

        with server.socket_servidor as sock:
            if sock.getsockname() == ('0.0.0.0', 0):
                sock.bind((self.host, self.port))

                sock.listen()

            with socket() as programming_sock:
                programming_sock.connect(sock.getsockname())

                server.clientes[3] = tuple(sock.accept())

                programming_sock.sendall(pickle.dumps(message))

                msg_sent = server.recibir_mensaje(3)
                self.assertEqual(str(msg_sent), str(message))
