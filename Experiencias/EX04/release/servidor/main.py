import sys

from flask import Flask, json, request, Response
from wsgiref.simple_server import make_server

from dccitas import DCCitas


app = Flask(__name__)

dccitas = DCCitas()
dccitas.cargar_datos()


def responder_json(codigo_estado, **body) -> Response:
    body = json.dumps(body)
    return Response(status=codigo_estado, response=body, content_type='application/json')

@app.route('/')
def hello_world() -> Response:
    return Response('Hello World!', 200)

@app.route('/registrar', methods=['POST'])
def registrar_usuario() -> Response:
    # TODO Parte 2.1: Para completar la solicitud hay 
    # que obtener el nombre y password que vienen en el body.
    nombre = None
    password = None

    dccitas.registrar_usuario(nombre, password)
    return responder_json(201, msg='Usuario registrado exitosamente')


@app.route('/eliminar', methods=['DELETE'])
def eliminar_usuario() -> Response:
    # TODO Parte 2.2: Para completar la solicitud hay 
    # que obtener el nombre desde el url.
    dccitas.eliminar_usuario(nombre)
    return responder_json(204, msg='Usuario eliminado exitosamente')


@app.route('/iniciar_sesion', methods=['POST'])
def iniciar_sesion() -> Response:
    # TODO Parte 2.3: El método se cae cuando las credenciales no son correctas,
    # hay que manejar el error.
    body_data = request.get_json(force=True)
    nombre = body_data['nombre']
    password = body_data['password']

    token = dccitas.iniciar_sesion(nombre, password)
    return responder_json(200, msg='Sesión iniciada exitosamente', token=token)


@app.route('/registrar_coordenadas', methods=['PATCH'])
def registrar_coordenadas() -> Response:
    # TODO Parte 2.4: Para completar la solicitud hay que obtener el token que
    # fue entregado en los headers y validar que le corresponda al usuario
    # con el que estamos trabajando.
    nombre = request.get_json(force=True).get('nombre')
    coordenadas = request.get_json(force=True).get('coordenadas')
    token = None

    dccitas.registrar_coordenadas(nombre, coordenadas)
    return responder_json(200, msg='Coordenadas registradas exitosamente')


@app.route('/encontrar_cita', methods=['GET'])
def agregar_gasto() -> Response:
    # TODO Parte 2.5: Para completar la solicitud hay que obtener desde 
    # los argumentos la cantidad de candidatos que hay que buscar. Como es un
    # valor opcional, si no fue entregado entonces se debe utilizar el valor 1.
    nombre = request.get_json(force=True).get('nombre')
    token = request.headers.get('Authorization', type=str)
    cantidad = None

    try:
        dccitas.validar_token(nombre, token)
    except ValueError as e:
        return responder_json(401, error=str(e))

    candidatos = dccitas.encontrar_citas(nombre, cantidad)
    return responder_json(200, msg='Candidatos/as encontrados', candidatos=candidatos)


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
