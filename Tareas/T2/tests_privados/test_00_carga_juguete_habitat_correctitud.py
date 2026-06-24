import os
from tests_privados.test_tools import IICTest, timeout, assert_es_generador, indexes_of
from backend.consultas import cargar_juguete_habitat
from utils import JugueteHabitat

N_SECOND_S = 0.006
N_SECOND_M = 0.008
N_SECOND_L = 0.01
N_SECOND_XL = 0.014
PATH_S = os.path.join("tests_privados", "data", "S")
PATH_M = os.path.join("tests_privados", "data", "M")
PATH_L = os.path.join("tests_privados", "data", "L")
PATH_XL = os.path.join("tests_privados", "data", "XL")


class TestCargaJugueteHabitatPrivado(IICTest):
    """
    Verifica que cargar_juguete_habitat retorne un generador con JugueteHabitat
    correctamente construidos usando el dataset privado.
    """

    @timeout(N_SECOND_S)
    def test_S_es_generador(self):
        """
        cargar_juguete_habitat debe ser una función generadora.
        """
        assert_es_generador(self, cargar_juguete_habitat)

    @timeout(N_SECOND_S)
    def test_S_ids_periodo_dia_es_tupla(self):
        """
        ids_periodo_dia debe ser una tupla, incluso con un solo periodo.
        """
        for juguete_habitat in cargar_juguete_habitat(os.path.join(PATH_S, "juguete_habitat.csv")):
            self.assertIsInstance(juguete_habitat.ids_periodo_dia, tuple)
    
    @timeout(N_SECOND_S)
    def test_S_valores(self):
        """
        S privado tiene 111 entradas; verifica la primera, la 55° y la última.
        """
        gen = cargar_juguete_habitat(os.path.join(PATH_S, "juguete_habitat.csv"))
        *items, largo = indexes_of(gen, [0, 54, -1])
        self.assertEqual(largo, 111)
        self.assertEqual(items[0], JugueteHabitat(1, 1, "00:01", (1,)))
        self.assertEqual(items[1], JugueteHabitat(4, 21, "05:24", (2,)))
        self.assertEqual(items[2], JugueteHabitat(31, 50, "03:59", (2,)))

    @timeout(N_SECOND_M)
    def test_M_valores(self):
        """
        M privado tiene 356 entradas; verifica la primera, la 178° y la última.
        """
        gen = cargar_juguete_habitat(os.path.join(PATH_M, "juguete_habitat.csv"))
        *items, largo = indexes_of(gen, [0, 177, -1])
        self.assertEqual(largo, 356)
        self.assertEqual(items[0], JugueteHabitat(1, 1, "00:01", (1,)))
        self.assertEqual(items[1], JugueteHabitat(76, 92, "00:36", (3, 5, 7, 8)))
        self.assertEqual(items[2], JugueteHabitat(76, 200, "04:39", (2,)))

    @timeout(N_SECOND_L)
    def test_L_valores(self):
        """
        L privado tiene 1366 entradas; verifica la primera, la 683° y la última.
        """
        gen = cargar_juguete_habitat(os.path.join(PATH_L, "juguete_habitat.csv"))
        *items, largo = indexes_of(gen, [0, 682, -1])
        self.assertEqual(largo, 1366)
        self.assertEqual(items[0], JugueteHabitat(1, 1, "00:01", (1,)))
        self.assertEqual(items[1], JugueteHabitat(58, 484, "01:17", (15,)))
        self.assertEqual(items[2], JugueteHabitat(418, 1000, "05:18", (2, 4, 14, 17, 18)))

    @timeout(N_SECOND_XL)
    def test_XL_valores(self):
        """
        XL privado tiene 2950 entradas; verifica la primera, la 1476° y la última.
        """
        gen = cargar_juguete_habitat(os.path.join(PATH_XL, "juguete_habitat.csv"))
        *items, largo = indexes_of(gen, [0, 1475, -1])
        self.assertEqual(largo, 2950)
        self.assertEqual(items[0], JugueteHabitat(1, 1, "00:01", (1,)))
        self.assertEqual(items[1], JugueteHabitat(445, 1230, "03:39", (77,)))
        self.assertEqual(items[2], JugueteHabitat(115, 2500, "04:02", (130,)))
