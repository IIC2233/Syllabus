from io import BytesIO
from os.path import join
from unittest import TestCase
from unittest.mock import patch

from cliente.main import Cliente
from servidor.main import Servidor
from tests_publicos.utils import assert_call_arguments, get_port


class VerificarCliente(TestCase):

    def setUp(self):
        """
        Prepara un cliente y sus atributos para poder correr los tests :)
        """
        mensaje = "¡Un ,saludo ,por ,parte ,del ,equipo ,docente!\n"
        chunks = dict(
            enumerate(
                map(
                    lambda x: bytes(x, 'utf-8'),
                    mensaje.split(',')
                )
            )
        )

        self.cliente = Cliente("Tanganana", 1234)
        self.cliente.bytes_por_chunk = chunks
        self.cliente.chunks_totales = len(chunks)
        self.cliente.archivo_completo = True
        self.cliente.archivo_nombre = "saluditos.txt"
        self.cliente.chunk_actual = 0

        self.cliente.socket.close()

    def test_guardar_archivo(self):
        """
        Verifica que el archivo recibido sea guardado íntegramente.
        """
        mock_file = BytesIO()
        mock_file._close = mock_file.close
        mock_file.close = lambda: None

        with patch("cliente.main.open", return_value=mock_file) as open:
            self.cliente.guardar_archivo()

            assert_call_arguments(
                open.call_args_list[0],
                join("cliente", "data", "saluditos.txt"),
                "file"
            )

            assert_call_arguments(
                open.call_args_list[0],
                "wb",
                "mode"
            )

            self.assertEqual(
                "¡Un saludo por parte del equipo docente!\n" ,
                mock_file.getvalue().decode('utf-8')
            )

            mock_file._close()

    def test_terminar_solicitud(self):
        """
        Verifica que el método ciente.terminar_solicitud reinicie los atributos
        usados y envíe el mensaje de termino.
        """

        cliente = self.cliente
        with patch("cliente.main.Cliente.enviar_mensaje") as enviar_mensaje, \
             patch("cliente.main.Mensaje") as mensaje:
            cliente.terminar_solicitud_archivo()

            assert_call_arguments(
                mensaje.call_args_list[0],
                "terminar_solicitud_archivo",
                "accion"
            )

            enviar_mensaje.assert_called()

        self.assertFalse(cliente.archivo_completo)
        self.assertEqual('', cliente.archivo_nombre)

        self.assertEqual(0, cliente.chunks_totales)
        self.assertEqual(0, cliente.chunk_actual)
        self.assertDictEqual({}, cliente.bytes_por_chunk)

class VerificarServidor(TestCase):

    def setUp(self):
        """
        Prepara un servidor para usar en los tests.
        """
        self.host = '127.0.0.1'
        self.port = get_port()

        self.servidor = Servidor(self.host, self.port)
        self.servidor.socket_servidor.close()

    def test_solicitar_chunk(self):
        """
        Verifica que solicitar chunk separe correctamente el archivo sin
        modificarlo, y entregue el chunk solicitado.
        """
        mensaje = ("Mientras hacen esta actividad" +
                   " me estoy echando distribuidos en la K202 :3").encode('utf-8')

        chunks = [
            b'Mientras ',
            b'hacen est',
            b'a activid',
            b'ad me est',
            b'oy echand',
            b'o distrib',
            b'uidos en ',
            b'la K202 :',
            b'3'
         ]

        mock_file = BytesIO(mensaje)
        mock_file._close = mock_file.close
        mock_file.close = lambda: None

        id = 3
        with patch("servidor.main.open", return_value=mock_file) as open:
            self.servidor.tamano_chunk = 9
            self.servidor.solicitudes_archivos[id] = "Final message.txt"


            for i in range(len(chunks)):
                mock_file.seek(0)

                chunk = self.servidor.solicitar_chunk(id_cliente=id, n_chunk=i)
                self.assertEqual(chunks[i], chunk)

                assert_call_arguments(
                    open.call_args_list[0],
                    join("servidor", "data", "Final message.txt"),
                    "file"
                )

        self.assertEqual(mensaje, mock_file.getvalue(), "Modificaste el archivo.")
