from flask import Flask, request, jsonify
import csv

app = Flask(__name__)
CSV_FILE = "puntajes.csv"

@app.route("/puntajes", methods=["GET"])
def obtener_puntajes():
    # Simplemente leemos el archivo puntajes.csv y le damos un nuevo valor

    with open(CSV_FILE, "r") as f:
        next(f)  # saltar cabecera
        lineas = f.readlines()
        puntajes = []

        for linea in lineas:
            nombre, puntaje = linea.strip().split(",")
            puntajes.append({"nombre": nombre, "puntaje": int(puntaje)})

        puntajes.sort(key=lambda x: x["puntaje"])
    return puntajes, 200

@app.route("/puntajes", methods=["POST"])
def agregar_puntaje():
    data = request.get_json()
    nombre = data["nombre"]
    puntaje = data["puntaje"]

    with open(CSV_FILE, 'a') as f:
        f.write(nombre + "," + str(puntaje)+"\n")
    return "OK", 200

if __name__ == "__main__":
    app.run(port=4631)