from flask import Flask, request, Response
import json

from utils import dano_ataque, AUTH_TOKEN

app = Flask(__name__)

def cargar_pokemons() -> list:
    with open('pokemon.json', encoding = 'utf-8') as file:
        return json.load(file)

@app.route('/pokedex', methods=['GET', 'POST'])
def acciones_pokedex():
    if request.method == 'GET':
        return Response(json.dumps(cargar_pokemons(), ensure_ascii=False), status=200, content_type='application/json')
    
    if request.headers.get('Authorization') != AUTH_TOKEN:
        return Response(json.dumps({"error": "No autorizado"}, ensure_ascii=False), status=401, content_type='application/json')

    body = request.get_json(force=True)
    try:
        id, nombre = int(body['id']), str(body['nombre'])
        tipos, stats = list(body['tipos']), body['stats']
        hp, atk, spd = int(stats['hp']), int(stats['atk']), int(stats['spd'])

    except KeyError:
        return Response(json.dumps({'error': 'Faltan campos'}, ensure_ascii=False), status=400, content_type='application/json')
    except (TypeError, ValueError):
        return Response(json.dumps({"error": "Tipos de datos inválidos en uno o más campos"}, ensure_ascii=False), status=400, content_type='application/json')
    
    pokemons = cargar_pokemons()
    if any(id == pokemon['id'] for pokemon in pokemons):
        return Response(json.dumps({'error': 'Ya existe un pokemon con ese id'}, ensure_ascii=False), status=409, content_type='application/json')
    if any(nombre == pokemon['nombre'] for pokemon in pokemons):
        return Response(json.dumps({'error': 'Ya existe un pokemon con ese nombre'}, ensure_ascii=False), status=409, content_type='application/json')

    nuevo_pokemon = {
        'id': id, 'nombre': nombre, 'tipos': tipos, 
            'stats': {'hp': hp, 'atk': atk, 'spd': spd}
    }

    pokemons.append(nuevo_pokemon)

    with open('pokemon.json', 'w', encoding = 'utf-8',) as file:
        json.dump(pokemons, file, indent=2, ensure_ascii=False)
    
    return Response(json.dumps({'Pokemon Agregado': nuevo_pokemon}, ensure_ascii=False), status=201, content_type='application/json')

@app.route('/pokedex/tipos', methods = ['GET'])
def obtener_tipos():
    tipos = set()
    for pokemon in cargar_pokemons():
        for tipo in pokemon['tipos']:
            tipos.add(tipo)
    return Response(json.dumps(list(tipos), ensure_ascii=False), status=200, content_type='application/json')

@app.route('/pokedex/tipos/<string:tipo>', methods = ['GET'])
def pokemons_por_tipo(tipo):
    return Response(json.dumps([pokemon['nombre'] for pokemon in cargar_pokemons() if tipo in pokemon['tipos']], ensure_ascii=False), status=200, content_type='application/json')

@app.route('/pokedex/<identifier>', methods=['GET', 'PATCH', 'DELETE'])
def obtener_pokemon(identifier: str | int):

    campo = 'id' if identifier.isdigit() else 'nombre'
    pokemon = None

    pokemons = cargar_pokemons()
    for pos, pokemon_data in enumerate(pokemons):
        if str(pokemon_data[campo]) == str(identifier):
            pokemon, position = pokemon_data, pos
            break
    
    if not pokemon:
        return Response(json.dumps({"error": "Pokemon no encontrado"}, ensure_ascii=False), status=404, content_type='application/json')
    if request.method == 'GET':
        return Response(json.dumps(pokemon, ensure_ascii=False), status=200, content_type='application/json')

    if request.headers.get('Authorization') != AUTH_TOKEN:
        return Response(json.dumps({"error": "No autorizado"}, ensure_ascii=False), status=401, content_type='application/json')

    if request.method == 'PATCH':
        body = request.get_json(force=True)
        
        for key in body:
            if key in pokemon['stats']:
                try:
                    pokemon['stats'][key] = int(body[key])
                except (TypeError, ValueError):
                    return Response(json.dumps({"error": "Tipos de datos inválidos en uno o más campos"}, ensure_ascii=False), status=400, content_type='application/json')
        output = {'Estadísticas Modificadas': pokemon}
    else:
        pokemons.pop(position)
        output = {'Pokemon Eliminado': pokemon}

    with open('pokemon.json', 'w', encoding = 'utf-8',) as file:
        json.dump(pokemons, file, indent=2, ensure_ascii=False)

    return Response(json.dumps(output, ensure_ascii=False), status=200, content_type='application/json')

@app.route('/batalla/<id_pokemon_1>/<id_pokemon_2>', methods = ['GET'])
def batalla_pokemon(id_pokemon_1: str | int, id_pokemon_2: str | int):
    p1 = obtener_pokemon(id_pokemon_1).get_json()
    p2 = obtener_pokemon(id_pokemon_2).get_json()
    try:
        hp1, hp2 = p1['stats']['hp'], p2['stats']['hp']
        spd1, spd2 = p1['stats']['spd'], p2['stats']['spd']
    except KeyError:
        return Response(json.dumps({"error": "Uno o más de los pokemones no encontrados"}, ensure_ascii=False), status=404, content_type='application/json')

    atacante, defensor = (p1, p2) if spd1 >= spd2 else (p2, p1)

    while hp1 > 0 and hp2 > 0:
        dano = dano_ataque(atacante, defensor)
        if atacante == p1:
            hp2 -= dano
        else:
            hp1 -= dano

        atacante, defensor = defensor, atacante

    return Response(json.dumps({'Combate': f"{p1['nombre']} vs {p2['nombre']}", 'ganador': p1['nombre'] if hp1 > 0 else p2['nombre']}, ensure_ascii=False), status=200, content_type='application/json')


@app.route("/pokedex/", methods=["GET"])
def obtener_condicional():

    # Filtrar condicionalmente con que pertenezca hasta 2 tipos y cumpla hp,atk,spd >=, todo opcional

    tipos_buscados = request.args.getlist('tipo', type=str)

    hp_min = request.args.get('hp', type=int)
    atk_min = request.args.get('atk', type=int)
    spd_min = request.args.get('spd', type=int)

    if not any([tipos_buscados, hp_min, atk_min, spd_min]):
        return Response(json.dumps({"error": "Debe proporcionar al menos un criterio de búsqueda (?tipo=, ?hp=, ?atk=, ?spd=)"}, ensure_ascii=False), status=400, content_type='application/json')

    if len(tipos_buscados) > 2:
        return Response(json.dumps({"error": "No se puede filtrar por más de 2 tipos (no existen)"}, ensure_ascii=False), status=400, content_type='application/json')

    pokemons = cargar_pokemons()
    resultados = []
    
    set_tipos_buscados = set(tipos_buscados)

    for pokemon in pokemons:

        if tipos_buscados and not set_tipos_buscados.issubset(set(pokemon['tipos'])):
            continue

        if hp_min is not None and pokemon['stats']['hp'] < hp_min:
            continue

        if atk_min is not None and pokemon['stats']['atk'] < atk_min:
            continue
            
        if spd_min is not None and pokemon['stats']['spd'] < spd_min:
            continue

        resultados.append(pokemon)

    return Response(json.dumps(resultados, ensure_ascii=False), status=200, content_type='application/json')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)