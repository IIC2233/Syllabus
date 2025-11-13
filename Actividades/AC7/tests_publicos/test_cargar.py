from unittest import TestCase
from pandas import DataFrame

from main import cargar_sismos


SISMOS_CSV_PATH = "sismos.csv"

class VerificarCargarSismos(TestCase):

    def setUp(self):
        self.sismos = cargar_sismos(SISMOS_CSV_PATH)

    def test_cargar_sismos(self):
        """
        Verifica que la función cargar sismos cargue correctamente los datos,
        además de retornar lo esperado.
        """
        columnas = [
            'Fecha y hora local', 'Magnitud Ms', 'Magnitud Mw',
            'Profundidad','Efecto', 'Coordenadas', 'Ubicación'
        ]

        ubicaciones_del_sismo_22 = ['Chile', 'Biobío', 'Arauco', 'Mar']

        self.assertIsInstance(self.sismos, DataFrame)

        self.assertEqual(list(self.sismos.columns), columnas)
        self.assertEqual(self.sismos.shape[0], 23)

        self.assertCountEqual(self.sismos.Ubicación[22], ubicaciones_del_sismo_22)
        self.assertEqual(self.sismos.loc[0]["Magnitud Mw"], "-")
