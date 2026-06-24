import os
from tests_privados.test_tools import IICTest, timeout, assert_es_generador, indexes_of
from backend.consultas import cargar_recurso_recurso
from utils import RecursoRecurso

N_SECOND_S = 0.006
N_SECOND_M = 0.006
N_SECOND_L = 0.008
N_SECOND_XL = 0.012
PATH_S = os.path.join("tests_privados", "data", "S")
PATH_M = os.path.join("tests_privados", "data", "M")
PATH_L = os.path.join("tests_privados", "data", "L")
PATH_XL = os.path.join("tests_privados", "data", "XL")


class TestCargaRecursoRecursoPrivado(IICTest):
    """
    Verifica que cargar_recurso_recurso retorne un generador con RecursoRecurso
    correctamente construidos usando el dataset privado.
    """

    @timeout(N_SECOND_S)
    def test_S_es_generador(self):
        """
        cargar_recurso_recurso debe ser una función generadora.
        """
        assert_es_generador(self, cargar_recurso_recurso)
    
    @timeout(N_SECOND_S)
    def test_S_recursos_es_tupla_de_tuplas(self):
        """
        El campo recursos debe ser una tupla de tuplas (id_recurso, cantidad).
        """
        for recurso_recurso in cargar_recurso_recurso(os.path.join(PATH_S, "recurso_recurso.csv")):
            self.assertIsInstance(recurso_recurso.recursos, tuple)
            for par in recurso_recurso.recursos:
                self.assertIsInstance(par, tuple)
                self.assertEqual(len(par), 2)

    @timeout(N_SECOND_S)
    def test_S_valores(self):
        """
        S privado tiene 19 entradas; verifica la primera, la décima y la última.
        """
        gen = cargar_recurso_recurso(os.path.join(PATH_S, "recurso_recurso.csv"))
        *items, largo = indexes_of(gen, [0, 9, -1])
        self.assertEqual(largo, 19)
        self.assertEqual(items[0], RecursoRecurso(20, ((18, 2),), 11))
        self.assertEqual(items[1], RecursoRecurso(11, ((5, 1),), 1))
        self.assertEqual(items[2], RecursoRecurso(2, ((1, 1),), 1))

    @timeout(N_SECOND_M)
    def test_M_valores(self):
        """
        M privado tiene 99 entradas ordenadas de mayor a menor; verifica la primera, la 50° y la última.
        """
        gen = cargar_recurso_recurso(os.path.join(PATH_M, "recurso_recurso.csv"))
        *items, largo = indexes_of(gen, [0, 49, -1])
        self.assertEqual(largo, 99)
        self.assertEqual(items[0], RecursoRecurso(100, ((63, 3), (58, 3)), 36))
        self.assertEqual(items[1], RecursoRecurso(51, ((38, 3), (18, 3), (17, 1), (16, 3)), 21))
        self.assertEqual(items[2], RecursoRecurso(2, ((1, 1),), 1))

    @timeout(N_SECOND_L)
    def test_L_valores(self):
        """
        L privado tiene 599 entradas ordenadas de mayor a menor; verifica la primera, la 300° y la última.
        """
        gen = cargar_recurso_recurso(os.path.join(PATH_L, "recurso_recurso.csv"))
        *items, largo = indexes_of(gen, [0, 299, -1])
        self.assertEqual(largo, 599)
        self.assertEqual(items[0], RecursoRecurso(600, ((419, 2), (183, 3)), 13))
        self.assertEqual(items[1], RecursoRecurso(301, ((201, 2), (132, 3), (129, 1), (94, 3)), 8))
        self.assertEqual(items[2], RecursoRecurso(2, ((1, 1),), 1))

    @timeout(N_SECOND_XL)
    def test_XL_valores(self):
        """
        XL privado tiene 1499 entradas ordenadas de mayor a menor; verifica la primera, la 750° y la última.
        """
        gen = cargar_recurso_recurso(os.path.join(PATH_XL, "recurso_recurso.csv"))
        *items, largo = indexes_of(gen, [0, 749, -1])
        self.assertEqual(largo, 1499)
        self.assertEqual(items[0], RecursoRecurso(1500, ((353, 1), (238, 2)), 36))
        self.assertEqual(items[1], RecursoRecurso(751, ((6, 3),), 20))
        self.assertEqual(items[2], RecursoRecurso(2, ((1, 1),), 1))
