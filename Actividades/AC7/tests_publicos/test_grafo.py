from unittest import TestCase

from main import cargar_sismos, crear_grafo_ubicaciones, ubicacion_tuvo_sismo_mar
from tests_publicos.data import grafo_ubicaciones_esperado
from tests_publicos.utils import timeout


SISMOS_CSV_PATH = "sismos.csv"

class VerificarGrafo(TestCase):

    def setUp(self):
        self.sismos = cargar_sismos(SISMOS_CSV_PATH)

    def test_crear_grafo_ubicaciones(self):
        """
        Verifica que el grafo de ubicaciones sea el correcto.
        """

        self.assertDictEqual(
            crear_grafo_ubicaciones(self.sismos),
            grafo_ubicaciones_esperado
        )

    @timeout(1)
    def test_ubicacion_tuvo_sismo_mar(self):
        """
        Verifica que ubicación_tuvo_sismo_mar entregue datos correctos a partir de un DataFrame.
        """

        consultas = {
            "Tamarugal": True,
            "Arica": False,
            "Elqui": True,
            "Coquimbo": True,
        }

        for consulta in consultas:
            with self.subTest(consulta=consulta):
                respuesta = ubicacion_tuvo_sismo_mar(grafo_ubicaciones_esperado, consulta)
                respuesta_esperada = consultas.get(consulta)

                if respuesta_esperada:
                    self.assertTrue(respuesta)
                else:
                    self.assertFalse(respuesta)
