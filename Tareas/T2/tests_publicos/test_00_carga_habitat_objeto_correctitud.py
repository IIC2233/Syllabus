import os
from tests_publicos.test_tools import IICTest, timeout, assert_es_generador, indexes_of
from backend.consultas import cargar_habitat_objeto
from utils import HabitatObjeto

N_SECOND = 2.0
PATH_S = os.path.join("data", "S")


class TestCargaHabitatObjeto(IICTest):
    """
    Verifica que cargar_habitat_objeto retorne un generador con HabitatObjeto
    correctamente construidos.
    """

    # ── S ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_S_es_generador(self):
        """
        cargar_habitat_objeto debe retornar un generador (GeneratorType).
        """
        assert_es_generador(self, cargar_habitat_objeto)

    @timeout(N_SECOND)
    def test_S_valores(self):
        """
        S tiene 50 entradas; verifica la primera, la 25° y la última.
        """
        gen = cargar_habitat_objeto(os.path.join(PATH_S, "habitat_objeto.csv"))
        *items, largo = indexes_of(gen, [0, 24, -1])
        self.assertEqual(largo, 50)
        self.assertEqual(items[0], HabitatObjeto(1,  ((6, 2),)))
        self.assertEqual(items[1], HabitatObjeto(25, ((7, 2),)))
        self.assertEqual(items[2], HabitatObjeto(50, ((1, 1), (9, 2))))

    @timeout(N_SECOND)
    def test_S_objetos_es_tupla_de_tuplas(self):
        """
        El campo 'objetos' debe ser una tupla de tuplas (id_objeto, cantidad).
        """
        for habitat_objeto in cargar_habitat_objeto(os.path.join(PATH_S, "habitat_objeto.csv")):
            self.assertIsInstance(habitat_objeto.objetos, tuple)
            for par in habitat_objeto.objetos:
                self.assertIsInstance(par, tuple)
                self.assertEqual(len(par), 2)
