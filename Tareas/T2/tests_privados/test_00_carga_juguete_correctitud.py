import os
from tests_privados.test_tools import IICTest, timeout, assert_es_generador, indexes_of
from backend.consultas import cargar_juguete
from utils import Juguete

N_SECOND_S = 0.006
N_SECOND_M = 0.006
N_SECOND_L = 0.008
N_SECOND_XL = 0.012
PATH_S = os.path.join("tests_privados", "data", "S")
PATH_M = os.path.join("tests_privados", "data", "M")
PATH_L = os.path.join("tests_privados", "data", "L")
PATH_XL = os.path.join("tests_privados", "data", "XL")


class TestCargaJuguetePrivado(IICTest):
    """
    Verifica que cargar_juguete retorne un generador con Juguete
    correctamente construidos usando el dataset privado.
    """

    @timeout(N_SECOND_S)
    def test_S_es_generador(self):
        """
        cargar_juguete debe ser una función generadora.
        """
        assert_es_generador(self, cargar_juguete)

    @timeout(N_SECOND_S)
    def test_S_afinidades_es_tupla(self):
        """
        afinidades debe ser una tupla, incluso con una sola afinidad.
        """
        for juguete in cargar_juguete(os.path.join(PATH_S, "juguetes.csv")):
            self.assertIsInstance(juguete.afinidades, tuple)

    @timeout(N_SECOND_S)
    def test_S_valores(self):
        """
        S privado tiene 50 juguetes; verifica el primero, el 25° y el último.
        """
        gen = cargar_juguete(os.path.join(PATH_S, "juguetes.csv"))
        *items, largo = indexes_of(gen, [0, 24, -1])
        self.assertEqual(largo, 50)
        self.assertEqual(items[0], Juguete(1, "Bulbasaur", (1, 2), "001"))
        self.assertEqual(items[1], Juguete(25, "Pikachu", (4, 10), "025"))
        self.assertEqual(items[2], Juguete(50, "Diglett", (1, 9, 18, 34), "050"))

    @timeout(N_SECOND_M)
    def test_M_valores(self):
        """
        M privado tiene 150 juguetes; verifica el primero, el 75° y el último.
        """
        gen = cargar_juguete(os.path.join(PATH_M, "juguetes.csv"))
        *items, largo = indexes_of(gen, [0, 74, -1])
        self.assertEqual(largo, 150)
        self.assertEqual(items[0], Juguete(1, "Bulbasaur", (1, 2), "001"))
        self.assertEqual(items[1], Juguete(75, "Graveler", (8, 14, 34, 35), "075"))
        self.assertEqual(items[2], Juguete(150, "Mewtwo", (7, 9, 14, 22), "150"))

    @timeout(N_SECOND_L)
    def test_L_valores(self):
        """
        L privado tiene 500 juguetes; verifica el primero, el 250° y el último.
        """
        gen = cargar_juguete(os.path.join(PATH_L, "juguetes.csv"))
        *items, largo = indexes_of(gen, [0, 249, -1])
        self.assertEqual(largo, 500)
        self.assertEqual(items[0], Juguete(1, "Bulbasaur", (1, 2), "001"))
        self.assertEqual(items[1], Juguete(250, "Ho-Oh", (33,), "250"))
        self.assertEqual(items[2], Juguete(500, "Tepig", (14, 28), "500"))

    @timeout(N_SECOND_XL)
    def test_XL_valores(self):
        """
        XL privado tiene 800 juguetes; verifica el primero, el 401° y el último.
        """
        gen = cargar_juguete(os.path.join(PATH_XL, "juguetes.csv"))
        *items, largo = indexes_of(gen, [0, 400, -1])
        self.assertEqual(largo, 800)
        self.assertEqual(items[0], Juguete(1, "Bulbasaur", (1, 2), "001"))
        self.assertEqual(items[1], Juguete(401, "Kricketot", (12, 24), "401"))
        self.assertEqual(items[2], Juguete(800, "Nihilego", (9, 27, 31, 32), "800"))
