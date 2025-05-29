from flask import Flask, request
from random import choice
import json

class Auxiliar:
    SOLICITUDES = 0
    RUTA = "base_de_Datos.json"
    respuestas = ["No puedes, estás en dicom", "No puedes, no eres cliente de este banco",
              "Préstamo aprobado por 100 millones de introcoins", "Banco cerrado, vuelva más tarde",
              "Son las 14:00:01 está cerrado el banco", "bueno bueno, pero solo 5 millones de introcoins"]
    
    
    @staticmethod
    def up_solicitud():
        Auxiliar.SOLICITUDES += 1

    @staticmethod
    def leer_cuentas():
        with open(Auxiliar.RUTA, "r", encoding="UTF-8") as archivo:
            contenido = json.load(archivo)
        return contenido
    
    @staticmethod
    def guardar_cuentas(cuentas):
        with open(Auxiliar.RUTA, "w", encoding="UTF-8") as archivo:
            json.dump(cuentas, archivo, ensure_ascii=False, indent=4) 

    @staticmethod
    def agregar_cuenta(nombre, apellido):
        cuentas_existentes = Auxiliar.leer_cuentas()

        for cuenta in cuentas_existentes:
            if cuenta.get("nombre") == nombre and \
               cuenta.get("apellido") == apellido:
                # la cuenta ya existe
                return False
            
        nueva_cuenta = {"nombre": nombre, "apellido": apellido}
        cuentas_existentes.append(nueva_cuenta)
        Auxiliar.guardar_cuentas(cuentas_existentes)
        return True
    


app = Flask(__name__)

respuestas = ["No puedes, estás en dicom", "No puedes, no eres cliente de este banco",
              "Préstamo aprobado por 100 millones de introcoins", "Banco cerrado, vuelva más tarde",
              "Son las 14:00:01 está cerrado el banco", "bueno bueno, pero solo 5 millones de introcoins"]


@app.route("/", methods=["GET"])
def hello_world():
    return {"saludo": "Bienvenido al Banco Estado"}


@app.route("/respuesta", methods=["GET"])
def respuesta():
    escogida = choice(Auxiliar.respuestas)
    return {"texto": escogida, "método": "GET"}


@app.route("/abrir_cuenta", methods=["POST"])
def abrir_cuenta():
    body_data = request.get_json(force=True)
    nombre = body_data["nombre"]
    apellido = body_data["apellido"]

    if nombre is None or apellido is None:
        return {"texto": "Nombre y apellido requeridos"}, 400
    
    resultado = Auxiliar.agregar_cuenta(nombre, apellido)

    if resultado: # true
        Auxiliar.up_solicitud()
        return {"texto": f"Cuenta abierta para: {nombre} {apellido}"}, 200
    else:
        return {"texto": "Cuenta ya existente"}, 406


@app.route("/buscar_cuenta", methods=["GET"])
def buscar_cuenta():
    Auxiliar.up_solicitud()
    nombre = request.args.get("nombre")
    apellido = request.args.get("apellido")

    if not nombre and not apellido:
        return {"error": "Se necesita al menos un nombre o un apellid"}, 400

    cuentas_existentes = Auxiliar.leer_cuentas()
    resultados = []

    for cuenta in cuentas_existentes:
        nombre_en_db = cuenta.get("nombre")
        apellido_en_db = cuenta.get("apellido")

        # Caso 1: Se proporcionan nombre y apellido
        if nombre and apellido:
            if nombre == nombre_en_db and apellido == apellido_en_db:
                resultados.append(cuenta) 

        # Caso 2: Solo se proporciona nombre
        elif nombre:
            if nombre == nombre_en_db:
                 resultados.append(cuenta)

        # Caso 3: Solo se proporciona apellido
        elif apellido:
            if apellido == apellido_en_db: 
                resultados.append(cuenta)
    
    if resultados:
        return {"cuentas_encontradas": resultados}, 200
    else:
        return {"mensaje": "No se encontraron cuentas"}, 404


@app.route("/solicitudes", methods=["GET", "POST"])
def respuesta_ingeniosa(): 
    if request.method == "POST":
        Auxiliar.up_solicitud()

        return {"texto": f"Llevamos: {Auxiliar.SOLICITUDES} solicitudes respondidas", "método": "POST"}
    
    return {"texto": f"Llevamos: {Auxiliar.SOLICITUDES} solicitudes respondidas", "método": "GET"}



if __name__ == "__main__":
    app.run(host="localhost", port=4444)