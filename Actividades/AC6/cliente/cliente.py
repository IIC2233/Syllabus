import socket
import sys

from cifrado import cifrar_bytes_mensaje, descifrar_bytes_mensaje


class Cliente:
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port

    def cerrar_socket(self):
        pass


if __name__ == '__main__':
    # Se recibe el puerto y host por consola:
    # Sintaxis: <comando python> cliente.py <puerto> <host>
    #     P.ej:          python3 cliente.py 4444 localhost
    # Si no llega uno de los valores, entonces se entrega un valor por defecto
    PORT = 23678 if len(sys.argv) < 2 else int(sys.argv[1])
    HOST = 'localhost' if len(sys.argv) < 3 else sys.argv[2]

    cliente = Cliente(HOST, PORT)
    try:
        pass
    except KeyboardInterrupt:
        cliente.cerrar_socket()
