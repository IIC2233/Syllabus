import json
import sys
import requests

from random import random


class ClienteApi:
    def __init__(self, host: str, port: int, nombre: str) -> None:
        self.base = f'http://{host}:{port}'

        self.nombre = nombre
        self.token = None

    def registrar_usuario(self, password: str) -> bool:
        # TODO: Parte 3.1: Hay que mandar el nombre y la contraseña en la request.
        url = self.base + '/registrar'

        respuesta = requests.post(url)

        print(respuesta.status_code, respuesta.json().get('msg', ''))
        return True

    def eliminar_usuario(self) -> bool:
        # TODO: Parte 3.2: Por alguna razón la request está fallando, ¿qué será?
        url = self.base + '/eliminar'
        respuesta = requests.delete(url)

        print(respuesta.status_code)
        return True

    def iniciar_sesion(self, password: str) -> bool:
        # TODO: Parte 3.3 Hay que manejar cuando la request falla.
        url = self.base + '/iniciar_sesion'

        body = {'nombre': self.nombre, 'password': password}
        respuesta = requests.post(url, data=json.dumps(body))

        print(respuesta.status_code, respuesta.json().get('msg', ''))
        return True


    @staticmethod
    def calcular_coordenadas() -> tuple:
        rangos = ((-90, 180), (-180, 360), (-30, 60), (-30, 60))
        coordenadas = []

        for min_val, rango_val in rangos:
            coordenada = round(min_val + rango_val * random(), 6)
            coordenadas.append(coordenada)

        return coordenadas

    def registrar_coordenadas(self) -> bool:
        # TODO: Parte 3.4: Hay que mandar el token junto a la solicitud.
        url = self.base + '/registrar_coordenadas'

        body = {'nombre': self.nombre, 'coordenadas': self.calcular_coordenadas()}

        respuesta = requests.patch(url, data=json.dumps(body))

        if not respuesta.ok:
            print('ERROR:', respuesta.status_code, respuesta.json().get('error', ''))
            return False

        print(respuesta.status_code, respuesta.json().get('msg', ''))
        return True

    def encontrar_cita(self, cantidad: int | None = None) -> bool:
        # TODO Parte 3.5: Hay que indicar la cantidad de candidatos que queremos.
        url = self.base + '/encontrar_cita'

        body = {'nombre': self.nombre}
        header = {'Authorization': self.token}

        respuesta = requests.get(url, data=json.dumps(body), headers=header)

        if not respuesta.ok:
            print(respuesta.status_code, respuesta.json().get('error', ''))
            return False

        print(respuesta.status_code, respuesta.json().get('msg', ''))
        for nombre, distancia in respuesta.json()['candidatos']:
            print(f'- {nombre} ({distancia})')
        return True


if __name__ == '__main__':
    HOST = 'localhost'
    PORT = 4160 if len(sys.argv) < 2 else int(sys.argv[1])

    cliente = ClienteApi(HOST, PORT, 'Pepa')

    cliente.registrar_usuario('Lechuga')
    print()
    cliente.eliminar_usuario()
    print()

    print('----\n')

    cliente.registrar_usuario('Lechuga')
    print()

    cliente.iniciar_sesion('Sandia')
    print()
    cliente.iniciar_sesion('Lechuga')
    print()

    cliente.registrar_coordenadas()
    print()

    cliente.encontrar_cita()
    print()
    cliente.encontrar_cita(3)
    print()

    cliente.eliminar_usuario()
