import os
from tests_privados.test_tools import IICTest, timeout, assert_es_generador, indexes_of
from backend.consultas import cargar_habitat_objeto
from utils import HabitatObjeto

N_SECOND_S = 0.006
N_SECOND_M = 0.008
N_SECOND_L = 0.01
N_SECOND_XL = 0.014
PATH_S = os.path.join("tests_privados", "data", "S")
PATH_M = os.path.join("tests_privados", "data", "M")
PATH_L = os.path.join("tests_privados", "data", "L")
PATH_XL = os.path.join("tests_privados", "data", "XL")


class TestCargaHabitatObjetoPrivado(IICTest):
    """
    Verifica que cargar_habitat_objeto retorne un generador con HabitatObjeto
    correctamente construidos usando el dataset privado.
    """

    @timeout(N_SECOND_S)
    def test_S_es_generador(self):
        """
        cargar_habitat_objeto debe ser una función generadora.
        """
        assert_es_generador(self, cargar_habitat_objeto)

    @timeout(N_SECOND_S)
    def test_S_objetos_es_tupla_de_tuplas(self):
        """
        El campo objetos debe ser una tupla de tuplas (id_objeto, cantidad).
        """
        for habitat_objeto in cargar_habitat_objeto(os.path.join(PATH_S, "habitat_objeto.csv")):
            self.assertIsInstance(habitat_objeto.objetos, tuple)
            for par in habitat_objeto.objetos:
                self.assertIsInstance(par, tuple)
                self.assertEqual(len(par), 2)

    @timeout(N_SECOND_S)
    def test_S_valores(self):
        """
        S privado tiene 50 entradas; verifica la primera, la 25° y la última.
        """
        gen = cargar_habitat_objeto(os.path.join(PATH_S, "habitat_objeto.csv"))
        *items, largo = indexes_of(gen, [0, 24, -1])
        self.assertEqual(largo, 50)
        self.assertEqual(items[0], HabitatObjeto(1, tuple()))
        self.assertEqual(items[1], HabitatObjeto(25, ((3, 3), (6, 3))))
        self.assertEqual(items[2], HabitatObjeto(50, ((6, 3),)))

    @timeout(N_SECOND_M)
    def test_M_valores(self):
        """
        M privado tiene 200 entradas; verifica la primera, la 100° y la última.
        """
        gen = cargar_habitat_objeto(os.path.join(PATH_M, "habitat_objeto.csv"))
        *items, largo = indexes_of(gen, [0, 99, -1])
        self.assertEqual(largo, 200)
        self.assertEqual(items[0], HabitatObjeto(1, tuple()))
        self.assertEqual(items[1], HabitatObjeto(100, ((17, 2), (18, 1), (33, 1), (39, 1))))
        self.assertEqual(items[2], HabitatObjeto(200, ((1, 2), (5, 1))))

    @timeout(N_SECOND_L)
    def test_L_valores(self):
        """
        L privado tiene 1000 entradas; verifica la primera, la 500° y la última.
        """
        gen = cargar_habitat_objeto(os.path.join(PATH_L, "habitat_objeto.csv"))
        *items, largo = indexes_of(gen, [0, 499, -1])
        self.assertEqual(largo, 1000)
        self.assertEqual(items[0], HabitatObjeto(1, tuple()))
        self.assertEqual(items[1], HabitatObjeto(500, ((41, 3), (121, 3), (140, 2))))
        self.assertEqual(items[2], HabitatObjeto(1000, ((17, 1), (68, 2))))

    @timeout(N_SECOND_XL)
    def test_XL_valores(self):
        """
        XL privado tiene 2500 entradas; verifica la primera, la 1251° y la última.
        """
        gen = cargar_habitat_objeto(os.path.join(PATH_XL, "habitat_objeto.csv"))
        *items, largo = indexes_of(gen, [0, 1250, -1])
        self.assertEqual(largo, 2500)
        self.assertEqual(items[0], HabitatObjeto(1, tuple()))
        self.assertEqual(items[1], HabitatObjeto(1251, ((42, 3), (123, 2), (303, 2))))
        self.assertEqual(items[2], HabitatObjeto(2500, ((259, 3),)))
