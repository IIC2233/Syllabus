from tests_publicos.test_tools import IICTest, timeout, assert_es_generador, indexes_of
from backend.consultas import recursos_a_partir_de_recurso
from utils import RecursoRecurso

N_SECOND = 0.3

# R2 = R1*1, afinidad 3
# R3 = R2*1, afinidad 5  → cadena completa: (3, 5)
# R4 = R2*3, afinidad 2  → cadena completa: (2, 3)
RR_BASE = (
    RecursoRecurso(6, ((5, 1),), 3),
    RecursoRecurso(5, ((3, 1),), 3),
    RecursoRecurso(4, ((3, 1), (2, 3)), 2),
    RecursoRecurso(3, ((2, 1),), 5),
    RecursoRecurso(2, ((1, 1),), 3),
)


class TestRecursosAPartirDeRecurso(IICTest):
    """
    Pruebas para recursos_a_partir_de_recurso(generador_recurso_recurso, id_recurso).
    Retorna (id_recurso_resultado, afinidades_necesarias, cantidad_requerida) por cada
    RecursoRecurso donde id_recurso aparece como ingrediente directo.
    afinidades_necesarias incluye toda la cadena de afinidades necesarias, ordenada por id.
    Resultado ordenado por id_recurso_resultado ascendente.
    """

    @timeout(N_SECOND)
    def test_retorna_generador(self):
        """
        La función debe retornar un generador lazy.
        """
        assert_es_generador(self, recursos_a_partir_de_recurso)

    @timeout(N_SECOND)
    def test_recurso_no_es_ingrediente(self):
        """
        id_recurso que no aparece como ingrediente en ninguna receta → generador vacío.
        """
        gen = (recurso_recurso for recurso_recurso in RR_BASE)
        *items, largo = indexes_of(recursos_a_partir_de_recurso(gen, 99), [])
        self.assertEqual(largo, 0)

    @timeout(N_SECOND)
    def test_ingrediente_en_multiples_recetas(self):
        """
        id_recurso aparece en más de una RecursoRecurso → retorna una entrada por cada
        una, ordenadas por id_recurso_resultado ascendente.
        """
        gen = (recurso_recurso for recurso_recurso in RR_BASE)
        # R2 es ingrediente de R3 (cantidad 1) y de R4 (cantidad 3)
        *items, largo = indexes_of(recursos_a_partir_de_recurso(gen, 2), [0, 1, 2, 3])
        self.assertEqual(largo, 4)
        self.assertEqual(items[0], (3, (5,), 1))
        self.assertEqual(items[1], (4, (2, 5), 4))
        self.assertEqual(items[2], (5, (3, 5), 1))
        self.assertEqual(items[3], (6, (3, 5), 1))

    @timeout(N_SECOND)
    def test_afinidades_necesarias_es_tupla(self):
        """
        afinidades_necesarias siempre es tupla, nunca un entero suelto.
        """
        gen = (recurso_recurso for recurso_recurso in RR_BASE)
        *items, largo = indexes_of(recursos_a_partir_de_recurso(gen, 1), [0])
        self.assertEqual(largo, 5)
        _, afinidades, _ = items[0]
        self.assertIsInstance(afinidades, tuple)

    @timeout(N_SECOND)
    def test_recursos_parciales(self):
        """
        No se puede armar recursos id 4 completamente con el id_entregado.
        """
        gen = (recurso_recurso for recurso_recurso in RR_BASE)
        *items, largo = indexes_of(recursos_a_partir_de_recurso(gen, 3), [0, 1])
        self.assertEqual(largo, 2)
        self.assertEqual(items[0], (5, (3,), 1))
        self.assertEqual(items[1], (6, (3,), 1))

    @timeout(N_SECOND)
    def test_recursos_insuficientes(self):
        """
        No se pueden armar recursos completamente con el id_entregado.
        """
        gen = (recurso_recurso for recurso_recurso in RR_BASE)
        *items, largo = indexes_of(recursos_a_partir_de_recurso(gen, 6), [])
        self.assertEqual(largo, 0)

    @timeout(N_SECOND)
    def test_ingrediente_base(self):
        """
        id_recurso es un recurso base →
        se pueden obtener todos los recursos.
        """
        gen = (recurso_recurso for recurso_recurso in RR_BASE)
        *items, largo = indexes_of(recursos_a_partir_de_recurso(gen, 1), [0, 2, -1])
        self.assertEqual(largo, 5)
        self.assertEqual(items[0], (2, (3,), 1))
        self.assertEqual(items[1], (4, (2, 3, 5), 4))
        self.assertEqual(items[2], (6, (3, 5), 1))

    @timeout(N_SECOND)
    def test_misma_afinidad(self):
        """
        Si hay varias recetas con la misma afinidad, solo debe aparecer una vez en afinidades_necesarias.
        """
        gen = (recurso_recurso for recurso_recurso in RR_BASE)
        *items, largo = indexes_of(recursos_a_partir_de_recurso(gen, 2), [0])
        self.assertEqual(largo, 4)
        _, afinidades, _ = items[0]
        self.assertEqual(afinidades, (5,))
