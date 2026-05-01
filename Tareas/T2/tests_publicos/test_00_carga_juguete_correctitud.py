import os
from tests_publicos.test_tools import IICTest, timeout, assert_es_generador, indexes_of
from backend.consultas import cargar_juguete
from utils import Juguete

N_SECOND = 2.0
PATH_S = os.path.join("data", "S")


class TestCargaJuguete(IICTest):
    """
    Verifica que cargar_juguete retorne un generador con Juguete
    correctamente construidos.
    """

    # ── S ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_S_es_generador(self):
        """
        cargar_juguete debe retornar un generador (GeneratorType).
        """
        assert_es_generador(self, cargar_juguete)

    @timeout(N_SECOND)
    def test_S_valores(self):
        """
        S tiene 50 juguetes; verifica el primero, el 25° y el último.
        """
        gen = cargar_juguete(os.path.join(PATH_S, "juguetes.csv"))
        *items, largo = indexes_of(gen, [0, 24, -1])
        self.assertEqual(largo, 50)
        self.assertEqual(items[0], Juguete(1,  "Bulbasaur", (2,),   "001"))
        self.assertEqual(items[1], Juguete(25, "Pikachu",   (1, 5), "025"))
        self.assertEqual(items[2], Juguete(50, "Diglett",   (1, 2), "050"))

    @timeout(N_SECOND)
    def test_S_afinidades_es_tupla(self):
        """
        afinidades debe ser una tupla, incluso con una sola afinidad.
        """
        for juguete in cargar_juguete(os.path.join(PATH_S, "juguetes.csv")):
            self.assertIsInstance(juguete.afinidades, tuple)
