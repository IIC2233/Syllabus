import os
import unittest

from servidor.main import Servidor


class VerificarTransacciones(unittest.TestCase):
    path_archivo = os.path.join('servidor', 'data.json')

    @classmethod
    def setUpClass(cls):
        contenido = '''{
    "Pablo": {
        "Dani": 14000.0,
        "Cristian": 33000.0
    },
    "Lucas": {
        "Dani": 14000.0,
        "Cristian": 36000.0,
        "Paqui": 2000.0
    },
    "Dani": {
        "Fran": 1250.0,
        "Cristian": 33000.0
    },
    "Fran": {
        "Dani": 10000.0,
        "Cristian": 33000.0
    },
    "Paqui": {
        "Cristian": 33000.0
    }
}'''

        with open(cls.path_archivo, 'w', encoding='utf-8') as file:
            file.write(contenido)

    def test_cargar_transacciones(self):
        """
        Verifica que las transacciones sean cargadas en
        su respectivo archivo, respetando el formato solicitado.
        """
        server = Servidor('localhost', 1904)

        contenido_esperado = {
            'Pablo': {'Dani': 14000.0, 'Cristian': 33000.0},
            'Lucas': {'Dani': 14000.0, 'Cristian': 36000.0, 'Paqui': 2000.0},
            'Dani': {'Fran': 1250.0, 'Cristian': 33000.0},
            'Fran': {'Dani': 10000.0, 'Cristian': 33000.0},
            'Paqui': {'Cristian': 33000.0}
        }

        server.cargar_transacciones()
        self.assertEqual(server.transacciones,
                         contenido_esperado)

    def test_guardar_transacciones(self):
        """
        Verifica que las transacciones sean guardadas en
        su respectivo archivo, respetando el formato solicitado.
        """
        server = Servidor('localhost', 1904)

        server.transacciones = {
            'Pepa': {'Luna': 7000.0},
            'Luna': {'Cachirulo': 2000.0}
        }

        server.guardar_transacciones()

        contenido_guardado = ''
        contenido_esperado = '{"Pepa":{"Luna":7000.0},"Luna":{"Cachirulo":2000.0}}'

        with open(server.path_transacciones, 'r', encoding='utf-8') as file:
            contenido_guardado = file.read()

        # Se quitan espacios y salto de lineas para asegurar
        # que no interfieran en la comparación de los contenidos
        contenido_guardado = contenido_guardado.replace('\n', '').replace(' ', '')
        contenido_esperado = contenido_esperado.replace('\n', '').replace(' ', '')

        self.assertEqual(contenido_esperado, contenido_guardado)
