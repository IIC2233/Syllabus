import unittest

from random import randint
from socket import error, socket, AF_INET, SOCK_STREAM
from threading import Thread

from servidor.main import Servidor


class VerificarConexion(unittest.TestCase):
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

    def test_init_socket_correcto(self):
        """
        Verifica que al instanciar el Servidor se
        cree un socket con los parámetros solicitados.
        """
        server = Servidor(self.host, self.port)

        with server.socket_servidor as sock:
            self.assertIsInstance(sock, socket)

            self.assertEqual(sock.family, AF_INET)
            self.assertEqual(sock.type, SOCK_STREAM)

    def test_bind_listen(self):
        """
        Verifica que sea posible conectarse al servidor
        después de ejecutar el método 'bind_listen'.
        """
        server = Servidor(self.host, self.port)

        with server.socket_servidor as sock:
            server.bind_listen()

            self.assertEqual(sock.getsockname(), (self.host, self.port))
            programming_sock = socket(sock.family, sock.type)

            programming_sock.connect((self.host, self.port))
            programming_sock.close()

    def test_aceptar_clientes(self):
        """
        Verifica que si sucede una conexión exitosa
        se le asigne un id y se guarden los datos del cliente.
        """
        server = Servidor(self.host, self.port)

        if not isinstance(server.socket_servidor, socket):
            server.socket_servidor = socket(AF_INET, SOCK_STREAM)

        with server.socket_servidor as sock:
            if sock.getsockname() == ('0.0.0.0', 0):
                sock.bind((self.host, self.port))
                sock.listen()

            thread_server = Thread(
                target=server.aceptar_clientes,
                daemon=True
            )

            thread_server.start()
            with socket(AF_INET, SOCK_STREAM) as client:
                client.connect((self.host, self.port))

                thread_server.join(1)

                self.assertEqual(len(server.clientes), 1)
                self.assertIsInstance(server.clientes[0][0], socket)
                self.assertEqual(server.clientes[0][1], client.getsockname())

    def test_desconectar_cliente(self):
        """
        Verifica que cuando se desconecte un cliente, se cierre su socket
        y se elimine correctamente del diccionario de clientes.
        """
        server = Servidor(self.host, self.port)

        with server.socket_servidor as sock:
            with socket() as client:
                server.clientes[3] = (client, 'AvenidaSiempreViva')

                server.desconectar_cliente(3)

                self.assertEqual(client.fileno(), -1)
                self.assertNotIn(3, server.clientes.keys())
