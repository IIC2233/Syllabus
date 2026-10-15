import socket
import sys

from cifrado import cifrar_mensaje, descrifrar_mensaje
from juego import JuegoOrdenarNumeros


class Servidor:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

        self.juego = JuegoOrdenarNumeros()

    def bind_listen(self):
        pass

    def cerrar_sockets(self):
        pass


if __name__ == '__main__':
    # Se recibe el puerto y host por consola:
    # Sintaxis: <comando python> servidor.py <puerto> <host>
    #     P.ej:          python3 servidor.py 4444 localhost
    # Si no llega uno de los valores, entonces se entrega un valor por defecto
    PORT = 23678 if len(sys.argv) < 2 else int(sys.argv[1])
    HOST = 'localhost' if len(sys.argv) < 3 else sys.argv[2]

    servidor = Servidor(HOST, PORT)
    servidor.bind_listen()

    try:
        pass
    except (KeyboardInterrupt, BrokenPipeError):
        pass
    finally:
        servidor.cerrar_sockets()

    exit(1)
