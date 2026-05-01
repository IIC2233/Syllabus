import os
from tests_publicos.test_tools import IICTest, timeout, indexes_of
from tests_publicos.solution.test_3 import (JUGUETES_PRODUCEN_L_0, JUGUETES_PRODUCEN_M_0, 
                                            JUGUETES_PRODUCEN_S_0, JUGUETES_PRODUCEN_S_1)
from backend.consultas import juguetes_producen, cargar_juguete_recurso

N_SECOND = 0.5
PATH_S = os.path.join("data", "S")
PATH_M = os.path.join("data", "M")
PATH_L = os.path.join("data", "L")


class TestJuguetesProducenCargaDatos(IICTest):
    """
    Verifica juguetes_producen cargando juguete_recurso desde L, M y S.
    Resultado ordenado por id_juguete ascendente.
    """

    # ── L ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_L_0(self):
        """
        L — id_recurso=1: solo J294 produce R1.
        Verifica resultado completo (1 elemento).
        """
        gen = cargar_juguete_recurso(os.path.join(PATH_L, "juguete_recurso.csv"))
        resultado = juguetes_producen(gen, 1)
        *items, largo = indexes_of(resultado, [0])
        self.assertEqual(largo, len(JUGUETES_PRODUCEN_L_0))
        self.assertEqual(items[0], JUGUETES_PRODUCEN_L_0[0])

    # ── M ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_M_0(self):
        """
        M — id_recurso=1: J58, J110, J130 y J147 producen R1.
        Verifica primero, último y largo total.
        """
        gen = cargar_juguete_recurso(os.path.join(PATH_M, "juguete_recurso.csv"))
        resultado = juguetes_producen(gen, 1)
        *items, largo = indexes_of(resultado, [0, -1])
        self.assertEqual(largo, len(JUGUETES_PRODUCEN_M_0))
        self.assertEqual(items[0], JUGUETES_PRODUCEN_M_0[0])
        self.assertEqual(items[1], JUGUETES_PRODUCEN_M_0[-1])

    # ── S ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_S_0(self):
        """
        S — id_recurso=12: J17, J18, J21, J33 y J44 producen R12.
        Verifica resultado completo (5 elementos).
        """
        gen = cargar_juguete_recurso(os.path.join(PATH_S, "juguete_recurso.csv"))
        resultado = juguetes_producen(gen, 12)
        *items, largo = indexes_of(resultado, [0, -1])
        self.assertEqual(largo, len(JUGUETES_PRODUCEN_S_0))
        self.assertEqual(items[0], JUGUETES_PRODUCEN_S_0[0])
        self.assertEqual(items[1], JUGUETES_PRODUCEN_S_0[-1])

    @timeout(N_SECOND)
    def test_S_1(self):
        """
        S — id_recurso=1: solo J11 produce R1.
        Verifica resultado completo (1 elemento).
        """
        gen = cargar_juguete_recurso(os.path.join(PATH_S, "juguete_recurso.csv"))
        resultado = juguetes_producen(gen, 1)
        *items, largo = indexes_of(resultado, [0])
        self.assertEqual(largo, len(JUGUETES_PRODUCEN_S_1))
        self.assertEqual(items[0], JUGUETES_PRODUCEN_S_1[0])
