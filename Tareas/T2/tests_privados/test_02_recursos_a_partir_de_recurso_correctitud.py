from tests_privados.test_tools import IICTest, timeout, assert_es_generador, indexes_of
from backend.consultas import recursos_a_partir_de_recurso
from utils import RecursoRecurso

N_SECOND_BASE = 0.3
# Estructura en diamante: R1 → R2 → {R3, R4} → R5
#   R1×1 → R2  (afin 3)
#   R2×1 → R3  (afin 5)
#   R2×2 → R4  (afin 7)
#   R3×1 + R4×1 → R5  (afin 11)
RR_BASE = (
    RecursoRecurso(5, ((4, 1), (3, 1)), 11),
    RecursoRecurso(4, ((2, 2),), 7),
    RecursoRecurso(3, ((2, 1),), 5),
    RecursoRecurso(2, ((1, 1),), 3),
)

class TestRecursosAPartirDeRecursoPrivado(IICTest):
    """
    Pruebas de correctitud para recursos_a_partir_de_recurso.
    RR_BASE tiene estructura en diamante: R3 y R4 son hijos de R2,
    y R5 los requiere a ambos. Verifica orden, deduplicacion de afinidades y
    acumulacion de cantidades a traves de multiples caminos.
    """

    @timeout(N_SECOND_BASE)
    def test_retorna_generador(self):
        """
        La funcion debe ser generadora.
        """
        assert_es_generador(self, recursos_a_partir_de_recurso)

    @timeout(N_SECOND_BASE)
    def test_recurso_no_es_ingrediente(self):
        """
        id_recurso inexistente en la tabla retorna generador vacio (no lanza error).
        """
        gen = (r for r in RR_BASE)
        *_, largo = indexes_of(recursos_a_partir_de_recurso(gen, 99), [])
        self.assertEqual(largo, 0)

    @timeout(N_SECOND_BASE)
    def test_nodo_hoja_no_produce(self):
        """
        R5 existe en la tabla pero no aparece como ingrediente de ninguna receta;
        retorna generador vacio.
        """
        gen = (r for r in RR_BASE)
        *_, largo = indexes_of(recursos_a_partir_de_recurso(gen, 5), [])
        self.assertEqual(largo, 0)

    @timeout(N_SECOND_BASE)
    def test_afinidades_es_tupla(self):
        """
        afinidades_necesarias debe ser tuple, incluso con un solo elemento.
        """
        gen = (r for r in RR_BASE)
        *items, _ = indexes_of(recursos_a_partir_de_recurso(gen, 1), [0])
        _, afinidades, _ = items[0]
        self.assertIsInstance(afinidades, tuple)

    @timeout(N_SECOND_BASE)
    def test_un_lado_del_diamante_insuficiente(self):
        """
        R3 es ingrediente de R5, pero R5 tambien necesita R4 (no fabricable desde R3).
        id_recurso=3 retorna vacio porque ningun recurso es completamente fabricable.
        """
        gen = (r for r in RR_BASE)
        *_, largo = indexes_of(recursos_a_partir_de_recurso(gen, 3), [])
        self.assertEqual(largo, 0)

    @timeout(N_SECOND_BASE)
    def test_diamante_desde_vertice(self):
        """
        id_recurso=2 es el vertice del diamante: habilita R3, R4 y R5.
        Resultado completo ordenado por id ascendente.
        """
        gen = (r for r in RR_BASE)
        self.assertEqual(list(recursos_a_partir_de_recurso(gen, 2)), [
            (3, (5,), 1),
            (4, (7,), 2),
            (5, (5, 7, 11), 3),
        ])

    @timeout(N_SECOND_BASE)
    def test_diamante_afinidades_deduplicadas(self):
        """
        Desde id=1, R5 acumula afinidades por dos caminos que comparten afin 3 (via R2).
        El 3 debe aparecer solo una vez: (3, 5, 7, 11).
        """
        gen = (r for r in RR_BASE)
        *items, largo = indexes_of(recursos_a_partir_de_recurso(gen, 1), [-1])
        self.assertEqual(largo, 4)
        _, afinidades, _ = items[0]
        self.assertEqual(afinidades, (3, 5, 7, 11))

    @timeout(N_SECOND_BASE)
    def test_diamante_cantidad_acumulada(self):
        """
        Desde id=1, R5 requiere R3×1 (=1×R1 via R2) y R4×1 (=2×R1 via R2×2).
        Total: 3 unidades de R1 para fabricar R5.
        """
        gen = (r for r in RR_BASE)
        *items, largo = indexes_of(recursos_a_partir_de_recurso(gen, 1), [-1])
        self.assertEqual(largo, 4)
        _, _, cantidad = items[0]
        self.assertEqual(cantidad, 3)

    @timeout(N_SECOND_BASE)
    def test_afinidades_sin_duplicados_en_cadena_lineal(self):
        """
        Cadena lineal con la misma afinidad en dos niveles.
        La afinidad 6 debe aparecer una sola vez en cada resultado.
        """
        rr = (
            RecursoRecurso(20, ((15, 1),), 6),
            RecursoRecurso(15, ((10, 2),), 6),
        )
        self.assertEqual(list(recursos_a_partir_de_recurso((r for r in rr), 10)), [
            (15, (6,), 2),
            (20, (6,), 2),
        ])

