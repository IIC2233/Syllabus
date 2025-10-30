from unittest import TestCase
from socket import AF_INET, SOCK_STREAM, socket

from cliente.main import Cliente
from tests_publicos.utils import get_port


class VerificarInit(TestCase):
    def test_verificar_init(self):
        """
        Verifica que un cliente cree correctamente un socket.
        """
        cliente = Cliente(host='127.0.0.1', port=0) 

        with cliente.socket as sock:
            self.assertIsInstance(sock, socket)
            self.assertEqual(sock.family, AF_INET)
            self.assertEqual(sock.type, SOCK_STREAM)


class VerificarConectar(TestCase):
    def __init__(self, methodName = "runTest"):
        super().__init__(methodName)
        self.host = '127.0.0.1'
        self.port = 0

    def setUp(self):
        """
        Aplicado antes de cada test obtiene un nuevo puerto y crea un cliente y un servidor.
        """

        self.port = get_port()

        self.cliente = Cliente(host=self.host, port=self.port)

        self.servidor = socket()
        self.servidor.bind((self.host, self.port))
        self.servidor.listen()

    def tearDown(self):
        """
        Cierra los sockets usados en cada test.
        """
        self.cliente.socket.close()
        self.servidor.close()

    def test_verificar_conectar(self):
        """
        Verifica que Cliente.conectar() conecte al cliente al servidor usando Cliente.socket.
        """

        with self.servidor as servidor, self.cliente.socket as socket_cliente:
            self.cliente.conectar()
            sock, conn = servidor.accept()

            self.assertEqual(conn, socket_cliente.getsockname())
            sock.close()