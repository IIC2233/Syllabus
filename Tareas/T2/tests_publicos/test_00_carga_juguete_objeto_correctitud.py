import os
from tests_publicos.test_tools import IICTest, timeout, assert_es_generador, indexes_of
from backend.consultas import cargar_juguete_objeto
from utils import JugueteObjeto

N_SECOND = 2.0
PATH_S = os.path.join("data", "S")


class TestCargaJugueteObjeto(IICTest):
    """
    Verifica que cargar_juguete_objeto retorne un generador con JugueteObjeto
    correctamente construidos.
    """

    # ── S ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_S_es_generador(self):
        """
        cargar_juguete_objeto debe retornar un generador (GeneratorType).
        """
        assert_es_generador(self, cargar_juguete_objeto)

    @timeout(N_SECOND)
    def test_S_valores(self):
        """
        S tiene 76 entradas; verifica la primera, la 40° y la última.
        """
        gen = cargar_juguete_objeto(os.path.join(PATH_S, "juguete_objeto.csv"))
        *items, largo = indexes_of(gen, [0, 39, -1])
        self.assertEqual(largo, 76)
        self.assertEqual(items[0], JugueteObjeto(1,  4))
        self.assertEqual(items[1], JugueteObjeto(27, 3))
        self.assertEqual(items[2], JugueteObjeto(50, 7))
