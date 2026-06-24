import os
from tests_privados.test_tools import IICTest, timeout, assert_es_generador, indexes_of
from backend.consultas import cargar_periodo_dia
from utils import PeriodoDia

N_SECOND_S = 0.006
N_SECOND_M = 0.006
N_SECOND_L = 0.006
N_SECOND_XL = 0.007
PATH_S = os.path.join("tests_privados", "data", "S")
PATH_M = os.path.join("tests_privados", "data", "M")
PATH_L = os.path.join("tests_privados", "data", "L")
PATH_XL = os.path.join("tests_privados", "data", "XL")


class TestCargaPeriodoDiaPrivado(IICTest):
    """
    Verifica que cargar_periodo_dia retorne un generador con PeriodoDia
    correctamente construidos usando el dataset privado.
    """

    @timeout(N_SECOND_S)
    def test_S_es_generador(self):
        """
        cargar_periodo_dia debe ser una función generadora.
        """
        assert_es_generador(self, cargar_periodo_dia)

    @timeout(N_SECOND_S)
    def test_S_valores(self):
        """
        S privado tiene 2 periodos; verifica ambos.
        """
        gen = cargar_periodo_dia(os.path.join(PATH_S, "periodo_dia.csv"))
        *items, largo = indexes_of(gen, [0, -1])
        self.assertEqual(largo, 2)
        self.assertEqual(items[0], PeriodoDia(1, "Madrugada", "00:25"))
        self.assertEqual(items[1], PeriodoDia(2, "Amanecer", "00:35"))

    @timeout(N_SECOND_M)
    def test_M_valores(self):
        """
        M privado tiene 8 periodos; verifica el primero y el último.
        """
        gen = cargar_periodo_dia(os.path.join(PATH_M, "periodo_dia.csv"))
        *items, largo = indexes_of(gen, [0, -1])
        self.assertEqual(largo, 8)
        self.assertEqual(items[0], PeriodoDia(1, "Madrugada", "00:24"))
        self.assertEqual(items[1], PeriodoDia(8, "Atardecer", "00:11"))

    @timeout(N_SECOND_L)
    def test_L_valores(self):
        """
        L privado tiene 20 periodos; verifica el primero, el 10° y el último.
        """
        gen = cargar_periodo_dia(os.path.join(PATH_L, "periodo_dia.csv"))
        *items, largo = indexes_of(gen, [0, 9, -1])
        self.assertEqual(largo, 20)
        self.assertEqual(items[0], PeriodoDia(1, "Madrugada", "00:35"))
        self.assertEqual(items[1], PeriodoDia(10, "Noche", "00:25"))
        self.assertEqual(items[2], PeriodoDia(20, "Manana_2", "00:34"))

    @timeout(N_SECOND_XL)
    def test_XL_valores(self):
        """
        XL privado tiene 250 periodos; verifica el primero, el 125° y el último.
        """
        gen = cargar_periodo_dia(os.path.join(PATH_XL, "periodo_dia.csv"))
        *items, largo = indexes_of(gen, [0, 124, -1])
        self.assertEqual(largo, 250)
        self.assertEqual(items[0], PeriodoDia(1, "Madrugada", "00:21"))
        self.assertEqual(items[1], PeriodoDia(125, "Aurora_8", "00:19"))
        self.assertEqual(items[2], PeriodoDia(250, "Noche_16", "00:28"))
