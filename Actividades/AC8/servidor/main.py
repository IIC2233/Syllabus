import json
import sys

from flask import Flask, request, Response
from wsgiref.simple_server import make_server

from dcconsumo import DCConsumo


app = Flask(__name__)

dcconsumo = DCConsumo()
dcconsumo.cargar_data()


def generar_respuesta(respuesta: dict, status_code: int) -> Response:
    return Response(
        response=json.dumps(respuesta),
        status=status_code,
        content_type='application/json'
    )


@app.route('/')
def hello_world() -> Response:
    return generar_respuesta({'msg': 'Hello World!'}, 200)


def obtener_saldo_total() -> Response:
    # TODO: Parte I
    pass


def obtener_saldo_banco(banco: str) -> Response:
    # TODO: Parte I
    pass


def obtener_transacciones(banco: str) -> Response:
    # TODO: Parte I
    pass


def agregar_gasto(banco: str) -> Response:
    # TODO: Parte I
    pass


def ajustar_saldo(banco: str) -> Response:
    # TODO: Parte I
    pass


def hacer_transferencia() -> Response:
    # TODO: Parte I
    pass


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
