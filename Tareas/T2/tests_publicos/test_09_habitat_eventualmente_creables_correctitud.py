from tests_publicos.test_tools import IICTest, timeout, assert_es_generador, indexes_of
from backend.consultas import habitat_eventualmente_creables
from utils import Juguete, JugueteRecurso, RecursoRecurso, HabitatObjeto, ObjetoRecurso

N_SECOND = 0.3

# J1: afinidades (5,) → produce R1
# J2: afinidades (7,) → produce R2
J_BASE = [
    Juguete(1, "J1", (5,), "001"),
    Juguete(2, "J2", (7,), "002"),
]
JR_BASE = [
    JugueteRecurso(1, 1, "00:10", 5),  # J1 → R1
    JugueteRecurso(2, 2, "00:20", 3),  # J2 → R2
]
# R3 = R1 + R2, necesita afinidad 5  → producible (J1 la tiene)
# R4 = R3,      necesita afinidad 7  → producible por cadena (J2 la tiene)
# R5 = R2,      necesita afinidad 99 → NO producible (ningún juguete la tiene)
RR_BASE = [
    RecursoRecurso(5, ((2, 1),), 99),
    RecursoRecurso(4, ((3, 1),), 7),
    RecursoRecurso(3, ((1, 1), (2, 1)), 5),
]

OR_BASE = [
    ObjetoRecurso(1, ((1, 1),)),
    ObjetoRecurso(2, ((2, 1),)),
    ObjetoRecurso(3, ((3, 1),)),
    ObjetoRecurso(4, ((4, 1),)),
    ObjetoRecurso(5, ((5, 1),)),
]


