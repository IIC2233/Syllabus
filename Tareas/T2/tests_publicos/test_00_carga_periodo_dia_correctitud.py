import os
from tests_publicos.test_tools import IICTest, timeout, assert_es_generador, indexes_of
from backend.consultas import cargar_periodo_dia
from utils import PeriodoDia

N_SECOND = 2.0
PATH_S = os.path.join("data", "S")


class TestCargaPeriodoDia(IICTest):
    """
    Verifica que cargar_periodo_dia retorne un generador con PeriodoDia
    correctamente construidos. Tiempos en formato hh:mm.
    """

    # ── S ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_S_es_generador(self):
        """
        cargar_periodo_dia debe retornar un generador (GeneratorType).
        """
        assert_es_generador(self, cargar_periodo_dia)

    @timeout(N_SECOND)
    def test_S_valores(self):
        """
        S tiene 2 períodos; verifica ambos.
        """
        gen = cargar_periodo_dia(os.path.join(PATH_S, "periodo_dia.csv"))
        *items, largo = indexes_of(gen, [0, -1])
        self.assertEqual(largo, 2)
        self.assertEqual(items[0], PeriodoDia(1, "Madrugada", "00:26"))
        self.assertEqual(items[1], PeriodoDia(2, "Amanecer",  "00:33"))
