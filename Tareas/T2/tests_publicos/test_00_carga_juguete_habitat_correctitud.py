# ruff: noqa: N802
import os
from tests_publicos.test_tools import IICTest, timeout, assert_es_generador, indexes_of
from backend.consultas import cargar_juguete_habitat
from utils import JugueteHabitat

N_SECOND = 2.0
PATH_S = os.path.join("data", "S")


class TestCargaJugueteHabitat(IICTest):
    """
    Verifica que cargar_juguete_habitat retorne un generador con JugueteHabitat
    correctamente construidos. Tiempos en formato hh:mm.
    """

    # ── S ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_S_es_generador(self):
        """
        cargar_juguete_habitat debe retornar un generador (GeneratorType).
        """
        assert_es_generador(self, cargar_juguete_habitat)

    @timeout(N_SECOND)
    def test_S_valores(self):
        """
        S tiene 111 entradas; verifica la primera, la 55° y la última.
        """
        gen = cargar_juguete_habitat(os.path.join(PATH_S, "juguete_habitat.csv"))
        *items, largo = indexes_of(gen, [0, 54, -1])
        self.assertEqual(largo, 111)
        self.assertEqual(items[0], JugueteHabitat(1,  1,  "00:30", (1, 2)))
        self.assertEqual(items[1], JugueteHabitat(14, 25, "00:16", (1, 2)))
        self.assertEqual(items[2], JugueteHabitat(10, 50, "00:45", (2,)))

    @timeout(N_SECOND)
    def test_S_ids_periodo_dia_es_tupla(self):
        """
        ids_periodo_dia debe ser una tupla, incluso con un solo período.
        """
        for juguete_habitat in cargar_juguete_habitat(os.path.join(PATH_S, "juguete_habitat.csv")):
            self.assertIsInstance(juguete_habitat.ids_periodo_dia, tuple)
