import unittest

from pickle import loads, dumps
from random import randint
from socket import error, socket, AF_INET, SOCK_STREAM

from cliente.main import Cliente
from cliente.utils import Mensaje


class VerificarClienteConexion(unittest.TestCase):
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

    def test_cliente_init(self):
        """
        Verifica que el cliente asigne los argumentos al socket de forma correcta.
        """

        client = Cliente(self.host, self.port)

        with client.socket as sock:
            self.assertIsInstance(sock, socket)
            self.assertEqual(sock.family, AF_INET)
            self.assertEqual(sock.type, SOCK_STREAM)

    def test_conectar_a_servidor(self):
        """
        Verifica que el cliente pueda conectarse al servidor.
        """

        client = Cliente(self.host, self.port)
        if not isinstance(client.socket, socket):
            client.socket = socket()

        with socket() as server:
            with client.socket as sock:
                server.bind((self.host, self.port))
                server.listen()

                client.conectar()
                addr, conn = server.accept()

                self.assertEqual(conn, sock.getsockname())
