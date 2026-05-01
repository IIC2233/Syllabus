import os
from tests_publicos.test_tools import IICTest, timeout, indexes_of
from tests_publicos.solution.test_9 import (HABITATS_EVENTUALMENTE_CREABLES_L, 
                                            HABITATS_EVENTUALMENTE_CREABLES_M,
                                            HABITATS_EVENTUALMENTE_CREABLES_S)
from backend.consultas import (
    habitat_eventualmente_creables,
    cargar_juguete,
    cargar_juguete_recurso,
    cargar_recurso_recurso,
    cargar_objeto_recurso,
    cargar_habitat_objeto,
)

N_SECOND = 0.5
PATH_S = os.path.join("data", "S")
PATH_M = os.path.join("data", "M")
PATH_L = os.path.join("data", "L")


class TestHabitatEventualmenteCreablesCargaDatos(IICTest):
    """
    Verifica habitat_eventualmente_creables cargando juguete, juguete_recurso,
    recurso_recurso y habitat_objeto desde L, M y S.
    Resultado ordenado por id_habitat ascendente.
    """

    # ── L ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_L_0(self):
        """
        L — hábitats eventualmente creables con el dataset grande.
        Verifica primero, último y largo total.
        """
        gen_j  = cargar_juguete(os.path.join(PATH_L, "juguetes.csv"))
        gen_jr = cargar_juguete_recurso(os.path.join(PATH_L, "juguete_recurso.csv"))
        gen_rr = cargar_recurso_recurso(os.path.join(PATH_L, "recurso_recurso.csv"))
        gen_or = cargar_objeto_recurso(os.path.join(PATH_L, "objeto_recurso.csv"))
        gen_ho = cargar_habitat_objeto(os.path.join(PATH_L, "habitat_objeto.csv"))
        resultado = habitat_eventualmente_creables(gen_j, gen_jr, gen_rr, gen_or, gen_ho)
        *items, largo = indexes_of(resultado, [0, -1])
        self.assertEqual(largo, len(HABITATS_EVENTUALMENTE_CREABLES_L))
        self.assertEqual(items[0], HABITATS_EVENTUALMENTE_CREABLES_L[0])
        self.assertEqual(items[1], HABITATS_EVENTUALMENTE_CREABLES_L[-1])

    # ── M ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_M_0(self):
        """
        M — hábitats eventualmente creables con el dataset mediano.
        Verifica primero, último y largo total.
        """
        gen_j  = cargar_juguete(os.path.join(PATH_M, "juguetes.csv"))
        gen_jr = cargar_juguete_recurso(os.path.join(PATH_M, "juguete_recurso.csv"))
        gen_rr = cargar_recurso_recurso(os.path.join(PATH_M, "recurso_recurso.csv"))
        gen_or = cargar_objeto_recurso(os.path.join(PATH_M, "objeto_recurso.csv"))
        gen_ho = cargar_habitat_objeto(os.path.join(PATH_M, "habitat_objeto.csv"))
        resultado = habitat_eventualmente_creables(gen_j, gen_jr, gen_rr, gen_or, gen_ho)
        *items, largo = indexes_of(resultado, [0, -1])
        self.assertEqual(largo, len(HABITATS_EVENTUALMENTE_CREABLES_M))
        self.assertEqual(items[0], HABITATS_EVENTUALMENTE_CREABLES_M[0])
        self.assertEqual(items[1], HABITATS_EVENTUALMENTE_CREABLES_M[-1])

    # ── S ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_S_0(self):
        """
        S — hábitats eventualmente creables: resultado completo verificado.
        """
        gen_j  = cargar_juguete(os.path.join(PATH_S, "juguetes.csv"))
        gen_jr = cargar_juguete_recurso(os.path.join(PATH_S, "juguete_recurso.csv"))
        gen_rr = cargar_recurso_recurso(os.path.join(PATH_S, "recurso_recurso.csv"))
        gen_or = cargar_objeto_recurso(os.path.join(PATH_S, "objeto_recurso.csv"))
        gen_ho = cargar_habitat_objeto(os.path.join(PATH_S, "habitat_objeto.csv"))
        resultado = habitat_eventualmente_creables(gen_j, gen_jr, gen_rr, gen_or, gen_ho)
        *items, largo = indexes_of(resultado, [0, -1])
        self.assertEqual(largo, len(HABITATS_EVENTUALMENTE_CREABLES_S))
        self.assertEqual(items[0], HABITATS_EVENTUALMENTE_CREABLES_S[0])
        self.assertEqual(items[1], HABITATS_EVENTUALMENTE_CREABLES_S[-1])
