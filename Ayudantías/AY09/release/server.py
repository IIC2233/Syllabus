from flask import Flask, request, Response, send_from_directory
import json

from utils import AUTH_TOKEN, comparar_juegos

app = Flask(__name__)


"""No MODIFICAR: Rutas para servir la app y cargar los juegos desde el JSON"""
@app.route('/')
def index():
    return send_from_directory('app', 'index.html')


@app.route('/app/<path:filename>')
def app_static(filename):
    return send_from_directory('app', filename)

def cargar_juegos() -> list:
    with open('juegos.json', encoding='utf-8') as file:
        return json.load(file)


# --------------------------------------------------------------------------- #
#  GET  /juegos          → lista completa de juegos
#  POST /juegos          → agregar un nuevo juego (requiere auth)
# --------------------------------------------------------------------------- #
@app.route('/juegos', methods=['GET', 'POST'])
def acciones_juegos():
    if request.method == 'GET':
        return Response(json.dumps(cargar_juegos(), ensure_ascii=False),
                        status=200, content_type='application/json')

    # --- POST ---
    if request.headers.get('Authorization') != AUTH_TOKEN:
        return Response(json.dumps({"error": "No autorizado"}, ensure_ascii=False),
                        status=401, content_type='application/json')

    body = request.get_json(force=True)
    try:
        id_juego = int(body['id'])
        nombre   = str(body['nombre'])
        generos  = list(body['generos'])
        stats    = body['stats']
        rating, horas, precio = int(stats['rating']), int(stats['horas_juego']), int(stats['precio'])
    except KeyError:
        return Response(json.dumps({'error': 'Faltan campos'}, ensure_ascii=False),
                        status=400, content_type='application/json')
    except (TypeError, ValueError):
        return Response(json.dumps({"error": "Tipos de datos inválidos en uno o más campos"}, ensure_ascii=False),
                        status=400, content_type='application/json')

    juegos = cargar_juegos()
    if any(id_juego == j['id'] for j in juegos):
        return Response(json.dumps({'error': 'Ya existe un juego con ese id'}, ensure_ascii=False),
                        status=409, content_type='application/json')
    if any(nombre == j['nombre'] for j in juegos):
        return Response(json.dumps({'error': 'Ya existe un juego con ese nombre'}, ensure_ascii=False),
                        status=409, content_type='application/json')

    nuevo_juego = {
        'id': id_juego, 'nombre': nombre, 'generos': generos,
        'stats': {'rating': rating, 'horas_juego': horas, 'precio': precio}
    }
    juegos.append(nuevo_juego)

    with open('juegos.json', 'w', encoding='utf-8') as file:
        json.dump(juegos, file, indent=2, ensure_ascii=False)

    return Response(json.dumps({'Juego Agregado': nuevo_juego}, ensure_ascii=False),
                    status=201, content_type='application/json')


# --------------------------------------------------------------------------- #
#  GET /juegos/generos   → lista de géneros únicos
# --------------------------------------------------------------------------- #
@app.route('/juegos/generos', methods=['GET'])
def obtener_generos():
    generos = set()
    for juego in cargar_juegos():
        for genero in juego['generos']:
            generos.add(genero)
    return Response(json.dumps(list(generos), ensure_ascii=False),
                    status=200, content_type='application/json')


# --------------------------------------------------------------------------- #
#  GET /juegos/generos/<genero>  → nombres de juegos de ese género
# --------------------------------------------------------------------------- #
@app.route('/juegos/generos/<string:genero>', methods=['GET'])
def juegos_por_genero(genero):
    nombres = [j['nombre'] for j in cargar_juegos() if genero in j['generos']]
    return Response(json.dumps(nombres, ensure_ascii=False),
                    status=200, content_type='application/json')


# --------------------------------------------------------------------------- #
#  GET    /juegos/<identifier>  → obtener juego por id o nombre
#  PATCH  /juegos/<identifier>  → actualizar stats (requiere auth)
#  DELETE /juegos/<identifier>  → eliminar juego   (requiere auth)
# --------------------------------------------------------------------------- #
@app.route('/juegos/<identifier>', methods=['GET', 'PATCH', 'DELETE'])
def obtener_juego(identifier: str):
    pass


# --------------------------------------------------------------------------- #
#  GET /comparar/<id_juego_1>/<id_juego_2>
# --------------------------------------------------------------------------- #
@app.route('/comparar/<id_juego_1>/<id_juego_2>', methods=['GET'])
def comparar_endpoint(id_juego_1: str, id_juego_2: str):
    pass


# --------------------------------------------------------------------------- #
#  GET /juegos/   (con query params opcionales)
#  Filtra juegos por: genero (list), rating (>=), horas_juego (>=), precio (<=)
# --------------------------------------------------------------------------- #
@app.route('/juegos/', methods=['GET'])
def obtener_condicional():
    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
