import os
from tests_publicos.test_tools import IICTest, timeout, assert_es_generador, indexes_of
from backend.consultas import cargar_juguete_recurso
from utils import JugueteRecurso

N_SECOND = 2.0
PATH_S = os.path.join("data", "S")


class TestCargaJugueteRecurso(IICTest):
    """
    Verifica que cargar_juguete_recurso retorne un generador con JugueteRecurso
    correctamente construidos. Tiempos en formato hh:mm.
    """

    # ── S ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_S_es_generador(self):
        """
        cargar_juguete_recurso debe retornar un generador (GeneratorType).
        """
        assert_es_generador(self, cargar_juguete_recurso)

    @timeout(N_SECOND)
    def test_S_valores(self):
        """
        S tiene 50 entradas; verifica el primero, el 25° y el último.
        """
        gen = cargar_juguete_recurso(os.path.join(PATH_S, "juguete_recurso.csv"))
        *items, largo = indexes_of(gen, [0, 24, -1])
        self.assertEqual(largo, 50)
        self.assertEqual(items[0], JugueteRecurso(1,  8,  "00:11", 1))
        self.assertEqual(items[1], JugueteRecurso(25, 16, "00:07", 4))
        self.assertEqual(items[2], JugueteRecurso(50, 18, "00:13", 2))
