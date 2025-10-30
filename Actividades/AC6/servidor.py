import sys

from servidor.main import Servidor


if __name__ == '__main__':
    print(
        'Iniciando programa.',
        'Utiliza "Ctrl + C" o "Cmd + C" para finalizar el programa.'
    )

    HOST = 'localhost'
    PORT = 4160 if len(sys.argv) < 2 else int(sys.argv[1])

    servidor = Servidor(HOST, PORT)
    try:
        servidor.iniciar_servidor()
    except KeyboardInterrupt:
        pass
    finally:
        servidor.cerrar_servidor()
