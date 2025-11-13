from unittest import TestCase
from pandas import DataFrame

from main import cargar_sismos, filtrar_sismos_magnitud, estadisticas_efectos


SISMOS_CSV_PATH = "sismos.csv"

class VerificarFiltros(TestCase):
    def setUp(self):
        self.sismos = cargar_sismos(SISMOS_CSV_PATH)

    def test_filtrar_sismos_magnitud(self):
        """
        Verifica que se filtren los datos cuando no se especifica la operación.
        """

        datos_filtrados = filtrar_sismos_magnitud(self.sismos, 8.5)

        self.assertIsInstance(datos_filtrados, DataFrame)
        self.assertEqual(datos_filtrados.size, 0)

    def test_filtrar_sismos_magnitud_igual(self):
        """
        Verifica que se filtren los datos con la operación "=".
        """

        magnitud = 8.5

        datos_filtrados = filtrar_sismos_magnitud(self.sismos, magnitud, "=")

        self.assertEqual(datos_filtrados.shape[0], 2)

        self.assertEqual(datos_filtrados.loc[6]["Magnitud Ms"], magnitud)
        self.assertEqual(datos_filtrados.loc[3]["Magnitud Ms"], magnitud)

    def test_filtrar_sismos_magnitud_menor(self):
        """
        Verifica que se filtren los datos con la operación "<".
        """

        datos_filtrados = filtrar_sismos_magnitud(self.sismos, 7.3, "<")

        self.assertEqual(datos_filtrados.shape[0], 6)
        for i in [14, 15, 16, 17, 18, 20]:
            magnitud = datos_filtrados.loc[i]["Magnitud Ms"]

            self.assertTrue(magnitud < 7.3)

    def test_filtrar_sismos_magnitud_mayor(self):
        """
        Verifica que se filtren los datos con la operación ">".
        """

        datos_filtrados = filtrar_sismos_magnitud(self.sismos, 8.0, ">")

        self.assertEqual(datos_filtrados.shape[0], 5)
        for i in [3, 6, 11, 13, 21]:
            magnitud = datos_filtrados.loc[i]["Magnitud Ms"]

            self.assertTrue(magnitud > 8.0)

class VerificarEstadisticas(TestCase):
    def setUp(self):
        self.sismos = cargar_sismos(SISMOS_CSV_PATH)

    def test_estadisticas_efectos(self):
        """
        Verifica que las estadísticas sean calculados correctamente.
        """

        estadisticas_esperadas = {
            "-": 0.09316,
            "T": 0.01242,
            "TD": 0.01242,
            "TM": 0.02484
        }

        estadisticas = estadisticas_efectos(self.sismos)

        for estadistica in estadisticas_esperadas:
            with self.subTest(estadistica=estadistica):
                valor_esperado = estadisticas_esperadas[estadistica]

                self.assertAlmostEqual(estadisticas[estadistica], valor_esperado, 4)
