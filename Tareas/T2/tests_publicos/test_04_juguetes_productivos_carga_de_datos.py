import os
from tests_publicos.test_tools import IICTest, timeout, indexes_of
from tests_publicos.solution.test_4 import (JUGUETES_PRODUCTIVOS_L_0, JUGUETES_PRODUCTIVOS_M_0,
                                            JUGUETES_PRODUCTIVOS_S_0, JUGUETES_PRODUCTIVOS_S_1)
from backend.consultas import juguetes_productivos, cargar_juguete_recurso

N_SECOND = 0.5
PATH_S = os.path.join("data", "S")
PATH_M = os.path.join("data", "M")
PATH_L = os.path.join("data", "L")


class TestJuguetesProductivosCargaDatos(IICTest):
    """
    Verifica juguetes_productivos cargando juguete_recurso desde L, M y S.
    Resultado ordenado por id_juguete ascendente.
    """

    # ── L ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_L_0(self):
        """
        L — minimo=None: J357 tiene la mayor productividad finita del dataset.
        Verifica resultado completo (1 elemento).
        """
        gen = cargar_juguete_recurso(os.path.join(PATH_L, "juguete_recurso.csv"))
        resultado = juguetes_productivos(gen, None)
        *items, largo = indexes_of(resultado, [0])
        self.assertEqual(largo, len(JUGUETES_PRODUCTIVOS_L_0))
        self.assertEqual(items[0], JUGUETES_PRODUCTIVOS_L_0[0])

    # ── M ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_M_0(self):
        """
        M — minimo=None: J33 y J151 tienen la mayor productividad (10.0 recursos/min).
        Verifica primero, último y largo total.
        """
        gen = cargar_juguete_recurso(os.path.join(PATH_M, "juguete_recurso.csv"))
        resultado = juguetes_productivos(gen, None)
        *items, largo = indexes_of(resultado, [0, -1])
        self.assertEqual(largo, len(JUGUETES_PRODUCTIVOS_M_0))
        self.assertEqual(items[0], JUGUETES_PRODUCTIVOS_M_0[0])
        self.assertEqual(items[1], JUGUETES_PRODUCTIVOS_M_0[-1])

    # ── S ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_S_0(self):
        """
        S — minimo=None: J10 y J18 tienen la mayor productividad (5.0 recursos/min).
        Verifica resultado completo (1 elemento).
        """
        gen = cargar_juguete_recurso(os.path.join(PATH_S, "juguete_recurso.csv"))
        resultado = juguetes_productivos(gen, None)
        *items, largo = indexes_of(resultado, [0])
        self.assertEqual(largo, len(JUGUETES_PRODUCTIVOS_S_0))
        self.assertEqual(items[0], JUGUETES_PRODUCTIVOS_S_0[0])

    @timeout(N_SECOND)
    def test_S_1(self):
        """
        S — minimo=1.0: juguetes con productividad estrictamente mayor a 1.0.
        Verifica resultado completo (6 elementos).
        """
        gen = cargar_juguete_recurso(os.path.join(PATH_S, "juguete_recurso.csv"))
        resultado = juguetes_productivos(gen, 1.0)
        *items, largo = indexes_of(resultado, [0, -1])
        self.assertEqual(largo, len(JUGUETES_PRODUCTIVOS_S_1))
        self.assertEqual(items[0], JUGUETES_PRODUCTIVOS_S_1[0])
        self.assertEqual(items[1], JUGUETES_PRODUCTIVOS_S_1[-1])
