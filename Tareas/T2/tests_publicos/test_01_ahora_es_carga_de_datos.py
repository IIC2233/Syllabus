import os
from tests_publicos.test_tools import IICTest, timeout
from tests_publicos.solution.test_1 import (AHORA_ES_L_0, AHORA_ES_L_1, AHORA_ES_M_0, 
                                            AHORA_ES_M_1, AHORA_ES_M_2, AHORA_ES_S_0, 
                                            AHORA_ES_S_1, AHORA_ES_S_2)
from backend.consultas import ahora_es, cargar_periodo_dia

N_SECOND = 0.5
PATH_S  = os.path.join("data", "S")
PATH_M  = os.path.join("data", "M")
PATH_L  = os.path.join("data", "L")


class TestAhoraEsCargaDatos(IICTest):
    """
    Verifica ahora_es cargando periodo_dia desde los datasets S, M y L.
    """

    # ── S ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_S_0(self):
        """
        S — minutos=0: primer minuto del día, primer período.
        """
        gen = cargar_periodo_dia(os.path.join(PATH_S, "periodo_dia.csv"))
        self.assertEqual(ahora_es(gen, 0), AHORA_ES_S_0)

    @timeout(N_SECOND)
    def test_S_1(self):
        """
        S — minutos=30: dentro del segundo período (Amanecer).
        """
        gen = cargar_periodo_dia(os.path.join(PATH_S, "periodo_dia.csv"))
        self.assertEqual(ahora_es(gen, 30), AHORA_ES_S_1)

    @timeout(N_SECOND)
    def test_S_2(self):
        """
        S — minutos=59: exactamente al inicio del día 1 (primer período).
        """
        gen = cargar_periodo_dia(os.path.join(PATH_S, "periodo_dia.csv"))
        self.assertEqual(ahora_es(gen, 59), AHORA_ES_S_2)

    # ── M ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_M_0(self):
        """
        M — minutos=0: primer minuto del día, primer período.
        """
        gen = cargar_periodo_dia(os.path.join(PATH_M, "periodo_dia.csv"))
        self.assertEqual(ahora_es(gen, 0), AHORA_ES_M_0)

    @timeout(N_SECOND)
    def test_M_1(self):
        """
        M — minutos=50: dentro del segundo período (Amanecer).
        """
        gen = cargar_periodo_dia(os.path.join(PATH_M, "periodo_dia.csv"))
        self.assertEqual(ahora_es(gen, 50), AHORA_ES_M_1)

    @timeout(N_SECOND)
    def test_M_2(self):
        """
        M — minutos=200: día 1, dentro del tercer período (Alba).
        """
        gen = cargar_periodo_dia(os.path.join(PATH_M, "periodo_dia.csv"))
        self.assertEqual(ahora_es(gen, 200), AHORA_ES_M_2)

    # ── L ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_L_0(self):
        """
        L — minutos=0: primer minuto del día, primer período.
        """
        gen = cargar_periodo_dia(os.path.join(PATH_L, "periodo_dia.csv"))
        self.assertEqual(ahora_es(gen, 0), AHORA_ES_L_0)

    @timeout(N_SECOND)
    def test_L_1(self):
        """
        L — minutos=40: dentro del segundo período (Amanecer).
        """
        gen = cargar_periodo_dia(os.path.join(PATH_L, "periodo_dia.csv"))
        self.assertEqual(ahora_es(gen, 40), AHORA_ES_L_1)
