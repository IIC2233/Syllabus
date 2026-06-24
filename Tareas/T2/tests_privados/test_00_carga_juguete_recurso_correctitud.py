import os
from tests_privados.test_tools import IICTest, timeout, assert_es_generador, indexes_of
from backend.consultas import cargar_juguete_recurso
from utils import JugueteRecurso

N_SECOND_S = 0.006
N_SECOND_M = 0.006
N_SECOND_L = 0.008
N_SECOND_XL = 0.01
PATH_S = os.path.join("tests_privados", "data", "S")
PATH_M = os.path.join("tests_privados", "data", "M")
PATH_L = os.path.join("tests_privados", "data", "L")
PATH_XL = os.path.join("tests_privados", "data", "XL")


class TestCargaJugueteRecursoPrivado(IICTest):
    """
    Verifica que cargar_juguete_recurso retorne un generador con JugueteRecurso
    correctamente construidos usando el dataset privado.
    """

    @timeout(N_SECOND_S)
    def test_S_es_generador(self):
        """
        cargar_juguete_recurso debe ser una función generadora.
        """
        assert_es_generador(self, cargar_juguete_recurso)

    @timeout(N_SECOND_S)
    def test_S_valores(self):
        """
        S privado tiene 50 entradas; verifica el primero, el 25° y el último.
        """
        gen = cargar_juguete_recurso(os.path.join(PATH_S, "juguete_recurso.csv"))
        *items, largo = indexes_of(gen, [0, 24, -1])
        self.assertEqual(largo, 50)
        self.assertEqual(items[0], JugueteRecurso(1, 7, "00:02", 2))
        self.assertEqual(items[1], JugueteRecurso(25, 8, "01:07", 2))
        self.assertEqual(items[2], JugueteRecurso(50, 19, "02:36", 1))

    @timeout(N_SECOND_M)
    def test_M_valores(self):
        """
        M privado tiene 150 entradas; verifica el primero, el 75° y el último.
        """
        gen = cargar_juguete_recurso(os.path.join(PATH_M, "juguete_recurso.csv"))
        *items, largo = indexes_of(gen, [0, 74, -1])
        self.assertEqual(largo, 150)
        self.assertEqual(items[0], JugueteRecurso(1, 7, "00:02", 2))
        self.assertEqual(items[1], JugueteRecurso(75, 70, "01:46", 7))
        self.assertEqual(items[2], JugueteRecurso(150, 80, "00:33", 7))

    @timeout(N_SECOND_L)
    def test_L_valores(self):
        """
        L privado tiene 500 entradas; verifica el primero, el 250° y el último.
        """
        gen = cargar_juguete_recurso(os.path.join(PATH_L, "juguete_recurso.csv"))
        *items, largo = indexes_of(gen, [0, 249, -1])
        self.assertEqual(largo, 500)
        self.assertEqual(items[0], JugueteRecurso(1, 7, "00:02", 2))
        self.assertEqual(items[1], JugueteRecurso(250, 471, "01:31", 4))
        self.assertEqual(items[2], JugueteRecurso(500, 159, "00:12", 4))

    @timeout(N_SECOND_XL)
    def test_XL_valores(self):
        """
        XL privado tiene 800 entradas; verifica el primero, el 400° y el último.
        """
        gen = cargar_juguete_recurso(os.path.join(PATH_XL, "juguete_recurso.csv"))
        *items, largo = indexes_of(gen, [0, 399, -1])
        self.assertEqual(largo, 800)
        self.assertEqual(items[0], JugueteRecurso(1, 7, "00:02", 2))
        self.assertEqual(items[1], JugueteRecurso(400, 883, "02:28", 12))
        self.assertEqual(items[2], JugueteRecurso(800, 634, "02:35", 8))
