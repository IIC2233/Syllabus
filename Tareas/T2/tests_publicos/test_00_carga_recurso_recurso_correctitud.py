import os
from tests_publicos.test_tools import IICTest, timeout, assert_es_generador, indexes_of
from backend.consultas import cargar_recurso_recurso
from utils import RecursoRecurso

N_SECOND = 2.0
PATH_S = os.path.join("data", "S")


class TestCargaRecursoRecurso(IICTest):
    """
    Verifica que cargar_recurso_recurso retorne un generador con RecursoRecurso
    correctamente construidos.
    """

    # ── S ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_S_es_generador(self):
        """
        cargar_recurso_recurso debe retornar un generador (GeneratorType).
        """
        assert_es_generador(self, cargar_recurso_recurso)

    @timeout(N_SECOND)
    def test_S_valores(self):
        """
        S tiene 19 entradas; verifica la primera, la décima y la última.
        """
        gen = cargar_recurso_recurso(os.path.join(PATH_S, "recurso_recurso.csv"))
        *items, largo = indexes_of(gen, [0, 9, -1])
        self.assertEqual(largo, 19)
        self.assertEqual(items[0], RecursoRecurso(20, ((13, 2),),       4))
        self.assertEqual(items[1], RecursoRecurso(11, ((3, 2), (5, 2)), 1))
        self.assertEqual(items[2], RecursoRecurso(2,  ((1, 1),),        1))

    @timeout(N_SECOND)
    def test_S_recursos_es_tupla_de_tuplas(self):
        """
        El campo 'recursos' debe ser una tupla de tuplas (id, cantidad),
        incluso con un solo ingrediente.
        """
        for recurso_recurso in cargar_recurso_recurso(os.path.join(PATH_S, "recurso_recurso.csv")):
            self.assertIsInstance(recurso_recurso.recursos, tuple)
            for par in recurso_recurso.recursos:
                self.assertIsInstance(par, tuple)
                self.assertEqual(len(par), 2)
