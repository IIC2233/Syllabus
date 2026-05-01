import os
from tests_publicos.test_tools import IICTest, timeout, assert_es_generador, indexes_of
from backend.consultas import cargar_objeto_recurso
from utils import ObjetoRecurso

N_SECOND = 2.0
PATH_S = os.path.join("data", "S")


class TestCargaObjetoRecurso(IICTest):
    """
    Verifica que cargar_objeto_recurso retorne un generador con ObjetoRecurso
    correctamente construidos.
    """

    # ── S ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_S_es_generador(self):
        """
        cargar_objeto_recurso debe retornar un generador (GeneratorType).
        """
        assert_es_generador(self, cargar_objeto_recurso)

    @timeout(N_SECOND)
    def test_S_valores(self):
        """
        S tiene 10 entradas; verifica la primera, la quinta y la última.
        """
        gen = cargar_objeto_recurso(os.path.join(PATH_S, "objeto_recurso.csv"))
        *items, largo = indexes_of(gen, [0, 4, -1])
        self.assertEqual(largo, 10)
        self.assertEqual(items[0], ObjetoRecurso(1,  ((2, 1), (9, 2))))
        self.assertEqual(items[1], ObjetoRecurso(5,  ((18, 1), (19, 2))))
        self.assertEqual(items[2], ObjetoRecurso(10, ((14, 1),)))

    @timeout(N_SECOND)
    def test_S_recursos_es_tupla_de_tuplas(self):
        """
        El campo 'recursos' debe ser una tupla de tuplas (id, cantidad).
        """
        for objeto_recurso in cargar_objeto_recurso(os.path.join(PATH_S, "objeto_recurso.csv")):
            self.assertIsInstance(objeto_recurso.recursos, tuple)
            for par in objeto_recurso.recursos:
                self.assertIsInstance(par, tuple)
                self.assertEqual(len(par), 2)
