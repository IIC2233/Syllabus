import os
from tests_privados.test_tools import IICTest, timeout, assert_es_generador, indexes_of
from backend.consultas import cargar_juguete_objeto
from utils import JugueteObjeto

N_SECOND_S = 0.006
N_SECOND_M = 0.006
N_SECOND_L = 0.008
N_SECOND_XL = 0.01
PATH_S = os.path.join("tests_privados", "data", "S")
PATH_M = os.path.join("tests_privados", "data", "M")
PATH_L = os.path.join("tests_privados", "data", "L")
PATH_XL = os.path.join("tests_privados", "data", "XL")


class TestCargaJugueteObjetoPrivado(IICTest):
    """
    Verifica que cargar_juguete_objeto retorne un generador con JugueteObjeto
    correctamente construidos usando el dataset privado.
    """

    @timeout(N_SECOND_S)
    def test_S_es_generador(self):
        """
        cargar_juguete_objeto debe ser una función generadora.
        """
        assert_es_generador(self, cargar_juguete_objeto)

    @timeout(N_SECOND_S)
    def test_S_valores(self):
        """
        S privado tiene 189 entradas; verifica la primera, la 95° y la última.
        """
        gen = cargar_juguete_objeto(os.path.join(PATH_S, "juguete_objeto.csv"))
        *items, largo = indexes_of(gen, [0, 94, -1])
        self.assertEqual(largo, 189)
        self.assertEqual(items[0], JugueteObjeto(1, 1))
        self.assertEqual(items[1], JugueteObjeto(32, 5))
        self.assertEqual(items[2], JugueteObjeto(50, 9))

    @timeout(N_SECOND_M)
    def test_M_valores(self):
        """
        M privado tiene 619 entradas; verifica la primera, la 310° y la última.
        """
        gen = cargar_juguete_objeto(os.path.join(PATH_M, "juguete_objeto.csv"))
        *items, largo = indexes_of(gen, [0, 309, -1])
        self.assertEqual(largo, 619)
        self.assertEqual(items[0], JugueteObjeto(1, 1))
        self.assertEqual(items[1], JugueteObjeto(81, 34))
        self.assertEqual(items[2], JugueteObjeto(150, 39))

    @timeout(N_SECOND_L)
    def test_L_valores(self):
        """
        L privado tiene 2194 entradas; verifica la primera, la 1097° y la última.
        """
        gen = cargar_juguete_objeto(os.path.join(PATH_L, "juguete_objeto.csv"))
        *items, largo = indexes_of(gen, [0, 1096, -1])
        self.assertEqual(largo, 2194)
        self.assertEqual(items[0], JugueteObjeto(1, 1))
        self.assertEqual(items[1], JugueteObjeto(259, 175))
        self.assertEqual(items[2], JugueteObjeto(500, 145))

    @timeout(N_SECOND_XL)
    def test_XL_valores(self):
        """
        XL privado tiene 3557 entradas; verifica la primera, la 1779° y la última.
        """
        gen = cargar_juguete_objeto(os.path.join(PATH_XL, "juguete_objeto.csv"))
        *items, largo = indexes_of(gen, [0, 1778, -1])
        self.assertEqual(largo, 3557)
        self.assertEqual(items[0], JugueteObjeto(1, 1))
        self.assertEqual(items[1], JugueteObjeto(407, 13))
        self.assertEqual(items[2], JugueteObjeto(800, 458))
