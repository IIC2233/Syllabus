from flask import Flask, Response, request
from pathlib import Path
import json

app = Flask(__name__)

@app.route("/controles", methods=["GET"])
def get_lista_de_controles() -> Response:
    """
    Recibe requests de tipo GET al path /controles.
    Retorna un Response que contiene un json con una 
    lista con los nombres de los 
    archivos de los controles ordenados
    """
    path_controles = Path('controles')
    controles = [file.name for file in Path(path_controles).iterdir()]
    controles.sort()
    response = json.dumps(controles)
    return Response(status=200, response=response, content_type='application/json')

@app.route("/controles/<string:nombre_control>", methods=["GET"])
def get_control(nombre_control) -> Response:
    """
    Recibe requests de tipo GET al path /controles/{nombre_control}.
    Debe retornar un Response con un json con 
    los detalles del control contenidos en el archivo
    correspondiente cargando el archivo json
    """
    pass

@app.route("/controles/<string:nombre_control>", methods=["POST"])
def post_control_answer(nombre_control) -> Response:
    """
    Recibe requests de tipo POST al path /controles/{nombre_control}.
    Además espera el nombre de alumno agregado al path de la forma
    ?alumno={alumno}, y espera las respuestas en el body del request
    en formato lista.
    Retorna un Response con un mensaje en formato json
    """
    pass

if __name__ == "__main__":
    app.run(host="localhost", port=4444)