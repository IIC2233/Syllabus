import unittest

from pickle import loads, dumps
from random import randint
from socket import error, socket, AF_INET, SOCK_STREAM

from cliente.main import Cliente
from cliente.utils import Mensaje


class VerificarManejoDeBytes(unittest.TestCase):
    def __init__(self, methodName = "runTest"):
        super().__init__(methodName)
        self.host = '127.0.0.1'
        self.port = randint(4000, 10000)

        self.port_servidor = randint(4000, 10000)

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

    def test_cliente_enviar_mensaje(self):
        """
        Verifica que el cliente retorne lo solicitado y envíe los datos de forma correcta.
        """

        client = Cliente(self.host, self.port)

        if not isinstance(client.socket, socket):
            client.socket = socket()

        with socket() as server:
            server.bind((self.host, self.port))
            server.listen()

            with client.socket as sock:
                sock.connect(server.getsockname())
                conn, addr = server.accept()

                message = Mensaje('consultar_deuda',
                                  'Arturo Prat')

                msg_send = loads(client.enviar_mensaje(message))
                msg_recv = loads(conn.recv(8000))

                self.assertEqual(str(msg_send), str(message))
                self.assertEqual(str(msg_recv), str(message))

    def test_cliente_recibir_mensaje(self):
        """
        Verifica que el cliente pueda recibir mensajes del el servidor.
        """

        client = Cliente(self.host, self.port)

        if not isinstance(client.socket, socket):
            client.socket = socket()

        with socket() as server:
            server.bind((self.host, self.port))
            server.listen()

            with client.socket as sock:
                sock.connect(server.getsockname())
                conn, addr = server.accept()

                message = Mensaje('consultar_deuda',
                                  'Arturo Prat')

                conn.sendall(dumps(message))
                msg_recv = client.recibir_mensaje()

                self.assertEqual(str(msg_recv), str(message))
