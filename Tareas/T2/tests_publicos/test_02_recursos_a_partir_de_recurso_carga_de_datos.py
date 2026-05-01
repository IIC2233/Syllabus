import os
from tests_publicos.test_tools import IICTest, timeout, indexes_of
from tests_publicos.solution.test_2 import (RECURSOS_APTR_L_0, RECURSOS_APTR_M_0, 
                                            RECURSOS_APTR_S_0, RECURSOS_APTR_S_1)
from backend.consultas import recursos_a_partir_de_recurso, cargar_recurso_recurso

N_SECOND = 0.5
PATH_S = os.path.join("data", "S")
PATH_M = os.path.join("data", "M")
PATH_L = os.path.join("data", "L")


class TestRecursosAPartirDeRecursoCargaDatos(IICTest):
    """
    Verifica recursos_a_partir_de_recurso cargando recurso_recurso desde L, M y S.
    Resultado ordenado por id_recurso_resultado ascendente.
    """

    # ── L ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_L_0(self):
        """
        L — id_recurso=1: todos los recursos que usan R1 como ingrediente.
        Verifica primero, último y largo total.
        """
        gen = cargar_recurso_recurso(os.path.join(PATH_L, "recurso_recurso.csv"))
        resultado = recursos_a_partir_de_recurso(gen, 1)
        *items, largo = indexes_of(resultado, [0, -1])
        self.assertEqual(largo, len(RECURSOS_APTR_L_0))
        self.assertEqual(items[0], RECURSOS_APTR_L_0[0])
        self.assertEqual(items[1], RECURSOS_APTR_L_0[-1])

    # ── M ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_M_0(self):
        """
        M — id_recurso=1: todos los recursos que usan R1 como ingrediente.
        Verifica primero, último y largo total.
        """
        gen = cargar_recurso_recurso(os.path.join(PATH_M, "recurso_recurso.csv"))
        resultado = recursos_a_partir_de_recurso(gen, 1)
        *items, largo = indexes_of(resultado, [0, -1])
        self.assertEqual(largo, len(RECURSOS_APTR_M_0))
        self.assertEqual(items[0], RECURSOS_APTR_M_0[0])
        self.assertEqual(items[1], RECURSOS_APTR_M_0[-1])

    # ── S ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_S_0(self):
        """
        S — id_recurso=1: R2, R3 y R17 usan R1 como ingrediente.
        Verifica resultado completo (3 elementos).
        """
        gen = cargar_recurso_recurso(os.path.join(PATH_S, "recurso_recurso.csv"))
        resultado = recursos_a_partir_de_recurso(gen, 1)
        *items, largo = indexes_of(resultado, [0, -1])
        self.assertEqual(largo, len(RECURSOS_APTR_S_0))
        self.assertEqual(items[0], RECURSOS_APTR_S_0[0])
        self.assertEqual(items[1], RECURSOS_APTR_S_0[-1])

    @timeout(N_SECOND)
    def test_S_1(self):
        """
        S — id_recurso=8: solo R10 usa R8 como ingrediente.
        Verifica resultado completo (1 elemento).
        """
        gen = cargar_recurso_recurso(os.path.join(PATH_S, "recurso_recurso.csv"))
        resultado = recursos_a_partir_de_recurso(gen, 8)
        *items, largo = indexes_of(resultado, [0])
        self.assertEqual(largo, len(RECURSOS_APTR_S_1))
        self.assertEqual(items[0], RECURSOS_APTR_S_1[0])
