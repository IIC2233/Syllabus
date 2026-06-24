import os
from tests_privados.test_tools import IICTest, timeout, assert_es_generador, indexes_of
from backend.consultas import cargar_objeto_recurso
from utils import ObjetoRecurso

N_SECOND_S = 0.006
N_SECOND_M = 0.006
N_SECOND_L = 0.008
N_SECOND_XL = 0.01
PATH_S = os.path.join("tests_privados", "data", "S")
PATH_M = os.path.join("tests_privados", "data", "M")
PATH_L = os.path.join("tests_privados", "data", "L")
PATH_XL = os.path.join("tests_privados", "data", "XL")


class TestCargaObjetoRecursoPrivado(IICTest):
    """
    Verifica que cargar_objeto_recurso retorne un generador con ObjetoRecurso
    correctamente construidos usando el dataset privado.
    """

    @timeout(N_SECOND_S)
    def test_S_es_generador(self):
        """
        cargar_objeto_recurso debe ser una función generadora.
        """
        assert_es_generador(self, cargar_objeto_recurso)

    @timeout(N_SECOND_S)
    def test_S_recursos_es_tupla_de_tuplas(self):
        """
        El campo recursos debe ser una tupla de tuplas (id_recurso, cantidad).
        """
        for objeto_recurso in cargar_objeto_recurso(os.path.join(PATH_S, "objeto_recurso.csv")):
            self.assertIsInstance(objeto_recurso.recursos, tuple)
            for par in objeto_recurso.recursos:
                self.assertIsInstance(par, tuple)
                self.assertEqual(len(par), 2)
    
    @timeout(N_SECOND_S)
    def test_S_valores(self):
        """
        S privado tiene 10 entradas; verifica la primera, la quinta y la última.
        """
        gen = cargar_objeto_recurso(os.path.join(PATH_S, "objeto_recurso.csv"))
        *items, largo = indexes_of(gen, [0, 4, -1])
        self.assertEqual(largo, 10)
        self.assertEqual(items[0], ObjetoRecurso(1, ((13, 1),)))
        self.assertEqual(items[1], ObjetoRecurso(5, ((7, 2),)))
        self.assertEqual(items[2], ObjetoRecurso(10, ((3, 1), (7, 4), (12, 2), (15, 4))))

    @timeout(N_SECOND_M)
    def test_M_valores(self):
        """
        M privado tiene 40 entradas; verifica la primera, la 20° y la última.
        """
        gen = cargar_objeto_recurso(os.path.join(PATH_M, "objeto_recurso.csv"))
        *items, largo = indexes_of(gen, [0, 19, -1])
        self.assertEqual(largo, 40)
        self.assertEqual(items[0], ObjetoRecurso(1, ((13, 1),)))
        self.assertEqual(items[1], ObjetoRecurso(20, ((2, 2),)))
        self.assertEqual(items[2], ObjetoRecurso(40, ((4, 1), (11, 3))))

    @timeout(N_SECOND_L)
    def test_L_valores(self):
        """
        L privado tiene 200 entradas; verifica la primera, la 100° y la última.
        """
        gen = cargar_objeto_recurso(os.path.join(PATH_L, "objeto_recurso.csv"))
        *items, largo = indexes_of(gen, [0, 99, -1])
        self.assertEqual(largo, 200)
        self.assertEqual(items[0], ObjetoRecurso(1, ((13, 1),)))
        self.assertEqual(items[1], ObjetoRecurso(100, ((537, 2),)))
        self.assertEqual(items[2], ObjetoRecurso(200, ((273, 2), (480, 2), (524, 1), (563, 4))))

    @timeout(N_SECOND_XL)
    def test_XL_valores(self):
        """
        XL privado tiene 500 entradas; verifica la primera, la 251° y la última.
        """
        gen = cargar_objeto_recurso(os.path.join(PATH_XL, "objeto_recurso.csv"))
        *items, largo = indexes_of(gen, [0, 250, -1])
        self.assertEqual(largo, 500)
        self.assertEqual(items[0], ObjetoRecurso(1, ((13, 1),)))
        self.assertEqual(items[1], ObjetoRecurso(251, ((191, 2), (411, 2), (575, 2), (723, 4))))
        self.assertEqual(items[2], ObjetoRecurso(500, ((122, 1), (254, 3), (1317, 2))))
