from flask import Flask, request
import json

from utils import dano_ataque, AUTH_TOKEN

app = Flask(__name__)

def cargar_pokemons() -> list:
    with open('pokemon.json', encoding = 'utf-8') as file:
        return json.load(file)

@app.route('/pokedex')
def acciones_pokedex():
    # COMPLETAR
    pass

@app.route('/pokedex/tipos')
def obtener_tipos():
    # COMPLETAR
    pass

@app.route('/pokedex/tipos/<string:tipo>')
def pokemons_por_tipo(tipo):
    # COMPLETAR
    pass

@app.route('/pokedex/<identifier>')
def obtener_pokemon(identifier: str | int):
    # COMPLETAR
    pass


@app.route("/pokedex/")
def obtener_condicional():
    # COMPLETAR
    pass



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)