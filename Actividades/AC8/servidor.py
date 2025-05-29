import sys

from wsgiref.simple_server import make_server

from servidor.main import app


if __name__ == '__main__':
    HOST = 'localhost'
    PORT = 4160 if len(sys.argv) < 2 else int(sys.argv[1])

    with make_server(HOST, PORT, app) as httpd:
        try:
            print(f'Iniciando servidor: http://{HOST}:{PORT}')
            print('''Utiliza 'Ctrl + C' o 'Cmd + C' para apagar el servidor''')
            httpd.serve_forever()
        except KeyboardInterrupt:
            print('\nApagando servidor')
            httpd.shutdown()
