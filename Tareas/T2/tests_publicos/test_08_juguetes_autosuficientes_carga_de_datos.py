import os
from tests_publicos.test_tools import IICTest, timeout, indexes_of
from tests_publicos.solution.test_8 import (JUGUETES_AUTOSUFICIENTES_L, JUGUETES_AUTOSUFICIENTES_M,
                                            JUGUETES_AUTOSUFICIENTES_S)
from backend.consultas import (
    juguetes_autosuficientes,
    cargar_juguete,
    cargar_juguete_objeto,
    cargar_objeto_recurso,
    cargar_juguete_recurso,
    cargar_recurso_recurso,
)

N_SECOND = 0.5
PATH_S = os.path.join("data", "S")
PATH_M = os.path.join("data", "M")
PATH_L = os.path.join("data", "L")


class TestJuguetesAutosuficientesCargaDatos(IICTest):
    """
    Verifica juguetes_autosuficientes cargando juguete, juguete_objeto,
    objeto_recurso, juguete_recurso y recurso_recurso desde L, M y S.
    Resultado ordenado por id_juguete ascendente, sin duplicados.
    """

    # ── L ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_L_0(self):
        """
        L — juguetes autosuficientes con el dataset grande.
        Verifica primero, último y largo total.
        """
        gen_j  = cargar_juguete(os.path.join(PATH_L, "juguetes.csv"))
        gen_jo = cargar_juguete_objeto(os.path.join(PATH_L, "juguete_objeto.csv"))
        gen_or = cargar_objeto_recurso(os.path.join(PATH_L, "objeto_recurso.csv"))
        gen_jr = cargar_juguete_recurso(os.path.join(PATH_L, "juguete_recurso.csv"))
        gen_rr = cargar_recurso_recurso(os.path.join(PATH_L, "recurso_recurso.csv"))
        resultado = juguetes_autosuficientes(gen_j, gen_jo, gen_or, gen_jr, gen_rr)
        *items, largo = indexes_of(resultado, [0, -1])
        self.assertEqual(largo, len(JUGUETES_AUTOSUFICIENTES_L))
        self.assertEqual(items[0], JUGUETES_AUTOSUFICIENTES_L[0])
        self.assertEqual(items[1], JUGUETES_AUTOSUFICIENTES_L[-1])

    # ── M ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_M_0(self):
        """
        M — juguetes autosuficientes con el dataset mediano.
        Verifica primero, último y largo total.
        """
        gen_j  = cargar_juguete(os.path.join(PATH_M, "juguetes.csv"))
        gen_jo = cargar_juguete_objeto(os.path.join(PATH_M, "juguete_objeto.csv"))
        gen_or = cargar_objeto_recurso(os.path.join(PATH_M, "objeto_recurso.csv"))
        gen_jr = cargar_juguete_recurso(os.path.join(PATH_M, "juguete_recurso.csv"))
        gen_rr = cargar_recurso_recurso(os.path.join(PATH_M, "recurso_recurso.csv"))
        resultado = juguetes_autosuficientes(gen_j, gen_jo, gen_or, gen_jr, gen_rr)
        *items, largo = indexes_of(resultado, [0, -1])
        self.assertEqual(largo, len(JUGUETES_AUTOSUFICIENTES_M))
        self.assertEqual(items[0], JUGUETES_AUTOSUFICIENTES_M[0])
        self.assertEqual(items[1], JUGUETES_AUTOSUFICIENTES_M[-1])

    # ── S ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_S_0(self):
        """
        S — juguetes autosuficientes con el dataset pequeño.
        Verifica primero, último y largo total.
        """
        gen_j  = cargar_juguete(os.path.join(PATH_S, "juguetes.csv"))
        gen_jo = cargar_juguete_objeto(os.path.join(PATH_S, "juguete_objeto.csv"))
        gen_or = cargar_objeto_recurso(os.path.join(PATH_S, "objeto_recurso.csv"))
        gen_jr = cargar_juguete_recurso(os.path.join(PATH_S, "juguete_recurso.csv"))
        gen_rr = cargar_recurso_recurso(os.path.join(PATH_S, "recurso_recurso.csv"))
        resultado = juguetes_autosuficientes(gen_j, gen_jo, gen_or, gen_jr, gen_rr)
        *items, largo = indexes_of(resultado, [0, -1])
        self.assertEqual(largo, len(JUGUETES_AUTOSUFICIENTES_S))
        self.assertEqual(items[0], JUGUETES_AUTOSUFICIENTES_S[0])
        self.assertEqual(items[1], JUGUETES_AUTOSUFICIENTES_S[-1])
