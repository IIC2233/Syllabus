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
    campo = 'id' if identifier.isdigit() else 'nombre'
    juego = None

    juegos = cargar_juegos()
    for pos, juego_data in enumerate(juegos):
        if str(juego_data[campo]) == str(identifier):
            juego, position = juego_data, pos
            break

    if not juego:
        return Response(json.dumps({"error": "Juego no encontrado"}, ensure_ascii=False),
                        status=404, content_type='application/json')
    if request.method == 'GET':
        return Response(json.dumps(juego, ensure_ascii=False),
                        status=200, content_type='application/json')

    if request.headers.get('Authorization') != AUTH_TOKEN:
        return Response(json.dumps({"error": "No autorizado"}, ensure_ascii=False),
                        status=401, content_type='application/json')

    if request.method == 'PATCH':
        body = request.get_json(force=True)
        for key in body:
            if key in juego['stats']:
                try:
                    juego['stats'][key] = int(body[key])
                except (TypeError, ValueError):
                    return Response(json.dumps({"error": "Tipos de datos inválidos en uno o más campos"}, ensure_ascii=False),
                                    status=400, content_type='application/json')
        output = {'Estadísticas Modificadas': juego}
    else:
        juegos.pop(position)
        output = {'Juego Eliminado': juego}

    with open('juegos.json', 'w', encoding='utf-8') as file:
        json.dump(juegos, file, indent=2, ensure_ascii=False)

    return Response(json.dumps(output, ensure_ascii=False),
                    status=200, content_type='application/json')


# --------------------------------------------------------------------------- #
#  GET /comparar/<id_juego_1>/<id_juego_2>
# --------------------------------------------------------------------------- #
@app.route('/comparar/<id_juego_1>/<id_juego_2>', methods=['GET'])
def comparar_endpoint(id_juego_1: str, id_juego_2: str):
    j1 = obtener_juego(id_juego_1).get_json()
    j2 = obtener_juego(id_juego_2).get_json()
    try:
        j1['stats'], j2['stats']
    except KeyError:
        return Response(json.dumps({"error": "Uno o más de los juegos no encontrados"}, ensure_ascii=False),
                        status=404, content_type='application/json')
    ganador = comparar_juegos(j1, j2)
    return Response(
        json.dumps({'Comparativa': f"{j1['nombre']} vs {j2['nombre']}", 'ganador': ganador['nombre']}, ensure_ascii=False),
        status=200, content_type='application/json'
    )


# --------------------------------------------------------------------------- #
#  GET /juegos/   (con query params opcionales)
#  Filtra juegos por: genero (list), rating (>=), horas_juego (>=), precio (<=)
# --------------------------------------------------------------------------- #
@app.route('/juegos/', methods=['GET'])
def obtener_condicional():
    generos_buscados = request.args.getlist('genero', type=str)
    # alternativamente: pedimos que el argumento sea strings separados por comas
    # (no funciona para la parte de app web)
    # generos_buscados = request.args.get('genero', type=str)
    # generos_buscados = generos_buscados.split(",") if generos_buscados else []

    rating_min  = request.args.get('rating',      type=int)
    horas_min   = request.args.get('horas_juego', type=int)
    precio_max  = request.args.get('precio',      type=int)

    if not any([generos_buscados, rating_min, horas_min, precio_max]):
        return Response(json.dumps({"error": "Debe proporcionar al menos un criterio de búsqueda (?genero=, ?rating=, ?horas_juego=, ?precio=)"}, ensure_ascii=False),
                        status=400, content_type='application/json')

    juegos = cargar_juegos()
    resultados = []

    set_generos_buscados = set(generos_buscados)

    for juego in juegos:
        if generos_buscados and not set_generos_buscados.issubset(set(juego['generos'])):
            continue
        if rating_min is not None and juego['stats']['rating'] < rating_min:
            continue
        if horas_min is not None and juego['stats']['horas_juego'] < horas_min:
            continue
        if precio_max is not None and juego['stats']['precio'] > precio_max:
            continue
        resultados.append(juego)

    return Response(json.dumps(resultados, ensure_ascii=False),
                    status=200, content_type='application/json')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
