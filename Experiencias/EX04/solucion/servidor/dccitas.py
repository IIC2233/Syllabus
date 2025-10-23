import json
import string

from copy import deepcopy
from math import sqrt
from random import choices
from typing import Tuple


def texto_random(largo: int) -> str:
    '''
    Genera un texto random del largo indicado.
    Los caracteres se pueden repetir.
    '''
    caracteres = string.ascii_letters + string.digits
    texto = ''.join(choices(caracteres, k=largo))
    return texto


def calcular_distancia(coordenada_1, coordenada_2) -> float:
    '''
    Calcula la distancia euclidiana entre dos coordenadas.
    '''
    distancia_cuadratica = 0

    for p1, p2 in zip(coordenada_1, coordenada_2):
        distancia_cuadratica += (p2 - p1) ** 2

    return sqrt(distancia_cuadratica)


class DCCitas:
    def __init__(self) -> None:
        self.path = 'datos_clientes.json'
        self.datos = {}
        self.tokens = {}

    def cargar_datos(self) -> None:
        '''
        Carga los datos del archivo JSON.
        '''
        # TODO: Parte 1.1: La información del archivo no está cargando correctamente.
        with open(self.path, 'r', encoding='utf-8') as archivo:
            self.datos = json.load(archivo)

    def guardar_datos(self) -> None:
        '''
        Guarda todos los datos en el archivo JSON.
        Sobrescribe la información anterior.
        '''
        # TODO: Parte 1.2: La información del archivo no está guardando correctamente.
        with open(self.path, 'w', encoding='utf-8') as archivo:
            json.dump(self.datos, archivo, indent=4, ensure_ascii=False)

    def registrar_usuario(self, nombre: str, password: str) -> None:
        '''
        Agrega un nuevo usuario al listado de datos y
        guarda su información en el archivo JSON.
        '''
        usuario = {
            'nombre': nombre,
            'password': password,
            'coordenadas': None
        }
        self.datos[nombre] = usuario
        self.guardar_datos()

    def eliminar_usuario(self, nombre: str) -> None:
        '''
        Elimina un usuario del diccionario de tokens, diccionario de datos y
        el archivo JSON.
        '''
        if nombre in self.tokens:
            del self.tokens[nombre]
        del self.datos[nombre]
        self.guardar_datos()

    def iniciar_sesion(self, nombre: str, password: str) -> str:
        '''
        Recibe los datos de inicio de sesión de un usuario y verifica que sean
        válidos. 
        - Si lo son, genera un token para el usuario, lo guarda en el 
          diccionario de tokens y lo retorna.
        - Si no lo son, levanta una excepción.
        '''
        if self.datos[nombre]['password'] != password:
            raise ValueError('Contraseña inválida')

        token = texto_random(12)
        self.tokens[nombre] = token
        return token

    def validar_token(self, nombre: str, token: str) -> None:
        '''
        Recibe el nombre y token de un usuario y verifica que sean válidos.
        Si no lo son, levanta una excepción.
        '''
        if self.tokens[nombre] != token:
            raise ValueError('Token inválido')

    def registrar_coordenadas(self, nombre: str, coordenadas: Tuple[float]) -> None:
        '''
        Guarda las coordenadas de un usuario en el diccionario de datos y
        el archivo JSON.
        '''
        self.datos[nombre]['coordenadas'] = coordenadas
        self.guardar_datos()

    def encontrar_citas(self, nombre: str, cantidad: int) -> str:
        '''
        En cuenta los usuario registrados más cercanos.
        '''
        def distancia_usuarios(usuario_original, otro_usuario):
            '''
            Calcula la distancia entre dos usuario, salvo que sean el mismo o
            que otro usuario no tenga coordenadas.
            '''
            if (not otro_usuario['coordenadas']) or \
               (usuario_original['nombre'] == otro_usuario['nombre']):
                return float('inf')

            return calcular_distancia(usuario_original['coordenadas'],
                                      otro_usuario['coordenadas'])

        usuario_original = self.datos[nombre]

        opciones = deepcopy(list(self.datos.values()))

        for otro_usuario in opciones:
            otro_usuario['distancia'] = distancia_usuarios(usuario_original, otro_usuario)

        opciones.sort(key=lambda op: op['distancia'])

        informacion = list(map(lambda op: (op['nombre'], op['distancia']), opciones))

        return informacion[:cantidad]


if __name__ == '__main__':
    dccitas = DCCitas()

    dccitas.cargar_datos()
    print(dccitas.datos, '\n')

    dccitas.registrar_usuario('Pepa', 'Lechuga')
    print(dccitas.datos, '\n')

    pepa_token = dccitas.iniciar_sesion('Pepa', 'Lechuga')
    print(pepa_token, '\n')

    dccitas.registrar_coordenadas('Pepa', [40.334424, -75.947936, 100.789729, 1.327397])
    print(dccitas.datos, '\n')

    citas = dccitas.encontrar_citas('Pepa', 3)
    print(citas, '\n')

    dccitas.eliminar_usuario('Pepa')