class TestHabitatEventualmenteCreables(IICTest):
    """
    Pruebas para habitat_eventualmente_creables(
        generador_juguete, generador_juguete_recurso,
        generador_recurso_recurso, generador_recurso_objeto,
        generador_habitat_objeto
    ).
    Un hábitat es eventualmente creable si todos sus recursos requeridos
    (campo 'objetos' de HabitatObjeto interpretado como (id_recurso, cantidad))
    pueden ser producidos directamente por algún juguete o vía RecursoRecurso
    con la afinidad correcta.
    Hábitats sin recursos requeridos siempre son creables.
    Resultado en el orden del generador de entrada (id_habitat ascendente desde CSV).
    """

    @timeout(N_SECOND)
    def test_retorna_generador(self):
        """
        La función debe retornar un generador lazy.
        """
        assert_es_generador(self, habitat_eventualmente_creables)

    @timeout(N_SECOND)
    def test_recurso_producible_directamente(self):
        """
        H10 necesita R1 (J1 lo produce directamente) → creable.
        H12 necesita R5 (requiere afinidad 99, ningún juguete la tiene) → no creable.
        """
        gen_j  = (juguete for juguete in J_BASE)
        gen_jr = (juguete_recurso for juguete_recurso in JR_BASE)
        gen_rr = (recurso_recurso for recurso_recurso in RR_BASE)
        gen_or = (objeto_recurso for objeto_recurso in OR_BASE)
        gen_ho = (habitat_objeto for habitat_objeto in [
            HabitatObjeto(10, ((1, 1),)),
            HabitatObjeto(12, ((5, 1),)),
        ])
        *items, largo = indexes_of(habitat_eventualmente_creables(gen_j, gen_jr, gen_rr, gen_or, gen_ho), [0])
        self.assertEqual(largo, 1)
        self.assertEqual(items[0], 10)

    @timeout(N_SECOND)
    def test_habitat_sin_objetos_siempre_creable(self):
        """
        Hábitat sin recursos requeridos → siempre creable, independiente de
        qué juguetes o recursos existan.
        """
        gen_j  = (juguete for juguete in [])
        gen_jr = (juguete_recurso for juguete_recurso in [])
        gen_rr = (recurso_recurso for recurso_recurso in [])
        gen_or = (objeto_recurso for objeto_recurso in OR_BASE)
        gen_ho = (habitat_objeto for habitat_objeto in [HabitatObjeto(20, ())])
        *items, largo = indexes_of(habitat_eventualmente_creables(gen_j, gen_jr, gen_rr, gen_or, gen_ho), [0])
        self.assertEqual(largo, 1)
        self.assertEqual(items[0], 20)

    @timeout(N_SECOND)
    def test_recurso_solo_via_recurso_recurso_sin_afinidad(self):
        """
        H12 necesita R5. R5 solo puede obtenerse vía RecursoRecurso con afinidad 99.
        Ningún juguete tiene afinidad 99 → R5 no es producible → generador vacío.
        """
        gen_j  = (juguete for juguete in J_BASE)
        gen_jr = (juguete_recurso for juguete_recurso in JR_BASE)
        gen_rr = (recurso_recurso for recurso_recurso in [RecursoRecurso(5, ((2, 1),), 99)])
        gen_or = (objeto_recurso for objeto_recurso in OR_BASE)
        gen_ho = (habitat_objeto for habitat_objeto in [HabitatObjeto(12, ((5, 1),))])
        *items, largo = indexes_of(habitat_eventualmente_creables(gen_j, gen_jr, gen_rr, gen_or, gen_ho), [])
        self.assertEqual(largo, 0)

    @timeout(N_SECOND)
    def test_cadena_larga_de_produccion(self):
        """
        H14 necesita R4. Cadena: R4 = R3 (afinidad 7), R3 = R1+R2 (afinidad 5).
        J1 produce R1 (afinidad 5), J2 produce R2 (afinidad 7).
        Tras propagación: R1, R2 → R3 → R4; todos producibles.
        H14 es eventualmente creable.
        """
        gen_j  = (juguete for juguete in J_BASE)
        gen_jr = (juguete_recurso for juguete_recurso in JR_BASE)
        gen_rr = (recurso_recurso for recurso_recurso in RR_BASE)
        gen_or = (objeto_recurso for objeto_recurso in OR_BASE)
        gen_ho = (x for x in [HabitatObjeto(14, ((4, 1),))])
        *items, largo = indexes_of(habitat_eventualmente_creables(gen_j, gen_jr, gen_rr, gen_or, gen_ho), [0])
        self.assertEqual(largo, 1)
        self.assertEqual(items[0], 14)

    @timeout(N_SECOND)
    def test_mezcla_creables_y_no_creables(self):
        """
        H10 (necesita R1, directo) → creable.
        H12 (necesita R5, afinidad 99 faltante) → NO creable.
        H13 (sin recursos requeridos) → creable.
        El orden de salida preserva el orden del generador de entrada.
        """
        gen_j  = (juguete for juguete in J_BASE)
        gen_jr = (juguete_recurso for juguete_recurso in JR_BASE)
        gen_rr = (recurso_recurso for recurso_recurso in RR_BASE)
        gen_or = (objeto_recurso for objeto_recurso in OR_BASE)
        gen_ho = (habitat_objeto for habitat_objeto in [
            HabitatObjeto(10, ((1, 1),)),
            HabitatObjeto(12, ((5, 1),)),
            HabitatObjeto(13, ()),
        ])
        *items, largo = indexes_of(habitat_eventualmente_creables(gen_j, gen_jr, gen_rr, gen_or, gen_ho), [0, 1])
        self.assertEqual(largo, 2)
        self.assertEqual(items[0], 10)
        self.assertEqual(items[1], 13)

    def test_sin_habitats_creables(self):
        """
        Si los hábitats requieren recursos no producibles, el generador resultante debe estar vacío.
        """
        gen_j  = (juguete for juguete in J_BASE)
        gen_jr = (juguete_recurso for juguete_recurso in JR_BASE)
        gen_rr = (recurso_recurso for recurso_recurso in [RecursoRecurso(5, ((2, 1),), 99)])
        gen_or = (objeto_recurso for objeto_recurso in OR_BASE)
        gen_ho = (habitat_objeto for habitat_objeto in [
            HabitatObjeto(12, ((5, 1),)),
            HabitatObjeto(15, ((5, 1),)),
        ])
        *items, largo = indexes_of(habitat_eventualmente_creables(gen_j, gen_jr, gen_rr, gen_or, gen_ho), [])
        self.assertEqual(largo, 0)