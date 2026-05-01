import os
from tests_publicos.test_tools import IICTest, timeout, indexes_of
from tests_publicos.solution.test_7 import (JUGUETES_A_APARECER_L_0, JUGUETES_A_APARECER_M_0, 
                                            JUGUETES_A_APARECER_M_1, JUGUETES_A_APARECER_S_0, 
                                            JUGUETES_A_APARECER_S_1, JUGUETES_A_APARECER_S_2)
from backend.consultas import juguetes_a_aparecer, cargar_juguete_habitat, cargar_periodo_dia

N_SECOND = 0.5
PATH_S = os.path.join("data", "S")
PATH_M = os.path.join("data", "M")
PATH_L = os.path.join("data", "L")


class TestJuguetesAAparecerCargaDatos(IICTest):
    """
    Verifica juguetes_a_aparecer cargando juguete_habitat y periodo_dia desde L, M y S.
    Resultado ordenado por (tiempo, id_juguete) ascendente.
    """

    # ── L ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_L_0(self):
        """
        L — id_habitat=1, momento_dia=0.
        """
        gen_jh = cargar_juguete_habitat(os.path.join(PATH_L, "juguete_habitat.csv"))
        gen_pd = cargar_periodo_dia(os.path.join(PATH_L, "periodo_dia.csv"))
        resultado = juguetes_a_aparecer(gen_jh, gen_pd, 1, 0)
        *items, largo = indexes_of(resultado, [0])
        self.assertEqual(largo, len(JUGUETES_A_APARECER_L_0))
        self.assertEqual(items[0], JUGUETES_A_APARECER_L_0[0])

    # ── M ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_M_0(self):
        """
        M — id_habitat=1, momento_dia=0.
        """
        gen_jh = cargar_juguete_habitat(os.path.join(PATH_M, "juguete_habitat.csv"))
        gen_pd = cargar_periodo_dia(os.path.join(PATH_M, "periodo_dia.csv"))
        resultado = juguetes_a_aparecer(gen_jh, gen_pd, 1, 0)
        *items, largo = indexes_of(resultado, [0])
        self.assertEqual(largo, len(JUGUETES_A_APARECER_M_0))
        self.assertEqual(items[0], JUGUETES_A_APARECER_M_0[0])

    @timeout(N_SECOND)
    def test_M_1(self):
        """
        M — id_habitat=2, momento_dia=0: tres juguetes con distintos tiempos.
        """
        gen_jh = cargar_juguete_habitat(os.path.join(PATH_M, "juguete_habitat.csv"))
        gen_pd = cargar_periodo_dia(os.path.join(PATH_M, "periodo_dia.csv"))
        resultado = juguetes_a_aparecer(gen_jh, gen_pd, 2, 0)
        *items, largo = indexes_of(resultado, [0, -1])
        self.assertEqual(largo, len(JUGUETES_A_APARECER_M_1))
        self.assertEqual(items[0], JUGUETES_A_APARECER_M_1[0])
        self.assertEqual(items[1], JUGUETES_A_APARECER_M_1[-1])

    # ── S ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_S_0(self):
        """
        S — id_habitat=1, momento_dia=0: un solo juguete asociado al hábitat.
        """
        gen_jh = cargar_juguete_habitat(os.path.join(PATH_S, "juguete_habitat.csv"))
        gen_pd = cargar_periodo_dia(os.path.join(PATH_S, "periodo_dia.csv"))
        resultado = juguetes_a_aparecer(gen_jh, gen_pd, 1, 0)
        *items, largo = indexes_of(resultado, [0])
        self.assertEqual(largo, len(JUGUETES_A_APARECER_S_0))
        self.assertEqual(items[0], JUGUETES_A_APARECER_S_0[0])

    @timeout(N_SECOND)
    def test_S_1(self):
        """
        S — id_habitat=2, momento_dia=0: J28 aparece en P1 y J1 debe esperar a P2.
        """
        gen_jh = cargar_juguete_habitat(os.path.join(PATH_S, "juguete_habitat.csv"))
        gen_pd = cargar_periodo_dia(os.path.join(PATH_S, "periodo_dia.csv"))
        resultado = juguetes_a_aparecer(gen_jh, gen_pd, 2, 0)
        *items, largo = indexes_of(resultado, [0, -1])
        self.assertEqual(largo, len(JUGUETES_A_APARECER_S_1))
        self.assertEqual(items[0], JUGUETES_A_APARECER_S_1[0])
        self.assertEqual(items[1], JUGUETES_A_APARECER_S_1[-1])

    @timeout(N_SECOND)
    def test_S_2(self):
        """
        S — id_habitat=9, momento_dia=0: varios juguetes con tiempos y períodos distintos.
        """
        gen_jh = cargar_juguete_habitat(os.path.join(PATH_S, "juguete_habitat.csv"))
        gen_pd = cargar_periodo_dia(os.path.join(PATH_S, "periodo_dia.csv"))
        resultado = juguetes_a_aparecer(gen_jh, gen_pd, 9, 0)
        *items, largo = indexes_of(resultado, [0, -1])
        self.assertEqual(largo, len(JUGUETES_A_APARECER_S_2))
        self.assertEqual(items[0], JUGUETES_A_APARECER_S_2[0])
        self.assertEqual(items[1], JUGUETES_A_APARECER_S_2[-1])
