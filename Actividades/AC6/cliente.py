import sys

from cliente.main import Cliente


if __name__ == '__main__':
    HOST = 'localhost'
    PORT = 4160 if len(sys.argv) < 2 else int(sys.argv[1])

    cliente = Cliente(HOST, PORT)
    cliente.iniciar_cliente()
