from unittest import TestCase
from socket import socket
from pickle import loads, dumps

from tests_publicos.utils import get_port
from cliente.main import Cliente
from cliente.utils import Mensaje


class VerificarManejoDeMensajes(TestCase):
    def setUp(self):
        self.host = '127.0.0.1'
        self.port = get_port()

        self.mensaje = Mensaje("recibir_saluditos")

        self.servidor = socket()
        self.servidor.bind((self.host, self.port))
        self.servidor.listen()

    def test_cliente_enviar_mensaje(self):
        """
        Verifica que el cliente retorne lo solicitado y envíe los datos de forma correcta.
        """
        cliente = Cliente(self.host, self.port)

        with self.servidor as server, cliente.socket as socket_cliente:
            cliente.conectar()

            conn, addr = self.servidor.accept()

            msg_send = loads(cliente.enviar_mensaje(self.mensaje))
            msg_recv = loads(conn.recv(8000))

            self.assertEqual(str(msg_send), str(self.mensaje))
            self.assertEqual(str(msg_recv), str(self.mensaje))

    def test_cliente_recibir_mensaje(self):
        """
        Verifica que el cliente retorne lo solicitado y reciba los datos de forma correcta.
        """
        cliente = Cliente(self.host, self.port)

        with self.servidor as server, cliente.socket as socket_cliente:
            cliente.conectar()

            conn, addr = self.servidor.accept()
            conn.sendall(dumps(self.mensaje))

            msg_recv = cliente.recibir_mensaje()

            self.assertEqual(str(msg_recv), str(self.mensaje))
